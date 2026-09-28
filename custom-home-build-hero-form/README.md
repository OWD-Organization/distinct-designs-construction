# Distinct Designs Construction — Custom Home Build Landing Page

Production-ready landing page for `/custom-home-build`. Pure HTML/CSS/vanilla JS.
**No frameworks, no build step, no dependencies.** Open `index.html` or serve the folder.

```
custom-home-build/
├── index.html      # Page markup + FAQ JSON-LD
├── styles.css      # Design system + page styles (18 numbered sections)
├── script.js       # Nav, scroll reveal, accordion, form
└── images/         # WebP placeholder photography (see "Swapping Photography")
```

---

## Reusing this for the Remodel and ADU pages

The stylesheet is a **shared design system**, not one-off page styling. To build
`/whole-home-remodel` and `/custom-adu`:

1. Copy `styles.css` and `script.js` as-is. Nothing in either file is specific to
   the custom-home page.
2. Copy `index.html`, then swap the copy from the matching `<article>` in
   `distinct-designs-landing-pages.html`.
3. Update `<title>`, `<meta name="description">`, `<link rel="canonical">`, and the
   FAQ JSON-LD block at the bottom.
4. Drop in that page's images using the same filenames.

Every section is built from reusable classes, so the structure carries over directly:

| Class | Purpose |
|---|---|
| `.section` | Standard section container (max-width + padding) |
| `.section--narrow` | Caps inner content to a reading measure, still left-aligned |
| `.section--tinted` | Full-bleed sand background, inner content re-wrapped |
| `.section--split` | Asymmetric text/media split (stacks below 1024px) |
| `.section__header` | Section heading + intro paragraph |
| `.process-steps` | Numbered process list |
| `.projects-grid` + `.project-tile` | Asymmetric 4-cell bento (see note below) |
| `.why-us-grid` + `.why-us-card` | 2×2 differentiator grid |
| `.testimonial-stack` | Editorial pull-quotes |
| `.accordion` | FAQ accordion |
| `.areas-grid` / `.areas-list` | Primary/secondary service areas |
| `.lead-section` + `.lead-form` | Dark lead-capture footer |
| `.btn` + `--primary` / `--secondary` / `--nav` / `--sticky` | Buttons |
| `.reveal` | Opt into the scroll-reveal animation |
| `.grade` | Unifying warm color grade on placeholder photos |

**Design tokens** live in `:root` at the top of `styles.css` (color, type scale,
spacing scale, layout widths, easing). Rebrand or retune by editing those values only.

> **Bento note:** `.projects-grid` places tiles *by position* (`:nth-child`) at
> ≥900px into a 4-cell asymmetric layout: tall left, two stacked right, one wide
> across the bottom. It expects **exactly 4 tiles**. Changing the count means
> updating those `nth-child` rules, or there will be empty cells.

---

## Swapping Photography

Most images are **temporary stock placeholders**, marked two ways:

- `data-placeholder="true"` on the `<img>`
- An HTML comment above it describing what belongs there

**Two assets are already real and must not be treated as placeholders:**

| Asset | Notes |
|---|---|
| `logo-distinct-designs.webp` | Brand logo in the nav. 350×128 source with transparency, shown at 46px tall. The lockup uses dark navy text, so it only works on a light bar — it needs a light variant before going on any dark background. |
| `process-crew.webp` | Real crew photography in a completed build. Carries **no** `.grade` class and **no** `data-placeholder`, so its true colour survives. The warm unifying grade skews skin tones, so never apply it to real photos of people. |
| `project-la-mirada.webp` | Real interior of the finished La Mirada remodel. Native 3:4 (900×1200), which matches the tall bento tile on mobile exactly; at desktop the tile is 0.65 so `cover` trims the sides. Also no `.grade`, no `data-placeholder`. |
| `project-hilltop.webp` | Real interior of the Hilltop build. Source was already 4:3, so it is a straight resize to 900×675. |
| `project-cubero.webp` | Real aerial of the Cubero build. Source was 3:2, centre-cropped to 4:3 before resizing — the house and pool sit centre-frame, so nothing important is lost. |
| `project-alturas.webp` | Real in-progress shot. Built from the 2400px Cloudinary original. Sized 1400×932 (1.6× the 857px display width) rather than larger: the fine sheathing texture encodes expensively, so more pixels cost far more bytes than they return. Its tile no longer carries `--tall`: the cell is placed wide at desktop and the photo is landscape, so the default 4:3 is correct on mobile too. |

| `footer-cta.webp` | Real interior for the lead section. Native 3:2. Note this slot's box **flips ratio** between breakpoints — roughly 0.60 (a tall column beside the form) at desktop, but 1.34 (a wide band above it) on mobile — so `cover` crops the sides at desktop and shows almost the full frame on mobile. A landscape source suits it because the mobile band is the wider of the two. |

| `process-break.webp` | Real dusk terrace for the full-width break. Native 16:9. This band is unusual: its height comes from the **image's own ratio** until `max-height: 640px` binds, so the source ratio changes the layout. At 16:9 the full frame shows on mobile, and wide desktops centre-crop to roughly 2.2–3.0, which still holds the string lights, fire bowl and spa. |

**Only the hero is still a placeholder.** Everything else is real photography,
and `.grade` now applies to exactly one image. Once the hero is replaced, delete
the `.grade` rule (§6) and its last usage — it exists only to reconcile mixed
stock sources.

> **The project-tile scrim uses PIXEL stops, not percentages** (§11). The label
> is a fixed size, so its protection band must be too. With percentages the
> short wide Alturas cell (310px tall) got far less absolute darkening than the
> 640px tall cell, and its label measured 3.84:1 over bright sheathing. Keep the
> stops in px, and re-measure if the label's size or position changes.
>
> The scrim was later lightened on request so more of each photograph shows
> through. Current worst-case label contrast: La Mirada 13.07, Hilltop 12.42,
> Cubero 10.86, Alturas 7.40 with its italic sub-line at 5.24. **The italic
> sub-line is the binding constraint** — it is the smallest text over the
> brightest photo. Lighten further only with a re-measurement; it has about
> 16% of headroom left before it drops under AA.

The wide bento tiles are **4:3 (900×675)**, matching the tile ratio on mobile
exactly. The older stock assets were 900×700, which was slightly off.

> **Reusing a filename busts nothing.** These replacements kept their existing
> names, so a browser that already has the old bytes will keep showing them until
> its cache revalidates. If you replace an image and it looks unchanged, hard-reload
> before assuming the swap failed.

Do the same for each real photo as it arrives: drop `.grade` and
`data-placeholder` rather than leaving the unifying filter on top of it.

Find them all with:

```bash
grep -n 'data-placeholder' index.html
```

| File | Slot | Target size | Replace with |
|---|---|---|---|
| `hero-loggia.webp` (+ `-1200`) | Hero background | 1672×941 / 1200×675 | Signature exterior or loggia, wide 16:9 |
| `process-crew.webp` | Process split | 1200×900 | **Already real** — crew in a finished build |
| `process-break.webp` | Full-width break | 1920×1081 | **Already real** — desert terrace at dusk |
| `project-la-mirada.webp` | Bento, tall | 900×1200 | **Already real** — La Mirada Remodel |
| `project-hilltop.webp` | Bento | 900×675 | **Already real** — Hilltop Build |
| `project-cubero.webp` | Bento | 900×675 | **Already real** — Cubero Build |
| `project-alturas.webp` | Bento, wide | 1400×932 | **Already real** — Alturas Build, in progress |
| `footer-cta.webp` | Lead section | 1600×1066 | **Already real** — finished great room |

Current placeholders are royalty-free Unsplash photography (Unsplash License —
free for commercial use, no attribution required), re-encoded to WebP. The hero
is a client-supplied generated image, also re-encoded to WebP.

`hero-desert-home.webp` (+ `-1200`, 504 KB) and `process-blueprint.webp` (104 KB)
are superseded and now unreferenced, kept only so the earlier treatments are easy
to restore. Safe to delete.

**The hero scrim is tuned to the hero image.** `.hero__scrim` (styles.css §9)
carries two stacked gradients sized for a *bright* photograph. If you swap in a
dark hero, re-measure rather than keeping these values: sample the pixels behind
each text block and check white/`#d1dae5` type still clears WCAG AA, then dial
the alpha back so the photograph is not needlessly flattened.

**Keep the hero's `width`/`height` attributes and `fetchpriority="high"`** — they
protect CLS and LCP. Below-the-fold images use `loading="lazy"`.

The `.grade` class applies a warm, slightly desaturated CSS filter so mixed-source
placeholders read as one set. **Once real, consistently-graded project photography
is in, remove `.grade` from the `<img>` tags** (or empty the rule in `styles.css`
§6) so the real color grading shows through untouched.

---

## Project lightbox

Each project tile opens its photograph in a native `<dialog>` (`#lightbox`).

The tiles are `<button>` elements, not links — they trigger in-page UI rather
than navigating. They previously pointed at `/la-mirada`, `/hilltop` and
`/cubero`, none of which exist on this site, so all three were 404s.

`showModal()` supplies focus trapping, Esc-to-close and an inert background from
the platform, so none of that is hand-rolled. `script.js` adds only: setting the
image and caption, the close button, outside-click-to-close, and clearing `src`
on close so a large photo is not held in memory. If `<dialog>` is unsupported the
tiles are disabled rather than left half-working.

Because the tiles are buttons, `.project-tile` clears the UA button styling
(padding, border, background, font, text-align) before the tile look applies.
Removing that reset will visibly break the grid.

---

## Wiring up the lead form

The form currently validates client-side and shows a confirmation message, but
**does not submit anywhere**. In `script.js`, find:

```js
// TODO: wire to real submission endpoint (CRM, email service, etc.)
```

Replace that branch with a `fetch()` to your CRM/webhook. Keep the existing
validation guard and the `#lead-form-note` status message (it is `aria-live`, so
screen readers announce the result).

---

## Accessibility & performance notes

Please preserve these when editing — each is deliberate:

- **Scroll reveal fails open.** Content is visible by default; the hidden start
  state is only applied via `html.js-reveal`, added by an inline script in `<head>`.
  If JS fails, the page still renders fully. Never move `opacity: 0` onto bare `.reveal`.
- **Reduced motion** is honored globally and in `script.js` (`prefers-reduced-motion`).
- **Hero sizing** is `calc(100dvh - var(--nav-h))`, not `100vh`. The sticky nav
  occupies layout flow, and `dvh` avoids the iOS Safari address-bar jump.
  `--nav-h` (71px) must match the nav's real height, which the logo now sets, so
  it is identical at every breakpoint and needs no media-query override.
  **If you resize the logo, re-measure the nav and update `--nav-h`**, or the
  hero will over- or under-shoot one viewport.
- **Contrast**: the palette is WCAG AA verified. `--color-text-muted` (`#686155`)
  is set to pass on *both* the page background and the sand background.
- **`[id] { scroll-margin-top }`** keeps anchor-linked headings clear of the sticky nav.
- **FAQ JSON-LD** at the bottom of `index.html` must be kept in sync with the
  visible FAQ copy, or the rich snippet becomes invalid.

---

## Verified

Checked in Chrome at 390×844, 768×1024, and 1440×900:

- Hero CTAs above the fold at all three; no horizontal overflow
- All 8 images load; lazy-loading and scroll reveals fire
- FAQ accordion, mobile nav toggle, sticky CTA bar, and form validation all work
- FAQ JSON-LD parses and matches the visible questions exactly
- All 405 distinct words of the source copy present verbatim
