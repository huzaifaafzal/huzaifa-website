# Custom Domain Setup: resume.huzaifaafzal.me

This website should be deployed on GitHub Pages and connected to the Namecheap subdomain:

```text
resume.huzaifaafzal.me
```

## 1. GitHub repository setup

1. Push the completed website files to the GitHub repository.
2. Make sure the published branch/folder contains a `CNAME` file with exactly this single line:

```text
resume.huzaifaafzal.me
```

3. Go to the repository on GitHub.
4. Open **Settings → Pages**.
5. Under **Build and deployment**, select the branch/folder being used for the site.
6. Under **Custom domain**, enter:

```text
resume.huzaifaafzal.me
```

7. Click **Save**.
8. After DNS verifies, enable **Enforce HTTPS**.

## 2. Namecheap DNS setup

In Namecheap:

1. Go to **Domain List**.
2. Select `huzaifaafzal.me`.
3. Open **Advanced DNS**.
4. Add or update this DNS record:

```text
Type:  CNAME Record
Host:  resume
Value: [YOUR-GITHUB-USERNAME].github.io
TTL:   Automatic
```

Replace `[YOUR-GITHUB-USERNAME]` with the GitHub username that owns the GitHub Pages repository.

Example:

```text
Type:  CNAME Record
Host:  resume
Value: huzaifaafzal.github.io
TTL:   Automatic
```

Do not include `https://` in the Value field.

## 3. Verification

DNS may take a few minutes to several hours to fully update. After it propagates, the site should open at:

```text
https://resume.huzaifaafzal.me
```

If GitHub shows a DNS error, confirm that:

- The `CNAME` file exists in the published site output.
- The `CNAME` file contains only `resume.huzaifaafzal.me`.
- Namecheap has a CNAME record with Host `resume`.
- The CNAME value points to `[YOUR-GITHUB-USERNAME].github.io`.
- There is no conflicting A record or URL Redirect record for the `resume` host.
