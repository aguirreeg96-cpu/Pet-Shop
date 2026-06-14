/* ============================================================
   PATITAS PET SHOP — script.js
   ============================================================ */

'use strict';

/* ---------- Sticky Header ---------- */
(function () {
  const header = document.getElementById('header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

/* ---------- Mobile Menu ---------- */
(function () {
  const hamburger = document.getElementById('hamburger');
  const menu = document.getElementById('navMenu');

  hamburger.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('open');
    hamburger.classList.toggle('open', isOpen);
    hamburger.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  /* Close on link click */
  menu.querySelectorAll('.nav__link').forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.remove('open');
      hamburger.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });

  /* Close on outside click */
  document.addEventListener('click', e => {
    if (!header.contains(e.target) && menu.classList.contains('open')) {
      menu.classList.remove('open');
      hamburger.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  });
})();

/* ---------- Scroll Reveal (IntersectionObserver) ---------- */
(function () {
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
    return;
  }

  const io = new IntersectionObserver(
    entries => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          /* Stagger siblings inside a grid */
          const siblings = entry.target.parentElement.querySelectorAll('.reveal:not(.visible)');
          siblings.forEach((sib, idx) => {
            if (sib === entry.target || entry.target.parentElement.contains(sib)) {
              setTimeout(() => sib.classList.add('visible'), idx * 90);
            }
          });
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
})();

/* ---------- Smooth Scroll for anchor links ---------- */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const headerH = document.getElementById('header').offsetHeight;
    const top = target.getBoundingClientRect().top + window.scrollY - headerH - 8;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});

/* ---------- Active NavLink on Scroll ---------- */
(function () {
  const sections = document.querySelectorAll('section[id], footer[id]');
  const navLinks = document.querySelectorAll('.nav__link');
  const headerH = () => document.getElementById('header').offsetHeight;

  const setActive = () => {
    const scrollY = window.scrollY;
    let current = '';
    sections.forEach(sec => {
      if (scrollY >= sec.offsetTop - headerH() - 60) current = sec.id;
    });
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      link.style.fontWeight = href === `#${current}` ? '700' : '';
    });
  };

  window.addEventListener('scroll', setActive, { passive: true });
})();

/* ---------- WhatsApp float: show after scroll ---------- */
(function () {
  const wa = document.querySelector('.wa-float');
  if (!wa) return;
  wa.style.opacity = '0';
  wa.style.transform = 'scale(0.8)';
  wa.style.transition = 'opacity .4s ease, transform .4s ease';

  const show = () => {
    if (window.scrollY > 300) {
      wa.style.opacity = '1';
      wa.style.transform = 'scale(1)';
    } else {
      wa.style.opacity = '0';
      wa.style.transform = 'scale(0.8)';
    }
  };

  window.addEventListener('scroll', show, { passive: true });
  show();
})();

/* ---------- Lazy load images fallback ---------- */
(function () {
  if ('loading' in HTMLImageElement.prototype) return;
  const imgs = document.querySelectorAll('img[loading="lazy"]');
  const io = new IntersectionObserver(entries => {
    entries.forEach(({ isIntersecting, target }) => {
      if (isIntersecting) {
        target.src = target.getAttribute('data-src') || target.src;
        io.unobserve(target);
      }
    });
  });
  imgs.forEach(img => io.observe(img));
})();

/* ---------- Gallery lightbox (simple) ---------- */
(function () {
  const items = document.querySelectorAll('.gallery__item');
  if (!items.length) return;

  const overlay = document.createElement('div');
  overlay.style.cssText = `
    display:none;position:fixed;inset:0;z-index:99999;
    background:rgba(0,0,0,.9);cursor:zoom-out;
    align-items:center;justify-content:center;
  `;
  const img = document.createElement('img');
  img.style.cssText = 'max-width:92vw;max-height:92vh;border-radius:12px;box-shadow:0 20px 80px rgba(0,0,0,.6);';
  overlay.appendChild(img);
  document.body.appendChild(overlay);

  items.forEach(item => {
    item.style.cursor = 'zoom-in';
    item.addEventListener('click', () => {
      const src = item.querySelector('img').src;
      img.src = src.replace(/w=\d+/, 'w=1200');
      overlay.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    });
  });

  overlay.addEventListener('click', () => {
    overlay.style.display = 'none';
    document.body.style.overflow = '';
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && overlay.style.display === 'flex') {
      overlay.style.display = 'none';
      document.body.style.overflow = '';
    }
  });
})();
