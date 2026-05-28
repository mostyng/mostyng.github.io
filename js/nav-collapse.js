(() => {
  const nav = document.querySelector(".site-nav") || document.querySelector("nav");
  if (!nav) return;

  const thresholdPx = 48;
  const hysteresisPx = 10;

  let lastY = window.scrollY || 0;
  let hidden = false;

  const setHidden = (next) => {
    if (hidden === next) return;
    hidden = next;
    nav.classList.toggle("site-nav--hidden", hidden);
  };

  const onScroll = () => {
    const y = window.scrollY || 0;

    if (y <= thresholdPx) {
      setHidden(false);
      lastY = y;
      return;
    }

    const delta = y - lastY;
    if (delta > hysteresisPx) setHidden(true);
    else if (delta < -hysteresisPx) setHidden(false);

    lastY = y;
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
})();
