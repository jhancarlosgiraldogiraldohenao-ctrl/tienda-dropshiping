/* Holly · interacciones (vanilla, sin dependencias) */
(function () {
  'use strict';
  // Varias secciones cargan este archivo: se inicializa una sola vez.
  if (window.__hlScripts) return;
  window.__hlScripts = true;

  function initReveals(root) {
    var els = (root || document).querySelectorAll('.hl-reveal:not(.is-visible)');
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('is-visible'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); } });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (e) { io.observe(e); });
  }

  function initZonas(root) {
    (root || document).querySelectorAll('[data-hl-zonas]').forEach(function (z) {
      var btns = z.querySelectorAll('[data-hl-zona-btn]');
      var paneles = z.querySelectorAll('[data-hl-zona]');
      var img = z.querySelector('[data-hl-zona-img]');
      btns.forEach(function (b) {
        b.addEventListener('click', function () {
          var i = b.getAttribute('data-hl-zona-btn');
          btns.forEach(function (x) { x.classList.toggle('is-activa', x === b); x.setAttribute('aria-pressed', x === b); });
          paneles.forEach(function (p) { p.classList.toggle('is-activa', p.getAttribute('data-hl-zona') === i); });
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
    (root || document).querySelectorAll('[data-hl-galeria]').forEach(function (g) {
      var principal = g.querySelector('.hl-galeria__principal img');
      g.querySelectorAll('.hl-galeria__min').forEach(function (m) {
        m.addEventListener('click', function () {
          g.querySelectorAll('.hl-galeria__min').forEach(function (x) { x.classList.remove('is-activo'); });
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
    (root || document).querySelectorAll('[data-hl-compra]').forEach(function (c) {
      var q = c.querySelector('input[name="quantity"]');
      var ahora = c.querySelector('[data-hl-comprar]');
      var id = c.querySelector('input[name="id"]');
      function cant() { return q ? Math.max(1, parseInt(q.value, 10) || 1) : 1; }
      function sync() { if (ahora && id) ahora.setAttribute('href', ahora.getAttribute('href').replace(/\/\d+:\d+$/, '/' + id.value + ':' + cant())); }
      c.querySelectorAll('[data-hl-cant]').forEach(function (b) {
        b.addEventListener('click', function () {
          if (!q) return;
          q.value = Math.max(1, cant() + parseInt(b.getAttribute('data-hl-cant'), 10));
          sync();
        });
      });
      if (q) q.addEventListener('change', sync);
      var precio = c.querySelector('[data-hl-precio]');
      var antes = c.querySelector('[data-hl-antes]');
      var pct = c.querySelector('[data-hl-pct]');
      var sPrecio = document.querySelector('[data-hl-sticky-precio]');
      var sComprar = document.querySelector('[data-hl-comprar-sticky]');
      var foto = document.querySelector('.hl-galeria__principal img');
      c.querySelectorAll('[data-hl-oferta]').forEach(function (r) {
        r.addEventListener('change', function () {
          if (!r.checked) return;
          c.querySelectorAll('.hl-oferta').forEach(function (l) { l.classList.toggle('is-activa', l.contains(r)); });
          if (id) id.value = r.value;
          if (precio) precio.textContent = r.dataset.price;
          if (sPrecio) sPrecio.textContent = r.dataset.price;
          if (antes) { antes.textContent = r.dataset.compare; antes.hidden = !r.dataset.compare; }
          if (pct) { pct.textContent = r.dataset.pct; pct.hidden = !r.dataset.pct; }
          if (sComprar) sComprar.setAttribute('href', sComprar.getAttribute('href').replace(/\/\d+:\d+$/, '/' + r.value + ':1'));
          var mins = document.querySelector('.hl-galeria__mins');
          if (mins) {
            var labels = c.querySelectorAll('[data-hl-oferta]');
            var modo = (labels.length > 1 && r === labels[1]) ? 'pack' : 'uno';
            mins.setAttribute('data-modo', modo);
            mins.querySelectorAll('.hl-galeria__min').forEach(function (m) {
              var gr = m.getAttribute('data-grupo');
              m.hidden = gr !== 'todos' && gr !== modo;
              m.classList.toggle('is-activo', gr === modo);
            });
          }
          if (foto && r.dataset.img && foto.getAttribute('src') !== r.dataset.img) {
            foto.style.opacity = 0;
            setTimeout(function () { foto.removeAttribute('srcset'); foto.src = r.dataset.img; foto.style.opacity = 1; }, 180);
          }
          var url = new URL(window.location.href); url.searchParams.set('variant', r.value); window.history.replaceState({}, '', url);
          sync();
        });
      });
      sync();
    });
    var barra = document.querySelector('[data-hl-sticky-compra]');
    var ancla = document.querySelector('[data-hl-compra] .hl-compra__form');
    if (barra && ancla && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        var e = en[0];
        barra.classList.toggle('is-visible', !e.isIntersecting && e.boundingClientRect.top < 0);
      }).observe(ancla);
    }
  }

  function initHeroPack(root) {
    (root || document).querySelectorAll('[data-hl-hero]').forEach(function (h) {
      var b = h.querySelector('[data-hl-h-pack]');
      if (!b) return;
      var comprar = h.querySelector('[data-hl-h-comprar]');
      var txt = comprar ? comprar.querySelector('span') : null;
      var precio = h.querySelector('[data-hl-h-precio]');
      var antes = h.querySelector('[data-hl-h-antes]');
      var pct = h.querySelector('[data-hl-h-pct]');
      var sello = h.querySelector('[data-hl-h-sello]');
      b.addEventListener('click', function () {
        var pack = !h.classList.contains('is-pack');
        var k = pack ? 'Pack' : 'Uno';
        h.classList.toggle('is-pack', pack);
        b.setAttribute('aria-pressed', pack);
        b.textContent = pack ? b.dataset.txtVolver : b.dataset.txtPack;
        if (comprar) comprar.setAttribute('href', b.dataset['url' + k]);
        if (txt) txt.textContent = b.dataset['txtComprar' + k];
        if (precio) precio.textContent = b.dataset['precio' + k];
        if (antes) antes.textContent = b.dataset['antes' + k];
        if (pct) pct.textContent = b.dataset['pct' + k];
        if (sello) sello.textContent = b.dataset['sello' + k];
      });
    });
  }

  function initComparador(root) {
    (root || document).querySelectorAll('[data-hl-comparador]').forEach(function (c) {
      var r = c.querySelector('input[type="range"]');
      if (r) r.addEventListener('input', function () { c.style.setProperty('--pos', r.value + '%'); });
    });
  }

  function initTodo(root) { initComparador(root); initReveals(root); initZonas(root); initGaleria(root); initCompra(root); initHeroPack(root); }
  document.addEventListener('DOMContentLoaded', function () { initTodo(document); });
  document.addEventListener('shopify:section:load', function (e) { initTodo(e.target); });
})();
