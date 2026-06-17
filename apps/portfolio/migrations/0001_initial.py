# Generated for the Coolify Django portfolio scaffold.
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("title", models.CharField(max_length=220)),
                ("slug", models.SlugField(blank=True, max_length=240, unique=True)),
                ("publication", models.CharField(max_length=160)),
                ("published_date", models.DateField(blank=True, null=True)),
                ("summary", models.TextField()),
                ("external_url", models.URLField(blank=True)),
                ("body", models.TextField(blank=True)),
                ("featured", models.BooleanField(default=False)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Certification",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("name", models.CharField(max_length=180)),
                ("issuer", models.CharField(max_length=180)),
                ("issue_date", models.DateField(blank=True, null=True)),
                ("credential_url", models.URLField(blank=True)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=180)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("school", models.CharField(max_length=180)),
                ("degree", models.CharField(max_length=180)),
                ("field", models.CharField(blank=True, max_length=160)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("company", models.CharField(max_length=160)),
                ("title", models.CharField(max_length=180)),
                ("location", models.CharField(blank=True, max_length=160)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("is_current", models.BooleanField(default=False)),
                ("summary", models.TextField()),
                ("category", models.CharField(choices=[("cloud", "Cloud / DevOps"), ("journalism", "Writing / Journalism"), ("ai_research", "AI Research / Academic"), ("security", "Cybersecurity")], default="cloud", max_length=30)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Metric",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("label", models.CharField(max_length=120)),
                ("value", models.CharField(max_length=40)),
                ("description", models.TextField()),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=160)),
                ("headline", models.CharField(max_length=220)),
                ("subheadline", models.TextField()),
                ("location", models.CharField(max_length=160)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("linkedin_url", models.URLField(blank=True)),
                ("github_url", models.URLField(blank=True)),
                ("short_bio", models.TextField()),
                ("long_bio", models.TextField()),
                ("profile_image", models.ImageField(blank=True, upload_to="profile/")),
                ("resume_summary", models.TextField(blank=True)),
                ("hero_badges", models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(blank=True, max_length=200, unique=True)),
                ("short_description", models.TextField()),
                ("full_description", models.TextField(blank=True)),
                ("problem", models.TextField(blank=True)),
                ("solution", models.TextField(blank=True)),
                ("impact", models.TextField(blank=True)),
                ("technologies", models.JSONField(blank=True, default=list)),
                ("project_type", models.CharField(max_length=120)),
                ("github_url", models.URLField(blank=True)),
                ("live_url", models.URLField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="projects/")),
                ("featured", models.BooleanField(default=False)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="ResumeFile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("file", models.FileField(upload_to="resumes/")),
                ("file_type", models.CharField(choices=[("PDF", "PDF"), ("DOCX", "DOCX")], max_length=10)),
                ("is_active", models.BooleanField(default=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-is_active", "-uploaded_at"]},
        ),
        migrations.CreateModel(
            name="SkillCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
            ],
            options={"verbose_name_plural": "skill categories", "ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="ExperienceBullet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("text", models.TextField()),
                ("experience", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="bullets", to="portfolio.experience")),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("name", models.CharField(max_length=120)),
                ("proficiency", models.PositiveIntegerField(blank=True, null=True)),
                ("featured", models.BooleanField(default=False)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="skills", to="portfolio.skillcategory")),
            ],
            options={"ordering": ["order", "id"]},
        ),
    ]
