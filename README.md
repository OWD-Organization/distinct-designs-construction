# Distinct Designs Construction — Landing Pages

High-ticket lead capture landing pages for **Distinct Designs Construction**, a licensed
luxury custom home builder (CA GC #1145786) serving the High Desert and Coachella Valley.

**Pure HTML / CSS / vanilla JS. No frameworks, no dependencies, no build step.**
Deployed as a static site on Vercel.

---

## Pages

| Page | Route | Status |
|---|---|---|
| Hub (index of landing pages) | `/` | Live |
| Custom Home Build | `/custom-home-build/` | Live |
| Whole-Home Remodel | `/whole-home-remodel/` | Not built yet |
| Custom ADU & Guest Suite | `/custom-adu/` | Not built yet |

The hub at `/` is an internal index — it is `noindex, nofollow` and links to each
landing page. The two unbuilt pages render as visibly inert cards until they ship.

---

## Structure

```
.
├── index.html                          # Hub page
├── styles.css                          # Hub styles (shares the design tokens)
├── assets/                             # Hub card images
├── custom-home-build/                  # Landing page 1 — self-contained
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
to `/custom-home-build/` will not resolve. Use a server.

---

## Adding the remaining two pages

Full instructions are in [`custom-home-build/README.md`](custom-home-build/README.md).
Short version:

1. `cp -r custom-home-build whole-home-remodel`
2. Swap in the copy from the matching `<article>` in `distinct-designs-landing-pages.html`
3. Update `<title>`, meta description, canonical URL, and the FAQ JSON-LD
4. Replace the images in that folder
5. In the hub's `index.html`, change that card's wrapper from
   `<div class="hub-card__link" aria-disabled="true">` to
   `<a class="hub-card__link" href="/whole-home-remodel/">`, and swap its
   `hub-card__status` to `hub-card__status--live` with the label `Live`

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
- **Scrims over photography are sized by measurement, not by eye.** The hero
  scrim and the project-tile scrim were both set by sampling the rendered
  background behind each text block and checking it against WCAG AA. The tile
  scrim deliberately uses pixel gradient stops rather than percentages, because
  the label is a fixed size while the tiles are not.
- **Replacing an image under its existing filename does not bust caches.** When
  verifying a swap, check the image's intrinsic size against the file on disk
  rather than trusting a screenshot.
- **FAQ JSON-LD must stay in sync** with the visible FAQ copy on each page.
- **Copy is client-supplied and used verbatim.** Do not paraphrase or condense it.
