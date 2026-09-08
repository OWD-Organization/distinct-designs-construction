/* =================================================================
   DISTINCT DESIGNS CONSTRUCTION — SITE INTERACTIONS
   Vanilla JS only. No dependencies.
   ================================================================= */

(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------------
     Footer year
     --------------------------------------------------------------- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------------------------------------------------------------
     Sticky nav shadow/border on scroll
     --------------------------------------------------------------- */
  var siteNav = document.getElementById("site-nav");
  var stickyCta = document.getElementById("sticky-cta");
  var hero = document.querySelector(".hero");

  function handleScrollState() {
    var scrolled = window.scrollY > 12;
    if (siteNav) siteNav.classList.toggle("is-scrolled", scrolled);

    if (stickyCta && hero) {
      var heroBottom = hero.getBoundingClientRect().bottom;
      stickyCta.classList.toggle("is-visible", heroBottom < 0);
    }
  }

  window.addEventListener("scroll", handleScrollState, { passive: true });
  handleScrollState();

  /* ---------------------------------------------------------------
     Mobile nav toggle
     --------------------------------------------------------------- */
  var navToggle = document.getElementById("nav-toggle");
  var mobileNav = document.getElementById("site-nav__mobile");

  if (navToggle && mobileNav) {
    navToggle.addEventListener("click", function () {
      var isOpen = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!isOpen));
      navToggle.setAttribute("aria-label", isOpen ? "Open menu" : "Close menu");
      mobileNav.classList.toggle("is-open", !isOpen);
    });

    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Open menu");
        mobileNav.classList.remove("is-open");
      });
    });
  }

  /* ---------------------------------------------------------------
     Scroll-triggered reveal animations
     --------------------------------------------------------------- */
  var revealEls = document.querySelectorAll(".reveal");

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      // threshold 0 so elements taller than the viewport still trigger
      { threshold: 0, rootMargin: "0px 0px -80px 0px" }
    );
    revealEls.forEach(function (el) { revealObserver.observe(el); });
  }

  /* ---------------------------------------------------------------
     FAQ accordion (multi-open, accessible)
     --------------------------------------------------------------- */
  var accordionTriggers = document.querySelectorAll(".accordion__trigger");

  accordionTriggers.forEach(function (trigger) {
    var panel = document.getElementById(trigger.getAttribute("aria-controls"));
    if (!panel) return;

    trigger.addEventListener("click", function () {
      var isOpen = trigger.getAttribute("aria-expanded") === "true";
      trigger.setAttribute("aria-expanded", String(!isOpen));

      if (isOpen) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    });
  });

  /* ---------------------------------------------------------------
     Lead form handling
     Note: no backend wired up yet — replace this handler's success
     branch with a real fetch() to your CRM/email endpoint.
     --------------------------------------------------------------- */
  var leadForm = document.getElementById("lead-form");
  var leadFormNote = document.getElementById("lead-form-note");

  if (leadForm && leadFormNote) {
    leadForm.addEventListener("submit", function (event) {
      event.preventDefault();

      if (!leadForm.checkValidity()) {
        leadFormNote.textContent = "Please complete all required fields before submitting.";
        leadForm.reportValidity();
        return;
      }

      // TODO: wire to real submission endpoint (CRM, email service, etc.)
      leadFormNote.textContent = "Thank you — Nick's team will reach out within one business day.";
      leadForm.reset();
    });
  }
})();
