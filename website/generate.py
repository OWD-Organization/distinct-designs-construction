#!/usr/bin/env python3
"""Generate the static Distinct Designs Construction website.

Run from anywhere:
    python3 website/generate.py

Output is plain HTML. Vercel does not need this script.
"""

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent

PHONE_DISPLAY = "(760) 221-4290"
PHONE_TEL = "+17602214290"
EMAIL = "distinctdesigns360@gmail.com"

# Published service area from the current site footer, plus Coachella,
# which the landing pages list as a city they serve.
AREAS = [
    "Joshua Tree",
    "Yucca Valley",
    "Twentynine Palms",
    "Pioneer Town",
    "Landers",
    "Morongo Valley",
    "Palm Springs",
    "Desert Hot Springs",
    "Palm Desert",
    "Cathedral City",
    "Rancho Mirage",
    "La Quinta",
    "Indian Wells",
    "Indio",
    "Coachella",
]

PRIMARY = [
    "Yucca Valley",
    "Joshua Tree",
    "Palm Springs",
    "Palm Desert",
    "La Quinta",
    "Indian Wells",
]
SECONDARY = [
    "Rancho Mirage",
    "Cathedral City",
    "Coachella",
    "Twentynine Palms",
    "Pioneer Town",
    "Landers",
    "Morongo Valley",
    "Desert Hot Springs",
    "Indio",
]

GUIDE_FORM = "YQYYVz28qqwYJWbc8ZUw"
CONTACT_FORM = "IbFWLZlZNETBrImKFVjN"
REFERRAL_FORM = "MyS2TrJSOhTn1mitpihf"

NAV = [
    ("Projects", "projects"),
    ("About", "about"),
    ("Contact", "contact"),
]
SERVICE_LINKS = [
    ("Custom Home Build", "services/custom-home-build"),
    ("Whole House Remodel", "services/whole-home-remodel"),
    ("Custom ADU and Guest Suite", "services/custom-adu"),
    ("Remodels", "services/remodels"),
]
# These six already appear on the published service-area list. Each has a page.
# Other cities in AREAS stay as text until a page exists for them.
AREA_LINKS = [
    ("Yucca Valley", "service-areas/yucca-valley"),
    ("Joshua Tree", "service-areas/joshua-tree"),
    ("Palm Springs", "service-areas/palm-springs"),
    ("Palm Desert", "service-areas/palm-desert"),
    ("La Quinta", "service-areas/la-quinta"),
    ("Indian Wells", "service-areas/indian-wells"),
]
AREA_TARGET = dict(AREA_LINKS)
# /remodels/ is the preserved best-general-contractor page, not the
# kitchens/baths/additions service. Keep it reachable without reusing
# the Services label "Remodels".
MOBILE_EXTRA = [
    ("Best general contractor", "remodels"),
    ("Planning Guide", "planning-guide"),
    ("Partners", "partners"),
]


def prefix(slug: str) -> str:
    depth = len([p for p in slug.split("/") if p])
    return "../" * depth


def href(slug: str, target: str) -> str:
    pre = prefix(slug)
    target = target.strip("/")
    if not target:
        return pre or "./"
    return f"{pre}{target}/"


def asset(slug: str, path: str) -> str:
    return prefix(slug) + path


def business_ld() -> str:
    data = {
        "@context": "https://schema.org",
        "@type": ["HomeAndConstructionBusiness", "GeneralContractor"],
        "name": "Distinct Designs Construction",
        "description": (
            "Luxury custom homes and high-end renovations across the High Desert "
            "and greater Southern California."
        ),
        "telephone": "+1-760-221-4290",
        "email": EMAIL,
        "image": "https://distinctdesignsconstruction.com/wp-content/uploads/2026/02/DD-logo-full.webp",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Joshua Tree",
            "addressRegion": "CA",
            "addressCountry": "US",
        },
        "areaServed": [
            {"@type": "City", "name": city} for city in AREAS
        ],
        "sameAs": [
            "https://www.instagram.com/distinctdesignsconst/",
            "https://www.facebook.com/profile.php?id=61561101665757",
            "https://www.yelp.com/biz/distinct-designs-yucca-valley-6",
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def faq_ld(items):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in items
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def head(slug, title, description, extra_ld=""):
    p = prefix(slug)
    extra = ""
    if extra_ld:
        extra = f'\n<script type="application/ld+json">{extra_ld}</script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{p}favicon.jpg" type="image/jpeg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400&amp;family=Manrope:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}styles.css">
<script>document.documentElement.classList.add("js-reveal");</script>
<script type="application/ld+json">{business_ld()}</script>{extra}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def current(slug, target):
    if slug == target or slug.startswith(target + "/"):
        return ' aria-current="page"'
    return ""


def dropdown_menu(slug, label, links, menu_id, active, start_open=False):
    current_attr = ' aria-current="true"' if active else ""
    expanded = "true" if start_open else "false"
    open_class = " is-open" if start_open else ""
    items = []
    for item_label, target in links:
        items.append(
            f'<a role="menuitem" href="{href(slug, target)}"{current(slug, target)}>{item_label}</a>'
        )
    return f"""<div class="nav-dropdown{open_class}">
      <button type="button" class="nav-dropdown__toggle" aria-expanded="{expanded}" aria-haspopup="true" aria-controls="{menu_id}"{current_attr}>{label}</button>
      <div class="nav-dropdown__panel" id="{menu_id}" role="menu" aria-label="{label}">
        {"".join(items)}
      </div>
    </div>"""


def service_menu(slug, menu_id, start_open=False):
    on_services = slug == "services" or slug.startswith("services/")
    return dropdown_menu(slug, "Services", SERVICE_LINKS, menu_id, on_services, start_open)


def area_menu(slug, menu_id):
    on_area = slug.startswith("service-areas/")
    return dropdown_menu(slug, "Service Areas", AREA_LINKS, menu_id, on_area)


def nav(slug):
    p = prefix(slug)
    links = [service_menu(slug, "services-menu"), area_menu(slug, "areas-menu")]
    mobile = [service_menu(slug, "services-menu-mobile", start_open=True), area_menu(slug, "areas-menu-mobile")]
    for label, target in NAV:
        links.append(
            f'<a href="{href(slug, target)}"{current(slug, target)}>{label}</a>'
        )
        mobile.append(
            f'<a href="{href(slug, target)}"{current(slug, target)}>{label}</a>'
        )
    for label, target in MOBILE_EXTRA:
        mobile.append(
            f'<a href="{href(slug, target)}"{current(slug, target)}>{label}</a>'
        )
    mobile.append(
        f'<a class="btn btn--nav" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>'
    )
    mobile.append(
        f'<a class="btn btn--primary" href="{href(slug, "contact")}">Schedule a Consultation</a>'
    )
    return f"""<header class="site-nav" id="site-nav">
  <div class="site-nav__inner">
    <a href="{href(slug, "")}" class="site-nav__logo">
      <img src="{p}images/logo-distinct-designs.webp" alt="Distinct Designs Construction" width="350" height="128">
    </a>
    <nav class="site-nav__links" aria-label="Primary">
      {"".join(links)}
    </nav>
    <div class="site-nav__actions">
      <a class="btn btn--nav" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <a class="btn btn--nav-primary" href="{href(slug, "contact")}">Schedule a Consultation</a>
    </div>
    <button class="site-nav__toggle" id="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav__mobile">
      <span></span><span></span><span></span>
    </button>
  </div>
  <nav class="site-nav__mobile" id="site-nav__mobile" aria-label="Mobile">
    {"".join(mobile)}
  </nav>
</header>
<div class="sticky-cta" id="sticky-cta">
  <p>Ready to talk about your project?</p>
  <a href="tel:{PHONE_TEL}" class="btn btn--sticky">Call {PHONE_DISPLAY}</a>
</div>
"""


def footer(slug):
    p = prefix(slug)
    cols_services = [
        ("Custom home build", "services/custom-home-build"),
        ("Whole-home remodel", "services/whole-home-remodel"),
        ("Custom ADU", "services/custom-adu"),
        ("All services", "services"),
        ("Remodels", "services/remodels"),
    ]
    cols_company = [
        ("About", "about"),
        ("Projects", "projects"),
        ("Best general contractor", "remodels"),
        ("Contact", "contact"),
        ("Planning guide", "planning-guide"),
        ("Partners", "partners"),
        ("Privacy policy", "privacy-policy"),
        ("Opt-out preferences", "opt-out-preferences"),
    ]
    def nav_list(items):
        return "".join(
            f'<a href="{href(slug, t)}">{label}</a>' for label, t in items
        )
    named = [city_anchor(slug, name) for name in AREAS]
    areas = ", ".join(named[:-1]) + ", and " + named[-1]
    return f"""<footer class="site-footer">
  <div class="site-footer__inner">
    <div class="site-footer__cols">
      <div>
        <img class="site-footer__logo" src="{p}images/site/distinct-web-white-300x112.png" alt="Distinct Designs Construction" width="300" height="112">
        <p class="site-footer__brand">Distinct Designs Construction</p>
        <p>Joshua Tree, CA</p>
        <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>Licensed, bonded, and insured.</p>
        <p><a href="https://www.instagram.com/distinctdesignsconst/">Instagram</a> · <a href="https://www.facebook.com/profile.php?id=61561101665757">Facebook</a> · <a href="https://www.yelp.com/biz/distinct-designs-yucca-valley-6">Yelp</a></p>
      </div>
      <div>
        <h2>Services</h2>
        <nav aria-label="Services">{nav_list(cols_services)}</nav>
      </div>
      <div>
        <h2>Company</h2>
        <nav aria-label="Company">{nav_list(cols_company)}</nav>
      </div>
      <div>
        <h2>Service areas</h2>
        <p>{areas}. For the right project, also greater Southern California.</p>
      </div>
    </div>
  </div>
  <p class="site-footer__legal">&copy; <span id="year"></span> Distinct Designs Construction. All rights reserved.</p>
</footer>
<dialog class="lightbox" id="lightbox" aria-label="Enlarged project photograph">
  <button class="lightbox__close" id="lightbox-close" type="button" aria-label="Close">&times;</button>
  <figure class="lightbox__figure">
    <img class="lightbox__img" id="lightbox-img" alt="">
    <figcaption class="lightbox__caption" id="lightbox-caption"></figcaption>
  </figure>
</dialog>
<script src="{p}script.js"></script>
</body>
</html>
"""


def hero(slug, image, alt, width, height, srcset, eyebrow, h1, sub, primary_href, primary_label, page=False):
    p = prefix(slug)
    klass = "hero hero--page" if page else "hero"
    srcset_attr = f'\n      srcset="{srcset}"\n      sizes="100vw"' if srcset else ""
    priority = "high" if not page else "auto"
    loading = "" if not page else ' loading="eager"'
    return f"""<header class="{klass}">
  <img class="hero__image" src="{p}{image}"{srcset_attr} alt="{alt}" width="{width}" height="{height}" fetchpriority="{priority}"{loading}>
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="subhead">{sub}</p>
    <nav class="hero-cta" aria-label="Hero">
      <a href="tel:{PHONE_TEL}" class="btn btn--secondary">Call {PHONE_DISPLAY}</a>
      <a href="{primary_href}" class="btn btn--primary">{primary_label}</a>
    </nav>
  </div>
</header>
"""


def faq_html(slug_prefix, items):
    blocks = []
    for i, (q, a) in enumerate(items, 1):
        fid = f"{slug_prefix}-faq-{i}"
        blocks.append(f"""<div class="accordion__item">
  <h3><button class="accordion__trigger" aria-expanded="false" aria-controls="{fid}">{q}</button></h3>
  <div class="accordion__panel" id="{fid}"><p>{a}</p></div>
</div>""")
    return '<div class="accordion">' + "".join(blocks) + "</div>"


def quotes_html(items):
    blocks = []
    for quote, cite in items:
        blocks.append(f"<blockquote><p>&ldquo;{quote}&rdquo;</p><cite>{cite}</cite></blockquote>")
    return '<div class="testimonial-stack reveal">' + "".join(blocks) + "</div>"


HOME_QUOTES = [
    ("Nick and team went above and beyond! Great attention to detail and excellent communication.", "Jessica &amp; Laura Myers"),
    ("Nick and everyone on his team are just simply the best. He gave us a magical bathroom and also helped out with new wood-trimmed windows and doors. Everyone was super kind, super fast, and really skilled. Nick's passion for his job shows, and it made the process really personal and fun. So happy with the results!", "Victoria Lynn Carroll"),
    ("Nick and his crew were very professional, always on time to the job site, respectable of the house, and cleaned up after themselves. Nick built a covered patio for me. It came out amazing and fair price too. I highly recommend Nick for any general construction.", "Troy Gatchell"),
    ("Nick and his crew were by far the best contractors I have worked with out here in Yucca Valley/Landers.", "Katie Lee"),
]

GUIDE_QUOTES = [
    ("A full down to the studs remodel finished on time and on budget, accessible the whole way, prompt with every update.", "Ken Z. · Whole-Home Remodel"),
    ("A complete remodel in Joshua Tree. Professional, detail-oriented, delivered on time and on budget.", "Benoit R. · Joshua Tree"),
    ("Called about our remodel and Nick came to the house the same day and communicated with us every step.", "Hannah S. · Remodel"),
]

HOME_FAQ = [
    ("What do you specialize in?",
     "We specialize exclusively in high-end custom construction and luxury renovations across the high desert and greater Southern California region. Our services include Custom Luxury Home Construction, Whole-Home Renovations and Transformations, Designer Kitchen Renovations and Remodels, Luxury Bathroom Renovations, Remodels and Additions, Custom ADU and Guest Suite Construction, and Full-Service Architecture and Engineering Coordination. Every project is handled by our dedicated in-house team from the first consultation to the final walkthrough: no rotating subcontractors, no compromises."),
    ("Are you licensed, bonded, and insured?",
     "Yes. Distinct Designs Construction is a fully licensed, bonded, and insured contractor. License #1039394. Your investment and your property are fully protected from day one."),
    ("How do you handle budgets and prevent cost overruns?",
     "Before a single shovel breaks ground we conduct a thorough pre-construction design-to-budget matching process. Every material selection, design detail, and architectural decision is carefully evaluated and priced upfront so you have a clear and accurate picture of your total investment from day one. No mid-build surprises, no forced compromises, and no uncomfortable conversations about costs that should have been addressed from the start. If an element of the design needs to be reconsidered we identify it early and present alternatives that meet the same standard, before you have committed to it."),
    ("How do you keep clients informed throughout the build?",
     "Communication is one of our most important commitments to every client. You receive real-time photo updates through our client portal powered by CompanyCam plus detailed bi-weekly field reports so you always know exactly where your project stands. When you reach out you hear back the same day, directly from leadership or your dedicated project manager, not a receptionist or voicemail box. Text, email, or phone call: we are always accessible. You will never feel out of the loop on your own project."),
    ("Do you work with architects and interior designers?",
     "Absolutely. We have longstanding relationships with top architects, designers, and realtors throughout the high desert and greater Southern California region. We are experienced at bringing precise design visions to life without ever compromising the intent, and our trusted partners regularly refer their most discerning clients to us because they know the work will be executed with the same level of care and precision they put into their own. When your architect, designer, and builder operate in true partnership the vision actually gets built exactly as intended."),
    ("What does your pre-construction process look like?",
     "Before we break ground we invest significant time in the pre-construction phase because we believe the work done before construction begins is what separates a smooth build from a stressful one. This includes a thorough consultation to understand your vision, lifestyle, and budget, complete design-to-budget matching to ensure everything is aligned before any commitments are made, full coordination with your architect or designer, permitting and approval management, and a detailed project timeline so you know exactly what to expect and when. You move forward with complete confidence knowing every dollar has been accounted for and every detail has been planned with purpose."),
    ("How long does a custom home build or full remodel typically take?",
     "Every project is unique and timelines vary based on scope, size, and complexity. A full custom home build typically ranges from 10 to 18 months depending on design, permitting, and finish selections. A full home remodel can range from 2 to 6 months. What sets us apart is not just the timeline we give you. It is how we protect it. Our pre-construction process, dedicated crew, and proactive communication system are all specifically designed to prevent the delays that derail most builds. You will always know where your project stands and why."),
    ("Can you manage my project if I live out of state or travel frequently?",
     "Yes and we do it regularly. Our client portal provides real-time photo updates, our bi-weekly field reports keep you fully informed, and we offer scheduled video calls throughout the build so you always feel completely in control without needing to be on site. We act as your eyes and ears on the ground so you never have to wonder what is happening with your investment. Many of our most successful and celebrated projects have been built for out-of-state clients who trusted our process and never once felt out of the loop."),
    ("What makes Distinct Designs Construction different from other contractors?",
     "Several things set us apart and none of them are accidental. We bring the same dedicated crew from day one to move-in day: no rotating strangers on your job site. We match your design to your budget before we ever break ground so there are no costly surprises mid-build. You have direct access to leadership on every project, not an assistant, not a call center. Our job sites are kept clean, organized, and fully protected throughout every phase of construction. And when something unexpected comes up, because in construction something always does, we are already handling it before you even knew there was a problem. We don't just build homes. We protect your investment and deliver something you will be proud of for decades."),
    ("Do you handle permits and inspections?",
     "Yes. We manage the entire permitting and inspection process on your behalf from plan approvals through certificates of occupancy. You never have to chase down paperwork, navigate local bureaucracy, or follow up with city offices on your own. This is especially valuable for first-time luxury builders and out-of-state clients who need a builder they can fully trust to manage every detail of the process, not just the construction itself."),
    ("How is my investment protected throughout the project?",
     "Financial transparency is a core part of how we operate. Every dollar is tied directly to a project milestone so you always know what you are paying for and why. We provide detailed documentation for every phase of your build, we never ask for funds beyond what the current scope requires, and our pre-construction budget matching process ensures your investment is fully accounted for before work ever begins. You will never be caught off guard financially on a Distinct Designs project."),
    ("Do you offer post-construction support after the project is complete?",
     "Yes and this is one of the things that truly separates us from virtually every other builder in the region. Our post-construction concierge service ensures that when we hand over the keys the only thing left behind is the home itself. This includes a full deep clean and site preparation, complete punch list management and coordination, subcontractor follow-up for warranties and certificates of occupancy, utility activation and smart home system setup, appliance registration, and a complete documentation package including warranties, manuals, as-built drawings, and maintenance schedules. Your home is not finished until everything works exactly as it should and you are completely taken care of."),
    ("What areas do you serve?",
     "We proudly serve the entire high desert and Coachella Valley region including Joshua Tree, Yucca Valley, Twentynine Palms, Palm Springs, Pioneer Town, Landers, Morongo Valley, Desert Hot Springs, Palm Desert, Rancho Mirage, Indian Wells, Indio, La Quinta and Cathedral City. For the right project we are also available for builds throughout greater Southern California."),
]

BUILD_FAQ = [
    ("How long does a custom home build take?",
     "Typically 10 to 18 months, depending on design, permitting, and finish selections. Our pre-construction process and dedicated crew are built to protect that timeline, not just estimate it."),
    ("Can you manage my project if I live out of state?",
     "Yes, regularly. Your client portal gives you real-time photo updates, you get bi-weekly field reports, and we schedule video calls throughout the build. Many of our most successful projects have been built for out-of-state clients who never once felt out of the loop."),
    ("Do you handle permits and inspections?",
     "Yes, the entire process, from plan approvals through certificates of occupancy. You never chase paperwork or navigate city offices yourself."),
    ("Are you licensed, bonded, and insured?",
     "Yes. Distinct Designs Construction is fully licensed, bonded, and insured. License #1145786."),
    ("How is my investment protected?",
     "Every dollar is tied to a project milestone, with detailed documentation at every phase. We never request funds beyond what the current scope requires, and our design-to-budget matching process means your total investment is accounted for before work ever begins."),
]

REMODEL_FAQ = [
    ("How long does a full home remodel take?",
     "Typically 2 to 6 months, depending on scope and finish selections. Our pre-construction process is built to protect that timeline, not just estimate it."),
    ("Can you manage my remodel if I live out of state?",
     "Yes, regularly. Real-time photo updates, bi-weekly field reports, and scheduled video calls keep you fully informed without needing to be on site."),
    ("Do you handle permits and inspections?",
     "Yes, the entire process, from plan approvals through certificates of occupancy."),
    ("Are you licensed, bonded, and insured?",
     "Yes. License #1145786, fully licensed, bonded, and insured."),
    ("How is my investment protected during the remodel?",
     "Every dollar is tied to a project milestone with full documentation. We never request funds beyond what the current scope requires."),
]

ADU_FAQ = [
    ("How long does an ADU build typically take?",
     "Timelines vary by size and scope, but our pre-construction process is designed to protect your timeline from the delays that derail most ADU projects."),
    ("Can you manage my ADU project if I live out of state?",
     "Yes. Real-time photo updates, bi-weekly reports, and scheduled video calls keep you informed throughout."),
    ("Do you handle permits for ADUs?",
     "Yes, the full process, from plan approval through certificate of occupancy."),
    ("Are you licensed, bonded, and insured?",
     "Yes. License #1145786."),
    ("How is my investment protected?",
     "Every dollar is tied to a milestone, with full documentation and no requests beyond the current scope."),
]


def project_tiles(slug):
    p = prefix(slug)
    tiles = [
        ("projects/la-mirada", "images/project-la-mirada.webp", "La Mirada Remodel: open-plan kitchen and living area with marble island, brass pendants and oak floors", 900, 1200, "La Mirada Remodel", "Luxury renovation"),
        ("projects/hilltop", "images/project-hilltop.webp", "Hilltop Build: open-plan living and kitchen with stone feature wall, opening to the desert", 900, 675, "Hilltop Build", "Rescue and completion"),
        ("projects/cubero", "images/project-cubero.webp", "Cubero Build: desert modern home from above, with pool and Joshua tree landscape", 900, 675, "Cubero Build", "Ground-up custom home"),
        ("projects/alturas", "images/project-alturas.webp", "Alturas Build in progress: sheathed walls with a circular window opening, against the desert and mountains", 1400, 932, "Alturas Build", "Currently in progress"),
    ]
    html_bits = []
    for i, (target, img, alt, w, h, name, note) in enumerate(tiles):
        tall = " project-tile--tall" if i == 0 else ""
        html_bits.append(f"""<a class="project-tile project-tile--link{tall}" href="{href(slug, target)}">
  <img src="{p}{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
  <span class="project-tile__label">{name} <em>{note}</em></span>
</a>""")
    return '<div class="projects-grid reveal">' + "".join(html_bits) + "</div>"


def city_anchor(slug, name):
    """Link a published city name when that city has a page."""
    target = AREA_TARGET.get(name)
    if not target:
        return name
    here = ' aria-current="page"' if slug == target else ""
    return f'<a class="city-link" href="{href(slug, target)}"{here}>{name}</a>'


def areas_html(slug=""):
    def col(title, cities):
        items = "".join(f"<li>{city_anchor(slug, c)}</li>" for c in cities)
        return f"<div><h3>{title}</h3><ul class=\"areas-list\">{items}</ul></div>"
    return f'<div class="areas-grid reveal">{col("Primary", PRIMARY)}{col("Also served", SECONDARY)}</div>'


# Longest names first. "Joshua Tree Rustic" is a finish style, not the city.
_CITY_RE = re.compile(
    r"\b(Indian Wells|Palm Springs|Palm Desert|Yucca Valley|Joshua Tree|La Quinta)\b(?! Rustic)"
)
_SKIP_CITY_LINK = {
    "a", "h1", "h2", "h3", "h4", "h5", "h6",
    "script", "style", "title", "textarea", "button", "option",
}


class _CityLinker(HTMLParser):
    """Wrap published city names in body text. Skip headings, titles,
    meta attributes, scripts, and text that is already inside a link."""

    def __init__(self, slug):
        super().__init__(convert_charrefs=False)
        self.slug = slug
        self.stack = []
        self.out = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        self.out.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack:
                if self.stack.pop() == tag:
                    break
        self.out.append(f"</{tag}>")

    def handle_startendtag(self, tag, attrs):
        self.out.append(self.get_starttag_text())

    def handle_data(self, data):
        if any(tag in _SKIP_CITY_LINK for tag in self.stack):
            self.out.append(data)
        else:
            self.out.append(_CITY_RE.sub(self._repl, data))

    def handle_entityref(self, name):
        self.out.append(f"&{name};")

    def handle_charref(self, name):
        self.out.append(f"&#{name};")

    def handle_comment(self, data):
        self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.out.append(f"<!{decl}>")

    def _repl(self, match):
        return city_anchor(self.slug, match.group(1))

    def result(self):
        return "".join(self.out)


def link_cities(html, slug):
    parser = _CityLinker(slug)
    parser.feed(html)
    parser.close()
    return parser.result()


def form_embed(form_id, title):
    """Standard GoHighLevel inline embed. form_embed.js resizes the iframe.

    data-height is only the fallback if that script cannot resize. The contact
    form is the tall one (fields through Submit). Guide forms are name and email.
    """
    # Pixel fallbacks measured from the live widgets (desktop and 390px),
    # rounded up so Submit stays in view if form_embed.js cannot resize.
    if form_id == CONTACT_FORM:
        kind, fallback = "contact", "1280"
    elif form_id == REFERRAL_FORM:
        kind, fallback = "referral", "2400"
    else:
        kind, fallback = "guide", "512"
    # data-layout uses single quotes, matching GoHighLevel's snippet.
    layout = "{'id':'INLINE'}"
    return f"""<div class="form-embed form-embed--{kind}">
  <iframe src="https://api.leadconnectorhq.com/widget/form/{form_id}" title="{title}" id="inline-{form_id}" data-layout="{layout}" data-trigger-type="alwaysShow" data-trigger-value="" data-activation-type="alwaysActivated" data-activation-value="" data-deactivation-type="neverDeactivate" data-deactivation-value="" data-form-name="{title}" data-height="{fallback}" data-layout-iframe-id="inline-{form_id}" data-form-id="{form_id}" scrolling="no"></iframe>
</div>"""


def gallery(slug, images, caption_prefix):
    p = prefix(slug)
    bits = []
    for i, (fn, w, h) in enumerate(images, 1):
        alt = f"{caption_prefix}, photograph {i}"
        bits.append(f"""<button class="gallery-item" type="button" data-caption="{alt}">
  <img src="{p}images/site/{fn}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
</button>""")
    return '<div class="gallery-grid reveal">' + "".join(bits) + "</div>"


def write_page(slug, html):
    html = link_cities(html, slug)
    if slug:
        path = ROOT.joinpath(*[p for p in slug.split("/") if p], "index.html")
    else:
        path = ROOT / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(path.relative_to(ROOT))


def page_shell(slug, title, description, body, extra_ld=""):
    html = head(slug, title, description, extra_ld) + nav(slug) + '<main id="main">' + body + "</main>" + footer(slug)
    if "api.leadconnectorhq.com/widget/form/" in html:
        html = html.replace(
            "</body>",
            '<script src="https://link.msgsndr.com/js/form_embed.js"></script>\n</body>',
            1,
        )
    return html


def why_cards(items):
    bits = []
    for h, text in items:
        bits.append(f'<article class="why-us-card"><h3>{h}</h3><p>{text}</p></article>')
    return '<div class="why-us-grid reveal">' + "".join(bits) + "</div>"


WHY_BUILD = [
    ("One crew, start to finish.", "No rotating strangers on your job site. The same team that breaks ground is the team that hands you the keys."),
    ("One price, not a maze of line items.", "Your proposal is delivered as a single price to build, with clear allowances for the materials you select, never a confusing trade-by-trade breakdown."),
    ("Direct access to leadership.", "When you call, you hear back the same day, from Nick or your dedicated project manager, never a receptionist or voicemail box."),
    ("Third-generation craftsmanship, 18 years in the desert.", "Built on standards passed down and refined over three generations, backed by nearly two decades of licensed work across the High Desert and Coachella Valley."),
]
WHY_REMODEL = [
    ("One crew, start to finish.", "No rotating strangers walking through your home. The same team that starts the job finishes it."),
    ("One price, not a maze of line items.", "Your proposal is a single price to build, with clear allowances for the finishes you choose, never a confusing trade-by-trade breakdown."),
    ("Direct access to leadership.", "Reach out and hear back the same day, from Nick or your dedicated project manager, never a call center."),
    ("Third-generation craftsmanship, 18 years in the desert.", "Standards passed down over three generations, backed by nearly two decades of licensed work across the region."),
]
WHY_ADU = [
    ("One crew, start to finish.", "The same team from groundbreaking to final walkthrough. No rotating subcontractors."),
    ("One price, not a maze of line items.", "A single price to build, with clear allowances for your material selections."),
    ("Direct access to leadership.", "Same-day responses from Nick or your dedicated project manager."),
    ("Third-generation craftsmanship, 18 years in the desert.", "The same standards we apply to $5M homes, applied to your ADU."),
]


def steps(items):
    bits = []
    for i, (h, text) in enumerate(items, 1):
        bits.append(f"""<li class="process-steps__item">
  <span class="process-steps__index">0{i}</span>
  <div><h4>{h}</h4><p>{text}</p></div>
</li>""")
    return '<ol class="process-steps">' + "".join(bits) + "</ol>"


PROCESS = [
    ("Consultation", "We learn your vision, lifestyle, and budget in detail."),
    ("Design-to-budget matching", "Every choice is priced and aligned before you commit to anything."),
    ("Permitting and engineering coordination", "We manage architects, engineers, and the entire approval process."),
    ("Build", "The same dedicated crew, start to finish. No rotating subcontractors."),
    ("Daily transparency", "Real-time photo updates through your client portal, plus bi-weekly field reports."),
]
PROCESS_REMODEL = [
    ("Consultation", "We walk the space and understand your vision, lifestyle, and budget."),
    ("Design-to-budget matching", "Every selection is priced and aligned before you commit."),
    ("Permitting and coordination", "We manage architects, designers, and approvals for you."),
    ("Build", "The same dedicated crew from demo to final walkthrough. No rotating subs."),
    ("Daily transparency", "Real-time photo updates through your client portal, plus bi-weekly field reports."),
]
PROCESS_ADU = [
    ("Consultation", "We assess your lot, vision, and budget."),
    ("Design-to-budget matching", "Every selection priced and aligned upfront."),
    ("Permitting and coordination", "We manage the full approval and utility process."),
    ("Build", "One dedicated crew, start to finish."),
    ("Daily transparency", "Real-time photo updates and bi-weekly field reports."),
]


def related(slug, links):
    bits = []
    for label, target in links:
        bits.append(f'<a class="btn btn--nav" href="{href(slug, target)}">{label}</a>')
    return '<div class="link-row">' + "".join(bits) + "</div>"


def main():
    import pages
    pages.build_all()


if __name__ == "__main__":
    main()
