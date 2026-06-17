from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, TemplateView

from .forms import ContactForm
from .models import (
    Article,
    Certification,
    Education,
    Experience,
    Metric,
    Profile,
    Project,
    ResumeFile,
    SkillCategory,
)


def get_profile():
    return Profile.objects.first()


class PortfolioContextMixin:
    page_title = ""
    meta_description = (
        "Premium portfolio for Syed Huzaifa Bin Afzal, AWS Cloud/DevOps engineer, "
        "cybersecurity leadership graduate student, AI builder, researcher, and technical writer."
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "profile": get_profile(),
                "page_title": self.page_title,
                "meta_description": self.meta_description,
                "site_url": settings.SITE_URL,
            }
        )
        return context


class HomeView(PortfolioContextMixin, TemplateView):
    template_name = "portfolio/home.html"
    page_title = "Cloud, Cybersecurity, and Systems Builder"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "metrics": Metric.objects.all()[:8],
                "experiences": Experience.objects.prefetch_related("bullets").all(),
                "projects": Project.objects.filter(featured=True)[:6],
                "articles": Article.objects.filter(featured=True)[:4],
                "skill_categories": SkillCategory.objects.prefetch_related("skills").all(),
                "resumes": ResumeFile.objects.filter(is_active=True)[:4],
                "education": Education.objects.all(),
                "certifications": Certification.objects.all(),
                "contact_form": ContactForm(),
            }
        )
        return context


class AboutView(PortfolioContextMixin, TemplateView):
    template_name = "portfolio/about.html"
    page_title = "About"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["education"] = Education.objects.all()
        context["certifications"] = Certification.objects.all()
        return context


class ExperienceView(PortfolioContextMixin, ListView):
    template_name = "portfolio/experience.html"
    model = Experience
    context_object_name = "experiences"
    page_title = "Experience"

    def get_queryset(self):
        return Experience.objects.prefetch_related("bullets").all()


class ProjectListView(PortfolioContextMixin, ListView):
    template_name = "portfolio/projects.html"
    model = Project
    context_object_name = "projects"
    page_title = "Projects"


class ProjectDetailView(PortfolioContextMixin, DetailView):
    template_name = "portfolio/project_detail.html"
    model = Project
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.title
        return context


class ArticleListView(PortfolioContextMixin, ListView):
    template_name = "portfolio/writing.html"
    model = Article
    context_object_name = "articles"
    page_title = "Writing"


class ArticleDetailView(PortfolioContextMixin, DetailView):
    template_name = "portfolio/article_detail.html"
    model = Article
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.title
        return context


class ResumeView(PortfolioContextMixin, TemplateView):
    template_name = "portfolio/resume.html"
    page_title = "Resume"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resumes"] = ResumeFile.objects.filter(is_active=True)
        return context


class ContactView(PortfolioContextMixin, FormView):
    template_name = "portfolio/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")
    page_title = "Contact"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thanks. Your message has been saved and Huzaifa can follow up from Django Admin.")
        return super().form_valid(form)


def health_check(request):
    return JsonResponse({"status": "ok"})


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {settings.SITE_URL}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def sitemap_xml(request):
    urls = ["home", "about", "experience", "projects", "writing", "resume", "contact"]
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for name in urls:
        path = reverse_lazy(name)
        body.append(f"<url><loc>{settings.SITE_URL}{path}</loc></url>")
    for project in Project.objects.all():
        body.append(f"<url><loc>{settings.SITE_URL}{project.get_absolute_url()}</loc></url>")
    for article in Article.objects.all():
        body.append(f"<url><loc>{settings.SITE_URL}{article.get_absolute_url()}</loc></url>")
    body.append("</urlset>")
    return HttpResponse("\n".join(body), content_type="application/xml")
