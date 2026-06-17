const year = document.getElementById("year");
if (year) {
  year.textContent = new Date().getFullYear();
}

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

roleTabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const activeFilter = tab.dataset.filter || "all";

    roleTabs.forEach((item) => {
      const isActive = item === tab;
      item.classList.toggle("active", isActive);
      item.setAttribute("aria-selected", String(isActive));
    });

    filterTargets.forEach((target) => {
      const tags = (target.dataset.tags || "").split(" ");
      const shouldShow = activeFilter === "all" || tags.includes(activeFilter);
      target.dataset.hiddenByFilter = String(!shouldShow);
    });
  });
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

const navLinks = [...document.querySelectorAll("nav a[href^='#']")];
const sections = navLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

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

sections.forEach((section) => observer.observe(section));

const canvas = document.getElementById("systems-map");
const context = canvas?.getContext("2d");

if (canvas && context) {
  const nodes = [
    { label: "AWS", x: 0.2, y: 0.28, color: "#58d6c9" },
    { label: "Terraform", x: 0.45, y: 0.18, color: "#88b7ff" },
    { label: "CI/CD", x: 0.72, y: 0.3, color: "#f0c766" },
    { label: "SRE", x: 0.78, y: 0.58, color: "#58d6c9" },
    { label: "GovernAI", x: 0.5, y: 0.66, color: "#ff8a6b" },
    { label: "NIST AI RMF", x: 0.25, y: 0.68, color: "#88b7ff" }
  ];

  const links = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 0],
    [1, 4]
  ];

  const resizeCanvas = () => {
    const rect = canvas.getBoundingClientRect();
    const ratio = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, Math.floor(rect.width * ratio));
    canvas.height = Math.max(1, Math.floor(rect.height * ratio));
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
  };

  const draw = (time = 0) => {
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    context.clearRect(0, 0, width, height);

    const pulse = (Math.sin(time / 900) + 1) / 2;
    context.fillStyle = "rgba(88, 214, 201, 0.04)";
    context.fillRect(0, 0, width, height);

    links.forEach(([from, to], index) => {
      const a = nodes[from];
      const b = nodes[to];
      const ax = a.x * width;
      const ay = a.y * height;
      const bx = b.x * width;
      const by = b.y * height;
      context.beginPath();
      context.moveTo(ax, ay);
      context.lineTo(bx, by);
      context.strokeStyle = `rgba(215, 228, 231, ${0.14 + pulse * 0.08})`;
      context.lineWidth = 1.2;
      context.stroke();

      const progress = ((time / 1600 + index * 0.17) % 1);
      context.beginPath();
      context.arc(ax + (bx - ax) * progress, ay + (by - ay) * progress, 3, 0, Math.PI * 2);
      context.fillStyle = "rgba(88, 214, 201, 0.8)";
      context.fill();
    });

    nodes.forEach((node, index) => {
      const x = node.x * width;
      const y = node.y * height + Math.sin(time / 900 + index) * 5;

      context.beginPath();
      context.arc(x, y, 42, 0, Math.PI * 2);
      context.fillStyle = "rgba(8, 16, 22, 0.86)";
      context.fill();
      context.strokeStyle = node.color;
      context.lineWidth = 2;
      context.stroke();

      context.beginPath();
      context.arc(x, y, 50 + pulse * 5, 0, Math.PI * 2);
      context.strokeStyle = `${node.color}33`;
      context.lineWidth = 1;
      context.stroke();

      context.fillStyle = "#f6fbfc";
      context.font = "700 12px Inter, sans-serif";
      context.textAlign = "center";
      context.textBaseline = "middle";
      context.fillText(node.label, x, y);
    });

    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      requestAnimationFrame(draw);
    }
  };

  resizeCanvas();
  window.addEventListener("resize", resizeCanvas);
  draw();
}
