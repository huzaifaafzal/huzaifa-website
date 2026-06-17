from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class Profile(models.Model):
    full_name = models.CharField(max_length=160)
    headline = models.CharField(max_length=220)
    subheadline = models.TextField()
    location = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    short_bio = models.TextField()
    long_bio = models.TextField()
    profile_image = models.ImageField(upload_to="profile/", blank=True)
    resume_summary = models.TextField(blank=True)
    hero_badges = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.full_name


class Metric(OrderedModel):
    label = models.CharField(max_length=120)
    value = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return f"{self.value} {self.label}"


class Experience(OrderedModel):
    class Category(models.TextChoices):
        CLOUD = "cloud", "Cloud / DevOps"
        JOURNALISM = "journalism", "Writing / Journalism"
        AI_RESEARCH = "ai_research", "AI Research / Academic"
        SECURITY = "security", "Cybersecurity"

    company = models.CharField(max_length=160)
    title = models.CharField(max_length=180)
    location = models.CharField(max_length=160, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    summary = models.TextField()
    category = models.CharField(max_length=30, choices=Category.choices, default=Category.CLOUD)

    def __str__(self):
        return f"{self.title} at {self.company}"


class ExperienceBullet(OrderedModel):
    experience = models.ForeignKey(Experience, related_name="bullets", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:80]


class Education(OrderedModel):
    school = models.CharField(max_length=180)
    degree = models.CharField(max_length=180)
    field = models.CharField(max_length=160, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree}, {self.school}"


class Certification(OrderedModel):
    name = models.CharField(max_length=180)
    issuer = models.CharField(max_length=180)
    issue_date = models.DateField(null=True, blank=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class SkillCategory(OrderedModel):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name_plural = "skill categories"

    def __str__(self):
        return self.name


class Skill(OrderedModel):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    proficiency = models.PositiveIntegerField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(OrderedModel):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField()
    full_description = models.TextField(blank=True)
    problem = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    impact = models.TextField(blank=True)
    technologies = models.JSONField(default=list, blank=True)
    project_type = models.CharField(max_length=120)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Article(OrderedModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    publication = models.CharField(max_length=160)
    published_date = models.DateField(null=True, blank=True)
    summary = models.TextField()
    external_url = models.URLField(blank=True)
    body = models.TextField(blank=True)
    featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class ResumeFile(models.Model):
    class FileType(models.TextChoices):
        PDF = "PDF", "PDF"
        DOCX = "DOCX", "DOCX"

    title = models.CharField(max_length=160)
    file = models.FileField(upload_to="resumes/")
    file_type = models.CharField(max_length=10, choices=FileType.choices)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_active", "-uploaded_at"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
