"""Gera as páginas HTML do site Kids Folia.

Uso: python3 tools/build.py
Header, rodapé, botões e mensagem do WhatsApp são definidos uma única vez aqui,
para ficarem idênticos em todas as páginas.
"""
import json, os, urllib.parse

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
# Base de produção atual (Vercel). Ao conectar o domínio próprio, troque só esta linha
# por https://www.kidsfolia.com.br e rode o script de novo.
SITE = 'https://kids-folia.vercel.app'
OG = 'assets/img/og.jpg'
HERO = 'assets/img/fachada-hero.jpg'

MSG = 'Olá! Vi o site da Kids Folia e quero um orçamento de festa. Data pretendida: '
WA = 'https://wa.me/5511993555359?text=' + urllib.parse.quote(MSG)
MAPS = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote('Rua Manuel Gaya, 1045, Vila Nova Mazzei, São Paulo - SP')
IG = 'https://www.instagram.com/kidsfolia'
EXT = 'target="_blank" rel="noopener noreferrer"'
NAV = [('index.html', 'Início'), ('espaco.html', 'O Espaço'), ('decoracao.html', 'Decoração e Locação'), ('contato.html', 'Contato')]
HOURS_LINE = 'Seg a sex 10h–18h · Sáb 10h–15h · Dom 10h–12h'


def jsonld():
    d = {"@context": "https://schema.org", "@type": "EntertainmentBusiness", "name": "Kids Folia",
         "description": "Casa de festas infantis com decoração temática na Vila Nova Mazzei, Zona Norte de São Paulo.",
         "url": SITE, "telephone": "+5511993555359", "image": SITE + '/' + OG,
         "address": {"@type": "PostalAddress", "streetAddress": "Rua Manuel Gaya, 1045", "addressLocality": "São Paulo", "addressRegion": "SP", "postalCode": "02313-000", "addressCountry": "BR"},
         "openingHoursSpecification": [
             {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "10:00", "closes": "18:00"},
             {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:00", "closes": "15:00"},
             {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "10:00", "closes": "12:00"}],
         "sameAs": [IG]}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'


def page(fn, title, desc, body, preload=None, ld=True, robots=''):
    nav = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == fn else ""}>{t}</a>' for h, t in NAV)
    url = SITE + '/' + ('' if fn == 'index.html' else fn)
    pre = f'<link rel="preload" href="{preload}" as="image" fetchpriority="high">\n' if preload else ''
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<!-- Domínio: hoje a base é {SITE}. Quando https://www.kidsfolia.com.br estiver conectado, troque a base em canonical, og:url e og:image (tools/build.py, constante SITE). -->
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#1D4EC4">
{robots}<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Kids Folia">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{OG}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/logo.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/baloo2-800.woff2" as="font" type="font/woff2" crossorigin>
{pre}<script src="assets/js/boot.js"></script>
<link rel="stylesheet" href="assets/css/style.css">
{jsonld() if ld else ''}
</head>
<body>
<a class="skip" href="#main">Pular para o conteúdo</a>
<header class="top"><div class="wrap">
<a class="brand" href="index.html" aria-label="Kids Folia, início"><span class="wm" translate="no">Kids <span>Folia</span></span></a>
<nav class="nav" id="nav" aria-label="Principal">{nav}<a class="btn btn-primary" href="{WA}" {EXT}>WhatsApp</a></nav>
<button class="menu-btn" type="button" aria-controls="nav" aria-expanded="false">Menu</button>
</div></header>
<main id="main">
{body}
</main>
<footer class="foot"><div class="wrap">
<div class="foot-grid">
<div><h3>Kids Folia</h3><p>Festa infantil e decoração temática na Vila Nova Mazzei, Zona Norte de São Paulo.</p></div>
<div><h3>Onde estamos</h3><p>Rua Manuel Gaya, 1045<br>Vila Nova Mazzei, São Paulo – SP<br>CEP 02313-000 · <a href="{MAPS}" {EXT}>Como chegar</a></p></div>
<div><h3>Fale com a gente</h3><p><a href="tel:+5511993555359">(11) 99355-5359</a> · <a href="{WA}" {EXT}>WhatsApp</a><br><a href="{IG}" {EXT}>Instagram @kidsfolia</a></p></div>
</div>
<p class="foot-hours">{HOURS_LINE}</p>
<small>© 2026 Kids Folia · <a href="privacidade.html">Privacidade</a></small>
</div></footer>
<a class="btn btn-wa fab" href="{WA}" {EXT} aria-label="Chamar no WhatsApp">WhatsApp</a>
<script src="assets/js/content.js" defer></script>
<script src="assets/js/site.js" defer></script>
</body></html>'''
    open(OUT + fn, 'w', encoding='utf-8').write(html)


def hours(h2=True):
    head = '<h2>Horário de atendimento e visitas</h2>\n' if h2 else ''
    return head + '''<table class="hours"><tbody>
<tr data-days="1 2 3 4 5"><th scope="row">Segunda a sexta</th><td>10h–18h</td></tr>
<tr data-days="6"><th scope="row">Sábado</th><td>10h–15h</td></tr>
<tr data-days="0"><th scope="row">Domingo</th><td>10h–12h</td></tr>
</tbody></table>
<p class="note">As festas acontecem em horários combinados com a gente. Consulte a sua data pelo WhatsApp. Em feriados o horário pode mudar.</p>'''


def cta(h='Vamos marcar a festa do seu pequeno?'):
    return f'''<section class="cta"><div class="wrap center"><h2>{h}</h2><p>Chame no WhatsApp, conte a data e o tema que você imaginou e receba as informações direto com a gente.</p><a class="btn btn-primary" href="{WA}" {EXT}>Chamar no WhatsApp</a></div></section>'''


def fig(src, w, h, alt, cap, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<figure><img{c} src="assets/img/{src}" width="{w}" height="{h}" loading="lazy" alt="{alt}"><figcaption>{cap}</figcaption></figure>'


MARG = ('decoracao-margarida.jpg', 1206, 1033, 'Mesa de festa decorada em tons de rosa com painel redondo, arcos de balões e margaridas')
MARIO = ('festa-mario.jpg', 208, 208, 'Mesa de festa com tema de videogame, balões coloridos e personagens recortados')
CORR = ('salao-entrada.jpg', 166, 208, 'Corredor interno com pirulitos gigantes e paredes coloridas')
HERO_ = ('vela-batman.jpg', 1206, 890, 'Vela de aniversário número 1 com personagem de super-herói sobre bolo amarelo')

# ---------- HOME ----------
home = f'''<section class="hero"><div class="wrap hero-grid">
<div>
<h1>Festa infantil que começa na fachada</h1>
<p class="lead">Espaço colorido e decoração temática para festa infantil na Vila Nova Mazzei, Zona Norte de São Paulo.</p>
<div class="cta-row"><a class="btn btn-primary" href="{WA}" {EXT}>Chamar no WhatsApp</a><a class="btn btn-ghost" href="espaco.html">Ver o espaço</a></div>
<p class="open-now" data-open>Confira nossos horários</p>
</div>
<div class="hero-ph"><img src="{HERO}" width="1206" height="745" alt="Fachada da Kids Folia decorada com pirulitos, cupcake e sorvete gigantes e telhado com glacê branco escorrendo" fetchpriority="high"></div>
</div><div class="drip" aria-hidden="true"></div></section>

<section><div class="wrap">
<h2>Um lugar com cara de festa</h2>
<div class="grid3">
<article class="card"><h3>Fachada que encanta</h3><p>Pirulitos, cupcakes e sorvete gigantes: as crianças já chegam felizes e os pais sabem que é o lugar certo.</p></article>
<article class="card y"><h3>Decoração temática</h3><p>Painéis redondos, arcos de balões, mesas e doces montados no tema que a criança ama, de margarida a super-heróis.</p></article>
<article class="card g"><h3>Abrimos todos os dias</h3><p>De segunda a domingo, inclusive sábado e domingo de manhã, para você conhecer o espaço quando puder.</p></article>
</div></div></section>

<section id="pode-ter" hidden><div class="wrap">
<h2>O que a sua festa pode ter</h2>
<div class="grid3" data-slot="pode-ter"></div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Cada festa, uma história</h2>
<div class="gallery">
{fig(*MARG, 'Tema margarida')}
{fig(*MARIO, 'Tema videogame')}
{fig(*CORR, 'Corredor do espaço')}
{fig(*HERO_, 'Tema super-herói', 'pos-left')}
</div>
<p class="center btn-row"><a class="btn btn-ghost" href="decoracao.html">Ver decoração e locação</a><a class="btn btn-ghost" href="{IG}" {EXT}>Veja mais festas no Instagram</a></p>
</div></section>

<section><div class="wrap">
<h2>Simples assim</h2>
<ol class="steps">
<li><h3>Chame no WhatsApp</h3><p>Conte a data e quantos convidados espera.</p></li>
<li><h3>Combine o tema</h3><p>Escolha o tema e confira a sua data.</p></li>
<li><h3>Curta a festa</h3><p>Chegue e aproveite o dia em família.</p></li>
</ol></div></section>

<section class="alt"><div class="wrap split">
<div><h2>Rua Manuel Gaya, 1045</h2>
<p>Vila Nova Mazzei, São Paulo – SP, CEP 02313-000.<br><a href="tel:+5511993555359">(11) 99355-5359</a></p>
<p class="btn-row left"><a class="btn btn-ghost" href="{MAPS}" {EXT}>Como chegar</a><a class="btn btn-ghost" href="tel:+5511993555359">Ligar</a></p></div>
<div>{hours()}</div>
</div></section>

<section><div class="wrap hp">
<h2>Antes de chamar</h2>
<div data-slot="faq-pre"></div>
<details><summary>Como peço um orçamento?</summary><p>Pelo WhatsApp (11) 99355-5359. Valores e condições são combinados direto com a gente, conforme data e tema.</p></details>
<details><summary>Vocês fazem decoração temática?</summary><p>Sim, mostramos temas já realizados. Consulte a disponibilidade e as opções para a sua data.</p></details>
</div></section>

<section id="depoimentos" class="alt" hidden><div class="wrap">
<h2>Quem já fez festa aqui</h2>
<div class="grid3" data-slot="depoimentos"></div>
</div></section>
{cta()}'''
page('index.html', 'Kids Folia · Festa infantil na Vila Nova Mazzei, São Paulo',
     'Espaço colorido e decoração temática para festa infantil na Vila Nova Mazzei, Zona Norte de São Paulo. Aberto de segunda a domingo. Chame no WhatsApp e consulte a data.',
     home, preload=HERO)

# ---------- ESPAÇO ----------
espaco = f'''<section class="hero"><div class="wrap hero-grid"><div><h1>O espaço onde a festa acontece</h1><p class="lead">Colorido, doce e acolhedor, do portão ao salão.</p><div class="cta-row"><a class="btn btn-primary" href="{WA}" {EXT}>Chamar no WhatsApp</a></div></div>
<div class="hero-ph"><img src="{HERO}" width="1206" height="745" alt="Fachada da Kids Folia com pirulitos e cupcakes gigantes" fetchpriority="high"></div></div><div class="drip" aria-hidden="true"></div></section>
<section><div class="wrap split"><div><h2>Você já sabe que chegou</h2><p>Pirulitos, cupcake e sorvete gigantes e um telhado com “glacê” escorrendo deixam a entrada tão divertida quanto a festa.</p><p>Por dentro, o corredor segue o clima, com pirulitos coloridos, paredes pintadas e mesas e cadeiras brancas.</p></div>
<div class="photo-fill"><img src="assets/img/salao-entrada.jpg" width="166" height="208" loading="lazy" alt="Corredor interno com pirulitos gigantes e paredes coloridas"></div></div></section>
<section class="alt"><div class="wrap hp">{hours()}</div></section>
{cta('Conheça o espaço e reserve sua data')}'''
page('espaco.html', 'O Espaço | Kids Folia, festa infantil na Vila Nova Mazzei',
     'Conheça o espaço da Kids Folia: fachada de doces gigantes e ambiente colorido para festa infantil na Vila Nova Mazzei, Zona Norte de São Paulo. Venha nos visitar.',
     espaco, preload=HERO)

# ---------- DECORAÇÃO ----------
deco = f'''<section class="hero"><div class="wrap hero-grid"><div><h1>Decoração e locação para festa infantil</h1><p class="lead">Temas montados com painéis, balões, mesas e doces. Veja o que já fizemos.</p><div class="cta-row"><a class="btn btn-primary" href="{WA}" {EXT}>Pedir orçamento</a></div></div>
<div class="hero-ph"><img src="assets/img/decoracao-margarida.jpg" width="1206" height="1033" alt="Mesa de festa decorada em tons de rosa com margaridas e arcos de balões" fetchpriority="high"></div></div><div class="drip" aria-hidden="true"></div></section>
<section><div class="wrap"><h2>Temas que já montamos</h2>
<div class="gallery g3">
{fig(*MARG, 'Margarida')}
{fig(*MARIO, 'Videogame')}
{fig(*HERO_, 'Super-herói', 'pos-left')}
</div>
<p class="btn-row"><a class="btn btn-ghost" href="{IG}" {EXT}>Veja mais festas no Instagram</a></p>
<div class="grid3">
<article class="card"><h3>Painéis e balões</h3><p>Painéis redondos e arcos de balões no tema escolhido.</p></article>
<article class="card y"><h3>Mesas e cilindros</h3><p>Mesas e suportes para doces, bolo e lembrancinhas.</p></article>
<article class="card g"><h3>Seu tema</h3><p>Conte sua ideia e vemos o que é possível para a sua data.</p></article>
</div>
<p class="note">Itens, valores e disponibilidade são informados no atendimento. Personagens citados são apenas temas de festa, sem vínculo com os detentores das marcas.</p></div></section>
{cta('Qual tema vai ser?')}'''
page('decoracao.html', 'Decoração e Locação para Festa Infantil | Kids Folia',
     'Decoração temática e locação para festa infantil na Zona Norte de São Paulo: painéis redondos, arcos de balões, mesas e doces. Veja os temas e peça orçamento pelo WhatsApp.',
     deco, preload='assets/img/decoracao-margarida.jpg')

# ---------- CONTATO ----------
contato = f'''<section class="hero"><div class="wrap"><h1>Fale com a Kids Folia</h1><p class="lead">O jeito mais rápido é o WhatsApp.</p><div class="cta-row"><a class="btn btn-primary" href="{WA}" {EXT}>Chamar no WhatsApp</a><a class="btn btn-ghost" href="tel:+5511993555359">Ligar (11) 99355-5359</a></div></div><div class="drip" aria-hidden="true"></div></section>
<section><div class="wrap split"><div><h2>Onde estamos</h2><p>Rua Manuel Gaya, 1045<br>Vila Nova Mazzei, São Paulo – SP<br>CEP 02313-000</p><p><a class="btn btn-ghost" href="{MAPS}" {EXT}>Abrir no Google Maps</a></p><p>Instagram: <a href="{IG}" {EXT}>@kidsfolia</a></p></div>
<div>{hours()}</div></div></section>'''
page('contato.html', 'Contato e Horários | Kids Folia, Vila Nova Mazzei',
     'Endereço, telefone, WhatsApp e horários da Kids Folia: Rua Manuel Gaya, 1045, Vila Nova Mazzei, São Paulo. Aberto de segunda a domingo, confira o horário de hoje.',
     contato)

# ---------- PRIVACIDADE ----------
priv = '''<section><div class="wrap hp"><h1>Política de privacidade</h1>
<p>Este site não usa cookies, não tem formulários e não coleta dados pessoais.</p>
<p>Ao clicar em “WhatsApp” ou em “Ligar”, você inicia uma conversa com a Kids Folia pelo aplicativo escolhido; os dados informados ali são tratados por esse serviço e usados só para atender seu pedido.</p>
<p>Links externos (Google Maps, Instagram, WhatsApp) têm políticas próprias.</p>
<p>Dúvidas ou pedidos sobre seus dados: fale com a gente pelo WhatsApp (11) 99355-5359.</p>
<p><a href="index.html">Voltar ao início</a></p></div></section>'''
page('privacidade.html', 'Política de Privacidade · Kids Folia',
     'Política de privacidade do site da Kids Folia: sem cookies, sem formulários e sem coleta de dados pessoais.',
     priv, ld=False, robots='<meta name="robots" content="noindex,follow">\n')

open(OUT + 'robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
urls = [''] + [n for n, _ in NAV[1:]]
open(OUT + 'sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}/{u}</loc><lastmod>2026-11-05</lastmod></url>\n' for u in urls) + '</urlset>\n')
open(OUT + '_headers', 'w').write("""/*
  Content-Security-Policy: default-src 'self'; img-src 'self'; style-src 'self'; script-src 'self'; font-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'none'
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
""")
