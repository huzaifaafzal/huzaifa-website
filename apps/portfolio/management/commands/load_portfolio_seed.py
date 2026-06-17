from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from apps.portfolio.models import (
    Article,
    Certification,
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


class Command(BaseCommand):
    help = "Load polished seed data for Syed Huzaifa Bin Afzal's portfolio."

    def handle(self, *args, **options):
        profile, _ = Profile.objects.update_or_create(
            full_name="Syed Huzaifa Bin Afzal",
            defaults={
                "headline": "AWS Cloud/DevOps Engineer | Cybersecurity & Leadership Graduate Student | Technical Writer",
                "subheadline": (
                    "Building secure, scalable cloud systems and explaining complex ideas clearly."
                ),
                "location": "United States",
                "email": "huzaifaafzal10@gmail.com",
                "phone": "+1 (206) 750-5956",
                "linkedin_url": "https://www.linkedin.com/in/syed-huzaifa-bin-afzal",
                "github_url": "",
                "short_bio": (
                    "AWS Cloud/DevOps engineer, Master of Cybersecurity & Leadership candidate at the "
                    "University of Washington, student journalist, and litigation-support professional."
                ),
                "long_bio": (
                    "Huzaifa works across infrastructure automation, AWS operations, Terraform, Kubernetes, "
                    "CI/CD, monitoring, production reliability, secure AI adoption, technical journalism, "
                    "and high-stakes written analysis. His profile combines production engineering discipline "
                    "with cybersecurity leadership study, public-facing writing, and legal analytical work."
                ),
                "resume_summary": (
                    "Active resumes are managed from Django Admin and can include PDF or DOCX versions for "
                    "cloud, DevOps, AI security, and platform engineering roles."
                ),
                "hero_badges": [
                    "AWS",
                    "Terraform",
                    "Kubernetes",
                    "Django",
                    "Cybersecurity",
                    "UW MCL",
                    "Technical Writing",
                    "Legal Analysis",
                ],
            },
        )

        metrics = [
            ("Cloud/DevOps experience", "5+ yrs", "Production infrastructure, automation, monitoring, and reliability work.", 1),
            ("AWS certified", "AWS SAA", "Certified Solutions Architect Associate with hands-on AWS infrastructure depth.", 2),
            ("Cloud cost reduction", "30%", "Approximate reduction through Trusted Advisor, rightsizing, and planning.", 3),
            ("Cybersecurity leadership", "UW MCL", "Master of Cybersecurity & Leadership candidate, expected June 2026.", 4),
            ("Multi-region exposure", "DR", "Disaster recovery readiness and cross-region reliability work.", 5),
            ("Communication range", "Writing", "Campus news, IT and AI developments, executive interviews, and public-facing analysis.", 6),
        ]
        for label, value, description, order in metrics:
            Metric.objects.update_or_create(label=label, defaults={"value": value, "description": description, "order": order})

        experiences = [
            {
                "company": "Harri",
                "title": "AWS Cloud/DevOps Engineer",
                "location": "Remote / Production SaaS",
                "category": Experience.Category.CLOUD,
                "summary": "Supported production AWS SaaS infrastructure with automation, CI/CD, monitoring, reliability, and cost optimization.",
                "order": 1,
                "bullets": [
                    "Built reusable Terraform modules for AWS API Gateway, CloudFront, Route 53, OpenSearch, and Redshift.",
                    "Supported IAM/RBAC, SSO, Systems Manager, CI/CD workflows, monitoring, and operational runbooks.",
                    "Worked on OpenSearch cross-cluster replication, Redis upgrades, disaster recovery readiness, and multi-region reliability improvements.",
                    "Used Trusted Advisor, Cost Optimization Hub, reservation planning, and rightsizing to reduce spend by approximately 30%.",
                ],
            },
            {
                "company": "Visionet Systems",
                "title": "Cloud/DevOps Engineer",
                "location": "Cloud engineering",
                "category": Experience.Category.CLOUD,
                "summary": "Built AWS automation and CI/CD workflows for cloud workloads, patching, validation, and containerized deployments.",
                "order": 2,
                "bullets": [
                    "Automated AWS patching, scheduling, validation, and maintenance workflows with Systems Manager, Lambda, Python, Bash, and PowerShell.",
                    "Built and maintained Jenkins pipelines and observability using CloudWatch and Datadog.",
                    "Provisioned AWS EMR and ECS workloads using Terraform, Docker, ECS, ALB, Route 53, and Fargate.",
                    "Supported migration of Spark/HDP workloads from EC2 to EMR to improve scalability and operations.",
                ],
            },
            {
                "company": "University of Washington",
                "title": "Student News Reporter",
                "location": "Tacoma, Washington",
                "category": Experience.Category.JOURNALISM,
                "summary": "Reports on campus news, student life, IT, AI developments, and public-facing technology stories.",
                "order": 3,
                "bullets": [
                    "Covers campus news, student life, IT, and AI developments for a University of Washington student audience.",
                    "Interviews university leaders and translates technical AI and IT topics into clear public-facing stories.",
                    "Builds communication range through reporting, podcast conversations, and technical storytelling.",
                ],
            },
            {
                "company": "Litigation Support / Legal Drafting",
                "title": "Legal Analyst / Litigation Support Professional",
                "location": "United States",
                "category": Experience.Category.LEGAL,
                "summary": "Supports high-stakes written analysis, factual synthesis, discovery review, and structured legal drafting.",
                "order": 4,
                "bullets": [
                    "Prepared motion drafting support, case chronology, issue spotting, and structured factual analysis.",
                    "Reviewed discovery materials and synthesized complex factual records into usable written work.",
                    "Supported client communications and high-stakes written analysis with careful attention to detail.",
                ],
            },
        ]
        for item in experiences:
            exp, _ = Experience.objects.update_or_create(
                company=item["company"],
                title=item["title"],
                defaults={
                    "location": item["location"],
                    "category": item["category"],
                    "summary": item["summary"],
                    "order": item["order"],
                    "is_current": item["company"] == "University of Washington",
                },
            )
            exp.bullets.all().delete()
            for order, text in enumerate(item["bullets"], start=1):
                ExperienceBullet.objects.create(experience=exp, text=text, order=order)

        education = [
            ("University of Washington", "Master of Cybersecurity & Leadership", "Cybersecurity & Leadership", "Expected June 2026. GPA 3.99. Beta Gamma Sigma. Upsilon Pi Epsilon.", 1),
            ("GIKI", "B.S. Computer Science", "Computer Science", "Ghulam Ishaq Khan Institute of Engineering Sciences and Technology.", 2),
        ]
        for school, degree, field, description, order in education:
            Education.objects.update_or_create(school=school, degree=degree, defaults={"field": field, "description": description, "order": order})

        certifications = [
            ("AWS Certified Solutions Architect - Associate", "Amazon Web Services", 1),
            ("Oracle Cloud Infrastructure Architect - Professional", "Oracle", 2),
            ("Oracle Cloud Infrastructure Developer - Associate", "Oracle", 3),
            ("Foundations for Cybersecurity Analytics", "University of Washington", 4),
        ]
        for name, issuer, order in certifications:
            Certification.objects.update_or_create(name=name, defaults={"issuer": issuer, "order": order})

        skill_groups = {
            "Cloud": ["AWS", "EC2", "S3", "VPC", "IAM", "RDS", "Aurora", "Route 53", "Lambda", "CloudWatch", "OpenSearch", "ElastiCache"],
            "Infrastructure": ["Terraform", "Docker", "Kubernetes", "EKS", "ECS", "Jenkins", "CI/CD", "Systems Manager"],
            "Programming/Scripting": ["Python", "Bash", "PowerShell", "Groovy", "Java", "SQL"],
            "Data/Databases": ["PostgreSQL", "Aurora", "Redis", "OpenSearch", "DynamoDB", "Redshift"],
            "Security": ["IAM", "Network security", "Cloud security", "Cybersecurity leadership", "AI governance", "Access control"],
            "Communication": ["Technical writing", "Journalism", "Executive interviews", "Legal analysis", "Client communications", "Runbooks"],
        }
        for group_order, (name, skills) in enumerate(skill_groups.items(), start=1):
            category, _ = SkillCategory.objects.update_or_create(
                name=name,
                defaults={"description": f"{name} capabilities presented as a recruiter-friendly skill matrix.", "order": group_order},
            )
            for order, skill in enumerate(skills, start=1):
                Skill.objects.update_or_create(
                    category=category,
                    name=skill,
                    defaults={"order": order, "featured": order <= 4, "proficiency": 90 if order <= 4 else 75},
                )

        projects = [
            ("Dynamic Portfolio Platform", "Django / Portfolio", "This deployable Django portfolio with Admin-managed content, PostgreSQL, WhiteNoise, Docker, and Coolify-ready settings.", ["Django", "PostgreSQL", "Docker", "WhiteNoise"], True, 1),
            ("Django SaaS / Business Platform", "Django / SaaS", "A business-platform pattern for authenticated workflows, structured data, admin operations, and production deployment.", ["Django", "PostgreSQL", "Gunicorn"], True, 2),
            ("AWS Infrastructure Automation", "Cloud / DevOps", "Reusable Terraform and AWS automation patterns for production infrastructure consistency and faster provisioning.", ["AWS", "Terraform", "Jenkins", "CloudWatch"], True, 3),
            ("EKS Deployment Workflow", "Kubernetes / Platform", "Container deployment workflow emphasizing repeatable build, release, and operational visibility patterns.", ["Kubernetes", "EKS", "Docker", "CI/CD"], True, 4),
            ("Cloud Cost Optimization Dashboard", "FinOps / Analytics", "Cost visibility and reporting workflows using AWS recommendations, reservation planning, storage inventory, and analytics.", ["AWS", "Redshift", "Superset", "S3 Inventory"], True, 5),
            ("Disaster Recovery Architecture", "Reliability / DR", "Multi-region reliability and disaster recovery readiness patterns for production cloud services.", ["AWS", "OpenSearch", "Redis", "Route 53"], True, 6),
            ("UW AI / Technology Reporting Archive", "Writing / Journalism", "Public-facing reporting and interviews on UW technology, AI, student life, and institutional change.", ["Writing", "Interviews", "AI", "UW"], False, 7),
        ]
        for title, project_type, description, technologies, featured, order in projects:
            Project.objects.update_or_create(
                title=title,
                defaults={
                    "short_description": description,
                    "full_description": description,
                    "problem": "Teams need credible systems, clear documentation, and deployable work that survives production constraints.",
                    "solution": "Use practical automation, strong defaults, operational visibility, and clean writing to make complex systems usable.",
                    "impact": "Improves recruiter visibility, admin maintainability, and the ability to explain infrastructure decisions clearly.",
                    "technologies": technologies,
                    "project_type": project_type,
                    "featured": featured,
                    "order": order,
                },
            )

        articles = [
            (
                "Building the future with AI: Purple UW students join forces with UW-IT",
                "The Tacoma Ledger",
                "Reporting on UW Purple, student involvement, and AI adoption across the University of Washington.",
                "https://thetacomaledger.com/2025/10/13/building-the-future-with-ai-purple-uw-students-join-forces-with-uw-it-to-shape-next-gen-ai/",
                True,
                1,
            ),
            ("Campus technology and AI reporting", "University of Washington", "Coverage of student life, campus news, IT, AI developments, and executive conversations.", "", True, 2),
            ("Executive interviews and podcast conversations", "University of Washington", "Interview-driven work that turns complex technical and institutional topics into readable public stories.", "", True, 3),
        ]
        for title, publication, summary, external_url, featured, order in articles:
            Article.objects.update_or_create(
                title=title,
                defaults={"publication": publication, "summary": summary, "external_url": external_url, "featured": featured, "order": order},
            )

        self.seed_resumes()
        self.stdout.write(self.style.SUCCESS(f"Portfolio seed loaded for {profile.full_name}."))

    def seed_resumes(self):
        resume_dir = Path(settings.BASE_DIR) / "assets" / "resumes"
        if not resume_dir.exists():
            return
        for path in resume_dir.glob("Syed_Huzaifa_Afzal_*"):
            file_type = path.suffix.lower().lstrip(".").upper()
            if file_type not in {"PDF", "DOCX"}:
                continue
            title = path.stem.replace("_", " ")
            resume, created = ResumeFile.objects.get_or_create(
                title=title,
                defaults={"file_type": file_type, "is_active": True},
            )
            if created or not resume.file:
                with path.open("rb") as source:
                    resume.file.save(path.name, File(source), save=True)
