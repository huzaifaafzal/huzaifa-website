# Coolify Deployment

This branch deploys the portfolio as a Django 5 application through a Dockerfile.

## Target

- Domain: `https://resume.huzaifaafzal.me`
- Platform: Coolify on a DigitalOcean Droplet
- App port: `8000`
- Database: separate Coolify PostgreSQL resource
- HTTPS and reverse proxy: handled by Coolify
- Persistent uploads: mount `/app/media`

## Coolify App Setup

1. Create a new Coolify application from the GitHub repository and select the `coolify` branch.
2. Use Dockerfile deployment.
3. Set the application port to `8000`.
4. Attach a separate Coolify PostgreSQL resource.
5. Add persistent storage:

```text
Container path: /app/media
```

6. Add the domain:

```text
resume.huzaifaafzal.me
```

## Environment Variables

Use the PostgreSQL internal connection string from Coolify for `DATABASE_URL`.

```text
DEBUG=False
SECRET_KEY=replace-with-a-long-random-secret
ALLOWED_HOSTS=resume.huzaifaafzal.me
CSRF_TRUSTED_ORIGINS=https://resume.huzaifaafzal.me
SITE_URL=https://resume.huzaifaafzal.me
DATABASE_URL=postgres://USER:PASSWORD@HOST:5432/DATABASE
LOAD_SEED_DATA=1
GUNICORN_WORKERS=3
```

Set `LOAD_SEED_DATA=1` for the first deployment to load the polished starter content and resume files. After confirming the site is populated, change it to `0` so future deploys do not refresh seed-managed records.

## Runtime Behavior

`entrypoint.sh` runs:

1. `python manage.py migrate --noinput`
2. `python manage.py collectstatic --noinput`
3. Optional `python manage.py load_portfolio_seed`
4. `gunicorn config.wsgi:application --bind 0.0.0.0:8000`

## Admin

Create an admin user from the Coolify terminal:

```bash
python manage.py createsuperuser
```

Then manage profile content, metrics, experience, projects, articles, resumes, and contact messages at:

```text
https://resume.huzaifaafzal.me/admin/
```
