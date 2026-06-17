# Deployment

This site is designed for GitHub Pages at:

```text
resume.huzaifaafzal.me
```

## Recommended GitHub Pages setup

1. Publish from the repository root. The root-level `index.html`, `styles.css`, `script.js`, `assets/`, and `CNAME` files are already arranged for this.
2. Keep the `assets/` folder at the repository root so the resume download links work.
3. Make sure the published root contains a `CNAME` file with exactly:

```text
resume.huzaifaafzal.me
```

4. In GitHub, open **Settings > Pages**.
5. Select the publishing branch and `/root`.
6. Enter `resume.huzaifaafzal.me` as the custom domain.

## Namecheap DNS

Use this exact DNS record in Namecheap:

```text
Type:  CNAME Record
Host:  resume
Value: [YOUR-GITHUB-USERNAME].github.io
TTL:   Automatic
```

Replace `[YOUR-GITHUB-USERNAME]` with the GitHub username that owns the GitHub Pages repository. Do not use `https://` in the Namecheap DNS Value field.

After DNS verifies in GitHub Pages, enable **Enforce HTTPS**.
