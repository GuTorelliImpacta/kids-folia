# Kids Folia — site institucional

Site estático (HTML, CSS e JS puros, sem build). Spec e decisões: `docs/spec/kids-folia.md`.

## Rodar localmente
`python3 -m http.server 8000` e abra http://localhost:8000

## Publicar
Qualquer hospedagem estática (Vercel, Hostinger, Netlify, GitHub Pages). Headers de segurança: `_headers` (Netlify/Cloudflare) e `vercel.json` (Vercel). Defina o domínio real: troque `https://www.kidsfolia.com.br` em `canonical`, `og:image`, JSON-LD, `sitemap.xml` e `robots.txt`.

## Dados do negócio (conferir antes de publicar)
Endereço, telefone, horários e link do WhatsApp aparecem nas 4 páginas, no rodapé, no JSON-LD e em `assets/js/site.js` (horários). Ao mudar um, mude todos.

## Decisões (ADR curto)
- Estático, sem formulário nem cookies: menos superfície de ataque, melhor LCP e hospedagem simples.
- Conversão única por WhatsApp com mensagem pré-preenchida.
- Fotos de menores: nomes e rostos borrados ou cortados; pedir autorização dos pais antes de ampliar o uso.
- Pendências `[CONFIRMAR]`: ver seção 3 da spec.
