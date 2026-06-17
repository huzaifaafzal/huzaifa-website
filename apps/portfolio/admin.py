from django.contrib import admin

from .models import (
    Article,
    Certification,
    ContactMessage,
    Education,
    Experience,
    ExperienceBullet,
    Metric,
    Profile,
    Project,
    ResumeFile,
    Skill,
    SkillCategory,
)


class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1
    fields = ("text", "order")
    ordering = ("order",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "headline", "location", "email")
    search_fields = ("full_name", "headline", "email", "short_bio")


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "order")
    search_fields = ("label", "description")
    ordering = ("order",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "category", "is_current", "order")
    list_filter = ("category", "is_current")
    search_fields = ("company", "title", "summary", "bullets__text")
    ordering = ("order",)
    inlines = [ExperienceBulletInline]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "field", "order")
    search_fields = ("school", "degree", "field", "description")
    ordering = ("order",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issue_date", "order")
    search_fields = ("name", "issuer")
    ordering = ("order",)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("name", "proficiency", "featured", "order")
    ordering = ("order",)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    search_fields = ("name", "description")
    ordering = ("order",)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "featured", "order")
    list_filter = ("category", "featured")
    search_fields = ("name", "category__name")
    ordering = ("category__order", "order")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "project_type", "featured", "order")
    list_filter = ("project_type", "featured")
    search_fields = ("title", "short_description", "full_description", "problem", "solution", "impact")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "publication", "published_date", "featured", "order")
    list_filter = ("publication", "featured", "published_date")
    search_fields = ("title", "publication", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order",)


@admin.register(ResumeFile)
class ResumeFileAdmin(admin.ModelAdmin):
    list_display = ("title", "file_type", "is_active", "uploaded_at")
    list_filter = ("file_type", "is_active")
    search_fields = ("title",)
    ordering = ("-is_active", "-uploaded_at")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
