const roleBriefs = {
  all: {
    kicker: "All roles",
    title: "Hybrid cloud, DevOps, SRE, and secure AI profile",
    copy:
      "Production AWS operations, Terraform automation, CI/CD, observability, cost optimization, disaster recovery, and secure GenAI research in one portfolio.",
    resume: "assets/resumes/Syed_Huzaifa_Afzal_Master_AI_DevOps_Resume.pdf"
  },
  cloud: {
    kicker: "Cloud infrastructure",
    title: "AWS infrastructure, automation, and cost visibility",
    copy:
      "Terraform modules, AWS service automation, EMR/ECS work, IAM patterns, cost optimization, S3 Inventory analytics, and production SaaS support.",
    resume: "assets/resumes/Syed_Huzaifa_Afzal_DevOps_Engineer_CV.pdf"
  },
  sre: {
    kicker: "SRE and operations",
    title: "Reliability work across monitoring, DR, runbooks, and incident follow-up",
    copy:
      "CloudWatch, Datadog, OpenSearch, Redis, disaster recovery readiness, multi-region planning, runbooks, and production troubleshooting.",
    resume: "assets/resumes/Syed_Huzaifa_Afzal_DevOps_Engineer_CV.pdf"
  },
  ai: {
    kicker: "AI security",
    title: "Governed private GenAI deployment and Shadow AI research",
    copy:
      "GovernAI uses Open WebUI, Ollama, Docker, Windows Server, role-based access, Wireshark validation, and NIST AI RMF / ISO 27001 control mapping.",
    resume: "assets/resumes/Syed_Huzaifa_Afzal_AI_Engineer_CV.pdf"
  },
  platform: {
    kicker: "Platform engineering",
    title: "Developer-enabling infrastructure with operational guardrails",
    copy:
      "Reusable infrastructure modules, Jenkins automation, Terraform state handling, deployment validation, containerized workloads, and AWS Systems Manager automation.",
    resume: "assets/resumes/Syed_Huzaifa_Afzal_Master_AI_DevOps_Resume.pdf"
  },
  communication: {
    kicker: "Communication",
    title: "Technical translation through reporting, interviews, and documentation",
    copy:
      "UW reporting, executive interviews, public-facing AI writing, runbooks, stakeholder communication, and practical explanation of AI and infrastructure tradeoffs.",
    resume: "assets/resumes/Syed_Huzaifa_Afzal_Master_AI_DevOps_Resume.pdf"
  }
};

const setText = (selector, text) => {
  const element = document.querySelector(selector);
  if (element) element.textContent = text;
};

const setAttribute = (selector, attribute, value) => {
  const element = document.querySelector(selector);
  if (element) element.setAttribute(attribute, value);
};

setText("#year", new Date().getFullYear());

const navToggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("site-nav");

if (navToggle && nav) {
  navToggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  nav.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      nav.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}

const filterTargets = [...document.querySelectorAll("[data-tags]")];
const roleTabs = [...document.querySelectorAll(".role-tab")];

const applyRoleFilter = (activeFilter) => {
  const brief = roleBriefs[activeFilter] || roleBriefs.all;

  roleTabs.forEach((tab) => {
    const isActive = tab.dataset.filter === activeFilter;
    tab.classList.toggle("active", isActive);
    tab.setAttribute("aria-selected", String(isActive));
  });

  filterTargets.forEach((target) => {
    const tags = (target.dataset.tags || "").split(" ");
    const shouldShow = activeFilter === "all" || tags.includes(activeFilter);
    target.dataset.hiddenByFilter = String(!shouldShow);
  });

  setText("#role-kicker", brief.kicker);
  setText("#role-title", brief.title);
  setText("#role-copy", brief.copy);
  setAttribute("#role-resume", "href", brief.resume);
};

roleTabs.forEach((tab) => {
  tab.addEventListener("click", () => applyRoleFilter(tab.dataset.filter || "all"));
});

document.querySelectorAll(".timeline-summary").forEach((button) => {
  button.addEventListener("click", () => {
    const details = button.parentElement?.querySelector(".timeline-details");
    if (!details) return;

    const isExpanded = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!isExpanded));
    details.hidden = isExpanded;
  });
});

const skillSearch = document.getElementById("skill-search");
const skillGroups = [...document.querySelectorAll(".skill-group")];

if (skillSearch) {
  skillSearch.addEventListener("input", () => {
    const query = skillSearch.value.trim().toLowerCase();

    skillGroups.forEach((group) => {
      const chips = [...group.querySelectorAll(".chips span")];
      let visibleCount = 0;

      chips.forEach((chip) => {
        const isMatch = !query || chip.textContent.toLowerCase().includes(query);
        chip.dataset.hiddenBySearch = String(!isMatch);
        if (isMatch) visibleCount += 1;
      });

      group.dataset.noSkillMatch = String(query && visibleCount === 0);
    });
  });
}

document.querySelectorAll("[data-copy]").forEach((button) => {
  button.addEventListener("click", async () => {
    const value = button.dataset.copy;
    if (!value) return;

    try {
      await navigator.clipboard.writeText(value);
      button.textContent = "Email copied";
    } catch {
      button.textContent = value;
    }

    window.setTimeout(() => {
      button.textContent = "Copy email";
    }, 1800);
  });
});

const navLinks = [...document.querySelectorAll("nav a[href^='#']")];
const observedSections = navLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

if (typeof IntersectionObserver !== "undefined") {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;

        navLinks.forEach((link) => {
          link.classList.toggle("active", link.getAttribute("href") === `#${entry.target.id}`);
        });
      });
    },
    { rootMargin: "-35% 0px -55% 0px", threshold: 0.01 }
  );

  observedSections.forEach((section) => observer.observe(section));
}
