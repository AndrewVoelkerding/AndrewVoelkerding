import json
import os
import shutil
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML  # Added for static PDF compilation

# 1. Define folder paths
OUTPUT_DIR = 'dist'
DATA_FILE = 'data.json'
TEMPLATES_DIR = 'templates'
STATIC_DIR = 'static'

def build_site():
    print("🚀 Starting static website build...")

    # Create or clean the output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # 2. Load the project data
    if not os.path.exists(DATA_FILE):
        print(f"❌ Error: {DATA_FILE} not found!")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"📁 Loaded data for: {data.get('name', 'Portfolio')}")

    # 3. Set up the Jinja2 template engine
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    # Mock Flask's url_for() so image paths work seamlessly in static HTML
    def static_url_for(endpoint, filename=None):
        if endpoint == 'static' and filename:
            return f"/static/{filename}"
        return filename

    env.globals['url_for'] = static_url_for

    # 4. Render and save each HTML page
    pages = [
        ('index.html', 'index.html'),
        ('projects.html', 'projects.html'),
        ('resume.html', 'resume.html')
    ]

    for template_name, output_name in pages:
        try:
            template = env.get_template(template_name)
            # For resume.html we will inject pdf filenames and link style class
            if template_name == 'resume.html':
                annotated_pdf_name = 'Andrew_Voelkerding_Resume_annotated.pdf'
                plain_pdf_name = 'Andrew_Voelkerding_Resume_plain.pdf'

                # Render the on-site HTML (default to annotated link style)
                rendered_html = template.render(
                    data=data,
                    link_style_class='link-annotated',
                    pdf_annotated=annotated_pdf_name,
                    pdf_plain=plain_pdf_name
                )
            else:
                rendered_html = template.render(data=data)

            output_path = os.path.join(OUTPUT_DIR, output_name)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered_html)
            print(f"✅ Generated: {output_path}")

            # 📄 Generate both annotated and plain PDFs for resume.html
            if template_name == 'resume.html':
                annotated_pdf_path = os.path.join(OUTPUT_DIR, annotated_pdf_name)
                plain_pdf_path = os.path.join(OUTPUT_DIR, plain_pdf_name)
                try:
                    # Annotated PDF (blue + underline)
                    annotated_html = template.render(
                        data=data,
                        link_style_class='link-annotated',
                        pdf_annotated=annotated_pdf_name,
                        pdf_plain=plain_pdf_name
                    )
                    HTML(string=annotated_html, base_url=os.path.abspath(TEMPLATES_DIR)).write_pdf(annotated_pdf_path)

                    # Plain PDF (black/grey + no underline)
                    plain_html = template.render(
                        data=data,
                        link_style_class='link-plain',
                        pdf_annotated=annotated_pdf_name,
                        pdf_plain=plain_pdf_name
                    )
                    HTML(string=plain_html, base_url=os.path.abspath(TEMPLATES_DIR)).write_pdf(plain_pdf_path)

                    print(f"📄 Generated static PDFs: {annotated_pdf_path}, {plain_pdf_path}")
                except Exception as pdf_err:
                    print(f"⚠️ PDF generation skipped (WeasyPrint dependencies?): {pdf_err}")

        except Exception as e:
            print(f"❌ Failed to generate {template_name}: {e}")

    # 5. Copy over the static folder (images, CSS, etc.)
    if os.path.exists(STATIC_DIR):
        dest_static = os.path.join(OUTPUT_DIR, STATIC_DIR)
        shutil.copytree(STATIC_DIR, dest_static)
        print(f"🖼️  Copied static assets to: {dest_static}")
    else:
        print("⚠️  No static/ folder found to copy.")

    cname_file = 'CNAME'
    if os.path.exists(cname_file):
        shutil.copy(cname_file, os.path.join(OUTPUT_DIR, 'CNAME'))
        print("📄 Copied CNAME file to dist/")
    else:
        print("⚠️ No CNAME file found.")

    print("\n🎉 Build complete! Your static site is ready inside the '/dist' folder.")

if __name__ == '__main__':
    build_site()
