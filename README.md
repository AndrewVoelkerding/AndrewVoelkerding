<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrew Voelkerding | Mechanical Engineering</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-main: #F8FAFC;
            --bg-card: #FFFFFF;
            --text-dark: #0F172A;
            --text-muted: #475569;
            --border: #E2E8F0;
            --accent-grey: #334155;
            --accent-light: #F1F5F9;
            --purdue-gold: #C59B27;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-dark);
            line-height: 1.6;
        }

        header {
            background-color: #0F172A;
            color: white;
            padding: 4rem 2rem;
            text-align: center;
            border-bottom: 4px solid var(--purdue-gold);
        }

        header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            letter-spacing: -0.02em;
        }

        header p.subtitle {
            font-size: 1.15rem;
            color: #94A3B8;
            margin-top: 0.5rem;
        }

        .contact-links {
            margin-top: 1.5rem;
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 0.5rem 1.25rem;
            background: #1E293B;
            color: #E2E8F0;
            text-decoration: none;
            border-radius: 6px;
            font-size: 0.9rem;
            font-weight: 600;
            border: 1px solid #334155;
            transition: all 0.2s ease;
        }

        .btn:hover {
            background: var(--purdue-gold);
            color: #0F172A;
            border-color: var(--purdue-gold);
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 3rem 1.5rem;
        }

        section {
            margin-bottom: 3.5rem;
        }

        h2.section-title {
            font-size: 1.5rem;
            color: var(--accent-grey);
            border-bottom: 2px solid var(--border);
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        .card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .card h3 {
            font-size: 1.2rem;
            color: var(--text-dark);
        }

        .card .meta {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 0.75rem;
            font-weight: 600;
        }

        .card ul {
            padding-left: 1.2rem;
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        .card ul li {
            margin-bottom: 0.5rem;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
        }

        .skill-box {
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 1rem;
            border-radius: 6px;
        }

        .skill-box h4 {
            font-size: 0.95rem;
            color: var(--accent-grey);
            margin-bottom: 0.5rem;
        }

        .skill-box p {
            font-size: 0.875rem;
            color: var(--text-muted);
        }

        .badge {
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent-grey);
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-top: 0.5rem;
        }

        footer {
            text-align: center;
            padding: 2rem;
            background: #0F172A;
            color: #64748B;
            font-size: 0.85rem;
            border-top: 1px solid #1E293B;
        }
    </style>
</head>
<body>

    <header>
        <h1>ANDREW VOELKERDING</h1>
        <p class="subtitle">Mechanical Engineering | Purdue University '28</p>
        <div class="contact-links">
            <a class="btn" href="mailto:voelkerd@purdue.edu">Email</a>
            <a class="btn" href="https://linkedin.com/in/andrew-voe" target="_blank">LinkedIn</a>
            <a class="btn" href="https://github.com/AndrewVoelkerding" target="_blank">GitHub</a>
            <a class="btn" href="tel:5139104107">513-910-4107</a>
        </div>
    </header>

    <div class="container">
        
        <section>
            <h2 class="section-title">Education</h2>
            <div class="card">
                <h3>Purdue University — West Lafayette, IN</h3>
                <p class="meta">Bachelor of Science in Mechanical Engineering | Expected Graduation: May 2028</p>
                <p><strong>GPA:</strong> 3.90 / 4.00</p>
                <p style="margin-top: 0.5rem;"><strong>Relevant Coursework:</strong> Statics, Geometric and Annotation Modeling (CAD), Electrical Engineering Fundamentals, Programming in C, Data Science</p>
                <div style="margin-top: 0.75rem;">
                    <span class="badge">ASME Member</span>
                    <span class="badge">Purdue Formula SAE</span>
                    <span class="badge">GD&T Milestones Certification</span>
                    <span class="badge">Undue Ultimate</span>
                </div>
            </div>
        </section>

        <section>
            <h2 class="section-title">Engineering Experience</h2>
            <div class="grid">
                
                <div class="card">
                    <h3>Formula SAE Suspension Team</h3>
                    <p class="meta">Purdue University | Aug 2025 – Present</p>
                    <ul>
                        <li>Modeled components in Siemens NX and performed FEA simulations in ANSYS Mechanical to evaluate stress concentrations and safety factors.</li>
                        <li>Designed welded front rockers, achieving an <strong>~18.8% weight reduction</strong> while maintaining a <strong>1.6 FoS</strong>.</li>
                        <li>Generated CAM toolpaths and GD&T technical drawings to streamline CNC manufacturing.</li>
                        <li>Supported multi-operation wheel hub production via 3-axis CNC milling, hand-tapping, and custom soft-jaw fixtures.</li>
                    </ul>
                </div>

                <div class="card">
                    <h3>Car Radios & Backup Camera Installation</h3>
                    <p class="meta">Cincinnati, OH | Jun 2023 – Present</p>
                    <ul>
                        <li>Soldered custom wiring harnesses for upgraded automotive head units.</li>
                        <li>Wired radios to interfaces including backup cameras and steering wheel control retention modules.</li>
                        <li>Retrofitted modern speedometers to relocate driver information functionality post-radio replacement.</li>
                    </ul>
                </div>

            </div>
        </section>

        <section>
            <h2 class="section-title">Industry Employment</h2>
            <div class="grid">

                <div class="card">
                    <h3>Manufacturing Engineering Intern</h3>
                    <p class="meta">General Tool Company | May 2026 – Present</p>
                    <ul>
                        <li>Completed cross-functional rotation across machining and fabrication departments for high-precision defense components.</li>
                        <li>Analyzed technical drawings and sales orders to generate competitive assembly quotes and ensure profitability.</li>
                        <li>Engineered custom 3D-printed instructional models demonstrating GD&T principles (True Position & MMC) for intern onboarding.</li>
                    </ul>
                </div>

                <div class="card">
                    <h3>Intern / Assistant</h3>
                    <p class="meta">Urban Sites | Nov 2023 – Dec 2023</p>
                    <ul>
                        <li>Engineered a functional Python prototype to assist in package tracking for ~50 tenant packages at a time.</li>
                        <li>Iterated on user feedback applying user-centered design and stakeholder communication principles.</li>
                    </ul>
                </div>

                <div class="card">
                    <h3>Head Auto Detailer / Owner</h3>
                    <p class="meta">Cincy Auto Detailing | Jun 2021 – Present</p>
                    <ul>
                        <li>Managed business operations, equipment investment, and finances for ~25 loyal customers and ~50 detailed vehicles.</li>
                    </ul>
                </div>

            </div>
        </section>

        <section>
            <h2 class="section-title">Technical Skills</h2>
            <div class="skills-grid">
                <div class="skill-box">
                    <h4>Design & Simulation</h4>
                    <p>Siemens NX, Fusion 360, ANSYS Mechanical, GD&T</p>
                </div>
                <div class="skill-box">
                    <h4>Programming & Data</h4>
                    <p>Python, C, MATLAB, Excel, Data Science</p>
                </div>
                <div class="skill-box">
                    <h4>Manufacturing</h4>
                    <p>3D Printing, Laser Cutting, CNC, Basic Tooling</p>
                </div>
                <div class="skill-box">
                    <h4>Electrical</h4>
                    <p>Soldering, Arduino, Wiring Harnesses</p>
                </div>
            </div>
        </section>

    </div>

    <footer>
        <p>&copy; 2026 Andrew Voelkerding | andrew.voelkerding.xyz</p>
    </footer>

</body>
</html>
