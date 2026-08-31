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
                color_pdf_name = 'Andrew_Voelkerding_Resume_color.pdf'
                bw_pdf_name = 'Andrew_Voelkerding_Resume_bw.pdf'

                # Render the on-site HTML (default to color)
                rendered_html = template.render(
                    data=data,
                    link_style_class='color',
                    pdf_color=color_pdf_name,
                    pdf_bw=bw_pdf_name
                )
            else:
                rendered_html = template.render(data=data)

            output_path = os.path.join(OUTPUT_DIR, output_name)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered_html)
            print(f"✅ Generated: {output_path}")

            # 📄 Generate color and black & white PDFs for resume.html
            if template_name == 'resume.html':
                color_pdf_path = os.path.join(OUTPUT_DIR, color_pdf_name)
                bw_pdf_path = os.path.join(OUTPUT_DIR, bw_pdf_name)
                try:
                    # Color PDF (blue links + gold section headers)
                    color_html = template.render(
                        data=data,
                        link_style_class='color',
                        pdf_color=color_pdf_name,
                        pdf_bw=bw_pdf_name
                    )
                    HTML(string=color_html, base_url=os.path.abspath(TEMPLATES_DIR)).write_pdf(color_pdf_path)

                    # Black & White PDF (all black text, no colors)
                    bw_html = template.render(
                        data=data,
                        link_style_class='bw',
                        pdf_color=color_pdf_name,
                        pdf_bw=bw_pdf_name
                    )
                    HTML(string=bw_html, base_url=os.path.abspath(TEMPLATES_DIR)).write_pdf(bw_pdf_path)

                    print(f"📄 Generated static PDFs: {color_pdf_path}, {bw_pdf_path}")
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
