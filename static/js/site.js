const navToggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("site-nav");
const root = document.documentElement;
const themeToggle = document.querySelector("[data-theme-toggle]");
const scrollProgress = document.querySelector("[data-scroll-progress]");
const cursorSpotlight = document.querySelector("[data-cursor-spotlight]");
const commandButtons = document.querySelectorAll("[data-command-button]");
const commandTitle = document.getElementById("command-title");
const commandCopy = document.getElementById("command-copy");
const deckHotkey = document.getElementById("deck-skill-hotkey");

const getActiveTheme = () => root.dataset.theme || "dark";
const setTheme = (theme) => {
  root.dataset.theme = theme;
  if (themeToggle) {
    themeToggle.setAttribute("aria-pressed", String(theme === "light"));
  }

  try {
    localStorage.setItem("portfolio-theme", theme);
  } catch (error) {
    // Theme still works for the current session if storage is unavailable.
  }
};

setTheme(getActiveTheme());

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    setTheme(getActiveTheme() === "light" ? "dark" : "light");
  });
}

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

const updateScrollProgress = () => {
  if (!scrollProgress) return;

  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const progress = maxScroll > 0 ? window.scrollY / maxScroll : 0;
  scrollProgress.style.setProperty("--scroll-progress", String(Math.min(Math.max(progress, 0), 1)));
};

window.addEventListener("scroll", updateScrollProgress, { passive: true });
window.addEventListener("resize", updateScrollProgress);
updateScrollProgress();

if (cursorSpotlight && !prefersReducedMotion) {
  window.addEventListener("pointermove", (event) => {
    document.body.classList.add("has-pointer");
    root.style.setProperty("--cursor-x", `${event.clientX}px`);
    root.style.setProperty("--cursor-y", `${event.clientY}px`);
  });
}

const revealTargets = document.querySelectorAll(".reveal");

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
    { threshold: 0.14 }
  );

  revealTargets.forEach((target) => revealObserver.observe(target));
} else {
  revealTargets.forEach((target) => target.classList.add("is-visible"));
}

const deckKeys = document.querySelectorAll(".skill-key");
const deckTitle = document.getElementById("deck-skill-title");
const deckCopy = document.getElementById("deck-skill-copy");

const activateSkill = (button, index) => {
  deckKeys.forEach((key) => key.classList.remove("is-active"));
  button.classList.add("is-active");

  if (deckTitle) deckTitle.textContent = button.dataset.skillTitle || button.textContent.trim();
  if (deckCopy) deckCopy.textContent = button.dataset.skillCopy || "";
  if (deckHotkey) deckHotkey.textContent = String(index + 1).padStart(2, "0");
};

deckKeys.forEach((button, index) => {
  const keycap = button.querySelector("kbd");
  const hotkey = index < 9 ? String(index + 1) : "0";
  button.dataset.hotkey = hotkey;
  if (keycap) keycap.textContent = hotkey;

  const activate = () => {
    activateSkill(button, index);
  };

  ["mouseenter", "focus", "click"].forEach((eventName) => {
    button.addEventListener(eventName, activate);
  });
});

if (deckKeys.length) {
  activateSkill(deckKeys[0], 0);

  window.addEventListener("keydown", (event) => {
    const activeElement = document.activeElement;
    const isTyping =
      activeElement instanceof HTMLInputElement ||
      activeElement instanceof HTMLTextAreaElement ||
      activeElement?.getAttribute("contenteditable") === "true";

    if (isTyping) return;

    const target = Array.from(deckKeys).find((button) => button.dataset.hotkey === event.key);
    if (!target) return;

    event.preventDefault();
    activateSkill(target, Array.from(deckKeys).indexOf(target));
    target.focus({ preventScroll: true });
  });
}

commandButtons.forEach((button) => {
  button.addEventListener("click", () => {
    commandButtons.forEach((item) => item.classList.remove("is-active"));
    button.classList.add("is-active");

    if (commandTitle) commandTitle.textContent = button.dataset.commandTitle || button.textContent.trim();
    if (commandCopy) commandCopy.textContent = button.dataset.commandCopy || "";
  });
});

document.querySelectorAll(".magnetic-card").forEach((card) => {
  card.addEventListener("pointermove", (event) => {
    const rect = card.getBoundingClientRect();
    const x = (event.clientX - rect.left) / rect.width;
    const y = (event.clientY - rect.top) / rect.height;
    card.style.setProperty("--mx", String(x * 100));
    card.style.setProperty("--my", String(y * 100));

    if (prefersReducedMotion) return;

    const rotateX = (0.5 - y) * 5;
    const rotateY = (x - 0.5) * 7;

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
  const pointer = { x: 0.52, y: 0.34 };
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

    const count = Math.max(56, Math.min(96, Math.floor(width / 18)));
    particles.length = 0;

    for (let index = 0; index < count; index += 1) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.26,
        vy: (Math.random() - 0.5) * 0.26,
        radius: 1 + Math.random() * 1.8
      });
    }
  };

  const draw = () => {
    context.clearRect(0, 0, width, height);

    const glowX = pointer.x * width;
    const glowY = pointer.y * height;
    const gradient = context.createLinearGradient(0, 0, width, height);
    gradient.addColorStop(0, "rgba(88, 216, 255, 0.14)");
    gradient.addColorStop(0.42, "rgba(154, 124, 255, 0.06)");
    gradient.addColorStop(1, "rgba(85, 239, 183, 0.08)");
    context.fillStyle = gradient;
    context.fillRect(0, 0, width, height);

    particles.forEach((particle, index) => {
      particle.x += particle.vx + (pointer.x - 0.5) * 0.02;
      particle.y += particle.vy + (pointer.y - 0.5) * 0.02;

      if (particle.x < 0 || particle.x > width) particle.vx *= -1;
      if (particle.y < 0 || particle.y > height) particle.vy *= -1;

      for (let nextIndex = index + 1; nextIndex < particles.length; nextIndex += 1) {
        const next = particles[nextIndex];
        const dx = particle.x - next.x;
        const dy = particle.y - next.y;
        const distance = Math.hypot(dx, dy);

        if (distance < 136) {
          context.strokeStyle = `rgba(88, 216, 255, ${0.13 * (1 - distance / 136)})`;
          context.lineWidth = 1;
          context.beginPath();
          context.moveTo(particle.x, particle.y);
          context.lineTo(next.x, next.y);
          context.stroke();
        }
      }

      const pointerDistance = Math.hypot(particle.x - glowX, particle.y - glowY);
      context.fillStyle = pointerDistance < 180 ? "rgba(85, 239, 183, 0.9)" : "rgba(220, 231, 244, 0.68)";
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
