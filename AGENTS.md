# AGENTS.md — Distinct Designs Construction

Landing pages for a licensed luxury home builder. **Pure HTML / CSS / vanilla JS —
no frameworks, no build step, no dependencies.** Deployed as a static site on Vercel
(push to `main` → production, PRs → preview URLs).

Read [`README.md`](README.md) for the project overview and
[`custom-home-build/README.md`](custom-home-build/README.md) for the full design-system
docs (tokens, classes, image slots, gotchas). This file captures the durable rules an
agent must not break.

## Run / preview locally

No build step. Serve the repo root with a static server:

```bash
python3 -m http.server 8000
# → http://localhost:8000/
```

Use a server, not `file://` — the root-relative link to `/custom-home-build/` only
resolves over HTTP. Test in Chrome and verify the hero CTAs, scroll reveals, FAQ
accordion, mobile nav, sticky CTA bar, project lightbox, and form validation.

## Architecture

- Each landing page folder (`custom-home-build/`, etc.) is **self-contained**: its own
  `index.html`, `styles.css`, `script.js`, and `images/`. Keep pages independently
  deployable — never make one page depend on another's files.
- `styles.css` inside a page folder is a **shared design system** driven by `:root`
  tokens. Rebrand/retune by editing tokens, not individual rules.
- `distinct-designs-landing-pages.html` holds the **source copy** for all three pages
  (custom home build, whole-home remodel, custom ADU) as semantic `<article>` blocks.

## Adding a landing page

Follow the recipe in `custom-home-build/README.md`. In short: copy `custom-home-build/`,
swap the copy from the matching `<article>` in `distinct-designs-landing-pages.html`,
update `<title>`, `<meta name="description">`, `<link rel="canonical">`, and the FAQ
JSON-LD, then flip its hub card in the root `index.html` from a disabled
`<div class="hub-card__link" aria-disabled="true">` to
`<a class="hub-card__link" href="/<slug>/">`, and swap its `hub-card__status` to
`hub-card__status--live` with the label `Live`. Keep clean in-page anchor ids
(`#process`, `#projects`, `#why-us`, `#faq`, `#areas-served`, `#form`) so the nav,
footer, sticky CTA, and `script.js` keep working — the `-remodel`/`-adu` id suffixes in
the source-copy file exist only to disambiguate the three articles in one document.

## Conventions worth preserving

- **Copy is client-supplied and used verbatim.** Do not paraphrase or condense body copy.
- **FAQ JSON-LD must stay in sync** with the visible FAQ copy on each page, or the rich
  snippet becomes invalid.
- **Scroll reveal fails open.** Content is visible by default; the hidden start-state is
  only armed by `html.js-reveal` (inline script in `<head>`). Never put `opacity: 0` on a
  bare `.reveal` — a JS failure must still render the full page.
- **Contrast is WCAG AA verified.** `--color-text-muted` is tuned to pass on both the page
  and sand backgrounds. Scrims over photography (hero + project tiles) are sized by
  measurement, not by eye; the tile scrim uses pixel gradient stops on purpose. Re-measure
  if you change text size/position over imagery.
- **The projects bento expects exactly 4 tiles** — placement is by `:nth-child`. Changing
  the count means updating those rules or you get empty cells.
- **Reduced motion** is honored globally and in `script.js` (`prefers-reduced-motion`).
- **Keep the hero's `width`/`height` + `fetchpriority="high"`** (protects CLS/LCP);
  below-the-fold images use `loading="lazy"`.
- **Placeholder images** are marked `data-placeholder="true"` with an HTML comment saying
  what belongs there. Find them all: `grep -rn 'data-placeholder' --include='*.html' .`
- **Reusing an image filename does not bust caches.** Verify a swap by checking the file
  on disk / intrinsic size, not by trusting a screenshot; hard-reload before assuming a
  swap failed.
- **The lead form is not wired to a backend** (see the `TODO` in `script.js`); it
  validates and shows a confirmation only.
