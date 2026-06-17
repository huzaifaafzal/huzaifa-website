from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("experience/", views.ExperienceView.as_view(), name="experience"),
    path("projects/", views.ProjectListView.as_view(), name="projects"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("writing/", views.ArticleListView.as_view(), name="writing"),
    path("writing/<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
