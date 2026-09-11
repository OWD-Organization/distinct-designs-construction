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
| Whole-Home Remodel | `/whole-home-remodel/` | Live |
| Custom ADU & Guest Suite | `/custom-adu/` | Live |

The hub at `/` is an internal index — it is `noindex, nofollow` and links to each
landing page. All three pages are now built and linked.

The remodel and ADU pages are fully photographed, and `placeholder.svg` is gone
with their last gray blocks. **One placeholder remains: the custom-home-build
hero**, which is also the only image still carrying the `.grade` filter — once it
is replaced, that rule and its last usage can be deleted.

The three hub card images are also stand-ins, but the hub is an internal
`noindex` index, so they are lower priority.

The ADU page's budget dropdown ranges are an assumption — the source copy does not
specify them — and are marked with a TODO in the markup.

### Shared photographs

Shared photos are duplicated into each page's own `images/` folder rather than
served from one place, which keeps every page folder self-contained and
independently deployable. The trade-off: replacing a shared photo means replacing
it in every folder that uses it.

| Photo | Used on |
|---|---|
| the four project tiles | all three pages |
| `footer-cta.webp` (great room) | custom-home-build, custom-adu |
| `process-crew.webp` | each page has its own crew photo |

Two photos were shared and then diverged. On the ADU page they are named for their
**subject** rather than their slot or origin, so no two files share a name with
different contents:

- `hero-garage.webp` — the garage, once the remodel hero
- `process-break-patio.webp` — the sunset patio, once the remodel transition band

Both of those slots on the remodel page now hold different photographs under their
original names. **When a shared photo diverges, rename the copy** rather than
leaving two files with one name and two contents.

---

## Structure

```
.
├── index.html                          # Hub page (no footer, no JS)
├── styles.css                          # Hub styles (shares the design tokens)
├── assets/                             # Hub card images
├── custom-home-build/                  # Landing page 1 — self-contained
│   ├── index.html
│   ├── styles.css                      # The design system
│   ├── script.js
│   ├── images/
│   └── README.md                       # Full page docs: tokens, classes, gotchas
├── whole-home-remodel/                 # Landing page 2 — self-contained
├── custom-adu/                         # Landing page 3 — self-contained
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

## Adding another page

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

The landing pages carry real project photography throughout. Only the
custom-home-build hero is still stock.

Placeholders are marked two ways, so any that reappear are easy to find:

```bash
grep -rn 'data-placeholder' --include='*.html' .
```

That currently returns the custom-home-build hero plus the three hub card images,
which are stand-ins on an internal `noindex` page.

When swapping a real photo in, drop both the `.grade` class and the
`data-placeholder` attribute — the grade exists only to reconcile mismatched stock
sources and skews skin tones over photographs of people. See the per-page README
for exact slot dimensions.

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
- **`--nav-h` must equal the bar's real height at every width.** The hero is
  `calc(100dvh - var(--nav-h))`, so a 2px drift shows up as the hero overshooting
  the viewport. The link list therefore carries `white-space: nowrap` and
  `flex-shrink: 0`: when flex squeezed a label into wrapping, the bar grew to 73px
  and broke the calculation. Measured minimum for logo + links + button pair is
  about 1090px, which is why the links appear at 1120 and not at 1024.
- **Copy is client-supplied and used verbatim.** Do not paraphrase or condense it.
