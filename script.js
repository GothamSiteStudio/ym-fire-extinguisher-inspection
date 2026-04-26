/* Y&M Fire Extinguisher Inspection & Services — site interactions */

(function () {
  'use strict';

  document.getElementById('year').textContent = new Date().getFullYear();

  // Header scroll state
  const header = document.getElementById('siteHeader');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile nav toggle
  const toggle = document.getElementById('navToggle');
  const nav = document.querySelector('.nav');
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }));

  // Reveal-on-scroll
  const reveal = (el) => el.classList.add('in');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { reveal(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.section-head, .card, .industry, .feature, .why-card, .steps li, .contact-form, .contact-list, .hero-copy, .hero-card, .cta-inner').forEach(el => {
      el.classList.add('reveal');
      io.observe(el);
    });
  } else {
    document.querySelectorAll('.reveal').forEach(reveal);
  }

  // Contact form — graceful fallback (mailto)
  const form = document.getElementById('contactForm');
  const success = document.getElementById('formSuccess');
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const fd = new FormData(form);
    const name = (fd.get('name') || '').toString().trim();
    const email = (fd.get('email') || '').toString().trim();
    const phone = (fd.get('phone') || '').toString().trim();

    if (!name || !email || !phone) {
      alert('Please fill in your name, phone, and email.');
      return;
    }

    const body =
      `Name: ${name}\n` +
      `Phone: ${phone}\n` +
      `Email: ${email}\n` +
      `Property type: ${fd.get('property') || ''}\n` +
      `Address: ${fd.get('address') || ''}\n\n` +
      `${fd.get('message') || ''}`;

    const subject = encodeURIComponent(`Inspection request — ${name}`);
    const mailto = `mailto:info@ymextinguishers.com?subject=${subject}&body=${encodeURIComponent(body)}`;

    // Open user's email client with prefilled details
    window.location.href = mailto;

    // Show in-page confirmation
    success.hidden = false;
    form.querySelector('button[type="submit"]').disabled = true;
  });

  // Smooth-scroll offset compensation for sticky header
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (id.length < 2) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const headerH = header.offsetHeight;
      const top = target.getBoundingClientRect().top + window.scrollY - headerH - 12;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
})();
