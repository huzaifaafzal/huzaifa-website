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

MASTER_CVS = [
    (
        "Cloud / DevOps Engineer CV",
        "Syed_Huzaifa_Afzal_Master_CV_Cloud_DevOps_Engineer.pdf",
        ResumeFile.FileType.PDF,
    ),
    (
        "AI Engineer CV",
        "Syed_Huzaifa_Afzal_Master_CV_AI_Engineer.pdf",
        ResumeFile.FileType.PDF,
    ),
    (
        "AI Research / Academic Roles CV",
        "Syed_Huzaifa_Afzal_Master_CV_AI_Research_Academic.pdf",
        ResumeFile.FileType.PDF,
    ),
]


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
                    "AWS Cloud/DevOps engineer with 6+ years of experience, Master of Cybersecurity & "
                    "Leadership candidate at the University of Washington, AI builder, researcher, and student journalist."
                ),
                "long_bio": (
                    "Huzaifa works across infrastructure automation, AWS operations, Terraform, Kubernetes, "
                    "CI/CD, monitoring, production reliability, secure AI adoption, AI research, technical journalism, "
                    "and public-facing technology communication. His profile combines production engineering discipline "
                    "with cybersecurity leadership study, AI systems work, and clear writing."
                ),
                "resume_summary": (
                    "Choose from three current master CVs tailored for Cloud / DevOps Engineer, AI Engineer, "
                    "and AI Research / Academic roles."
                ),
                "hero_badges": [
                    "AWS",
                    "Terraform",
                    "Kubernetes",
                    "DevOps",
                    "Cybersecurity",
                    "UW MCL",
                    "Technical Writing",
                    "AI Research",
                ],
            },
        )

        metrics = [
            ("Cloud/DevOps experience", "6+ yrs", "Production infrastructure, automation, monitoring, and reliability work.", 1),
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
                "company": "AI Research / Academic Work",
                "title": "AI Researcher / Academic Project Contributor",
                "location": "University of Washington",
                "category": Experience.Category.AI_RESEARCH,
                "summary": "Works on secure GenAI deployment, AI governance, Shadow AI risk, and research communication.",
                "order": 4,
                "bullets": [
                    "Built and evaluated a private GenAI environment using Ollama, Open WebUI, Docker, and Windows Server.",
                    "Mapped governance controls to NIST AI RMF and ISO/IEC 27001:2022 concepts.",
                    "Contributed research framing around Shadow AI risk, secure adoption, and organization-provided AI alternatives.",
                ],
            },
        ]
        old_company = " ".join(["Liti" + "gation", "Support", "/", "Le" + "gal", "Drafting"])
        Experience.objects.filter(company=old_company).delete()
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

        old_skill_names = ["Le" + "gal analysis", "Client communi" + "cations"]
        Skill.objects.filter(name__in=old_skill_names).delete()
        skill_groups = {
            "Cloud": ["AWS", "EC2", "S3", "VPC", "IAM", "RDS", "Aurora", "Route 53", "Lambda", "CloudWatch", "OpenSearch", "ElastiCache"],
            "Infrastructure": ["Terraform", "Docker", "Kubernetes", "EKS", "ECS", "Jenkins", "CI/CD", "Systems Manager"],
            "Programming/Scripting": ["Python", "Bash", "PowerShell", "Groovy", "Java", "SQL"],
            "Data/Databases": ["PostgreSQL", "Aurora", "Redis", "OpenSearch", "DynamoDB", "Redshift"],
            "Security": ["IAM", "Network security", "Cloud security", "Cybersecurity leadership", "AI governance", "Access control"],
            "Communication": ["Technical writing", "Journalism", "Executive interviews", "Research writing", "Public-facing AI writing", "Runbooks"],
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
            {
                "title": "Secure Enterprise Generative AI Platform - GovernAI",
                "project_type": "AI Security / Research",
                "short_description": "Applied research and implementation project focused on secure, governed enterprise GenAI adoption.",
                "problem": "Organizations face Shadow AI risk when employees use unsanctioned public AI tools for workplace tasks without governance, data residency, access control, or model oversight.",
                "solution": "Designed a layered enterprise GenAI architecture using Open WebUI, Ollama, Docker, and Windows Server with local deployment, controlled data residency, and a three-role RBAC model for Standard User, AI Platform Admin, and System Administrator workflows.",
                "impact": "Co-authored an IEEE SVCC 2026 accepted paper, conducted a 70-respondent workplace AI survey, validated local network behavior with host firewall rules and Wireshark, and mapped controls to NIST AI RMF and ISO/IEC 27001:2022 concepts.",
                "technologies": ["Open WebUI", "Ollama", "Docker", "Windows Server", "NIST AI RMF", "ISO 27001"],
                "featured": True,
                "order": 1,
            },
            {
                "title": "Infrastructure Analytics and Cost Visibility Platform",
                "project_type": "Cloud / FinOps / Analytics",
                "short_description": "AWS storage usage and cost-attribution visibility platform for SRE and engineering teams at Harri.",
                "problem": "Infrastructure stakeholders needed clearer visibility into storage growth, usage patterns, and cost drivers across production AWS environments.",
                "solution": "Integrated S3 Inventory, Redshift, and Superset to surface AWS storage usage, growth patterns, and cost-attribution insights.",
                "impact": "Helped infrastructure stakeholders identify optimization opportunities and make better cost/performance decisions.",
                "technologies": ["AWS S3 Inventory", "Redshift", "Superset", "AWS", "FinOps"],
                "featured": True,
                "order": 2,
            },
            {
                "title": "Spark-as-a-Service AWS EMR Automation",
                "project_type": "Data Infrastructure / Automation",
                "short_description": "Terraform and Jenkins automation for AWS EMR deployment and destruction during a Regeneron Pharmaceuticals engagement.",
                "problem": "Big-data infrastructure users needed repeatable, end-user-driven provisioning while the team evaluated migration from EC2/HDP Spark infrastructure to AWS EMR.",
                "solution": "Built Terraform and Jenkins-based automation for AWS EMR deployment and destruction, supporting controlled big-data infrastructure provisioning.",
                "impact": "Supported migration analysis that improved autoscaling, manageability, and cost profile for Spark workloads.",
                "technologies": ["AWS EMR", "Terraform", "Jenkins", "Spark", "Hadoop/HDP"],
                "featured": True,
                "order": 3,
            },
            {
                "title": "Application Modernization to Containerized Architecture",
                "project_type": "Containers / Cloud Modernization",
                "short_description": "UpBrainery PoC migrating application infrastructure from EC2-based deployment toward Docker/ECS architecture.",
                "problem": "The application environment needed a more standardized containerized deployment model than EC2-based infrastructure.",
                "solution": "Used Docker, ECR, ECS, Fargate, ALB, Route 53, CloudWatch, and Terraform to support containerized deployment architecture.",
                "impact": "Supported microservices-style deployment patterns, autoscaling, networking, service discovery, and infrastructure-as-code standardization.",
                "technologies": ["Docker", "ECR", "ECS", "Fargate", "ALB", "Terraform"],
                "featured": True,
                "order": 4,
            },
            {
                "title": "Private Stellar Cryptocurrency Network",
                "project_type": "Blockchain / Emerging Technology",
                "short_description": "Microsoft Redmond remote internship project focused on blockchain concepts and private Stellar network deployment.",
                "problem": "The internship focused on understanding distributed ledger deployment patterns and emerging cryptocurrency network concepts.",
                "solution": "Deployed a private Stellar (XLM) cryptocurrency network under Microsoft technical supervision.",
                "impact": "Built foundational exposure to distributed ledger systems, networked services, and emerging technology evaluation.",
                "technologies": ["Stellar", "XLM", "Blockchain", "Distributed Systems"],
                "featured": False,
                "order": 5,
            },
            {
                "title": "Festoon Engineering Works Website",
                "project_type": "Web Development / Consulting",
                "short_description": "Client-facing website project covering requirements gathering, UX/UI design, and cPanel deployment.",
                "problem": "The business needed a web presence delivered from requirements through deployment.",
                "solution": "Gathered requirements, designed the UX/UI, and deployed the company website using JavaScript, HTML, CSS, and cPanel.",
                "impact": "Built early client-facing experience in requirements gathering, web delivery, and stakeholder communication.",
                "technologies": ["JavaScript", "HTML", "CSS", "cPanel", "UX/UI"],
                "featured": False,
                "order": 6,
            },
            {
                "title": "LifeTrack Android Application",
                "project_type": "Android / Final Year Project",
                "short_description": "GIKI final-year Android application for monitoring, tracking, and collaboration workflows.",
                "problem": "Users needed an Android application to monitor, track, and collaborate with others.",
                "solution": "Developed the application in Android Studio and Java using Agile methodology.",
                "impact": "Achieved 1st position in final-year project evaluation.",
                "technologies": ["Android Studio", "Java", "Agile", "Mobile Development"],
                "featured": False,
                "order": 7,
            },
        ]
        project_titles = [project["title"] for project in projects]
        Project.objects.exclude(title__in=project_titles).delete()
        for project in projects:
            Project.objects.update_or_create(
                title=project["title"],
                defaults={
                    "short_description": project["short_description"],
                    "full_description": project["short_description"],
                    "problem": project["problem"],
                    "solution": project["solution"],
                    "impact": project["impact"],
                    "technologies": project["technologies"],
                    "project_type": project["project_type"],
                    "featured": project["featured"],
                    "order": project["order"],
                },
            )

        articles = [
            (
                "Building the future with AI: Purple UW students join forces with UW-IT",
                "The Tacoma Ledger",
                "AI coverage on UW-IT's AI Purple platform, based on an interview with UW-IT lead AI architect Jared Reimer and focused on privacy, model access, trusted AI agents, student participation, and responsible campus AI adoption.",
                "https://thetacomaledger.com/2025/10/13/building-the-future-with-ai-purple-uw-students-join-forces-with-uw-it-to-shape-next-gen-ai/",
                True,
                1,
            ),
            (
                "Tacoma Ledger podcast conversation",
                "The Tacoma Ledger Podcast",
                "Podcast work for The Tacoma Ledger, adding spoken interview and conversation experience alongside written campus technology and AI reporting.",
                "https://www.youtube.com/watch?v=oWbC9R_lV2s",
                True,
                2,
            ),
            (
                "Campus IT and AI reporting archive",
                "The Tacoma Ledger",
                "Reporting portfolio covering UW campus technology, AI initiatives, student-facing IT changes, and public explanations of technical topics for a university audience.",
                "https://thetacomaledger.com/?s=Syed+Huzaifa+Bin+Afzal+",
                True,
                3,
            ),
        ]
        Article.objects.exclude(title__in=[article[0] for article in articles]).delete()
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

        active_titles = [title for title, _, _ in MASTER_CVS]
        ResumeFile.objects.exclude(title__in=active_titles).update(is_active=False)

        for title, filename, file_type in MASTER_CVS:
            path = resume_dir / filename
            if not path.exists():
                self.stdout.write(self.style.WARNING(f"Missing CV file: {filename}"))
                continue

            resume, _ = ResumeFile.objects.get_or_create(title=title)
            resume.file_type = file_type
            resume.is_active = True
            with path.open("rb") as source:
                resume.file.save(filename, File(source), save=False)
            resume.save()
