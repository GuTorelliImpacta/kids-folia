# Spec — Site institucional Kids Folia (São Paulo/SP)

> Fonte da verdade do projeto. Skills de implementação trabalham dentro deste documento. Data da spec: 2026-10-30. O usuário pediu "implemente toda a solução": decisões tomadas sem nova rodada de perguntas; suposições declaradas abaixo.

## 1. Missão e resultado esperado
Criar o site institucional da **Kids Folia**, casa de festas infantis na Vila Nova Mazzei (Zona Norte de SP), para que pais que buscam "espaço para festa infantil" na região entendam a oferta em segundos e **chamem no WhatsApp** para pedir orçamento/consultar data.
- Conversão principal: **WhatsApp** com mensagem pré-preenchida. Secundárias: ligação, rota no Google Maps, Instagram.
- Porquê: o telefone da ficha é celular (9 dígitos), o negócio é local e o público decide pelo celular.

## 2. Fatos confirmados (origem)
| Fato | Origem |
|---|---|
| Nome: Kids Folia | Dono do projeto / Instagram @kidsfolia |
| Endereço: Rua Manuel Gaya, 1045 – Vila Nova Mazzei, São Paulo – SP, 02313-000 | Print Google Maps; número 1045 visível na fachada |
| Telefone: (11) 99355-5359 | Print Google Maps |
| Horários: qui–sex 10h–18h; sáb 10h–15h; dom 10h–12h; seg 10h–18h (feriado Finados: "o horário pode mudar"); ter–qua 10h–18h | Print Google Maps |
| Fachada temática de doces (pirulitos, cupcakes, sorvete e "glacê" branco escorrendo no telhado) | Foto da fachada |
| Faixa na grade da fachada indica "locação de … decor… mesas… provençal…" (texto parcialmente legível) | Foto da fachada |
| Interior com paredes e corredor com pirulitos gigantes, mesas e cadeiras brancas, parede pintada com efeito "tinta escorrendo" | Miniaturas enviadas |
| Trabalhos de decoração com painéis redondos, arcos de balões, cilindros, doces e personagens (tema margarida; tema Mario; tema Batman) | Fotos enviadas |

## 3. O que ainda não sabemos ([CONFIRMAR]) e regras de integridade
- [CONFIRMAR] O serviço exato: salão de festas completo, aluguel de espaço, locação de decoração/mesas, ou os três. **Suposição do site:** "Espaço para festas + decoração e locação".
- [CONFIRMAR] O número (11) 99355-5359 atende no WhatsApp (suposição: sim, é celular).
- [CONFIRMAR] Capacidade do salão, pacotes, preços, comida/bebida inclusos, monitores/recreação, estacionamento, acessibilidade.
- [CONFIRMAR] Ano de fundação, nome do dono, e-mail, bio e destaques do Instagram (acesso automático bloqueado: HTTP 429).
- [CONFIRMAR] Autorização dos pais para exibir as festas fotografadas.
- [CONFIRMAR] Se o horário de segunda segue "10h–18h" no feriado de Finados (Google avisa que pode mudar).
- Pesquisa pública (Google/web, 2026-10-30) **não encontrou** página própria nem diretório confiável da Kids Folia. Resultados com nome parecido (ex.: "Folia Kids Locação de Brinquedos", "Folia e Fantasia", "Kid Corner Buffet") são **outras empresas**: não usar nada deles.

**Regras de integridade (inegociáveis):** nada de depoimento, nota, número de festas, prêmio, preço, capacidade ou selo inventado. Seções que dependem de dado real ficam ocultas enquanto vazias (depoimentos, preços, pacotes). Sem logo de terceiros. Sem hotlink de imagem de rede social. Menores: sem rosto identificável nem nome; nomes de crianças foram borrados/cortados nas fotos enviadas. Personagens (Batman, Mario, Mickey) só como descrição de temas realizados, sem logos oficiais nem "licenciado/oficial".

## 4. Análise de marca
- **Nome:** "Folia" = festa alegre, barulho bom, confete. "Kids" = público direto. Nome curto, brincalhão, fácil de falar e de buscar.
- **Logo:** não recebido. [CONFIRMAR] enviar o arquivo. Até lá, usar **wordmark tipográfico provisório** ("Kids Folia" com estrela/confete), claramente trocável (um único arquivo `assets/logo.svg`).
- **Paleta (amostrada da fachada e confirmada visualmente nas fotos; hex aproximados, usar como tokens):**
  - Azul-folia `#1D4EC4` (muro azul e cupcake) — cor de marca principal
  - Amarelo-glacê `#F6C21C` (muro, pirulito, sorvete)
  - Vermelho-doce `#D8364B` (pirulitos, sorvete) — destaque
  - Verde-bala `#2FAE5B` (pirulito gigante)
  - Chocolate `#5C3D33` (fachada) — texto escuro e rodapé
  - Creme `#FBF6EE` — fundo; branco-glacê `#FFFFFF`
- **Personalidade:** festeira, doce, acolhedora, de bairro. Não é parque corporativo: é a casa de festas onde a fachada já é um convite.
- **Narrativa:** "Sua festa começa na porta." A fachada de doce é o ativo mais memorável e é prova real.
- **Fraquezas atuais:** sem site, sem logo digital em boa resolução, poucas fotos boas, presença web difícil de achar, sem preço/capacidade públicos.

## 5. Nicho e tendências
- Festas infantis representavam 16% de R$ 17,2 bi movimentados por festas e eventos no Brasil em 2023 (Abrafesta, citada em matéria da ABC da Comunicação; data da matéria [CONFIRMAR]).
- Mercado de eventos projetado em R$ 141,1 bi em 2025, +8,4% (Abrape, via Jovem Pan, 01/04/2025). Tendências citadas: personalização, fachadas/ambientes temáticos, cabine de fotos, influência das redes sociais nas indicações.
- Concorrência local: poucos resultados específicos para a Vila Nova Mazzei; um diretório lista "Kid Corner Buffet" (Av. Mazzei, 1580) com status "Fechado" e dados contraditórios — **tratar como não confiável**. Oportunidade: SEO local ainda aberto.
- Diferenciais **provados**: fachada temática única; temas decorados variados (margarida, Mario, Batman) mostrados em fotos; horário amplo incluindo fim de semana.

## 6. Público e objetivos
- **Público:** mães, pais e avós da Zona Norte (Tucuruvi, Vila Nova Mazzei, Jaçanã, Mandaqui) que planejam aniversário de 1 a 10 anos; buscam no Google/Instagram pelo celular. Dores: "cabe no orçamento?", "tem data?", "como é o espaço?", "quem cuida da decoração?".
- **KPIs:** cliques em WhatsApp, ligações, "como chegar", visitas orgânicas locais.
- **Metas técnicas:** LCP ≤ 2,5 s (4G), CLS ≤ 0,1, INP ≤ 200 ms, Lighthouse ≥ 95 (Performance/Acessibilidade/SEO/Boas práticas).

## 7. Direção de design
- **Conceito:** "Glacê" — superfícies cremes com **bordas onduladas de glacê escorrendo** (inspiradas no telhado da fachada), faixas de cor chapada e confete geométrico discreto. Nasce da fachada real, não de template.
- **Tokens:** os da seção 4. Azul é a cor de ação estrutural; **amarelo = CTA primário** (texto chocolate sobre amarelo, contraste ≥ 7:1); vermelho/verde só como acento pontual (máx. 2 acentos além da paleta).
- **Tipografia:** títulos arredondados e amigáveis porém legíveis (candidatas: Baloo 2, Fredoka, Nunito Black); texto em Nunito/Inter. Auto-hospedar fontes (woff2, `font-display: swap`).
- **Hero:** foto real da fachada ocupando o fundo/lado, H1: "Festa infantil que começa na fachada" (a Vila Nova Mazzei fica no subtítulo e no title) Subtítulo curto, CTA "Chamar no WhatsApp" amarelo e "Ver o espaço" secundário, acima da dobra a 390 px. Linha "Aberto hoje até 18h" calculada pelo horário real.
- **Não fazer:** gradiente roxo genérico; mascotes/personagens licenciados; emojis como ícones; carrossel automático; contadores/estatísticas inventadas; fotos de banco; depoimentos fictícios; pop-up de entrada.

## 8. UX: páginas e fluxo
Páginas (site estático multipágina, navegação simples, botão WhatsApp fixo no celular):
1. **Home** — hero; faixa de 3 diferenciais reais; temas realizados (galeria curta); como funciona (3 passos: chamar → combinar data/tema → festa); horários e mapa; FAQ curto; CTA final.
2. **O Espaço** — fachada, interior, fotos; texto prudente sobre o que o dono confirmar.
3. **Decoração e Locação** — temas realizados (margarida, Mario, Batman), itens (painéis redondos, arcos de balões, cilindros, mesas) apenas como "consulte disponibilidade".
4. **Contato** — WhatsApp, telefone, endereço, horários, mapa (link, sem iframe para não pesar), Instagram.
5. **Privacidade** — política LGPD curta.
Fluxo celular: Google → Home → botão WhatsApp (1 toque), com mensagem: "Olá! Vi o site da Kids Folia e gostaria de um orçamento para a festa do(a) meu(minha) filho(a). Data pretendida: ___".
Sem formulário (reduz fricção e superfície de ataque); canal único é WhatsApp.

## 9. Conteúdo
Tom: caloroso, direto, sem exagero. Copy final está no código das páginas (nada de lorem ipsum). Textos que citam capacidade, preço, comida ou recreação **não existem** até confirmação; usar "Fale com a gente para saber o que está incluso".
FAQ (respostas só com fatos confirmados): Onde fica? Quais os horários? Como peço orçamento? Vocês fazem decoração temática? (resposta: "Sim, mostramos temas já realizados; consulte disponibilidade"). Aviso: valores e condições são combinados direto pelo WhatsApp.

## 10. SEO
- Termos: "festa infantil Vila Nova Mazzei", "espaço para festa infantil zona norte SP", "decoração festa infantil Tucuruvi", "locação de decoração infantil zona norte".
- `title` ≤ 60 e `description` ≤ 155 por página; `canonical` por página; `lang="pt-BR"`; Open Graph com a foto da fachada.
- JSON-LD `LocalBusiness` com nome, endereço, telefone, `openingHoursSpecification`; **sem** `aggregateRating`/`review`/`priceRange` inventados. NAP idêntico ao Maps.
- `sitemap.xml`, `robots.txt`. URL base via variável (`SITE_URL`), padrão provisório.
- Checklist Google Meu Negócio (para o dono): validar categoria "Casa de festas"/"Buffet infantil", adicionar fotos reais, descrição, link do site, perguntas e respostas, pedir avaliações.
- Analytics: nenhum por padrão (sem consentimento = sem rastreio). Eventos futuros: `click_whatsapp`, `click_call`, `click_route`.

## 11. Performance e acessibilidade
- Imagens: WebP/JPEG otimizados, `width/height`, `loading="lazy"` abaixo da dobra, hero com `fetchpriority="high"`.
- Sem framework JS; CSS único; JS ≤ 5 KB (menu, "aberto agora").
- WCAG 2.1 AA: contraste, foco visível, alvos ≥ 44 px, `prefers-reduced-motion`, `alt` descritivo, ordem de títulos. Testar a 360 px.

## 12. Segurança e privacidade
- Site estático, sem backend, sem formulário, sem segredos.
- Headers (via `_headers`/config de hospedagem): CSP restritiva (`default-src 'self'`), HSTS, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` mínima.
- `rel="noopener noreferrer"` em links externos; sem scripts de terceiros.
- LGPD: política de privacidade; WhatsApp é fluxo iniciado pelo usuário; sem cookies.

## 13. Stack e estrutura
- **HTML + CSS + JS puros**, sem build. Porquê: repositório vazio, site de 5 páginas, melhor performance/segurança e fácil de editar e hospedar em qualquer lugar (Vercel, Hostinger, GitHub Pages).
- Dados editáveis do negócio centralizados em `assets/site.js` (`SITE`: telefone, endereço, horários, links) e replicados nas páginas; mudar um dado exige conferir o NAP.
- Estrutura: `index.html`, `espaco.html`, `decoracao.html`, `contato.html`, `privacidade.html`, `assets/{css,js,img}`, `sitemap.xml`, `robots.txt`, `_headers`.

## 14. Assets e política de imagens
| Arquivo | Mostra | Resolução | Uso |
|---|---|---|---|
| fachada.jpg | Fachada de doces (nomes/crianças borrados) | 1206×1068 | Hero e Espaço |
| decoracao-margarida.jpg | Mesa decorada tema margarida (nome borrado) | 1206×1033 | Decoração, galeria |
| vela-batman.jpg | Detalhe tema Batman (cortado acima do nome) | 1206×890 | Decoração, galeria |
| festa-mario.jpg | Festa tema Mario | 208×208 (baixa) | Só miniatura de galeria pequena |
| salao-entrada.jpg | Corredor com pirulitos | 166×208 (baixa) | Só miniatura |
Regras: nada de miniatura de rede social em destaque; hero ≥ 1600 px **ideal** — a fachada (1206 px) é o melhor ativo disponível e entra como hero provisório. **Fotos necessárias:** interior do salão (larga, ≥1600 px), mesa de festa montada, parede/decoração, área de brincar, logo em SVG/PNG alta resolução, mais fotos dos temas (sem rostos de crianças).

## 15. Processo e QA
1. Estrutura + Home → checkpoint visual (390/768/1440 px).
2. Demais páginas.
3. Revisão final em 390, 768 e 1440 px com ao menos um ciclo de correção.
4. Relatório final com pendências `[CONFIRMAR]` e fotos faltantes.

## 16. Critérios de aceite
- [ ] 5 páginas existem e navegam entre si; links sem 404.
- [ ] Endereço, telefone e horários idênticos ao print do Maps em todas as páginas e no JSON-LD.
- [ ] Nenhum dado inventado (preço, capacidade, depoimento, nota).
- [ ] CTA WhatsApp visível acima da dobra a 390 px e botão fixo no celular.
- [ ] Sem scroll horizontal em 360–1440 px; foco por teclado visível; contraste AA.
- [ ] JSON-LD válido; metadados únicos por página; sitemap/robots.
- [ ] Imagens conforme inventário; nomes de crianças ilegíveis.
- [ ] Sem scripts/CSS de terceiros; headers de segurança documentados.

## 17. Fontes
- Print do Google Maps (enviado pelo usuário) — endereço, telefone, horários.
- Fotos enviadas pelo usuário — fachada, decoração, temas.
- "Mercado de eventos está em crescimento e traz muitas inovações", Jovem Pan, 01/04/2025 — https://jovempan.com.br/economia/negocios/mercado-de-eventos-esta-em-crescimento-e-traz-muitas-inovacoes/
- Dado Abrafesta 2023 (festas infantis = 16% de R$ 17,2 bi) citado em ABC da Comunicação — https://www.abcdacomunicacao.com.br/?p=291285 (data [CONFIRMAR])
- Instagram @kidsfolia — acesso automático bloqueado (HTTP 429), não usado como fonte.
