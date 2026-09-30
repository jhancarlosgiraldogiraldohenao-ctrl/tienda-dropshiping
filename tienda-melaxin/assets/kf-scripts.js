/* Kojicfur · interacciones (vanilla, sin dependencias) */
(function () {
  'use strict';

  function initReveals(root) {
    var els = (root || document).querySelectorAll('.kf-reveal:not(.is-visible)');
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('is-visible'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); } });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (e) { io.observe(e); });
  }

  function initZonas(root) {
    (root || document).querySelectorAll('[data-kf-zonas]').forEach(function (z) {
      var btns = z.querySelectorAll('[data-kf-zona-btn]');
      var paneles = z.querySelectorAll('[data-kf-zona]');
      var img = z.querySelector('[data-kf-zona-img]');
      btns.forEach(function (b) {
        b.addEventListener('click', function () {
          var i = b.getAttribute('data-kf-zona-btn');
          btns.forEach(function (x) { x.classList.toggle('is-activa', x === b); x.setAttribute('aria-pressed', x === b); });
          paneles.forEach(function (p) { p.classList.toggle('is-activa', p.getAttribute('data-kf-zona') === i); });
          var src = b.getAttribute('data-img');
          if (img && src && img.getAttribute('src') !== src) {
            img.style.opacity = 0;
            setTimeout(function () { img.src = src; img.style.opacity = ''; }, 200);
          }
        });
      });
    });
  }

  function initGaleria(root) {
    (root || document).querySelectorAll('[data-kf-galeria]').forEach(function (g) {
      var principal = g.querySelector('.kf-galeria__principal img');
      g.querySelectorAll('.kf-galeria__min').forEach(function (m) {
        m.addEventListener('click', function () {
          g.querySelectorAll('.kf-galeria__min').forEach(function (x) { x.classList.remove('is-activo'); });
          m.classList.add('is-activo');
          principal.style.opacity = 0;
          setTimeout(function () {
            principal.src = m.getAttribute('data-src');
            principal.srcset = m.getAttribute('data-srcset') || '';
            principal.alt = m.getAttribute('data-alt') || '';
            principal.style.opacity = 1;
          }, 180);
        });
      });
    });
  }

  function initCompra(root) {
    (root || document).querySelectorAll('[data-kf-compra]').forEach(function (c) {
      var q = c.querySelector('input[name="quantity"]');
      var ahora = c.querySelector('[data-kf-comprar]');
      var id = c.querySelector('input[name="id"]');
      function cant() { return q ? Math.max(1, parseInt(q.value, 10) || 1) : 1; }
      function sync() { if (ahora && id) ahora.setAttribute('href', ahora.getAttribute('href').replace(/\/\d+:\d+$/, '/' + id.value + ':' + cant())); }
      c.querySelectorAll('[data-kf-cant]').forEach(function (b) {
        b.addEventListener('click', function () {
          if (!q) return;
          q.value = Math.max(1, cant() + parseInt(b.getAttribute('data-kf-cant'), 10));
          sync();
        });
      });
      if (q) q.addEventListener('change', sync);
      sync();
    });
    var barra = document.querySelector('[data-kf-sticky-compra]');
    var ancla = document.querySelector('[data-kf-compra] .kf-compra__form');
    if (barra && ancla && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        var e = en[0];
        barra.classList.toggle('is-visible', !e.isIntersecting && e.boundingClientRect.top < 0);
      }).observe(ancla);
    }
  }

  function initTodo(root) { initReveals(root); initZonas(root); initGaleria(root); initCompra(root); }
  document.addEventListener('DOMContentLoaded', function () { initTodo(document); });
  document.addEventListener('shopify:section:load', function (e) { initTodo(e.target); });
})();
