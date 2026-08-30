# Andrew Voelkerding — Engineering Portfolio

Personal portfolio and interactive resume for Mechanical Engineering (Purdue '28). 

Hosted live on GitHub Pages at [andrew.voelkerding.xyz](https://andrew.voelkerding.xyz).

---

## How It Works

This site uses a data-driven static generator setup so content stays completely separate from HTML layout:

* **Single Source of Truth:** All project details, work experience, skills, and resume entries live in `data.json`.
* **Automated CI/CD:** Commits to `main` trigger a GitHub Action that runs `build.py`. The workflow compiles the Jinja2 templates into static HTML in an ephemeral build directory and deploys it straight to GitHub Pages.
* **Interactive Showcase:** Side-tab project selection system rendered directly from JSON data using lightweight client-side JavaScript.
* **Print-Ready Resume:** ATS-friendly resume template formatted for both browser viewing and clean PDF downloads.

---

## Project Structure

```text
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions build & deployment pipeline
├── templates/
│   ├── index.html          # Main landing page template
│   ├── projects.html       # Master-detail projects showcase template
│   └── resume.html         # Printable ATS resume template
├── static/
│   └── images/             # Project photos & media assets
├── data.json               # Master content database
├── build.py                # Local/CI static site generator script
└── README.md
