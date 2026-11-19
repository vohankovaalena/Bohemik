// Mobilní menu
document.querySelectorAll(".nav-toggle").forEach((btn) => {
  const nav = document.querySelector("[data-nav]");
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", String(open));
  });
});

// Přepínač variant – jen pro prezentaci návrhů
(() => {
  const names = ["Podle návrhu", "Redakční", "Industriální", "Přehledná", "Ilustrovaná", "Technický výkres", "Doporučená", "Zakázky"];
  const N = names.length;
  const m = location.pathname.match(/varianta-(\d)\.html$/);
  if (!m || window.self !== window.top) return;
  const cur = Number(m[1]);
  const bar = document.createElement("nav");
  bar.className = "vswitch";
  bar.setAttribute("aria-label", "Přepínání variant");
  let html = `<a href="index.html" title="Přehled variant">← přehled</a><span class="vswitch__name">${cur}. ${names[cur - 1]}</span>`;
  for (let i = 1; i <= N; i++) html += `<a href="varianta-${i}.html" ${i === cur ? 'aria-current="page"' : ""} title="${names[i - 1]}">${i}</a>`;
  bar.innerHTML = html;
  document.body.appendChild(bar);
  document.addEventListener("keydown", (e) => {
    if (e.target.closest("input, textarea")) return;
    if (e.key === "ArrowRight" && cur < N) location.href = `varianta-${cur + 1}.html`;
    if (e.key === "ArrowLeft" && cur > 1) location.href = `varianta-${cur - 1}.html`;
  });
})();
