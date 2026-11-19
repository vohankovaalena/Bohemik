// Mobilní menu
document.querySelectorAll(".nav-toggle").forEach((btn) => {
  const nav = document.querySelector("[data-nav]");
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", String(open));
  });
  // Po kliknutí na odkaz v menu ho na mobilu zavřeme
  nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => {
    nav.classList.remove("is-open");
    btn.setAttribute("aria-expanded", "false");
  }));
});

// Roky na trhu: firma vznikla 4. 9. 2012 (ARES, IČ 24265021).
// Počítá se z aktuálního roku v prohlížeči, číslo v HTML je záloha bez JavaScriptu.
document.querySelectorAll("[data-since]").forEach((el) => {
  el.textContent = String(new Date().getFullYear() - Number(el.dataset.since));
});
