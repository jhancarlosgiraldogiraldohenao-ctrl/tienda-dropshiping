/* Zero Club — interacciones de las secciones zc- */
(function () {
  function money(cents) {
    return '$' + Math.round(cents / 100).toLocaleString('es-CO').replace(/,/g, '.');
  }

  function initProduct(root) {
    var form = root.querySelector('[data-zc-form]');
    if (!form) return;
    var idInput = form.querySelector('input[name="id"]');
    var offers = root.querySelectorAll('[data-zc-offer]');
    var main = root.querySelector('[data-zc-main]');
    var thumbs = root.querySelectorAll('[data-zc-thumb]');
    var commit = root.querySelector('[data-zc-commit]');
    var btn = form.querySelector('[data-zc-buy]');
    var btnPrice = form.querySelector('[data-zc-btnprice]');
    var sticky = document.querySelector('[data-zc-sticky]');

    function setImage(src) {
      if (!main || !src) return;
      main.style.opacity = 0.2;
      var img = new Image();
      img.onload = function () { main.src = src; main.style.opacity = 1; };
      img.onerror = function () { main.style.opacity = 1; };
      img.src = src;
    }

    function select(el) {
      offers.forEach(function (o) {
        var on = o === el;
        o.classList.toggle('is-on', on);
        var r = o.querySelector('input');
        if (r) r.checked = on;
      });
      idInput.value = el.getAttribute('data-variant');
      var price = parseInt(el.getAttribute('data-price'), 10);
      if (btnPrice) btnPrice.textContent = money(price);
      if (sticky) {
        var sp = sticky.querySelector('[data-zc-sticky-price]');
        if (sp) sp.textContent = money(price);
      }
      setImage(el.getAttribute('data-image'));
    }

    offers.forEach(function (o) {
      o.addEventListener('click', function () { select(o); });
    });

    thumbs.forEach(function (t) {
      t.addEventListener('click', function () {
        thumbs.forEach(function (x) { x.classList.toggle('is-on', x === t); });
        setImage(t.getAttribute('data-src'));
      });
    });

    function syncBtn() {
      if (!commit || !btn) return;
      btn.classList.toggle('zc-pulse', commit.checked);
    }
    if (commit) {
      commit.addEventListener('change', syncBtn);
      syncBtn();
    }

    form.addEventListener('submit', function (e) {
      if (commit && !commit.checked) {
        e.preventDefault();
        var box = commit.closest('.zc-commit');
        if (box) {
          box.classList.remove('is-missing');
          void box.offsetWidth;
          box.classList.add('is-missing');
          box.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }
    });

    if (sticky) {
      var target = btn || form;
      var io = new IntersectionObserver(function (entries) {
        sticky.classList.toggle('is-on', !entries[0].isIntersecting && entries[0].boundingClientRect.top < 0);
      });
      io.observe(target);
      var sbtn = sticky.querySelector('[data-zc-sticky-go]');
      if (sbtn) sbtn.addEventListener('click', function (e) {
        e.preventDefault();
        form.scrollIntoView({ behavior: 'smooth', block: 'center' });
      });
    }
  }

  function initReveal() {
    var els = document.querySelectorAll('.zc-reveal');
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (e) { e.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (e) { io.observe(e); });
  }

  function init() {
    document.querySelectorAll('[data-zc-product]').forEach(initProduct);
    initReveal();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
  document.addEventListener('shopify:section:load', init);
})();
