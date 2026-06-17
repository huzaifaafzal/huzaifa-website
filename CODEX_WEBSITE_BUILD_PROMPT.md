# Codex Task: Build My Resume + Job Application Website

You are working on a personal portfolio and job application website for **Syed Huzaifa Bin Afzal**.

## Main goal

Create a modern, professional, ATS-friendly portfolio website that supports job applications for:

- AI Engineer
- AI Research / AI Security roles
- Cloud Infrastructure Engineer
- DevOps Engineer
- Site Reliability Engineer
- Platform Engineer

The website should help recruiters quickly understand that Huzaifa has a combined profile in:

- Production AWS cloud infrastructure and DevOps
- Terraform, CI/CD, monitoring, reliability, and cloud cost optimization
- Secure enterprise GenAI research and AI governance
- Cybersecurity graduate education at the University of Washington
- Strong technical communication through UW student reporting and executive interviews

## Source of truth

Use `content/resume-data.json` and `content/site-copy.md` as the factual source of truth.

Do **not** invent employers, titles, dates, degrees, certifications, tools, metrics, publications, awards, or achievements. If something is not in the provided content, leave it out or use a clear placeholder.


## Custom domain requirement

The website must be ready to publish at this custom Namecheap subdomain:

```text
resume.huzaifaafzal.me
```

Include a `CNAME` file in the published site output/root with exactly this single line:

```text
resume.huzaifaafzal.me
```

Also create or update `DEPLOYMENT.md` with these exact Namecheap DNS instructions:

```text
Type:  CNAME Record
Host:  resume
Value: [YOUR-GITHUB-USERNAME].github.io
TTL:   Automatic
```

Tell Huzaifa to replace `[YOUR-GITHUB-USERNAME]` with the GitHub username that owns the GitHub Pages repository. Do not use `https://` in the Namecheap DNS Value field. After DNS verifies in GitHub Pages, enable Enforce HTTPS.

## Website requirements

Build a responsive website with these sections:

1. Hero
   - Name: Syed Huzaifa Bin Afzal
   - Headline: Cloud Infrastructure, DevOps, SRE, and Secure AI Systems
   - Short summary
   - Buttons for: Download AI Resume, Download DevOps Resume, Contact, LinkedIn

2. About
   - Explain the combined AI + DevOps + cybersecurity background in a natural voice.

3. Focus Areas
   Include cards for:
   - Cloud Infrastructure & DevOps
   - Secure GenAI & AI Governance
   - Site Reliability & Operations
   - Technical Communication

4. Experience
   - Timeline/cards for Harri/Kalam 4 Solutions, Visionet/Systems Limited, and University of Washington.

5. Projects & Research
   Include:
   - GovernAI – Secure Enterprise GenAI Platform
   - AWS Infrastructure Automation and Cost Optimization
   - UW AI and Technical Storytelling

6. Skills
   Group skills into:
   - Cloud & DevOps
   - AI & Security
   - Communication

7. Education & Certifications
   Include University of Washington MCL expected June 2026 and GIKI BS CS.

8. Publications / Writing
   Include the IEEE SVCC 2026 accepted paper title and UW Purple article link.

9. Resume Downloads
   Include downloadable links to files in `assets/resumes/`:
   - AI Engineer CV
   - DevOps Engineer CV
   - Master AI + DevOps Resume

10. Contact
   - Email: huzaifaafzal10@gmail.com
   - Phone: +1 (206) 750-5956
   - LinkedIn: https://www.linkedin.com/in/syed-huzaifa-bin-afzal
   - GitHub placeholder: [ADD_GITHUB_PROFILE_URL]

## Design direction

- Clean, professional, recruiter-friendly.
- Dark modern theme is preferred, but it must be readable.
- Use strong section spacing and clear headings.
- Avoid flashy animations that hurt performance.
- Make it mobile responsive.
- Use semantic HTML and accessible contrast.
- Do not use icons unless they are installed through the project dependency setup.
- Keep page speed high.

## Implementation preference

A static site is acceptable and recommended for GitHub Pages. You may either:

- Improve the existing `src/index.html`, `src/styles.css`, and `src/script.js`, or
- Convert the project into a simple Vite + React app if that is better.

If you convert to React, include all needed files: `package.json`, `src/App.jsx`, `src/main.jsx`, `src/index.css`, and deployment instructions.

For simplest GitHub Pages deployment, keeping the static HTML/CSS/JS version is preferred.

## Content style

The writing should sound human-written, not AI-generated. Avoid generic phrases like:

- dynamic professional
- proven track record
- passionate about innovation
- cutting-edge
- fast-paced environment
- results-driven
- leveraged

Use direct, specific, natural language.

## Quality checks before finishing

- Verify all resume download links work.
- Verify the site works locally from the `src` folder.
- Verify responsive layout for mobile and desktop.
- Verify no unsupported claims were added.
- Verify no typos in the name: **Syed Huzaifa Bin Afzal**.
- Verify the UW degree is written exactly as: **Master of Cybersecurity & Leadership — Expected June 2026**.

## Deliverables

Commit the completed website files. Also include a short `DEPLOYMENT.md` explaining how to publish the site through GitHub Pages and connect the Namecheap custom domain `resume.huzaifaafzal.me`.
