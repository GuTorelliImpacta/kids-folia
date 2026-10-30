(function () {
  var btn = document.querySelector(".menu-btn");
  var nav = document.getElementById("nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open);
      btn.textContent = open ? "Fechar" : "Menu";
    });
  }
  /* horário de funcionamento (print Google Maps) — dom=0 */
  var H = { 0: [10, 12], 1: [10, 18], 2: [10, 18], 3: [10, 18], 4: [10, 18], 5: [10, 18], 6: [10, 15] };
  var now = new Date();
  var parts = new Intl.DateTimeFormat("pt-BR", { timeZone: "America/Sao_Paulo", weekday: "short", hour: "numeric", minute: "numeric", hour12: false }).formatToParts(now);
  var wk = ["dom.", "seg.", "ter.", "qua.", "qui.", "sex.", "sáb."];
  var p = {}; parts.forEach(function (x) { p[x.type] = x.value; });
  var day = wk.indexOf(p.weekday.toLowerCase()); var hr = parseInt(p.hour, 10) + parseInt(p.minute, 10) / 60;
  var el = document.querySelector("[data-open]");
  if (el && day > -1) {
    var h = H[day];
    if (hr >= h[0] && hr < h[1]) { el.textContent = "Aberto agora · fecha às " + h[1] + "h"; el.classList.add("is-open"); }
    else { el.textContent = "Fechado agora · confira os horários"; }
  }
  var row = document.querySelector('[data-day="' + day + '"]');
  if (row) row.classList.add("today");
  /* entradas escalonadas */
  var items = document.querySelectorAll("main section:not(.hero) h2, main section:not(.hero) .card, main section:not(.hero) .steps li, main section:not(.hero) figure, main section:not(.hero) details, .hero .lead, .hero .cta-row, .hero-ph");
  items.forEach(function (n, k) { n.classList.add("rv"); n.style.setProperty("--i", String(k % 4)); });
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: 0.15 });
    items.forEach(function (n) { io.observe(n); });
  } else { items.forEach(function (n) { n.classList.add("in"); }); }
})();
