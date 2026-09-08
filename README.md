# Distinct Designs Construction — Landing Pages

High-ticket lead capture landing pages for **Distinct Designs Construction**, a licensed
luxury custom home builder (CA GC #1145786) serving the High Desert and Coachella Valley.

**Pure HTML / CSS / vanilla JS. No frameworks, no dependencies, no build step.**
Deployed as a static site on Vercel.

---

## Pages

Every landing page ships in **two versions**: one with temporary stock
photography, one with the real project photography.

| Page | Route | Status |
|---|---|---|
| Hub (index of landing pages) | `/` | Live |
| Custom Home Build — stock photos | `/custom-home-build-stock/` | Live |
| Custom Home Build — real photos | `/custom-home-build-real/` | Awaiting photography |
| Whole-Home Remodel — stock photos | `/whole-home-remodel-stock/` | Not built yet |
| Whole-Home Remodel — real photos | `/whole-home-remodel-real/` | Awaiting photography |
| Custom ADU & Guest Suite — stock photos | `/custom-adu-stock/` | Not built yet |
| Custom ADU & Guest Suite — real photos | `/custom-adu-real/` | Awaiting photography |

The hub at `/` is an internal index — it is `noindex, nofollow`. It shows one card
per landing page, each listing its two versions with an independent status; versions
that do not exist yet render as visibly inert, non-clickable rows.

Both versions of a page share the same `<link rel="canonical">` (the client's real
URL, e.g. `https://distinctdesignsconstruction.com/custom-home-build`), because they
are the same page — only the photography differs.

---

## Structure

```
.
├── index.html                          # Hub page
├── styles.css                          # Hub styles (shares the design tokens)
├── assets/                             # Hub card images
├── custom-home-build-stock/            # Landing page 1, stock photos — self-contained
│   ├── index.html
│   ├── styles.css                      # The design system
│   ├── script.js
│   ├── images/
│   └── README.md                       # Full page docs: tokens, classes, gotchas
└── distinct-designs-landing-pages.html # Source copy for all three pages
```

Each landing page folder is **self-contained** — its own HTML, CSS, JS, and images.
That keeps pages independently deployable and avoids one page's changes breaking another.

---

## Local development

No build step. Serve the folder with any static server:

```bash
python3 -m http.server 8000
# → http://localhost:8000/
```

Opening `index.html` directly via `file://` also works, but the root-relative link
to `/custom-home-build-stock/` will not resolve. Use a server.

---

## Adding the remaining two pages

Full instructions are in [`custom-home-build-stock/README.md`](custom-home-build-stock/README.md).
Short version:

1. `cp -r custom-home-build-stock whole-home-remodel-stock`
2. Swap in the copy from the matching `<article>` in `distinct-designs-landing-pages.html`
3. Update `<title>`, meta description, canonical URL, and the FAQ JSON-LD
4. Replace the images in that folder
5. In the hub's `index.html`, change that version's row from
   `<span class="hub-version hub-version--pending" aria-disabled="true">` to
   `<a class="hub-version" href="/whole-home-remodel-stock/">`, and swap its
   `hub-version__state` to `hub-version__state--live` with the label `Live`.
   Drop `hub-card--pending` from the `<li>` once that card has any live version.

To produce the **real-photo** version of a page, copy its stock folder to the
`-real` suffix, replace the images, and remove the `data-placeholder="true"`
attributes and `.grade` class as described in the per-page README.

The stylesheet is a shared design system driven by `:root` tokens — rebrand or
retune by editing those values, not individual rules.

---

## Photography

**Every image is currently a temporary stock placeholder** (royalty-free Unsplash,
re-encoded to WebP). They are all marked with `data-placeholder="true"` plus an
HTML comment describing what belongs in the slot.

Find every one that still needs swapping:

```bash
grep -rn 'data-placeholder' --include='*.html' .
```

Real project photography (La Mirada, Hilltop, Cubero, Alturas) replaces these.
See the per-page README for exact slot dimensions.

---

## Deployment

Deployed on Vercel as a static site — no framework preset, no build command.
Pushes to `main` deploy to production; pull requests get preview URLs.

---

## Conventions worth preserving

- **Scroll reveal fails open.** Content is visible by default; the hidden state is
  only armed by JS. Never move `opacity: 0` onto a bare `.reveal`.
- **Contrast is WCAG AA verified.** `--color-text-muted` is tuned to pass on both
  the page background and the sand background.
- **FAQ JSON-LD must stay in sync** with the visible FAQ copy on each page.
- **Copy is client-supplied and used verbatim.** Do not paraphrase or condense it.
