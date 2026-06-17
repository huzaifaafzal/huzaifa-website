# GitHub Pages Deployment

## Static HTML deployment

1. Create a GitHub repository, for example `huzaifa-portfolio`.
2. Copy the contents of the `src` folder into the repository root, or keep the `src` folder and configure Pages accordingly.
3. Copy the `assets` folder into the repository root so resume links work.
4. Commit and push the files.
5. Go to GitHub repository settings.
6. Open **Pages**.
7. Under **Build and deployment**, select **Deploy from a branch**.
8. Select the `main` branch and `/root` folder if files are in the root, or `/docs` if you move the static site into a `docs` folder.
9. Save. GitHub will publish the website and provide a URL.

## Recommended structure for easiest deployment

For GitHub Pages, use this repository layout:

```text
index.html
styles.css
script.js
assets/
  resumes/
    Syed_Huzaifa_Afzal_AI_Engineer_CV.pdf
    Syed_Huzaifa_Afzal_DevOps_Engineer_CV.pdf
    Syed_Huzaifa_Afzal_Master_AI_DevOps_Resume.pdf
.nojekyll
```

## Custom domain required for this project

This portfolio should use the custom Namecheap subdomain:

```text
resume.huzaifaafzal.me
```

Make sure the published site includes a `CNAME` file with exactly this line:

```text
resume.huzaifaafzal.me
```

Then follow `docs/namecheap-custom-domain.md` for the GitHub Pages and Namecheap DNS steps. For the Namecheap record, use:

```text
Type:  CNAME Record
Host:  resume
Value: [YOUR-GITHUB-USERNAME].github.io
TTL:   Automatic
```

Replace `[YOUR-GITHUB-USERNAME]` with the GitHub username that owns the Pages repository. Do not include `https://` in the DNS value.

