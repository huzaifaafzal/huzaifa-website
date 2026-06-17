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

const header = document.querySelector("[data-header]");

if (header && "IntersectionObserver" in window) {
  const sentinel = document.createElement("div");
  sentinel.setAttribute("aria-hidden", "true");
  document.body.prepend(sentinel);

  new IntersectionObserver(([entry]) => {
    header.dataset.scrolled = String(!entry.isIntersecting);
  }).observe(sentinel);
}

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const revealTargets = document.querySelectorAll(".reveal-panel, .reveal-section");

if ("IntersectionObserver" in window) {
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.16 }
  );

  revealTargets.forEach((target) => revealObserver.observe(target));
} else {
  revealTargets.forEach((target) => target.classList.add("is-visible"));
}

const applySkillReadout = (button, titleSelector, copySelector) => {
  const title = document.querySelector(titleSelector);
  const copy = document.querySelector(copySelector);

  if (!title || !copy) return;

  title.textContent = button.dataset.skillTitle || button.textContent.trim();
  copy.textContent = button.dataset.skillCopy || "";
};

document.querySelectorAll("[data-skill-grid] button").forEach((button) => {
  ["mouseenter", "focus"].forEach((eventName) => {
    button.addEventListener(eventName, () => {
      applySkillReadout(button, "#skill-readout-title", "#skill-readout-copy");
    });
  });
});

const deckKeys = document.querySelectorAll(".skill-key");

deckKeys.forEach((button) => {
  const activate = () => {
    deckKeys.forEach((key) => key.classList.remove("is-active"));
    button.classList.add("is-active");
    applySkillReadout(button, "#deck-skill-title", "#deck-skill-copy");
  };

  ["mouseenter", "focus", "click"].forEach((eventName) => {
    button.addEventListener(eventName, activate);
  });
});

document.querySelectorAll(".tilt-card").forEach((card) => {
  if (prefersReducedMotion) return;

  card.addEventListener("pointermove", (event) => {
    const rect = card.getBoundingClientRect();
    const x = (event.clientX - rect.left) / rect.width;
    const y = (event.clientY - rect.top) / rect.height;
    const rotateX = (0.5 - y) * 7;
    const rotateY = (x - 0.5) * 9;

    card.style.setProperty("--mx", `${x * 100}%`);
    card.style.setProperty("--my", `${y * 100}%`);
    card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-3px)`;
  });

  card.addEventListener("pointerleave", () => {
    card.style.transform = "";
  });
});

const canvas = document.querySelector("[data-network-canvas]");

if (canvas && !prefersReducedMotion) {
  const context = canvas.getContext("2d");
  const particles = [];
  const pointer = { x: 0.5, y: 0.35 };
  let width = 0;
  let height = 0;
  let pixelRatio = 1;

  const resizeCanvas = () => {
    const rect = canvas.getBoundingClientRect();
    pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
    width = rect.width;
    height = rect.height;
    canvas.width = Math.floor(width * pixelRatio);
    canvas.height = Math.floor(height * pixelRatio);
    context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);

    const targetCount = Math.max(46, Math.min(90, Math.floor(width / 18)));
    particles.length = 0;

    for (let index = 0; index < targetCount; index += 1) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.28,
        vy: (Math.random() - 0.5) * 0.28,
        radius: 1 + Math.random() * 1.8
      });
    }
  };

  const draw = () => {
    context.clearRect(0, 0, width, height);

    const glowX = pointer.x * width;
    const glowY = pointer.y * height;
    const gradient = context.createRadialGradient(glowX, glowY, 0, glowX, glowY, Math.max(width, height) * 0.52);
    gradient.addColorStop(0, "rgba(66, 232, 244, 0.18)");
    gradient.addColorStop(0.35, "rgba(74, 140, 255, 0.08)");
    gradient.addColorStop(1, "rgba(5, 9, 20, 0)");
    context.fillStyle = gradient;
    context.fillRect(0, 0, width, height);

    particles.forEach((particle, index) => {
      particle.x += particle.vx;
      particle.y += particle.vy;

      if (particle.x < 0 || particle.x > width) particle.vx *= -1;
      if (particle.y < 0 || particle.y > height) particle.vy *= -1;

      for (let nextIndex = index + 1; nextIndex < particles.length; nextIndex += 1) {
        const next = particles[nextIndex];
        const dx = particle.x - next.x;
        const dy = particle.y - next.y;
        const distance = Math.hypot(dx, dy);

        if (distance < 132) {
          context.strokeStyle = `rgba(66, 232, 244, ${0.12 * (1 - distance / 132)})`;
          context.lineWidth = 1;
          context.beginPath();
          context.moveTo(particle.x, particle.y);
          context.lineTo(next.x, next.y);
          context.stroke();
        }
      }

      context.fillStyle = "rgba(219, 234, 254, 0.72)";
      context.beginPath();
      context.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
      context.fill();
    });

    requestAnimationFrame(draw);
  };

  window.addEventListener("resize", resizeCanvas);
  window.addEventListener("pointermove", (event) => {
    pointer.x = event.clientX / window.innerWidth;
    pointer.y = event.clientY / window.innerHeight;
  });

  resizeCanvas();
  draw();
}
