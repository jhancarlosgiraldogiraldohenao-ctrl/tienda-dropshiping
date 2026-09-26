/* VURONIX · interacciones propias (vanilla, sin librerías) */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function formato(n, dec) {
    return Number(n).toLocaleString('es-CO', { minimumFractionDigits: dec, maximumFractionDigits: dec });
  }

  /* Un único observador para reveals y contadores */
  var observador = null;
  function obs() {
    if (observador || !('IntersectionObserver' in window)) return observador;
    observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        el.classList.add('vx-visible');
        if (el.hasAttribute('data-vx-count')) contar(el);
        if (el.hasAttribute('data-vx-hud')) arrancarHud(el);
        observador.unobserve(el);
      });
    }, { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
    return observador;
  }

  function initReveals(root) {
    var els = (root || document).querySelectorAll('.vx-reveal, [data-vx-count], [data-vx-hud], .vx-cifra');
    if (!els.length) return;
    var o = obs();
    els.forEach(function (el) {
      if (!o || reduce) {
        el.classList.add('vx-visible');
        if (el.hasAttribute('data-vx-count')) el.textContent = el.getAttribute('data-vx-prefijo') + formato(el.getAttribute('data-vx-count'), +el.getAttribute('data-vx-dec') || 0);
        if (el.hasAttribute('data-vx-hud')) arrancarHud(el, true);
        return;
      }
      o.observe(el);
    });
  }

  function contar(el) {
    var fin = parseFloat(el.getAttribute('data-vx-count')) || 0;
    var dec = parseInt(el.getAttribute('data-vx-dec') || '0', 10);
    var pre = el.getAttribute('data-vx-prefijo') || '';
    var dur = 1600, t0 = null;
    function paso(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      var ease = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + formato(fin * ease, dec);
      if (p < 1) requestAnimationFrame(paso);
    }
    requestAnimationFrame(paso);
  }

  /* HUD del hero: simula la pantalla inflando hasta la presión objetivo */
  function arrancarHud(hud, instantaneo) {
    var valor = hud.querySelector('[data-vx-hud-valor]');
    var barra = hud.querySelector('[data-vx-hud-barra]');
    var estado = hud.querySelector('[data-vx-hud-estado]');
    var desde = parseFloat(hud.getAttribute('data-desde')) || 18;
    var hasta = parseFloat(hud.getAttribute('data-hasta')) || 32;
    var txtInflando = hud.getAttribute('data-txt-inflando') || '';
    var txtListo = hud.getAttribute('data-txt-listo') || '';
    function pintar(v) {
      valor.firstChild.nodeValue = v.toFixed(1);
      barra.style.width = ((v - desde) / (hasta - desde)) * 100 + '%';
    }
    if (instantaneo) { pintar(hasta); hud.classList.add('is-listo'); estado.textContent = txtListo; return; }
    function ciclo() {
      hud.classList.remove('is-listo'); estado.textContent = txtInflando;
      var t0 = null, dur = 3200;
      function paso(t) {
        if (!t0) t0 = t;
        var p = Math.min((t - t0) / dur, 1);
        pintar(desde + (hasta - desde) * p);
        if (p < 1) return requestAnimationFrame(paso);
        hud.classList.add('is-listo'); estado.textContent = txtListo;
        setTimeout(ciclo, 3800);
      }
      requestAnimationFrame(paso);
    }
    ciclo();
  }

  /* Parallax suave de la foto del hero */
  function initParallax() {
    var imgs = document.querySelectorAll('[data-vx-parallax]');
    if (!imgs.length || reduce) return;
    var ticking = false;
    function actualizar() {
      imgs.forEach(function (img) {
        var r = img.parentElement.getBoundingClientRect();
        var k = parseFloat(img.getAttribute('data-vx-parallax')) || 0;
        var desp = (r.top + r.height / 2 - window.innerHeight / 2) * -k / 100;
        img.style.transform = 'translate3d(0,' + (desp - r.height * 0.07).toFixed(1) + 'px,0)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(actualizar); } }, { passive: true });
    actualizar();
  }

  /* Anatomía: puntos <-> tarjetas */
  function initAnatomia(root) {
    (root || document).querySelectorAll('[data-vx-anatomia]').forEach(function (sec) {
      var items = sec.querySelectorAll('[data-vx-punto]');
      function activar(id) {
        items.forEach(function (i) { i.classList.toggle('is-activo', i.getAttribute('data-vx-punto') === id); });
      }
      items.forEach(function (i) {
        var id = i.getAttribute('data-vx-punto');
        i.addEventListener('mouseenter', function () { activar(id); });
        i.addEventListener('click', function () { activar(id); });
        i.addEventListener('focus', function () { activar(id); });
      });
    });
  }

  /* Modos: tabs que cambian la lectura */
  function initModos(root) {
    (root || document).querySelectorAll('[data-vx-modos]').forEach(function (sec) {
      var panel = sec.querySelector('.vx-modos__panel');
      var lcd = sec.querySelector('[data-vx-modo-valor]');
      var unidad = sec.querySelector('[data-vx-modo-unidad]');
      var nombre = sec.querySelector('[data-vx-modo-nombre]');
      var nota = sec.querySelector('[data-vx-modo-nota]');
      var tabs = sec.querySelectorAll('.vx-modo');
      tabs.forEach(function (tab) {
        tab.addEventListener('click', function () {
          tabs.forEach(function (t) { t.classList.remove('is-activo'); t.setAttribute('aria-selected', 'false'); });
          tab.classList.add('is-activo'); tab.setAttribute('aria-selected', 'true');
          panel.classList.add('is-cambiando');
          setTimeout(function () {
            lcd.firstChild.nodeValue = tab.getAttribute('data-valor');
            unidad.textContent = tab.getAttribute('data-unidad');
            nombre.textContent = tab.getAttribute('data-nombre');
            nota.textContent = tab.getAttribute('data-nota');
            panel.classList.remove('is-cambiando');
          }, 260);
        });
      });
    });
  }

  /* Pasos: escena sticky que cambia de foto */
  function initPasos(root) {
    (root || document).querySelectorAll('[data-vx-pasos]').forEach(function (sec) {
      var pasos = sec.querySelectorAll('.vx-paso');
      var fotos = sec.querySelectorAll('.vx-pasos__pila img');
      var cont = sec.querySelector('[data-vx-pasos-num]');
      if (!pasos.length || !('IntersectionObserver' in window)) { pasos.forEach(function (p) { p.classList.add('is-activo'); }); return; }
      var o = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (e) {
          if (!e.isIntersecting) return;
          var i = +e.target.getAttribute('data-i');
          pasos.forEach(function (p, j) { p.classList.toggle('is-activo', j === i); });
          fotos.forEach(function (f, j) { f.classList.toggle('is-activo', j === i); });
          if (cont) cont.textContent = String(i + 1).padStart(2, '0');
        });
      }, { rootMargin: '-45% 0px -45% 0px' });
      pasos.forEach(function (p) { o.observe(p); });
    });
  }

  /* Galería de producto */
  function initGaleria(root) {
    (root || document).querySelectorAll('[data-vx-galeria]').forEach(function (g) {
      var principal = g.querySelector('.vx-galeria__principal img');
      var mins = g.querySelectorAll('.vx-galeria__min');
      mins.forEach(function (m) {
        m.addEventListener('click', function () {
          mins.forEach(function (x) { x.classList.remove('is-activo'); });
          m.classList.add('is-activo');
          principal.classList.add('is-cambiando');
          setTimeout(function () {
            principal.src = m.getAttribute('data-src');
            principal.srcset = m.getAttribute('data-srcset') || '';
            principal.alt = m.getAttribute('data-alt') || '';
            principal.classList.remove('is-cambiando');
          }, 180);
        });
      });
    });
  }

  /* Producto: variantes, cantidad y barra fija en móvil */
  function initCompra(root) {
    (root || document).querySelectorAll('[data-vx-compra]').forEach(function (c) {
      var datos = c.querySelector('[data-vx-variantes]');
      var input = c.querySelector('input[name="id"]');
      var precio = c.querySelector('[data-vx-precio]');
      var antes = c.querySelector('[data-vx-antes]');
      var boton = c.querySelector('button[name="add"]');
      var txtBoton = boton ? boton.querySelector('span') : null;
      var txtCompra = c.getAttribute('data-txt-comprar');
      var txtAgotado = c.getAttribute('data-txt-agotado');
      var selects = c.querySelectorAll('[data-vx-opcion]');
      var formatoDinero = c.getAttribute('data-formato');
      function dinero(cents) {
        var v = (cents / 100);
        var entero = Math.round(v).toLocaleString('es-CO');
        var dec = v.toLocaleString('es-CO', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        return (formatoDinero || '${{amount_no_decimals_with_comma_separator}}')
          .replace(/\{\{\s*amount_no_decimals_with_comma_separator\s*\}\}/, entero)
          .replace(/\{\{\s*amount_no_decimals\s*\}\}/, entero)
          .replace(/\{\{\s*amount_with_comma_separator\s*\}\}/, dec)
          .replace(/\{\{\s*amount\s*\}\}/, dec);
      }
      var barraPrecio = document.querySelector('[data-vx-sticky-compra] strong');
      var duoImg = document.querySelector('[data-vx-duo-principal] img');
      var duoOriginal = duoImg ? duoImg.getAttribute('src') : null;
      function aplicar(v) {
        input.value = v.id;
        if (precio) precio.textContent = dinero(v.price);
        if (barraPrecio) barraPrecio.textContent = dinero(v.price);
        if (antes) antes.textContent = v.compare_at_price > v.price ? dinero(v.compare_at_price) : '';
        if (boton) {
          if (v.available) { boton.removeAttribute('disabled'); boton.removeAttribute('aria-disabled'); if (txtBoton) txtBoton.textContent = txtCompra; }
          else { boton.setAttribute('disabled', ''); if (txtBoton) txtBoton.textContent = txtAgotado; }
        }
        if (duoImg && v.img !== undefined) {
          var nueva = v.primera ? duoOriginal : v.img;
          if (nueva && duoImg.getAttribute('src') !== nueva) {
            duoImg.style.opacity = 0;
            setTimeout(function () { duoImg.removeAttribute('srcset'); duoImg.src = nueva; duoImg.style.opacity = 1; }, 180);
          }
        }
        var url = new URL(window.location.href); url.searchParams.set('variant', v.id); window.history.replaceState({}, '', url);
      }
      var radios = c.querySelectorAll('[data-vx-oferta]');
      radios.forEach(function (r, idx) {
        r.addEventListener('change', function () {
          radios.forEach(function (x) { x.closest('.vx-oferta').classList.toggle('is-activa', x.checked); });
          aplicar({ id: r.value, price: +r.dataset.price, compare_at_price: +r.dataset.compare, available: r.dataset.available === 'true', img: r.dataset.img, primera: idx === 0 });
        });
      });
      var marcada = c.querySelector('[data-vx-oferta]:checked');
      if (marcada && marcada !== radios[0]) marcada.dispatchEvent(new Event('change'));
      if (datos && selects.length) {
        var variantes = JSON.parse(datos.textContent);
        selects.forEach(function (s) {
          s.addEventListener('change', function () {
            var elegidas = Array.prototype.map.call(selects, function (x) { return x.value; });
            var v = variantes.find(function (vv) { return vv.options.every(function (o, i) { return o === elegidas[i]; }); });
            if (!v) { if (boton) boton.setAttribute('disabled', ''); if (txtBoton) txtBoton.textContent = txtAgotado; return; }
            aplicar(v);
          });
        });
      }
      c.querySelectorAll('[data-vx-cant]').forEach(function (b) {
        b.addEventListener('click', function () {
          var q = c.querySelector('input[name="quantity"]');
          q.value = Math.max(1, (parseInt(q.value, 10) || 1) + parseInt(b.getAttribute('data-vx-cant'), 10));
        });
      });
      var barra = document.querySelector('[data-vx-sticky-compra]');
      if (barra && boton && 'IntersectionObserver' in window) {
        new IntersectionObserver(function (e) {
          barra.classList.toggle('is-visible', !e[0].isIntersecting && e[0].boundingClientRect.top < 0);
        }).observe(boton);
        var irA = barra.querySelector('button');
        if (irA) irA.addEventListener('click', function () { boton.click(); });
      }
    });
  }

  function initTodo(root) {
    initReveals(root); initAnatomia(root); initModos(root); initPasos(root); initGaleria(root); initCompra(root);
  }

  document.addEventListener('DOMContentLoaded', function () { initTodo(document); initParallax(); });
  document.addEventListener('shopify:section:load', function (e) { initTodo(e.target); });
})();
