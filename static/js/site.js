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
