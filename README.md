# Huzaifa Portfolio

Premium dynamic portfolio for **Syed Huzaifa Bin Afzal**. The site is now a Django application built for Coolify on a DigitalOcean Droplet, with PostgreSQL, Docker, Gunicorn, WhiteNoise, Admin-managed content, resume uploads, and a polished recruiter-facing frontend.

## What This Project Includes

- Django 5 portfolio app with production settings
- Admin-managed profile, metrics, experience, education, certifications, skills, projects, writing, resume files, and contact messages
- Premium dark-first responsive UI with lightweight CSS and JavaScript
- Contact form that saves messages to the database
- Project and writing detail pages with slugs
- Resume downloads for PDF and DOCX files
- SEO basics: meta tags, canonical URL, Open Graph tags, robots.txt, sitemap.xml, and Person JSON-LD
- Dockerfile and entrypoint for Coolify deployment
- Seed command for polished starter content

## Tech Stack

- Python 3.12
- Django 5.x
- PostgreSQL
- Gunicorn
- WhiteNoise
- dj-database-url
- Pillow
- python-dotenv
- Docker
- Coolify reverse proxy and HTTPS

## Project Structure

```text
.
|-- apps/
|   |-- core/
|   `-- portfolio/
|       |-- management/commands/load_portfolio_seed.py
|       |-- migrations/
|       |-- admin.py
|       |-- forms.py
|       |-- models.py
|       |-- urls.py
|       `-- views.py
|-- assets/
|   |-- images/
|   `-- resumes/
|-- config/
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- static/
|   |-- css/site.css
|   `-- js/site.js
|-- templates/
|-- Dockerfile
|-- entrypoint.sh
|-- manage.py
|-- requirements.txt
`-- DEPLOYMENT.md
```

The `assets/` folder is intentionally kept. It provides the abstract visual and the three active master CV files used by the app and seed command:

- `Syed_Huzaifa_Afzal_Master_CV_Cloud_DevOps_Engineer.pdf`
- `Syed_Huzaifa_Afzal_Master_CV_AI_Engineer.pdf`
- `Syed_Huzaifa_Afzal_Master_CV_AI_Research_Academic.pdf`

## Environment Variables

Copy `.env.example` to `.env` for local development, or add these in Coolify:

```text
DEBUG=False
SECRET_KEY=replace-with-a-long-random-secret
ALLOWED_HOSTS=resume.huzaifaafzal.me,localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=https://resume.huzaifaafzal.me,http://localhost:8000,http://127.0.0.1:8000
SITE_URL=https://resume.huzaifaafzal.me
DATABASE_URL=postgres://USER:PASSWORD@HOST:5432/DATABASE
LOAD_SEED_DATA=1
GUNICORN_WORKERS=3
GUNICORN_TIMEOUT=60
```

For production, use the internal PostgreSQL connection string provided by Coolify as `DATABASE_URL`.

## Local Development

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py load_portfolio_seed
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Open:

```text
http://127.0.0.1:8000
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

## Main Routes

- `/`
- `/about/`
- `/experience/`
- `/projects/`
- `/projects/<slug>/`
- `/writing/`
- `/writing/<slug>/`
- `/resume/`
- `/contact/`
- `/health/`
- `/robots.txt`
- `/sitemap.xml`

## Seed Data

Run this command to load polished starter content for Syed Huzaifa Bin Afzal:

```bash
python manage.py load_portfolio_seed
```

It creates or updates:

- Profile
- Impact metrics
- Experience timeline and bullets
- Education
- Certifications
- Skill categories and skills
- Featured projects
- Writing samples
- Three active resume/CV records from `assets/resumes/`: Cloud / DevOps Engineer, AI Engineer, and AI Research / Academic Roles

In Coolify, set `LOAD_SEED_DATA=1` for the first deployment. After the data appears, set it to `0` so later deploys do not refresh seed-managed records.

## Coolify Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for the complete setup. Short version:

1. Create a Coolify application from the GitHub repository.
2. Deploy the `coolify` branch with the Dockerfile.
3. Set app port to `8000`.
4. Attach a separate Coolify PostgreSQL resource.
5. Add persistent storage for `/app/media`.
6. Add the domain `resume.huzaifaafzal.me`.
7. Configure environment variables.
8. Deploy.

The container entrypoint runs migrations, collects static files, optionally loads seed data, and starts Gunicorn on `0.0.0.0:8000`.

## Content Management

Use Django Admin to keep the portfolio dynamic:

- Edit the personal profile and hero badges
- Add metrics for recruiter-facing proof points
- Manage experience timeline entries and bullet points
- Add or edit projects and case studies
- Add writing and journalism entries
- Upload active resume files as PDF or DOCX
- Review contact form submissions

Create the first admin user with:

```bash
python manage.py createsuperuser
```
