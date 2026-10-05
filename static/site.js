(function () {
  document.documentElement.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Header border on scroll
  var header = document.querySelector(".site-header");
  function onScroll() { header && header.classList.toggle("is-scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  // Videos: play/pause toggle, respect reduced motion, pause when off-screen
  document.querySelectorAll(".video").forEach(function (fig) {
    var v = fig.querySelector("video"), b = fig.querySelector(".video__toggle");
    if (!v || !b) return;
    function sync() {
      b.classList.toggle("is-paused", v.paused);
      b.setAttribute("aria-label", v.paused ? "Play video" : "Pause video");
    }
    if (reduce) { v.removeAttribute("autoplay"); v.pause(); }
    v.userPaused = reduce;
    b.addEventListener("click", function () {
      if (v.paused) { v.play(); v.userPaused = false; } else { v.pause(); v.userPaused = true; }
    });
    v.addEventListener("play", sync); v.addEventListener("pause", sync); sync();
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { if (!v.userPaused) v.play().catch(function () {}); }
          else v.pause();
        });
      }, { threshold: 0.2 }).observe(v);
    }
  });

  // Table of contents: highlight current section
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var targets = tocLinks.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); }).filter(Boolean);
    var current = null;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) current = e.target.id; });
      tocLinks.forEach(function (a) { a.classList.toggle("is-active", a.getAttribute("href") === "#" + current); });
    }, { rootMargin: "-20% 0px -70% 0px" });
    targets.forEach(function (t) { io.observe(t); });
  }

  // Gentle reveal on homepage cards
  if (!reduce && "IntersectionObserver" in window) {
    var els = document.querySelectorAll(".case, .tile, .highlights li");
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-in"); ro.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el) { el.classList.add("reveal"); ro.observe(el); });
  }
})();
