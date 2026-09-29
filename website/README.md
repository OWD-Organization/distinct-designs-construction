# Distinct Designs Construction website

Static HTML, CSS, and vanilla JS for the company website. It is self-contained in this folder so it can be deployed as its own Vercel project with **Root Directory = `website`**.

It does not replace the ad landing pages at the repository root. Those stay where they are.

No build step is required to deploy. `generate.py` and `pages.py` only regenerate the HTML if the copy changes:

```bash
python3 generate.py
python3 -m http.server 8000
# open http://localhost:8000/
```

## Do not index this site yet

Every page is `noindex, nofollow` until the client's domain is switched. Three layers:

1. `<meta name="robots" content="noindex, nofollow">` on every page.
2. `robots.txt` disallows all crawlers.
3. `vercel.json` sends `X-Robots-Tag: noindex, nofollow` on every route.

There is no sitemap.

### Removing noindex at launch

Do all of these in the same release, after the new domain is the one that should rank:

1. Delete the robots meta tag from `head()` in `generate.py`, regenerate, or remove the tag from each `index.html`.
2. Replace `robots.txt` with a normal allow rule, and only then add a sitemap if you want one.
3. Remove the `X-Robots-Tag` header from `vercel.json`.
4. Add a self-referencing canonical on each page pointing at the new domain (canonicals are intentionally omitted while the site is noindex).
5. Confirm the CSLB license number before publishing it sitewide. See TODOs.
6. Point DNS at this Vercel project only after the tags above are gone. Leaving noindex on the live domain hides the site from Google.

The `X-Robots-Tag` header applies when this folder is the Vercel root. On a preview of the whole repository, the meta tag is what keeps `/website/` out of the index.

## Deploy as its own Vercel project

1. New Project, same Git repository.
2. Root Directory: `website`.
3. Framework preset: Other. No build command. Output directory: leave blank (the folder itself is the site).
4. Do not attach the production domain until noindex is removed.
5. Leave the existing landing-page project on the repository root alone.

Clean URLs come from folder `index.html` files (`/services/custom-home-build/`).

## Lead forms

Forms are the same public LeadConnector widgets already embedded on distinctdesignsconstruction.com. They are not a new backend.

| Form | Widget id | Used on |
|---|---|---|
| Planning guide | `YQYYVz28qqwYJWbc8ZUw` | Home, service pages, guide landings |
| Contact | `IbFWLZlZNETBrImKFVjN` | Home, contact |
| Guide variant 1 | `d3BGxWF34ECOkqZdjpSI` | `/guides/custom-home-builder-1/` |
| Guide variant 2 | `BAGEhP3HzpQSiPNrrCqf` | `/guides/custom-home-builder-2/` |
| Guide variant 3 | `9M9TcIWN7yJsuz9QWG1R` | `/guides/custom-home-builder-3/` |
| Agent referral | `MyS2TrJSOhTn1mitpihf` | `/partners/referral-agreement/` |

TODO: confirm LeadConnector accepts submissions from the new domain.

## TODOs and missing information

- **Street address.** The current site only publishes "Joshua Tree, CA". No street, ZIP, or postal address was found. JSON-LD uses locality and region only.
- **Two license numbers are published today.** The homepage FAQ says License #1039394. The ad landing pages and the guide pages say License #1145786. Both are copied where they appeared. The sitewide footer does not pick one. Confirm which CSLB number should be shown everywhere before launch.
- **Sun Mesa.** `/sun-mesa/` on the current site repeats the Hilltop case study (including the words "Hilltop build") and uses the La Mirada photo set. Copied as published. See the HTML comment on `/projects/sun-mesa/`.
- **Cookie statement.** `/opt-out-preferences/` is only the Complianz shortcode `[cmplz-document type="cookie-statement" region="us"]`. That statement did not render in the page source. The visible cookie-banner sentence is included, with a TODO on the page.
- **Gallery category URLs 404.** `/general-construction/`, `/home-remodels/`, `/kitchen-remodels/`, and `/tile-stone-masonry/` are linked from the current projects page and return 404. The card titles and photos are kept on `/projects/`. FooGallery albums exist in WordPress but are not public pages, so their full image sets were not copied.
- **Joel photo.** The file beside Joel's name on the current about page has the alt text "General Lead Tile and Stone Installer". The heading is Joel, tile and stone designer and installer. Randy and Fredo were duplicated in the source layout and are listed once.
- **Tracking not copied.** The current site loads Google tags `G-ZN3C7W7TY1` and `GT-PLHFGS6K`, and Facebook pixel `2036241113908440`. They were left off this noindex build. Add them at launch if they should carry over. The ad landing pages' WhatConverts and Feedbucket scripts were not added here.
- **Hero-form landing variants** are A/B tests of the same three services. They are not separate service pages.
- **Price bands differ by source.** Guide pages say project levels from $250K to $4.5M+. Custom-home landing copy says ground-up homes from $870K to $5M+. Both are kept on the pages they came from.
- **Coachella** (the city) is listed on the landing pages and was added to the combined service-area list. The current site footer did not name it separately from "Coachella Valley".
- **Phone punctuation.** The current footer link text is missing a closing parenthesis: `(760 221-4290`. The contact page shows `(760) 221-4290`. This site uses the contact-page formatting.

## Photography

Real project photos already in this repository are reused (logo, remodel and ADU heroes, project tiles, crew and detail shots). The stock custom-home hero (`hero-loggia`, marked `data-placeholder`) was not used. Photos that exist only on the current site (team, Mario Trujillo, project galleries, planning-guide cover) were downloaded into `images/site/`.
