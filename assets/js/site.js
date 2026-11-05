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
  document.querySelectorAll("[data-days]").forEach(function (r) {
    if (r.getAttribute("data-days").split(" ").indexOf(String(day)) > -1) r.classList.add("today");
  });
  /* blocos que dependem de dados reais (assets/js/content.js): só aparecem se preenchidos */
  var C = window.KF_CONTENT || {};
  function mk(tag, cls, txt) { var n = document.createElement(tag); if (cls) n.className = cls; if (txt) n.textContent = txt; return n; }
  var cap = (C.capacidade || "").trim();
  var itens = (C.itensInclusos || []).filter(function (s) { return s && s.trim(); });
  var slot = document.querySelector('[data-slot="pode-ter"]');
  if (slot && (cap || itens.length)) {
    if (cap) { var c1 = mk("article", "card"); c1.appendChild(mk("h3", "", "Capacidade")); c1.appendChild(mk("p", "", cap)); slot.appendChild(c1); }
    if (itens.length) { var c2 = mk("article", "card y"); c2.appendChild(mk("h3", "", "Itens inclusos")); var ul = mk("ul", "list"); itens.forEach(function (s) { ul.appendChild(mk("li", "", s)); }); c2.appendChild(ul); slot.appendChild(c2); }
    slot.closest("section").hidden = false;
  }
  var faq = document.querySelector('[data-slot="faq-pre"]');
  function qa(q, a) { var d = mk("details"); d.appendChild(mk("summary", "", q)); d.appendChild(mk("p", "", a)); faq.appendChild(d); }
  if (faq) {
    if (cap) qa("Quantos convidados cabem?", cap + ".");
    if (itens.length) qa("O que está incluso na locação?", itens.join(", ") + ".");
  }
  var dep = document.querySelector('[data-slot="depoimentos"]');
  var deps = (C.depoimentos || []).filter(function (d) { return d && d.texto && d.nome; }).slice(0, 3);
  if (dep && deps.length) {
    deps.forEach(function (d) {
      var a = mk("article", "card"); var q = mk("blockquote"); q.appendChild(mk("p", "", "“" + d.texto + "”")); a.appendChild(q);
      a.appendChild(mk("p", "who", d.nome + (d.tema ? " · " + d.tema : ""))); dep.appendChild(a);
    });
    dep.closest("section").hidden = false;
  }
  /* botão flutuante some quando já há um botão de WhatsApp na tela */
  var fab = document.querySelector(".fab");
  if (fab && "IntersectionObserver" in window) {
    var seen = new Set();
    var fo = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) seen.add(e.target); else seen.delete(e.target); });
      fab.classList.toggle("fab-off", seen.size > 0);
    });
    document.querySelectorAll(".hero .cta-row, .cta, .foot").forEach(function (n) { fo.observe(n); });
  }
  /* entradas escalonadas */
  var items = document.querySelectorAll("main section:not(.hero) h2, main section:not(.hero) .card, main section:not(.hero) .steps li, main section:not(.hero) figure, main section:not(.hero) details, .hero .lead, .hero .cta-row, .hero-ph");
  items.forEach(function (n, k) { n.classList.add("rv"); n.style.setProperty("--i", String(k % 4)); });
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: 0.15 });
    items.forEach(function (n) { io.observe(n); });
  } else { items.forEach(function (n) { n.classList.add("in"); }); }
})();
