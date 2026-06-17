# Resume + Job Application Website Package for Codex

This package gives Codex everything it needs to create a polished personal website for **Syed Huzaifa Bin Afzal** focused on AI research, secure GenAI systems, DevOps, cloud infrastructure, and job applications.

## What is included

- `CODEX_WEBSITE_BUILD_PROMPT.md` — paste this into Codex as the main instruction.
- `content/resume-data.json` — structured resume/profile content Codex must use as the source of truth.
- `content/site-copy.md` — human-written website copy for the main sections.
- `docs/design-brief.md` — visual and UX direction.
- `docs/github-pages-deployment.md` — deployment steps for GitHub Pages.
- `docs/namecheap-custom-domain.md` — exact Namecheap DNS and GitHub Pages custom-domain setup for `resume.huzaifaafzal.me`.
- `src/index.html`, `src/styles.css`, `src/script.js` — a clean static starter site Codex can improve or convert to React/Next.js.
- `assets/resumes/` — downloadable AI, DevOps, and master resume files.

## Recommended workflow

1. Create a new GitHub repository, for example `huzaifa-portfolio`.
2. Upload this package or open it in a Codex workspace.
3. Paste the full contents of `CODEX_WEBSITE_BUILD_PROMPT.md` into Codex.
4. Ask Codex to implement the website and commit the changes.
5. Enable GitHub Pages from the repository settings.
6. Connect the site to the Namecheap subdomain `resume.huzaifaafzal.me` using `docs/namecheap-custom-domain.md`.

## Important rule

Do not let Codex invent extra employers, degrees, tools, metrics, publications, awards, or projects. The website should use only the content provided in this package unless Huzaifa manually adds more information.
