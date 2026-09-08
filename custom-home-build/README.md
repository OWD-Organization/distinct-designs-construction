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

Every image is a **temporary stock placeholder** and is marked two ways:

- `data-placeholder="true"` on the `<img>`
- An HTML comment above it describing what belongs there

Find them all with:

```bash
grep -n 'data-placeholder' index.html
```

| File | Slot | Target size | Replace with |
|---|---|---|---|
| `hero-loggia.webp` (+ `-1200`) | Hero background | 1672×941 / 1200×675 | Signature exterior or loggia, wide 16:9 |
| `process-blueprint.webp` | Process split | 1200×900 | Real renderings / permit set |
| `process-break.webp` | Full-width break | 1600×750 | In-progress job site |
| `project-la-mirada.webp` | Bento, tall | 900×1100 | La Mirada Remodel |
| `project-hilltop.webp` | Bento | 900×700 | Hilltop Build |
| `project-cubero.webp` | Bento | 900×700 | Cubero Build |
| `project-alturas.webp` | Bento, wide | 900×1100 | Alturas Build |
| `footer-cta.webp` | Lead section | 1600×1000 | Hero-quality exterior |

Current placeholders are royalty-free Unsplash photography (Unsplash License —
free for commercial use, no attribution required), re-encoded to WebP. The hero
is a client-supplied generated image, also re-encoded to WebP.

`hero-desert-home.webp` (+ `-1200`) is the previous hero, now unreferenced —
kept only so the earlier treatment is easy to restore. Safe to delete.

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
  occupies layout flow, and `dvh` avoids the iOS Safari address-bar jump. If nav
  height changes, update `--nav-h` (mobile) and its `@media (min-width: 1024px)` override.
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
