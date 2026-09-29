"""Page bodies for the Distinct Designs website. Imported by generate.py."""

import generate as g

H = g.hero
F = g.form_embed
Q = g.quotes_html
A = g.areas_html
P = g.project_tiles
W = g.write_page
S = g.page_shell
R = g.related
FAQ = g.faq_html
STEPS = g.steps
WHY = g.why_cards
GAL = g.gallery
HREF = g.href
LD = g.faq_ld
PHONE = g.PHONE_DISPLAY
TEL = g.PHONE_TEL
EMAIL = g.EMAIL
GUIDE = g.GUIDE_FORM
CONTACT = g.CONTACT_FORM


def build_all():
    home()
    about()
    services()
    service_build()
    service_remodel()
    service_adu()
    projects()
    project_pages()
    contact()
    privacy()
    optout()
    planning()
    thanks()
    remodels()
    partners()
    referral()
    guides()
    missing()


def home():
    slug = ""
    body = H(
        slug,
        "images/hero-remodel.webp",
        "Finished open-plan living room and kitchen with a stone feature wall, oak floors and sliding doors onto the desert",
        1920, 960,
        f'{g.prefix(slug)}images/hero-remodel-1200.webp 1200w, {g.prefix(slug)}images/hero-remodel.webp 1920w',
        "Joshua Tree, CA · High Desert &amp; Coachella Valley",
        "The High Desert's Luxury Custom Home Builder",
        "Distinct Designs Construction specializes exclusively in luxury custom homes and high-end renovations across the high desert and greater Southern California.",
        HREF(slug, "contact"),
        "Start Your Journey",
    )
    body += f"""
<section class="section">
  <p class="pull-line reveal">We don't build homes for everyone. We build signature homes for clients who refuse to settle.</p>
  <div class="service-grid" style="margin-top:2rem">
    <a class="service-card" href="{HREF(slug, "services/custom-home-build")}">
      <h3>Custom luxury home construction</h3>
      <p>Ground-up homes from $870K to $5M+, with one crew and a budget matched before groundbreaking.</p>
      <span class="service-card__more">View custom homes</span>
    </a>
    <a class="service-card" href="{HREF(slug, "services/whole-home-remodel")}">
      <h3>Whole-home renovations</h3>
      <p>Designer kitchens, spa bathrooms, and full transformations, priced as one number before demo day.</p>
      <span class="service-card__more">View remodels</span>
    </a>
    <a class="service-card" href="{HREF(slug, "services/custom-adu")}">
      <h3>Custom ADU construction</h3>
      <p>Guest suites built to the same standard as our luxury homes, with permitting handled.</p>
      <span class="service-card__more">View ADUs</span>
    </a>
  </div>
  <p class="page-intro" style="margin-top:1.5rem">Also: designer kitchens and bathrooms, and full-service architecture and engineering coordination. <a href="{HREF(slug, "services")}">See every service</a>.</p>
</section>
<section class="section section--tinted" id="guide">
  <div class="two-col">
    <div>
      <p class="eyebrow">Free guide</p>
      <h2>Get your free guide. Know before you hire.</h2>
      <p class="page-intro">Two homes can be the same size, yet one costs $900K and the other $2.5M. Most builders never explain why.</p>
      <p><a href="{HREF(slug, "planning-guide")}">Read the planning guide</a></p>
    </div>
    <div class="reveal">{F(GUIDE, "Get your free planning guide")}</div>
  </div>
</section>
<section class="section section--split">
  <div>
    <p class="eyebrow">Owner</p>
    <h2>Nicholas Aguilar</h2>
    <h3 class="section--split__subhead">The High Desert's luxury custom home builder</h3>
    <p>Your home is one of the most significant investments you will ever make. Not just financially, but in the life you are building around it.</p>
    <p>Distinct Designs Construction specializes exclusively in luxury custom homes and high-end renovations across the high desert and greater Southern California.</p>
    <p>We don't build homes for everyone. We build signature homes for clients who refuse to settle.</p>
    <p>High quality custom luxury home construction · Whole-home renovations · Designer kitchens and bathrooms · Custom ADU construction · Architecture and engineering coordination</p>
    <div class="link-row"><a class="btn btn--nav" href="{HREF(slug, "about")}">Meet the team</a></div>
  </div>
  <div class="section--split__media reveal">
    <img src="{g.prefix(slug)}images/site/Nick-DD.jpg" alt="Nicholas Aguilar, owner of Distinct Designs Construction" width="800" height="1000" loading="lazy">
  </div>
</section>
<section class="section" id="projects">
  <div class="section__header">
    <h2>Signature builds and remodels</h2>
    <p>Every project is handled by our in-house team, from first consultation to final walkthrough.</p>
  </div>
  {P(slug)}
  <div class="link-row"><a class="btn btn--nav" href="{HREF(slug, "projects")}">All projects</a></div>
</section>
<section class="section section--tinted" id="testimonials">
  <h2>What our clients say</h2>
  {Q(g.HOME_QUOTES)}
</section>
<section class="section" id="faq">
  <h2>Frequently asked questions</h2>
  {FAQ("home", g.HOME_FAQ)}
</section>
<section class="section section--tinted" id="areas-served">
  <h2>Areas we serve</h2>
  <p class="page-intro">Joshua Tree, CA, and the High Desert and Coachella Valley.</p>
  {A()}
</section>
<section class="lead-section" id="form">
  <div class="lead-section__media">
    <img src="{g.prefix(slug)}images/footer-cta.webp" alt="Finished great room with wood floors and desert-view windows" width="1600" height="1200" loading="lazy">
  </div>
  <div class="lead-section__content">
    <h2>Start your custom home journey now</h2>
    <p>Talk with Distinct Designs about a custom home, remodel, or ADU. Call <a href="tel:{TEL}">{PHONE}</a> or send a note below.</p>
    {F(CONTACT, "Start your custom home journey")}
  </div>
</section>
"""
    W(slug, S(slug,
              "Luxury Custom Home Builder in Joshua Tree, CA | Distinct Designs Construction",
              "Distinct Designs Construction builds luxury custom homes and high-end renovations in Joshua Tree, Yucca Valley, Palm Springs, and the Coachella Valley. Call (760) 221-4290.",
              body, LD(g.HOME_FAQ)))


def about():
    slug = "about"
    p = g.prefix(slug)
    body = f"""
<header class="hero hero--page">
  <img class="hero__image" src="{p}images/process-crew-home.webp" alt="The Distinct Designs crew inside a completed custom home, desert mountains beyond the open sliders" width="1200" height="900">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">About Distinct Designs</p>
    <h1>Your trusted Joshua Tree luxury custom home builder</h1>
  </div>
</header>
<section class="section">
  <h2>Dedication to my grandfather, Mario Trujillo</h2>
  <div class="portrait-row reveal" style="margin:1.5rem 0">
    <img src="{p}images/site/Mario-Trulillo-old-school-2.jpg" alt="Mario Trujillo, earlier in his career" width="900" height="1100" loading="lazy">
    <img src="{p}images/site/Mario-Trulillo.jpg" alt="Mario Trujillo" width="900" height="1100" loading="lazy">
  </div>
  <div class="prose">
    <p>Mario Trujillo, a decorated war veteran and Master Gunnery Sergeant of the United States Marine Corps, laid the foundation upon which Distinct Designs Construction was built. He upheld principles of hard work, diligence, adaptability, and treating every employee like family. These standards continue to guide our company today.</p>
    <p>Every one of us at Distinct Designs Construction has been shaped and influenced by Mr. Trujillo's leadership, whether through direct mentorship or through the guidance passed down from those he mentored. His values and craftsmanship became the blueprint that continues to branch throughout the company, instilling integrity, diligence, and a commitment to building quality from the ground up.</p>
    <p>Mr. Trujillo taught us the importance of working hard, taking pride in our craft, going the extra mile, and never settling for anything less than excellence. But more than that, he built a culture rooted in loyalty, mutual respect, and a shared commitment to high standards, where every project was approached with the same diligence to excellence.</p>
    <p>He didn't just take us on as employees, he mentored us as young adults and molded us into men. His dedication went beyond teaching skills; it was about building character and passing down values that would endure. His legacy of excellence continues to shape Distinct Designs Construction.</p>
    <p>Mr. Trujillo laid the concrete foundation and paved the road for Distinct Designs Construction to thrive. His mentorship, diligence, and relentless pursuit of excellence continue to be the backbone of our success. We are forever grateful for his guidance, vision, and commitment to nurturing both our skills and our character.</p>
    <p>Thank you, Mario Trujillo, for everything you have done. Your unwavering dedication and wisdom have built more than just a company, you have built a family. Distinct Designs Construction stands strong today because of the foundation you laid. We will honor you by carrying your legacy forward through the principles and values you instilled in all of us.</p>
  </div>
</section>
<section class="section section--split section--tinted">
  <div>
    <h2>We are one of the best luxury custom home builders serving Joshua Tree and the surrounding areas.</h2>
    <p>We specialize in custom new homes, custom cabinets, custom luxury kitchen and bathroom remodels, custom tile and stone, backsplashes, showers, mosaics, and floors, creating products in a variety of themes, including but not limited to: Spanish, Mediterranean, Industrial, Modern, Elegant, Clean, and Joshua Tree Rustic.</p>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/site/Team-Distinct-Designs-768x576.jpg" alt="Distinct Designs tile, stone, and general construction professionals" width="768" height="576" loading="lazy">
  </div>
</section>
<section class="section">
  <div class="card-grid">
    <article class="info-card"><h3>Our team</h3><p>With over 50 plus years of combined experience, our team can turn any client's dream into a reality.</p></article>
    <article class="info-card"><h3>Our mission</h3><p>Our mission is to provide a high-quality product that radiates elegance and creativity. We exceed in this because of the drive we share with our employees, the innovative nature of our senior designers, and the coordination of our managers. Providing secure jobs for the working class derives their ambition to invest hard work and time in a company that they can grow with and achieve greatness in their workmanship, providing a professional but family environment that cares for their employees and clients.</p></article>
    <article class="info-card"><h3>Our vision</h3><p>Our vision is to gain long-lasting relationships with our clients by exceeding their expectations and gaining their loyalty and trust. Ensuring that they become a part of the Distinct Designs family knowing they will be well taken care of.</p></article>
  </div>
</section>
<section class="section section--tinted" id="team">
  <div class="section__header"><h2>Our experts</h2><p>The team</p></div>
  <div class="team-grid">
    <article class="team-card"><img src="{p}images/site/Nick-DD.jpg" alt="Nicholas Aguilar, owner of Distinct Designs" width="600" height="700" loading="lazy"><h3>Nicholas</h3><p>Owner</p></article>
    <article class="team-card"><img src="{p}images/site/eric-pancho-2-2.jpg" alt="Eric, custom cabinet and door specialist" width="600" height="700" loading="lazy"><h3>Eric</h3><p>Cabinet and door specialist</p></article>
    <article class="team-card"><img src="{p}images/site/jerry-spider-1.jpg" alt="Jerry, in-house demo and plumbing specialist" width="600" height="700" loading="lazy"><h3>Jerry</h3><p>In-house demo and plumbing specialist</p></article>
    <article class="team-card"><img src="{p}images/site/pops32.jpg" alt="Joel, tile and stone designer and installer" width="600" height="700" loading="lazy"><h3>Joel</h3><p>Tile and stone designer and installer</p></article>
    <article class="team-card"><img src="{p}images/site/randy-hoher-drywall-and-paint-specialist-02.jpg" alt="Randy, drywall and paint specialist" width="600" height="700" loading="lazy"><h3>Randy</h3><p>Drywall and paint specialist</p></article>
    <article class="team-card"><img src="{p}images/site/fredo.jpg" alt="Fredo, general lead tile and stone installer" width="600" height="700" loading="lazy"><h3>Fredo</h3><p>General lead tile and stone installer</p></article>
    <article class="team-card"><img src="{p}images/site/Travis-Vanzee.jpg" alt="Travis Vanzee, electrician" width="600" height="700" loading="lazy"><h3>Travis</h3><p>Electrician specialist</p></article>
  </div>
</section>
<section class="section">
  <h2>We follow best practices</h2>
  <p class="page-intro">We provide excellent service and quality workmanship for all projects, ensuring that every stage of your custom home build or remodeling construction project is done with detail.</p>
  <div class="stat-row" style="margin-top:1.5rem">
    <article class="stat-card"><span>Custom designs</span></article>
    <article class="stat-card"><span>Top quality</span></article>
    <article class="stat-card"><span>Projects done on time</span></article>
  </div>
  {R(slug, [("Our services", "services"), ("Our projects", "projects"), ("Contact", "contact")])}
</section>
"""
    # TODO: source about page repeated Randy and Fredo. Listed once each.
    # TODO: pops32.jpg alt text on the source site said "General Lead Tile and Stone Installer"; the heading beside it is Joel.
    W(slug, S(slug,
              "About Distinct Designs Construction | Joshua Tree Custom Home Builder",
              "Meet Nicholas Aguilar and the Distinct Designs team, a Joshua Tree luxury custom home builder shaped by Mario Trujillo's standards. Serving the High Desert and Coachella Valley.",
              body))


def services():
    slug = "services"
    p = g.prefix(slug)
    body = f"""
<header class="hero hero--page">
  <img class="hero__image" src="{p}images/site/Custom-Desert-Home.webp" alt="Photograph of the Cubero custom home by Distinct Designs Construction" width="1536" height="1024">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">Distinct Designs · High Desert &amp; Coachella Valley</p>
    <h1>New custom luxury home build and residential remodeling experts</h1>
  </div>
</header>
<section class="section">
  <h2>Luxury custom homes and high-end remodels, built without compromise</h2>
  <p class="page-intro">We are a fully integrated design-build firm specializing in luxury custom home construction and high-end remodeling across the High Desert and Coachella Valley. One team. One standard. Every detail, every finish, every system, designed around your vision and built to last in the desert.</p>
  <p class="page-intro">Joshua Tree · Yucca Valley · Twentynine Palms · Pioneer Town · Landers · Morongo Valley · Desert Hot Springs · Palm Springs · Palm Desert · Cathedral City · Indian Wells · Rancho Mirage · Greater Southern California</p>
  <div class="service-grid" style="margin-top:2rem">
    <a class="service-card" href="{HREF(slug, "services/custom-home-build")}"><h3>Custom home build</h3><p>Ground-up luxury homes in Joshua Tree, Palm Springs, and the High Desert.</p><span class="service-card__more">Service page</span></a>
    <a class="service-card" href="{HREF(slug, "services/whole-home-remodel")}"><h3>Whole-home remodel</h3><p>Kitchens, bathrooms, and full-home transformations.</p><span class="service-card__more">Service page</span></a>
    <a class="service-card" href="{HREF(slug, "services/custom-adu")}"><h3>Custom ADU and guest suite</h3><p>Built to the same standard as our $870K+ homes.</p><span class="service-card__more">Service page</span></a>
  </div>
</section>
<section class="section section--tinted">
  <blockquote class="prose"><p>"Most builders hand you a contract and disappear. We stay at your side from the first sketch to the moment you walk through the finished door, and we're proud of every inch of what's behind it."</p></blockquote>
  <h2>What makes us different</h2>
  <p class="page-intro">We're not a general contractor who dabbles in high-end work. Distinct Designs was built from the ground up for luxury clients, people who know what they want and expect a builder who can actually deliver it.</p>
  <div class="card-grid" style="margin-top:1.5rem">
    <article class="info-card"><h3>Fully integrated design-build</h3><p>Architecture, engineering, permitting, and construction under one roof. One team, one contract, one point of accountability.</p></article>
    <article class="info-card"><h3>Engineered for desert living</h3><p>Materials, systems, and structural methods built for extreme heat, UV, and wind, not repurposed coastal California specs.</p></article>
    <article class="info-card"><h3>Transparent pricing, no surprises</h3><p>Detailed scopes, honest timelines, and real conversations about budget before work begins.</p></article>
    <article class="info-card"><h3>Obsessed with the details</h3><p>The tile work, the cabinetry, the transitions: this is where most builders cut corners. It's where we set our standard.</p></article>
  </div>
</section>
<section class="section" id="new-construction">
  <p class="eyebrow">New construction</p>
  <h2>Luxury custom home building in the High Desert and Coachella Valley</h2>
  <div class="prose">
    <p>From raw desert land to a fully finished, move-in-ready custom home, we manage every phase of design and construction so the result reflects exactly how you want to live. No developer floor plans. No compromises on materials. No gaps between the team who designed it and the team who builds it.</p>
    <p>We build luxury custom homes in Palm Springs, Joshua Tree, Rancho Mirage, Indian Wells, Yucca Valley, Twentynine Palms, and throughout the greater High Desert.</p>
    <p><a href="{HREF(slug, "services/custom-home-build")}">Read the custom home builder page</a></p>
  </div>
  <div class="card-grid" style="margin-top:1.5rem">
    <article class="info-card"><h3>Design and pre-construction</h3><ul class="check-list"><li>Site evaluation and lot consultation</li><li>Custom architecture and design</li><li>Structural engineering</li><li>Permitting and submittal administration</li></ul></article>
    <article class="info-card"><h3>Construction and systems</h3><ul class="check-list"><li>Grading, underground and foundation</li><li>Structural framing</li><li>Full MEP: plumbing, electrical, HVAC</li><li>Panel upgrades and rewires</li></ul></article>
    <article class="info-card"><h3>Interior and finishes</h3><ul class="check-list"><li>Luxury flooring: tile, stone, polished concrete</li><li>Custom cabinetry and built-ins</li><li>Designer kitchens and bathrooms</li><li>Drywall, insulation and painting</li></ul></article>
    <article class="info-card"><h3>Outdoor and exterior</h3><ul class="check-list"><li>Indoor-outdoor living design</li><li>Masonry, concrete and hardscape</li><li>Landscaping and shade structures</li><li>Stone facades and exterior finishes</li></ul></article>
  </div>
</section>
<section class="section section--tinted">
  <p class="eyebrow">Signature inclusions, every new build</p>
  <h2>The finishes and technology that define a Distinct Designs home</h2>
  <p class="page-intro">These aren't optional upgrades or line items you negotiate for. Artisan-level finishes and fully integrated technology are how we build, because anything less wouldn't carry our name.</p>
  <div class="two-col" style="margin-top:1.5rem">
    <article class="info-card"><h3>Custom surfaces and artisan stonework</h3><ul class="check-list"><li>Large-format tile, precision-set</li><li>Natural stone surfaces, counters and facades</li><li>Designer backsplashes and accent walls</li><li>Custom cabinetry and built-in millwork</li><li>Statement shower systems and soaking rooms</li><li>Stone patios and hardscape</li></ul></article>
    <article class="info-card"><h3>Integrated technology and private cinema</h3><ul class="check-list"><li>Dedicated home theater design and build</li><li>Whole-home AV and immersive audio</li><li>Smart lighting, climate and automation</li><li>Structured wiring and network infrastructure</li><li>Hidden AV integration</li><li>Motorized shading, security and access</li></ul></article>
  </div>
</section>
<section class="section" id="remodeling">
  <p class="eyebrow">Remodeling</p>
  <h2>High-end whole-home remodels and luxury renovations</h2>
  <p class="page-intro">You already have the property. Now make it the home you always intended. Whether it's a complete structural transformation or a targeted renovation of the spaces that matter most, we bring the same design precision and craftsmanship to remodeling that we bring to a ground-up build.</p>
  <p><a href="{HREF(slug, "services/whole-home-remodel")}">Read the whole-home remodel page</a></p>
  <div class="card-grid" style="margin-top:1.5rem">
    <article class="info-card"><h3>Whole-home renovation</h3><ul class="check-list"><li>Full gut renovations and structural changes</li><li>Floor plan reconfiguration</li><li>Sunken living spaces and custom millwork</li><li>Indoor-outdoor living transformations</li></ul></article>
    <article class="info-card"><h3>Kitchens and bathrooms</h3><ul class="check-list"><li>Luxury kitchen redesigns and custom layouts</li><li>Spa-style bathrooms and steam rooms</li><li>Designer shower systems and soaking tubs</li><li>Custom vanities and bespoke storage</li></ul></article>
    <article class="info-card"><h3>Systems and infrastructure</h3><ul class="check-list"><li>Full rewires and panel upgrades</li><li>Plumbing relocation and upgrades</li><li>Insulation and energy performance</li><li>Drywall, texture and painting</li></ul></article>
    <article class="info-card"><h3>Finishes and detail</h3><ul class="check-list"><li>Luxury tile, stone and hardwood flooring</li><li>Custom cabinetry and built-in storage</li><li>Backsplashes, accent walls and feature tile</li><li>Stone patios, hardscape and facades</li></ul></article>
  </div>
</section>
<section class="section section--tinted">
  <p class="eyebrow">Signature inclusions, every remodel</p>
  <h2>Remodeling is your opportunity to build it right this time</h2>
  <div class="two-col" style="margin-top:1.5rem">
    <article class="info-card"><h3>Artisan surfaces and premium stonework</h3><ul class="check-list"><li>Luxury tile and natural stone installation</li><li>Custom cabinetry and built-in millwork</li><li>Stone facades, feature walls and hardscape</li><li>Polished concrete and premium flooring</li></ul></article>
    <article class="info-card"><h3>Technology integration and home cinema</h3><ul class="check-list"><li>Dedicated screening room design and build</li><li>Whole-home AV and smart home retrofit</li><li>Structured wiring built into the renovation</li></ul></article>
  </div>
</section>
<section class="section">
  <h2>Built for the desert, not just in it.</h2>
  <div class="prose">
    <p>Building luxury homes in the Coachella Valley and High Desert requires more than standard California construction knowledge. Temperature extremes, intense UV, seismic considerations, and wind load all demand materials and methods that most builders never think about. We've spent years developing a construction methodology specific to this region, specifying products that perform at 115°F, designing thermal envelopes that reduce energy loads without sacrificing design, and building structures that hold up over decades of desert conditions. The result isn't just a beautiful home. It's a home that works as hard as it looks.</p>
  </div>
</section>
<section class="section section--tinted" id="adu">
  <h2>Custom ADU and guest suite construction</h2>
  <p class="page-intro">Custom ADU construction is part of what Distinct Designs builds across the High Desert, to the same standard as our luxury homes. Architecture and engineering coordination is included on design-build projects.</p>
  {R(slug, [("Custom ADU page", "services/custom-adu"), ("Custom homes", "services/custom-home-build"), ("Whole-home remodels", "services/whole-home-remodel"), ("Contact", "contact")])}
</section>
<section class="lead-section">
  <div class="lead-section__media"><img src="{p}images/process-break-terrace.webp" alt="Desert terrace at dusk with a fire bowl, string lights and a spa" width="1920" height="1081" loading="lazy"></div>
  <div class="lead-section__content">
    <h2>Begin your project.</h2>
    <p>Every Distinct Designs project starts with a private consultation: a direct conversation about your vision, your site, and what it actually takes to build it right. No sales pitch. No pressure. We take on a limited number of projects each year to ensure every client receives our full attention.</p>
    <a class="btn btn--primary" href="{HREF(slug, "contact")}">Start your journey today</a>
  </div>
</section>
"""
    W(slug, S(slug,
              "Custom Home Building & Remodeling Services | Distinct Designs Construction",
              "Luxury custom homes, whole-home remodels, designer kitchens and bathrooms, and custom ADUs across Joshua Tree, Palm Springs, and the Coachella Valley.",
              body))


def service_build():
    slug = "services/custom-home-build"
    p = g.prefix(slug)
    body = H(
        slug, "images/site/Custom-Desert-Home.webp",
        "Photograph of the Cubero custom home by Distinct Designs Construction",
        1536, 1024, "",
        "Licensed CA General Contractor #1145786 · High Desert &amp; Coachella Valley",
        "Custom home builder in Joshua Tree and the Coachella Valley",
        "Ground-up custom homes from $870K to $5M+. One dedicated crew from groundbreaking to move-in, a budget you can trust before you sign, and daily progress you can see, even if you live out of state.",
        HREF(slug, "contact"), "Schedule a Consultation", page=True,
    )
    body += f"""
<section class="section">
  <h2>Two homes, same size, very different price tags</h2>
  <div class="prose">
    <p>Two custom homes can be nearly identical in square footage, and a million dollars apart in cost. Most builders never explain why until you're already committed.</p>
    <p>The difference isn't luck. It's decisions made months before the first shovel breaks ground, decisions most buyers never get to see until it's too late to change course.</p>
    <p>That's exactly what our <a href="{HREF(slug, "planning-guide")}">free planning guide</a> walks you through, before you ever sign with a builder.</p>
  </div>
</section>
<section class="section section--split section--tinted" id="process">
  <div>
    <h2>Your budget, locked in before we break ground</h2>
    <p>Every material selection, design detail, and architectural decision is priced and matched to your budget upfront, before construction begins. No mid-build surprises. No forced compromises. No uncomfortable conversations about costs that should have been addressed on day one.</p>
    <h3 class="section--split__subhead">How it works</h3>
    {STEPS(g.PROCESS)}
    <p class="pull-line">You'll always know where your project stands, what it costs, and why, even if you're managing it from out of state.</p>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/process-crew-home.webp" alt="The Distinct Designs crew inside a completed custom home, desert mountains beyond the open sliders" width="1200" height="900" loading="lazy">
  </div>
</section>
<figure class="image-break"><img src="{p}images/process-break-terrace.webp" alt="Desert terrace at dusk with a fire bowl, string lights and a spa, valley lights beyond" width="1920" height="1081" loading="lazy"></figure>
<section class="section" id="projects">
  <div class="section__header">
    <h2>Signature homes we've built</h2>
    <p>Homes and remodels in the High Desert, including Joshua Tree, Yucca Valley, and the Coachella Valley. <a href="{HREF(slug, "services")}#new-construction">See the full new-build scope</a>.</p>
  </div>
  {P(slug)}
</section>
<section class="section section--tinted" id="why-us">
  <h2>Why serious buyers choose Distinct Designs</h2>
  {WHY(g.WHY_BUILD)}
</section>
<section class="section" id="testimonials">
  <h2>What our clients say</h2>
  {Q(g.HOME_QUOTES)}
</section>
<section class="section section--tinted" id="faq">
  <h2>Custom home questions</h2>
  {FAQ("build", g.BUILD_FAQ)}
</section>
<section class="section" id="areas-served">
  <h2>Where we build custom homes</h2>
  <p class="page-intro">Joshua Tree, Yucca Valley, Palm Springs, Palm Desert, and the rest of the High Desert and Coachella Valley.</p>
  {A()}
  {R(slug, [("Whole-home remodels", "services/whole-home-remodel"), ("Custom ADUs", "services/custom-adu"), ("All services", "services"), ("Contact", "contact")])}
</section>
<section class="lead-section" id="form">
  <div class="lead-section__media"><img src="{p}images/footer-cta-home.webp" alt="Finished great room used as the custom-home consultation backdrop" width="1600" height="1066" loading="lazy"></div>
  <div class="lead-section__content">
    <h2>Start your custom home journey</h2>
    <p>Building at this level is about trust, not the lowest bid. Talk to Nick directly about your project. No call center, no sales script. Call <a href="tel:{TEL}">{PHONE}</a>.</p>
    {F(GUIDE, "Request the custom home planning guide")}
  </div>
</section>
"""
    W(slug, S(slug,
              "Custom Home Builder in Joshua Tree & the High Desert | Distinct Designs",
              "Ground-up custom homes from $870K to $5M+ in Joshua Tree, Yucca Valley, Palm Springs, and the Coachella Valley. One crew, a budget matched before you sign.",
              body, LD(g.BUILD_FAQ)))


def service_remodel():
    slug = "services/whole-home-remodel"
    p = g.prefix(slug)
    body = H(
        slug, "images/hero-remodel.webp",
        "Finished open-plan living room and kitchen with a stone feature wall, oak floors and sliding doors onto the desert",
        1920, 960,
        f"{p}images/hero-remodel-1200.webp 1200w, {p}images/hero-remodel.webp 1920w",
        "Licensed CA General Contractor #1145786 · High-End Renovations, High Desert &amp; Coachella Valley",
        "Luxury whole-home remodels in the High Desert and Coachella Valley",
        "Designer kitchens, spa-level bathrooms, and full-home transformations, built by one dedicated crew, priced as one number, with daily photo updates you can see from anywhere.",
        HREF(slug, "contact"), "Schedule a Consultation", page=True,
    )
    body += f"""
<section class="section">
  <h2>Most remodel budgets don't break. They get broken.</h2>
  <div class="prose">
    <p>Luxury remodels rarely blow up because of one big mistake. They blow up from dozens of small decisions nobody priced before demo started: a selection here, a structural surprise there, until the number you signed up for doesn't mean much anymore.</p>
    <p>That's the part most contractors never walk you through before you commit.</p>
    <p>Our <a href="{HREF(slug, "planning-guide")}">free planning guide</a> shows you exactly what separates a remodel that stays on budget from one that doesn't, before you sign with anyone.</p>
  </div>
</section>
<section class="section section--split section--tinted" id="process">
  <div>
    <h2>Your number is locked in before demo day</h2>
    <p>Before a single wall comes down, we run a full design-to-budget matching process: every material, every design detail, every structural unknown we can reasonably anticipate, priced and aligned with your budget in advance.</p>
    <h3 class="section--split__subhead">How it works</h3>
    {STEPS(g.PROCESS_REMODEL)}
    <p class="pull-line">You always know what's happening, what it costs, and why, even managing it from out of state.</p>
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/process-crew-remodel.webp" alt="The Distinct Designs crew standing in front of a completed custom desert home under a clear blue sky" width="1200" height="1600" loading="lazy">
  </div>
</section>
<figure class="image-break"><img src="{p}images/process-break-bath.webp" alt="Spa-level bathroom remodel with a freestanding soaking tub, subway tile, penny-round floor and desert views" width="1920" height="960" loading="lazy"></figure>
<section class="section" id="kitchens">
  <h2>Designer kitchens and spa bathrooms in Yucca Valley, Joshua Tree, and Palm Springs</h2>
  <p class="page-intro">Whole-home work and the rooms people feel every day. The same crew prices kitchens, baths, and the rest of the house as one project.</p>
  <div class="two-col" style="margin-top:1.5rem">
    <article class="info-card"><h3>Kitchens</h3><ul class="check-list"><li>Luxury kitchen redesigns and custom layouts</li><li>Custom cabinetry and built-in storage</li><li>Designer backsplashes and feature tile</li></ul></article>
    <article class="info-card"><h3>Bathrooms</h3><ul class="check-list"><li>Spa-style bathrooms and steam rooms</li><li>Designer shower systems and soaking tubs</li><li>Custom vanities and bespoke storage</li></ul></article>
  </div>
  <p style="margin-top:1.25rem"><a href="{HREF(slug, "services")}#remodeling">See the full remodel scope</a> or the <a href="{HREF(slug, "remodels")}">remodels overview</a>.</p>
</section>
<section class="section section--tinted" id="projects">
  <div class="section__header"><h2>Signature remodels we've delivered</h2></div>
  {P(slug)}
</section>
<section class="section" id="why-us">
  <h2>Why serious homeowners choose Distinct Designs</h2>
  {WHY(g.WHY_REMODEL)}
</section>
<section class="section section--tinted" id="testimonials">
  <h2>What our clients say</h2>
  {Q(g.HOME_QUOTES)}
</section>
<section class="section" id="faq">
  <h2>Remodel questions</h2>
  {FAQ("remodel", g.REMODEL_FAQ)}
</section>
<section class="section section--tinted" id="areas-served">
  <h2>Remodeling across the High Desert and Coachella Valley</h2>
  {A()}
  {R(slug, [("Custom homes", "services/custom-home-build"), ("Custom ADUs", "services/custom-adu"), ("All services", "services"), ("Contact", "contact")])}
</section>
<section class="lead-section" id="form">
  <div class="lead-section__media"><img src="{p}images/footer-cta-remodel.webp" alt="Finished open-plan living room and kitchen remodel with wood floors, a bright island and desert-view windows" width="1600" height="1200" loading="lazy"></div>
  <div class="lead-section__content">
    <h2>Start your remodel the right way</h2>
    <p>A remodel at this level is about trust, not the lowest bid. Talk to Nick directly about your project. Call <a href="tel:{TEL}">{PHONE}</a>.</p>
    {F(GUIDE, "Request the remodel planning guide")}
  </div>
</section>
"""
    W(slug, S(slug,
              "Whole-Home Remodeling in Yucca Valley & Palm Springs | Distinct Designs",
              "Designer kitchens, spa bathrooms, and whole-home remodels in Yucca Valley, Joshua Tree, Palm Springs, and the Coachella Valley. One crew and one price before demo day.",
              body, LD(g.REMODEL_FAQ)))


def service_adu():
    slug = "services/custom-adu"
    p = g.prefix(slug)
    body = H(
        slug, "images/hero-garage.webp",
        "Finished custom garage with polished concrete floors and two Porsche 911 sports cars, desert landscape through the window",
        1672, 1115,
        f"{p}images/hero-garage-1200.webp 1200w, {p}images/hero-garage.webp 1672w",
        "Licensed CA General Contractor #1145786 · Custom ADUs &amp; Guest Suites",
        "Custom ADU and guest suite builder in the High Desert",
        "Add real, lasting value to your property with a fully custom ADU or guest suite, designed and built to the same standard as our $870K+ luxury homes, with one crew and one clear price.",
        HREF(slug, "contact"), "Schedule a Consultation", page=True,
    )
    body += f"""
<section class="section">
  <h2>A well-built ADU adds value. A poorly planned one adds problems.</h2>
  <div class="prose">
    <p>An ADU sounds simple until permitting, utility hookups, and design decisions start piling up, and a project that should add value to your property turns into a budget and paperwork headache instead.</p>
    <p>The difference between an ADU that pays for itself and one that becomes a regret comes down to planning most builders skip.</p>
    <p>Our <a href="{HREF(slug, "planning-guide")}">free planning guide</a> shows you what to get right before you break ground on a Joshua Tree, Yucca Valley, or Palm Springs lot.</p>
  </div>
</section>
<section class="section section--split section--tinted" id="process">
  <div>
    <h2>Your ADU budget, matched before we start</h2>
    <p>Before construction begins, we match your design to your budget in full, materials, finishes, and utility work included, so there are no mid-build surprises on a smaller project that deserves the same discipline as a full custom home.</p>
    <h3 class="section--split__subhead">How it works</h3>
    {STEPS(g.PROCESS_ADU)}
  </div>
  <div class="section--split__media reveal">
    <img src="{p}images/process-crew-adu.webp" alt="The Distinct Designs crew together inside a finished build, Joshua trees and desert mountains through the open sliders" width="1200" height="1600" loading="lazy">
  </div>
</section>
<figure class="image-break"><img src="{p}images/process-break-patio.webp" alt="Desert backyard patio at sunset with a hot tub, string lights, lounge seating and a Joshua Tree, CA sign" width="1920" height="1440" loading="lazy"></figure>
<section class="section" id="projects">
  <div class="section__header">
    <h2>Recent custom builds</h2>
    <p>The same in-house team that builds custom homes in the Coachella Valley and High Desert builds the ADU.</p>
  </div>
  {P(slug)}
</section>
<section class="section section--tinted" id="why-us">
  <h2>Why homeowners trust us with their ADU</h2>
  {WHY(g.WHY_ADU)}
</section>
<section class="section">
  <h2>What our clients say</h2>
  {Q(g.HOME_QUOTES[:3])}
</section>
<section class="section section--tinted" id="faq">
  <h2>ADU questions</h2>
  {FAQ("adu", g.ADU_FAQ)}
</section>
<section class="section" id="areas-served">
  <h2>ADUs across Joshua Tree, Palm Springs, and the valley</h2>
  {A()}
  {R(slug, [("Custom homes", "services/custom-home-build"), ("Whole-home remodels", "services/whole-home-remodel"), ("All services", "services"), ("Contact", "contact")])}
</section>
<section class="lead-section" id="form">
  <div class="lead-section__media"><img src="{p}images/footer-cta.webp" alt="Finished interior used beside the ADU consultation form" width="1600" height="1200" loading="lazy"></div>
  <div class="lead-section__content">
    <h2>Add value to your property the right way</h2>
    <p>Talk to Nick directly about your ADU or guest suite. Call <a href="tel:{TEL}">{PHONE}</a>.</p>
    {F(GUIDE, "Request the ADU planning guide")}
  </div>
</section>
"""
    W(slug, S(slug,
              "Custom ADU & Guest Suite Builder in Joshua Tree | Distinct Designs",
              "Custom ADUs and guest suites in Joshua Tree, Yucca Valley, Palm Springs, and the Coachella Valley, built to the same standard as our $870K+ homes, with permits handled.",
              body, LD(g.ADU_FAQ)))


def projects():
    slug = "projects"
    p = g.prefix(slug)
    cats = [
        ("General construction", "images/site/outdoor-decks-2-1.jpg", "Outdoor deck and general construction work by Distinct Designs"),
        ("Home remodels", "images/site/Distinct-Designs-General-Remodel.jpg", "Home remodel by Distinct Designs Construction"),
        ("Kitchen remodels", "images/site/Distinct-Designs-contact-us-background.jpg", "Kitchen remodel by Distinct Designs Construction"),
        ("Tile and stone masonry", "images/site/img_20140707_090216.jpg", "Tile and stone masonry by Distinct Designs Construction"),
    ]
    cards = []
    for name, img, alt in cats:
        cards.append(f"""<article class="project-tile project-tile--link" id="{name.split()[0].lower()}">
  <img src="{p}{img}" alt="{alt}" loading="lazy">
  <span class="project-tile__label">{name}</span>
</article>""")
    body = f"""
<header class="hero hero--page">
  <img class="hero__image" src="{p}images/site/outdoor-decks-2-1.jpg" alt="Outdoor deck built by Distinct Designs Construction" width="1600" height="1000">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">Portfolio</p>
    <h1>Projects</h1>
    <p class="subhead">Signature builds and remodels across the High Desert.</p>
  </div>
</header>
<section class="section">
  <h2>Signature builds and remodels</h2>
  {P(slug)}
  <p style="margin-top:1.5rem"><a href="{HREF(slug, "projects/sun-mesa")}">Sun Mesa remodel</a></p>
</section>
<section class="section section--tinted" id="galleries">
  <h2>More of the work</h2>
  <p class="page-intro">These categories are published on the current projects page. The old links to standalone gallery pages do not resolve, so the photographs stay here.</p>
  <div class="projects-grid" style="margin-top:1.5rem">{"".join(cards)}</div>
</section>
"""
    W(slug, S(slug,
              "Projects | Distinct Designs Construction",
              "Signature builds and remodels by Distinct Designs Construction: La Mirada, Hilltop, Cubero, Alturas, and Sun Mesa, plus kitchens, remodels, and stone work.",
              body))


LA_MIRADA_IMGS = [
    ("img_8659.jpg", 1200, 900),
    ("img_8662.jpg", 1200, 900),
    ("20231227_131415.jpg", 1200, 900),
    ("20231227_131555.jpg", 1200, 900),
    ("20231227_131611.jpg", 1200, 900),
    ("20231227_131709.jpg", 1200, 900),
    ("img_8658.jpg", 1200, 900),
]
HILLTOP_IMGS = [
    ("hilltop-01-7.webp", 1440, 1080),
    ("hilltop-01-6.webp", 1440, 1080),
    ("hilltop-01-4.webp", 1440, 1080),
    ("hilltop-01-5.webp", 1440, 1080),
    ("hilltop-01-3.webp", 1440, 1080),
    ("hilltop-01-1-2.webp", 1440, 1080),
    ("hilltop-01-2.webp", 1440, 1080),
]
CUBERO_IMGS = [
    ("Custom-Desert-Home.webp", 1536, 1024),
    ("living-room.jpg", 1200, 800),
    ("kitchen.jpg", 1200, 800),
    ("DSC00366-HDR-scaled.jpg", 1600, 1066),
    ("cubero-bathroom.jpg", 1200, 800),
    ("Garage.jpg", 1200, 800),
]
ALTURAS_IMGS = [
    ("Alturas-build.jpg", 1400, 900),
    ("dsc01975.jpg", 1200, 800),
    ("dsc01973.webp", 800, 1200),
    ("dsc01970.jpg", 1200, 800),
    ("dsc01971.jpg", 1200, 800),
    ("dsc02051.jpg", 1200, 800),
    ("dsc02013.jpg", 1200, 800),
    ("dsc02002.jpg", 1200, 800),
]


def case_study(slug, title, meta, h2, kicker, headline, place, stat_label, stat, stage_label, stage, paragraphs, lesson, images, image_prefix, note=""):
    p = g.prefix(slug)
    paras = "".join(f"<p>{t}</p>" for t in paragraphs)
    body = f"""
<header class="hero hero--page">
  <img class="hero__image" src="{p}images/site/{images[0][0]}" alt="{image_prefix}, photograph 1" width="{images[0][1]}" height="{images[0][2]}">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">Recent work</p>
    <h1>Recent work</h1>
  </div>
</header>
{note}
<section class="section">
  <p class="eyebrow">{kicker}</p>
  <h2>{headline}</h2>
  <p class="page-intro">{place}</p>
  <div class="stat-row" style="margin-top:1.5rem">
    <article class="stat-card"><small>{stat_label}</small><span>{stat}</span></article>
    <article class="stat-card"><small>{stage_label}</small><span>{stage}</span></article>
  </div>
  <div class="prose" style="margin-top:2rem">{paras}<h3>The lesson</h3><blockquote><p>{lesson}</p></blockquote></div>
</section>
<section class="section section--tinted">
  <h2>{h2}</h2>
  {GAL(slug, images, image_prefix)}
  {R(slug, [("All projects", "projects"), ("Custom homes", "services/custom-home-build"), ("Remodels", "services/whole-home-remodel"), ("Contact", "contact")])}
</section>
"""
    W(slug, S(slug, title, meta, body))


def project_pages():
    case_study(
        "projects/la-mirada",
        "La Mirada Remodel | Distinct Designs Construction",
        "La Mirada luxury renovation by Distinct Designs Construction. A hidden cloth-wiring fire risk was replaced with a full rewire before the finishes went in.",
        "La Mirada remodel",
        "Luxury renovation | Electrical safety",
        "The previous owner's electrical system was a fire waiting to happen. We caught it before it did.",
        "La Mirada project · Southern California",
        "Risk eliminated", "Fire hazard",
        "System replaced", "Full rewire",
        [
            "These clients hired us for a high-end renovation. Before we touched a single finish, our preconstruction walkthrough revealed something that no amount of beautiful tile or custom cabinetry could fix: the home was running on cloth wiring, an aging electrical system that presents a hidden and serious fire risk.",
            "Unlike a modern breaker that trips when it is overloaded, cloth wiring deteriorates silently. The insulation degrades from the inside out through a process called thermal degradation, overheating repeatedly over years without triggering any warning. There is no alarm, no tripped breaker, no early sign until there is a fire.",
            "It is not a question of if. It is a question of when.",
            "We removed the system entirely and rewired the home to current code, protecting our clients' investment, their property, and most importantly, their family. The renovation they came to us for was delivered in full, with the peace of mind that comes from knowing the home beneath the finishes is as sound as everything visible in it.",
            "We also encountered challenges with the project's material delivery timeline. A designer who was consistently behind on deadlines was creating downstream delays across the entire build schedule. After a direct conversation with our clients, we restructured the material procurement process around confirmed pickup dates rather than waiting on delivery promises. The project moved forward on schedule from that point forward.",
        ],
        "A renovation that looks exceptional but hides a compromised system is not a finished home. It is a liability waiting to surface. We don't just build beautiful spaces. We make sure everything behind the walls earns the same standard as what's in front of them.",
        LA_MIRADA_IMGS, "La Mirada remodel",
    )
    case_study(
        "projects/hilltop",
        "Hilltop Build | Distinct Designs Construction",
        "Hilltop build in the High Desert. Distinct Designs replaced out-of-code electrical and underspanned structural framing after another contractor left with $70,000.",
        "Hilltop build",
        "Rescue and completion | Structural and electrical",
        "Their contractor vanished with $70,000. We came in, made it safe, and finished it right.",
        "Hilltop build · High Desert, CA",
        "Contractor fraud", "$70,000",
        "Hazards remediated", "Structural + fire",
        [
            "These clients called us after their contractor had all but disappeared, showing up one week a month for two months while collecting payments in full. By the time they reached us, they had already lost $70,000 and had no idea what, if anything, had been done correctly.",
            "Our on-site assessment revealed two serious and interconnected problems. The first was the electrical: a significant portion of it had been installed out of compliance with code standards and had to be fully removed and rerun. The second was more alarming: the load-bearing framing and structural beams had been installed incorrectly relative to the engineering specifications. They were underspanned for the load they were meant to carry, a condition that, left unaddressed, creates real risk of roof failure over time.",
            "We remediated both issues completely, brought every system into full compliance, and delivered the finished home our clients had originally envisioned, but now built to the standard that actually keeps a family safe. The decision to stop and call us, rather than continue with a contractor who had already proven he couldn't be trusted, saved them from a far more costly outcome down the road.",
            "This is one of the most common calls we receive: a client who hired on price, discovered too late that price was the only thing that was competitive, and is now paying twice to fix what should have been done right the first time. We never want to be your second call. But if you need one, we will not leave until it is right.",
        ],
        "A low bid doesn't protect your investment. It shifts the risk onto you. When a contractor disappears or cuts corners, the liability stays with the homeowner. The right builder is the one who isn't trying to win your project on price.",
        HILLTOP_IMGS, "Hilltop build",
    )
    case_study(
        "projects/cubero",
        "Cubero Build | Distinct Designs Construction",
        "Cubero ground-up custom home in the High Desert. Pre-construction site analysis avoided Joshua tree relocation, major regrading, and a $58,000 well.",
        "Cubero build",
        "Ground-up new build | Site analysis and planning",
        "They thought they needed a well. We found a better path and saved them $177,000.",
        "Cubero build · High Desert, CA",
        "Total savings", "$177,000+",
        "Stage", "Pre-construction",
        [
            "These clients had already purchased their land and were ready to build. They came to us with a site plan, a vision, and the assumption that the heavy decisions had already been made. Within the first phase of our preconstruction process, we identified three costly assumptions that would have derailed the project, before a single permit had been filed.",
            "The planned building location required the relocation of protected Joshua trees, a process that would have cost over $90,000 alone, and necessitated regrading more than half of the five-acre parcel to accommodate the natural water channels running through the property. That regrading cost: over $150,000.",
            "Neither had been factored into the budget. Neither had been caught by anyone prior to our involvement. By conducting a comprehensive site analysis, we identified an alternate building location that offered superior views, eliminated the need for any tree relocation, and worked with the natural topography of the land rather than against it. The project moved forward on schedule and within budget, because the right questions were asked before the expensive decisions were locked in.",
            "We also resolved a utility challenge the clients had resigned themselves to: they believed a $58,000 well was their only option for water access. After analyzing the property and surrounding easement rights, we determined a water line connection was achievable for half that cost. No well required.",
        ],
        "What you don't know before you build will cost you. Our preconstruction process exists for one reason: to ensure that every dollar you commit is being spent on the right decision, in the right location, for the right reasons.",
        CUBERO_IMGS, "Cubero build",
    )
    case_study(
        "projects/alturas",
        "Alturas Build | Distinct Designs Construction",
        "Alturas custom home in the High Desert, currently in progress. A pre-construction review caught a setback error and a septic conflict before demolition-level cost.",
        "Alturas build",
        "New construction | Design phase oversight",
        "We found a $200,000+ error before a single shovel hit the ground.",
        "Alturas build · High Desert, CA",
        "Losses prevented", "$200,000+",
        "Stage caught", "Pre-construction",
        [
            "Our clients came to us mid-process, frustrated by delays and a build that had stalled. What we uncovered when we stepped in went far beyond a scheduling problem. It was a mistake that would have eventually forced a demolition.",
            "The home had been positioned incorrectly on the architectural plans. The property lines had never been surveyed before the architect placed the structure, meaning the home as drawn was in direct violation of county setback requirements. Had this gone undetected, the building department would have eventually caught it, at whatever phase construction had reached, requiring a complete teardown and restart at devastating cost. We identified the error during our preconstruction review, corrected the placement, and kept the project moving forward without losing a dollar to avoidable demolition.",
            "We also discovered the septic tank had been positioned directly adjacent to the planned pool location. Drawing on our knowledge of how heavy equipment operates and what future site access demands, we relocated it to an optimal position, one that allowed pool construction to proceed unimpeded once the home was complete.",
            "This is precisely why involving a contractor during the design phase, before plans are finalized and submitted, is one of the highest-leverage decisions a client at this level can make. Our fee before groundbreaking is a fraction of what a single overlooked error in this phase can produce.",
        ],
        "The most expensive contractor mistake doesn't happen on the job site. It happens before anyone shows up. The right eyes in the design phase protect hundreds of thousands of dollars that most clients don't even know are at risk.",
        ALTURAS_IMGS, "Alturas build",
    )
    # Sun Mesa is published with Hilltop's case-study copy and La Mirada's photos.
    case_study(
        "projects/sun-mesa",
        "Sun Mesa Remodel | Distinct Designs Construction",
        "Sun Mesa remodel page as published by Distinct Designs Construction.",
        "Sun Mesa remodel",
        "Rescue and completion | Structural and electrical",
        "Their contractor vanished with $70,000. We came in, made it safe, and finished it right.",
        "Hilltop build · High Desert, CA",
        "Contractor fraud", "$70,000",
        "Hazards remediated", "Structural + fire",
        [
            "These clients called us after their contractor had all but disappeared, showing up one week a month for two months while collecting payments in full. By the time they reached us, they had already lost $70,000 and had no idea what, if anything, had been done correctly.",
            "Our on-site assessment revealed two serious and interconnected problems. The first was the electrical: a significant portion of it had been installed out of compliance with code standards and had to be fully removed and rerun. The second was more alarming: the load-bearing framing and structural beams had been installed incorrectly relative to the engineering specifications. They were underspanned for the load they were meant to carry, a condition that, left unaddressed, creates real risk of roof failure over time.",
            "We remediated both issues completely, brought every system into full compliance, and delivered the finished home our clients had originally envisioned, but now built to the standard that actually keeps a family safe. The decision to stop and call us, rather than continue with a contractor who had already proven he couldn't be trusted, saved them from a far more costly outcome down the road.",
            "This is one of the most common calls we receive: a client who hired on price, discovered too late that price was the only thing that was competitive, and is now paying twice to fix what should have been done right the first time. We never want to be your second call. But if you need one, we will not leave until it is right.",
        ],
        "A low bid doesn't protect your investment. It shifts the risk onto you. When a contractor disappears or cuts corners, the liability stays with the homeowner. The right builder is the one who isn't trying to win your project on price.",
        LA_MIRADA_IMGS, "Sun Mesa remodel",
        note="<!-- TODO: On distinctdesignsconstruction.com/sun-mesa/ the written case study matches the Hilltop page, including the label Hilltop build, and the gallery photos match La Mirada. Copied as published. Confirm the correct Sun Mesa story and photos before launch. -->",
    )


def contact():
    slug = "contact"
    p = g.prefix(slug)
    areas = ", ".join(g.AREAS)
    body = f"""
<header class="hero hero--page">
  <img class="hero__image" src="{p}images/process-break-patio.webp" alt="Desert backyard patio at sunset with a hot tub, string lights, lounge seating and a Joshua Tree, CA sign" width="1920" height="1440">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">Joshua Tree, CA</p>
    <h1>Contact our Joshua Tree construction professionals</h1>
  </div>
</header>
<section class="section" id="form">
  <h2>Distinct Designs contact details</h2>
  <div class="two-col" style="margin-top:1.5rem">
    <div>
      <h3>Phone</h3>
      <p><a href="tel:{TEL}">{PHONE}</a></p>
      <h3>Email</h3>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <h3>Location</h3>
      <p>Joshua Tree, CA</p>
      <h3>Service areas include</h3>
      <p>{areas}.</p>
      <p>Instagram: <a href="https://www.instagram.com/distinctdesignsconst/">@distinctdesignsconst</a><br>
      Facebook: <a href="https://www.facebook.com/profile.php?id=61561101665757">Distinct Designs</a><br>
      Yelp: <a href="https://www.yelp.com/biz/distinct-designs-yucca-valley-6">Distinct Designs, Yucca Valley</a></p>
    </div>
    <div>
      <h3>Start your custom home journey now</h3>
      {F(CONTACT, "Contact Distinct Designs Construction")}
    </div>
  </div>
</section>
"""
    W(slug, S(slug,
              "Contact Distinct Designs Construction | Joshua Tree, CA",
              "Call Distinct Designs Construction at (760) 221-4290 or email distinctdesigns360@gmail.com. Joshua Tree, CA. Serving the High Desert and Coachella Valley.",
              body))


def privacy():
    slug = "privacy-policy"
    body = f"""
<section class="section prose">
  <h1>Privacy policy</h1>
  <h2>Who we are</h2>
  <p>Our website address is: https://distinctdesignsconstruction.com.</p>
  <h2>Comments</h2>
  <p>When visitors leave comments on the site we collect the data shown in the comments form, and also the visitor's IP address and browser user agent string to help spam detection.</p>
  <p>An anonymized string created from your email address (also called a hash) may be provided to the Gravatar service to see if you are using it. The Gravatar service privacy policy is available here: https://automattic.com/privacy/. After approval of your comment, your profile picture is visible to the public in the context of your comment.</p>
  <h2>Media</h2>
  <p>If you upload images to the website, you should avoid uploading images with embedded location data (EXIF GPS) included. Visitors to the website can download and extract any location data from images on the website.</p>
  <h2>Cookies</h2>
  <p>Do we use cookies and other tracking technologies?</p>
  <p>In short: we may use cookies and other tracking technologies to collect and store your information.</p>
  <p>We may use cookies and similar tracking technologies (like web beacons and pixels) to gather information when you interact with our Services. Some online tracking technologies help us maintain the security of our Services, prevent crashes, fix bugs, save your preferences, and assist with basic site functions.</p>
  <p>We also permit third parties and service providers to use online tracking technologies on our Services for analytics and advertising, including to help manage and display advertisements, to tailor advertisements to your interests, or to send abandoned shopping cart reminders (depending on your communication preferences). The third parties and service providers use their technology to provide advertising about products and services tailored to your interests which may appear either on our Services or on other websites.</p>
  <p>To the extent these online tracking technologies are deemed to be a "sale"/"sharing" (which includes targeted advertising, as defined under the applicable laws) under applicable US state laws, you can opt out of these online tracking technologies by submitting a request as described below.</p>
  <p>Specific information about how we use such technologies and how you can refuse certain cookies is set out in our Cookie Notice.</p>
  <h3>Google Analytics</h3>
  <p>We may share your information with Google Analytics to track and analyze the use of the Services.</p>
  <p>To opt out of being tracked by Google Analytics across the Services, visit <a href="https://tools.google.com/dlpage/gaoptout">https://tools.google.com/dlpage/gaoptout</a>.</p>
  <p>For more information on the privacy practices of Google, please visit the <a href="https://policies.google.com/privacy">Google Privacy &amp; Terms page</a>.</p>
  <h2>Embedded content from other websites</h2>
  <p>Articles on this site may include embedded content (e.g. videos, images, articles, etc.). Embedded content from other websites behaves in the exact same way as if the visitor has visited the other website.</p>
  <p>These websites may collect data about you, use cookies, embed additional third-party tracking, and monitor your interaction with that embedded content, including tracking your interaction with the embedded content if you have an account and are logged in to that website.</p>
  <h2>Who we share your data with</h2>
  <p>If you request a password reset, your IP address will be included in the reset email.</p>
  <h2>How long we retain your data</h2>
  <p>If you leave a comment, the comment and its metadata are retained indefinitely. This is so we can recognize and approve any follow-up comments automatically instead of holding them in a moderation queue.</p>
  <p>For users that register on our website (if any), we also store the personal information they provide in their user profile. All users can see, edit, or delete their personal information at any time (except they cannot change their username). Website administrators can also see and edit that information.</p>
  <h2>What rights you have over your data</h2>
  <p>If you have an account on this site, or have left comments, you can request to receive an exported file of the personal data we hold about you, including any data you have provided to us. You can also request that we erase any personal data we hold about you. This does not include any data we are obliged to keep for administrative, legal, or security purposes.</p>
  <h2>Where your data is sent</h2>
  <p>Visitor comments may be checked through an automated spam detection service.</p>
  <p><a href="{HREF(slug, "opt-out-preferences")}">Opt-out preferences</a></p>
</section>
"""
    W(slug, S(slug,
              "Privacy Policy | Distinct Designs Construction",
              "Privacy policy for Distinct Designs Construction, including comments, media, cookies, Google Analytics, and the rights you have over your data.",
              body))


def optout():
    slug = "opt-out-preferences"
    body = f"""
<section class="section prose">
  <h1>Opt-out preferences</h1>
  <p>The current site's opt-out page is a cookie-statement placeholder. The rendered banner says:</p>
  <blockquote><p>We use cookies to enhance your browsing experience, serve personalised ads or content, and analyse our traffic. By clicking "Accept All", you consent to our use of cookies.</p></blockquote>
  <p>We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.</p>
  <!-- TODO: The live page only contains the shortcode [cmplz-document type="cookie-statement" region="us"]. Complianz did not render a full cookie statement in the page source. Paste the real Complianz cookie statement here before launch, and wire a consent banner. -->
  <p><strong>TODO:</strong> The full cookie statement from the current site did not render (it is a Complianz shortcode). Do not treat this page as a complete cookie policy until that statement is pasted in.</p>
  <p>Cookie categories named on the current banner: necessary, analytics, and advertisement.</p>
  <p>To opt out of Google Analytics, visit <a href="https://tools.google.com/dlpage/gaoptout">https://tools.google.com/dlpage/gaoptout</a>.</p>
  <p>Read the <a href="{HREF(slug, "privacy-policy")}">privacy policy</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</section>
"""
    W(slug, S(slug,
              "Opt-out Preferences | Distinct Designs Construction",
              "Cookie and tracking opt-out preferences for Distinct Designs Construction. The full Complianz cookie statement still needs to be pasted in before launch.",
              body))


def planning():
    slug = "planning-guide"
    body = f"""
<section class="section">
  <p class="eyebrow">Free guide</p>
  <h1>Planning guide</h1>
  <p class="page-intro">To download the guide, use the reader below.</p>
  <iframe class="embed-frame" src="https://heyzine.com/flip-book/4c5f65a1bc.html" title="Distinct Designs planning guide" allowfullscreen></iframe>
  <div class="link-row">
    <a class="btn btn--nav" href="{HREF(slug, "guides/custom-home-builder-1")}">Guide landing 1</a>
    <a class="btn btn--nav" href="{HREF(slug, "guides/custom-home-builder-2")}">Guide landing 2</a>
    <a class="btn btn--nav" href="{HREF(slug, "guides/custom-home-builder-3")}">Guide landing 3</a>
  </div>
</section>
"""
    W(slug, S(slug,
              "Planning Guide | Distinct Designs Construction",
              "Read the Distinct Designs planning guide: what it takes to build a custom home in the High Desert and Coachella Valley.",
              body))


def thanks():
    slug = "guide-thank-you"
    body = """
<section class="section">
  <h1>Guide thank you</h1>
  <div class="video-frame">
    <iframe src="https://player.vimeo.com/video/1188183562?playsinline=1" title="Guide thank you video" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
  </div>
</section>
"""
    W(slug, S(slug,
              "Guide Thank You | Distinct Designs Construction",
              "Thank you for requesting the Distinct Designs planning guide.",
              body))


def remodels():
    slug = "remodels"
    p = g.prefix(slug)
    body = f"""
<header class="hero hero--page">
  <img class="hero__image" src="{p}images/hero-remodel.webp" alt="Finished open-plan living room and kitchen with a stone feature wall, oak floors and sliding doors onto the desert" width="1920" height="960">
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="hero__content reveal">
    <p class="eyebrow">Remodels</p>
    <h1>The best general contractor in the High Desert and all of the Coachella Valley</h1>
  </div>
</header>
<section class="section">
  <h2>Distinct Designs · the best general contractor in the High Desert and all of the Coachella Valley</h2>
  <h3>We do whole home remodels.</h3>
  <div class="prose">
    <p>Transform your house into the home you've always wanted with expert whole home remodeling services from Distinct Designs Construction. We specialize in complete home renovations, custom interior upgrades, kitchen and bathroom remodeling, open-concept layouts, flooring, lighting, and modern design solutions tailored to your lifestyle. Whether you're updating an older property or creating a luxury living space, our experienced remodeling team delivers high-quality craftsmanship, innovative design, and attention to detail from start to finish. Serving homeowners throughout the Coachella Valley, we provide professional whole house remodels that increase comfort, functionality, and property value.</p>
    <p>Joshua Tree · Yucca Valley · Twentynine Palms · Pioneer Town · Landers · Morongo Valley · Desert Hot Springs · Palm Springs · Palm Desert · Cathedral City · Indian Wells · Rancho Mirage · Greater Southern California</p>
  </div>
  <blockquote class="prose"><p>What makes us the best is we stay at your side from the first sketch to the moment you walk through the finished door, and we're proud of every inch of what's behind it.</p></blockquote>
  <div class="card-grid">
    <article class="info-card"><h3>Fully integrated design-build</h3><p>Architecture, engineering, permitting, and construction under one roof. One team, one contract, one point of accountability.</p></article>
    <article class="info-card"><h3>Engineered for desert living</h3><p>Materials, systems, and structural methods built for extreme heat, UV, and wind, not repurposed coastal California specs.</p></article>
    <article class="info-card"><h3>Transparent pricing, no surprises</h3><p>Detailed scopes, honest timelines, and real conversations about budget before work begins.</p></article>
    <article class="info-card"><h3>Obsessed with the details</h3><p>The tile work, the cabinetry, the transitions: this is where most builders cut corners. It's where we set our standard.</p></article>
  </div>
</section>
<section class="section section--tinted">
  <p class="eyebrow">Signature inclusions, every remodel</p>
  <h2>Remodeling is your opportunity to build it right this time</h2>
  <div class="two-col" style="margin-top:1.5rem">
    <article class="info-card"><h3>Artisan surfaces and premium stonework</h3><ul class="check-list"><li>Luxury tile and natural stone installation</li><li>Custom cabinetry and built-in millwork</li><li>Stone facades, feature walls and hardscape</li><li>Polished concrete and premium flooring</li></ul></article>
    <article class="info-card"><h3>Technology integration and home cinema</h3><ul class="check-list"><li>Dedicated screening room design and build</li><li>Whole-home AV and smart home retrofit</li><li>Structured wiring built into the renovation</li></ul></article>
  </div>
  {R(slug, [("Whole-home remodel service", "services/whole-home-remodel"), ("Contact", "contact")])}
</section>
<section class="lead-section">
  <div class="lead-section__media"><img src="{p}images/footer-cta-remodel.webp" alt="Finished open-plan living room and kitchen remodel" width="1600" height="1200" loading="lazy"></div>
  <div class="lead-section__content">
    <h2>Begin your project.</h2>
    <p>Every Distinct Designs project starts with a private consultation: a direct conversation about your vision, your site, and what it actually takes to build it right. No sales pitch. No pressure. We take on a limited number of projects each year to ensure every client receives our full attention.</p>
    <a class="btn btn--primary" href="{HREF(slug, "contact")}">Start your journey today</a>
  </div>
</section>
"""
    W(slug, S(slug,
              "Whole-Home Remodels in the High Desert & Coachella Valley | Distinct Designs",
              "Whole-home remodels, kitchens, and bathrooms from Distinct Designs Construction across the High Desert and Coachella Valley.",
              body))


def partners():
    slug = "partners"
    p = g.prefix(slug)
    body = f"""
<section class="section">
  <img src="{p}images/site/DD-logo-full.webp" alt="Distinct Designs Construction" width="350" height="128">
  <p class="eyebrow" style="margin-top:1.5rem">Partners</p>
  <h1>When luxury buyers can't find it, we build it</h1>
  <h2>Custom home builds</h2>
  <p class="page-intro">6–7 figure remodels · High and Low Desert. Elite clients don't settle. When the right property doesn't exist, we create it with structured budgets, controlled timelines, and professional execution.</p>
  <div class="card-grid" style="margin-top:1.5rem">
    <article class="info-card"><h3>Partnership program</h3><ul class="check-list"><li>2% on the first project</li><li>3% on the second project</li><li>4% on every project after</li></ul></article>
    <article class="info-card"><h3>Illustrative commission model</h3><ul class="check-list"><li>$2,500,000 × 4% = $100,000</li><li>$2,000,000 × 3% = $60,000</li><li>$1,000,000 × 2% = $20,000</li></ul></article>
    <article class="info-card"><h3>Volume partner incentive</h3><p>Partners referring 2+ projects annually qualify for preferred 4% tier status and priority scheduling access.</p></article>
  </div>
  <h2 style="margin-top:2.5rem">Submit a referral. Lock in your commission.</h2>
  <p>Click next to access the official referral agreement.</p>
  <p><a href="tel:{TEL}">{PHONE}</a><br>www.distinctdesignsconstruction.com</p>
  <div class="link-row"><a class="btn btn--primary" href="{HREF(slug, "partners/referral-agreement")}">Next</a></div>
</section>
"""
    W(slug, S(slug,
              "Partner Referral Program | Distinct Designs Construction",
              "Distinct Designs partner program for agents: 2% on the first referred project, 3% on the second, and 4% after that. High Desert and Coachella Valley custom homes and remodels.",
              body))


def referral():
    slug = "partners/referral-agreement"
    body = f"""
<section class="section">
  <h1>Referral agreement</h1>
  <p class="page-intro">Official agent referral agreement.</p>
  {F(g.REFERRAL_FORM, "Agent referral agreement")}
</section>
"""
    W(slug, S(slug,
              "Agent Referral Agreement | Distinct Designs Construction",
              "Submit the Distinct Designs Construction agent referral agreement.",
              body))


def guides():
    shared_for = [
        "You're planning a custom home or major remodel at $1M or above",
        "You want real numbers before you start designing",
        "You've been burned before, or don't want to be",
        "You're building from out of state and need it handled right",
        "You want it done once, done right",
    ]
    shared_not = [
        "You're collecting three bids to find the cheapest crew",
        "You want the lowest price over the right result",
        "You're not actually planning to build",
        "You'd rather learn the hard way, mid-construction",
    ]
    variants = [
        ("guides/custom-home-builder-1",
         "What It Really Takes to Build a Custom Home in the Desert | Distinct Designs",
         "Free guide for $1M+ custom homes in the High Desert and Coachella Valley: real costs, timelines, and the mistakes that blow budgets.",
         "Free guide · For $1M+ builds in the High Desert &amp; Coachella Valley",
         "What it really takes to build a custom home in the desert",
         "The clarity most homeowners wish they'd had before they started: real costs, real timelines, and the mistakes that quietly blow budgets. Written by a third-generation desert builder.",
         ["What a custom home actually costs here in 2026, by project level",
          "The 5 factors that really drive your budget (it isn't square footage)",
          "The 7 costly mistakes that derail builds, and how to avoid them",
          "The real 18–27 month timeline, phase by phase"],
         "d3BGxWF34ECOkqZdjpSI",
         "This guide is for you if",
         "This isn't for you if",
         "Build with clarity, not surprises"),
        ("guides/custom-home-builder-2",
         "Custom Home Guide for the High Desert | Distinct Designs",
         "Free guide for $1M+ builds in the High Desert and Coachella Valley from Distinct Designs Construction.",
         "Free guide · $1M+ builds · High Desert &amp; Coachella Valley",
         "What it really takes to build a custom home in the desert",
         "The clarity most homeowners wish they'd had before they started: real costs, real timelines, and the mistakes that quietly blow budgets. Written by a third-generation desert builder.",
         ["What a custom home actually costs here in 2026, by project level",
          "The 5 factors that really drive your budget (it isn't square footage)",
          "The 7 costly mistakes that derail builds, and how to avoid them",
          "The real 18–27 month timeline, phase by phase"],
         "BAGEhP3HzpQSiPNrrCqf",
         "This guide is for you if",
         "This isn't for you if",
         "Build with clarity, not surprises"),
        ("guides/custom-home-builder-3",
         "What It Really Costs to Build a Custom Home in the Desert | Distinct Designs",
         "Real numbers, real timelines, and the mistakes that blow custom-home budgets in the High Desert and Coachella Valley.",
         "Free guide · $1M+ builds · High Desert &amp; Coachella Valley",
         "What it really costs to build a custom home in the desert",
         "Real numbers. Real timelines. The mistakes that quietly blow budgets, and how to avoid every one. From a third-generation desert builder.",
         ["What it actually costs here in 2026, by project level",
          "The 5 factors that really drive your budget",
          "The 7 costly mistakes that derail builds",
          "The real 18–27 month timeline"],
         "9M9TcIWN7yJsuz9QWG1R",
         "For you if",
         "Not for you if",
         "Build with clarity, not surprises"),
    ]
    prices = [
        ("Major remodel", "$250K – $400K"),
        ("Large remodel / expansion", "$400K – $750K"),
        ("Custom home", "$750K – $1.35M"),
        ("Luxury custom home", "$2.2M – $3.8M+"),
        ("Luxury estate build", "$4.5M+"),
    ]
    for slug, title, meta, eyebrow, h1, sub, bullets, form_id, for_h, not_h, cta_h in variants:
        p = g.prefix(slug)
        bl = "".join(f"<li>{b}</li>" for b in bullets)
        fl = "".join(f"<li>{b}</li>" for b in shared_for)
        nl = "".join(f"<li>{b}</li>" for b in shared_not)
        cards = "".join(f'<article class="price-card"><h3>{n}</h3><strong>{v}</strong></article>' for n, v in prices)
        body = f"""
<section class="section">
  <p class="eyebrow">Distinct Designs · <a href="tel:{TEL}">760·221·4290</a></p>
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  <p class="page-intro">{sub}</p>
  <ul class="check-list" style="margin-top:1.25rem">{bl}</ul>
  <div class="two-col" style="margin-top:2rem">
    <div>
      <p><strong>Free · instant download</strong></p>
      <img src="{p}images/site/Distinct-Design-Planning-Guide-2.png" alt="Distinct Designs planning guide cover" width="600" height="780" loading="lazy">
    </div>
    <div>{F(form_id, "Download the planning guide")}</div>
  </div>
  <div class="stat-row" style="margin-top:2rem">
    <article class="stat-card"><span>4.9★</span><small>15+ reviews</small></article>
    <article class="stat-card"><span>18 years</span><small>Building</small></article>
    <article class="stat-card"><span>3rd generation</span><small>Desert builder</small></article>
    <article class="stat-card"><span>#1145786</span><small>License</small></article>
  </div>
  <p class="page-intro" style="margin-top:1rem">High Desert · Coachella Valley</p>
</section>
<section class="section section--tinted">
  <p class="eyebrow">Inside the guide</p>
  <h2>The numbers most builders never put in writing</h2>
  <p>The same information we walk serious clients through before the first dollar is spent. Yours, free.</p>
  <div class="card-grid" style="margin-top:1.5rem">
    <article class="info-card"><p class="eyebrow">01. Real investment levels</p><h3>What it actually costs</h3><p>Honest ranges for every project level, from a major remodel to a luxury estate, $250K to $4.5M+, plus real cost-per-square-foot for the desert market.</p></article>
    <article class="info-card"><p class="eyebrow">02. The 5 cost drivers</p><h3>What really moves the budget</h3><p>Why square footage is the smallest part of the equation, and how architecture, engineering, materials, and site conditions swing a build by six figures.</p></article>
    <article class="info-card"><p class="eyebrow">03. 7 costly mistakes</p><h3>What derails a build</h3><p>The seven mistakes that blow budgets, including why a $5,000 design change becomes $30,000+ once framing is up.</p></article>
    <article class="info-card"><p class="eyebrow">04. The real timeline</p><h3>What to actually expect</h3><p>The true 18–27 month path from first conversation to move-in, phase by phase, so nothing catches you off guard.</p></article>
  </div>
</section>
<section class="section">
  <p class="eyebrow">A preview. Know your investment.</p>
  <h2>Where projects typically land</h2>
  <p class="page-intro">Every project is priced to its site, scope, and selections. The full guide breaks down what each level includes.</p>
  <div class="price-grid" style="margin-top:1.5rem">{cards}</div>
  <p style="margin-top:1rem">Get the full breakdown, what each level includes and real cost-per-square-foot, in the free guide.</p>
</section>
<section class="section section--split section--tinted">
  <div class="section--split__media"><img src="{p}images/site/Nick-DD.jpg" alt="Nick Aguilar, owner of Distinct Designs" width="800" height="1000" loading="lazy"></div>
  <div>
    <p class="eyebrow">Who wrote this</p>
    <p>My grandfather, Mario Trujillo, a decorated Marine Corps Master Gunnery Sergeant, put me to work at 11 and taught me discipline, pride in craftsmanship, and treating every project like it's your own.</p>
    <p>I wrote this guide to give homeowners what most builders never offer: clear information before the first dollar is spent.</p>
    <p><strong>Nick Aguilar</strong><br>Third-generation builder · Distinct Designs</p>
  </div>
</section>
<section class="section">
  <p class="eyebrow">What clients say</p>
  <h2>On time. On budget. No surprises.</h2>
  {Q(g.GUIDE_QUOTES)}
</section>
<section class="section section--tinted">
  <p class="eyebrow">Is this guide for you?</p>
  <h2>Let's be honest about who this is for</h2>
  <div class="two-col" style="margin-top:1.5rem">
    <article class="info-card"><h3>{for_h}</h3><ul class="check-list">{fl}</ul></article>
    <article class="info-card"><h3>{not_h}</h3><ul class="check-list">{nl}</ul></article>
  </div>
</section>
<section class="section" id="form">
  <p class="eyebrow">Get the guide</p>
  <h2>{cta_h}</h2>
  <p>Enter your details and we'll send the full Ultimate Planning Guide straight to your inbox.</p>
  {F(GUIDE, "Get the free guide")}
  <p style="margin-top:2rem">Third-generation luxury custom home building and whole-home remodels across the High Desert and Coachella Valley. CA License #1145786.</p>
  <p><a href="tel:{TEL}">760·221·4290</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>Yucca Valley · Joshua Tree · Palm Springs · Palm Desert · Rancho Mirage · La Quinta</p>
</section>
"""
        W(slug, S(slug, title, meta, body))


def missing():
    """Placeholder so a forgotten route is obvious during review. Not a public page."""
    return None
