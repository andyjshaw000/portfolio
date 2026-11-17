(function(){
  'use strict';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  /* nav border on scroll, reading progress, back to top */
  var nav = document.querySelector('nav.top');
  var bar = document.querySelector('.progress');
  var top = document.createElement('button');
  top.className = 'to-top'; top.setAttribute('aria-label', 'Back to top');
  top.innerHTML = '<svg viewBox="0 0 44 44" aria-hidden="true"><rect x="1" y="1" width="42" height="42" pathLength="100"/></svg><span>↑</span>';
  var ring = top.querySelector('rect');
  document.body.appendChild(top);
  top.addEventListener('click', function(){ scrollTo({top:0, behavior: reduce ? 'auto' : 'smooth'}); });
  var ticking = false;
  function onScroll(){
    ticking = false;
    if (nav) nav.classList.toggle('scrolled', scrollY > 10);
    var h = document.documentElement.scrollHeight - innerHeight;
    var pct = h > 0 ? scrollY / h * 100 : 0;
    if (bar) bar.style.width = pct + '%';
    ring.style.strokeDashoffset = 100 - pct;
    top.classList.toggle('show', scrollY > 900);
  }
  addEventListener('scroll', function(){ if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, {passive:true});
  onScroll();

  /* mixed-size image grids: lay out as justified rows */
  var justGrids = Array.prototype.slice.call(document.querySelectorAll('.figs.contain'));
  function justify(g){
    var figs = Array.prototype.slice.call(g.querySelectorAll(':scope > figure'));
    if (innerWidth < 640 || figs.length < 2) {
      g.classList.remove('just'); figs.forEach(function(f){ f.style.width = ''; }); return;
    }
    var gap = 20, W = g.clientWidth, target = Math.max(220, Math.min(380, W * .34)), row = [], sum = 0;
    function ar(f){ var im = f.querySelector('img'); return im && im.naturalWidth ? im.naturalWidth / im.naturalHeight : 4 / 3; }
    function place(items, total, last){
      var h = (W - gap * (items.length - 1)) / total;
      if (last && h > target * 1.25) h = target * 1.25;
      items.forEach(function(f){ f.style.width = Math.floor(ar(f) * h) + 'px'; });
    }
    figs.forEach(function(f){
      row.push(f); sum += ar(f);
      if ((W - gap * (row.length - 1)) / sum <= target) { place(row, sum, false); row = []; sum = 0; }
    });
    if (row.length) place(row, sum, true);
    g.classList.add('just');
  }
  justGrids.forEach(function(g){
    g.querySelectorAll('img').forEach(function(im){ if (!im.complete) im.addEventListener('load', function(){ justify(g); }); });
    justify(g);
  });
  var jt = null;
  addEventListener('resize', function(){ clearTimeout(jt); jt = setTimeout(function(){ justGrids.forEach(justify); }, 120); });

  /* images: show a placeholder if one fails to load */
  document.querySelectorAll('img[data-wix]').forEach(function(img){
    function fail(){ if (img.parentElement) img.parentElement.classList.add('failed'); }
    img.addEventListener('error', fail);
    if (img.complete && img.naturalWidth === 0) fail();
  });

  /* page transitions: a quick fade out on internal links */
  if (!reduce) {
    document.querySelectorAll('a[href$=".html"], a[href*=".html#"]').forEach(function(a){
      if (a.target === '_blank') return;
      a.addEventListener('click', function(e){
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
        e.preventDefault(); document.body.classList.add('page-out');
        var href = a.getAttribute('href');
        setTimeout(function(){ location.href = href; }, 180);
      });
    });
    addEventListener('pageshow', function(ev){ if (ev.persisted) document.body.classList.remove('page-out'); });
  }

  /* project filters */
  var fb = document.querySelectorAll('.filters button');
  fb.forEach(function(b){
    b.setAttribute('aria-pressed', b.classList.contains('on'));
    b.addEventListener('click', function(){
      fb.forEach(function(x){ x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); });
      b.classList.add('on'); b.setAttribute('aria-pressed', 'true');
      var f = b.dataset.f, cards = Array.prototype.slice.call(document.querySelectorAll('.proj'));
      var before = new Map();
      cards.forEach(function(p){ if (!p.classList.contains('hide')) before.set(p, p.getBoundingClientRect()); });
      cards.forEach(function(p){
        var hide = f !== 'all' && p.dataset.c.split(' ').indexOf(f) < 0;
        p.classList.toggle('hide', hide);
      });
      if (reduce) return;
      cards.forEach(function(p){
        if (p.classList.contains('hide')) return;
        var a = before.get(p), r = p.getBoundingClientRect();
        if (a) {
          var dx = a.left - r.left, dy = a.top - r.top;
          if (dx || dy) p.animate([{transform:'translate(' + dx + 'px,' + dy + 'px)'}, {transform:'none'}], {duration:380, easing:'cubic-bezier(.2,.7,.2,1)'});
        } else {
          p.animate([{opacity:0, transform:'scale(.96)'}, {opacity:1, transform:'none'}], {duration:300, easing:'cubic-bezier(.2,.7,.2,1)'});
        }
      });
    });
  });

  /* sliders */
  document.querySelectorAll('.slider').forEach(function(s){
    var track = s.querySelector('.track'), slides = s.querySelectorAll('.slide'), count = s.querySelector('.count');
    var pv = s.querySelector('.pv'), nx = s.querySelector('.nx');
    function step(){ return slides[0].getBoundingClientRect().width + 16; }
    var prog = document.createElement('div'); prog.className = 'slider-prog'; prog.innerHTML = '<i></i>';
    track.after(prog); var progBar = prog.firstChild;
    function upd(){
      var max = track.scrollWidth - track.clientWidth;
      progBar.style.transform = 'scaleX(' + (max > 0 ? Math.max(.06, track.scrollLeft / max) : 1) + ')';
      var i = Math.round(track.scrollLeft / step());
      if (count) count.textContent = (i + 1) + ' / ' + slides.length;
      pv.disabled = track.scrollLeft < 4;
      nx.disabled = track.scrollLeft > track.scrollWidth - track.clientWidth - 4;
    }
    track.addEventListener('scroll', function(){ requestAnimationFrame(upd); }, {passive:true});
    pv.addEventListener('click', function(){ track.scrollBy({left:-step(), behavior: reduce ? 'auto' : 'smooth'}); });
    nx.addEventListener('click', function(){ track.scrollBy({left:step(), behavior: reduce ? 'auto' : 'smooth'}); });
    upd();
  });

  /* lightbox: keyboard accessible, focus managed, never moves the page */
  var zoomables = Array.prototype.slice.call(document.querySelectorAll('[data-full]'));
  if (zoomables.length) {
    var lb = document.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Image viewer'); lb.tabIndex = -1;
    lb.innerHTML = '<img alt=""><div class="count" aria-hidden="true"></div><div class="cap" aria-live="polite"></div><button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous image">←</button><button class="nx" aria-label="Next image">→</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.cap'), lbCount = lb.querySelector('.count'), closeBtn = lb.querySelector('.x'), cur = 0, opener = null, savedY = 0;
    function thumbRect(el){ var im = el.querySelector('img') || el; return im.getBoundingClientRect(); }
    function zoomFrom(el, reverse){
      // FLIP: animate the big image from where the thumbnail sits on the page.
      if (reduce || !lbImg.animate) return null;
      var a = thumbRect(el), b = lbImg.getBoundingClientRect();
      if (!a.width || !b.width) return null;
      var t = 'translate(' + (a.left + a.width / 2 - b.left - b.width / 2) + 'px,' + (a.top + a.height / 2 - b.top - b.height / 2) + 'px) scale(' + Math.min(a.width / b.width, a.height / b.height) + ')';
      var frames = [{transform:t, opacity:.6}, {transform:'none', opacity:1}];
      return lbImg.animate(reverse ? frames.reverse() : frames, {duration: reverse ? 220 : 320, easing:'cubic-bezier(.2,.7,.2,1)', fill:'both'});
    }
    function show(i){
      var step = i - cur, wasOpen = lb.classList.contains('open');
      cur = (i + zoomables.length) % zoomables.length;
      var el = zoomables[cur];
      lbImg.src = el.dataset.full; lbImg.alt = el.dataset.cap || '';
      if (wasOpen && !reduce && lbImg.animate) lbImg.animate([{opacity:0, transform:'translateX(' + (step > 0 ? 40 : -40) + 'px)'}, {opacity:1, transform:'none'}], {duration:240, easing:'cubic-bezier(.2,.7,.2,1)'});
      lbCap.textContent = el.dataset.cap || '';
      lbCount.textContent = (cur + 1) + ' / ' + zoomables.length;
      if (!lb.classList.contains('open')) {
        opener = document.activeElement; savedY = scrollY;
        lb.classList.add('open');
        document.documentElement.style.overflow = 'hidden';
        closeBtn.focus({preventScroll:true});
        var go = function(){ zoomFrom(el, false); };
        if (lbImg.complete && lbImg.naturalWidth) go(); else lbImg.addEventListener('load', go, {once:true});
      }
    }
    function close(){
      var anim = lb.classList.contains('open') ? zoomFrom(zoomables[cur], true) : null;
      if (anim) { anim.onfinish = function(){ anim.cancel(); }; }
      lb.classList.remove('open');
      document.documentElement.style.overflow = '';
      if (scrollY !== savedY) scrollTo(0, savedY);
      if (opener && opener.focus) opener.focus({preventScroll:true});
      setTimeout(function(){ if (!lb.classList.contains('open')) lbImg.removeAttribute('src'); }, 250);
    }
    zoomables.forEach(function(el, i){
      el.tabIndex = 0; el.setAttribute('role', 'button');
      el.setAttribute('aria-label', 'Enlarge image' + (el.dataset.cap ? ': ' + el.dataset.cap : ''));
      el.addEventListener('click', function(e){ e.preventDefault(); if (!el.classList.contains('failed')) show(i); });
      el.addEventListener('keydown', function(e){ if ((e.key === 'Enter' || e.key === ' ') && !el.classList.contains('failed')) { e.preventDefault(); show(i); } });
    });
    closeBtn.addEventListener('click', close);
    lb.querySelector('.pv').addEventListener('click', function(e){ e.stopPropagation(); show(cur - 1); });
    lb.querySelector('.nx').addEventListener('click', function(e){ e.stopPropagation(); show(cur + 1); });
    lb.addEventListener('click', function(e){ if (e.target === lb || e.target === lbImg) close(); });
    var tx = null;
    lb.addEventListener('touchstart', function(e){ tx = e.touches[0].clientX; }, {passive:true});
    lb.addEventListener('touchend', function(e){ if (tx === null) return; var dx = e.changedTouches[0].clientX - tx; if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1)); tx = null; });
    document.addEventListener('keydown', function(e){
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(cur - 1);
      else if (e.key === 'ArrowRight') show(cur + 1);
      else if (e.key === 'Tab') {
        var f = lb.querySelectorAll('button'), first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* videos: play only while visible */
  var vids = document.querySelectorAll('video[data-vid]');
  if (vids.length) {
    if (reduce || !hasIO) vids.forEach(function(v){ v.controls = true; v.preload = 'metadata'; });
    else {
      var vo = new IntersectionObserver(function(es){
        es.forEach(function(e){
          var v = e.target._v;
          if (e.isIntersecting) { v.preload = 'auto'; var p = v.play(); if (p && p.catch) p.catch(function(){ v.controls = true; }); }
          else v.pause();
        });
      }, {threshold:.25});
      vids.forEach(function(v){ var host = v.closest('.ph, .cs-cover') || v; host = host.parentElement || host; host._v = v; vo.observe(host); });
    }
  }

  /* case study section nav */
  var tocLinks = document.querySelectorAll('.toc a');
  if (tocLinks.length && hasIO) {
    var map = {};
    tocLinks.forEach(function(a){ map[a.getAttribute('href').slice(1)] = a; });
    var so = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (e.isIntersecting && map[e.target.id]) {
          tocLinks.forEach(function(a){ a.classList.remove('on'); a.removeAttribute('aria-current'); });
          var a = map[e.target.id]; a.classList.add('on'); a.setAttribute('aria-current', 'true');
          var row = a.parentElement;
          row.scrollTo({left: a.offsetLeft - row.clientWidth / 2 + a.clientWidth / 2, behavior: reduce ? 'auto' : 'smooth'});
        }
      });
    }, {rootMargin:'-40% 0px -55% 0px'});
    document.querySelectorAll('.cs-sec[id]').forEach(function(s){ so.observe(s); });
  }

  /* home nav scrollspy */
  var links = document.querySelectorAll('.nav-links a[href^="#"]');
  if (links.length && hasIO) {
    var lm = {}; links.forEach(function(a){ lm[a.getAttribute('href').slice(1)] = a; });
    var spy = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting && lm[e.target.id]) { links.forEach(function(a){ a.classList.remove('on'); }); lm[e.target.id].classList.add('on'); } });
    }, {rootMargin:'-45% 0px -50% 0px'});
    Object.keys(lm).forEach(function(id){ var el = document.getElementById(id); if (el) spy.observe(el); });
  }

  /* a single underline that slides to the active link */
  function slider(row, sel){
    if (!row) return null;
    var ind = document.createElement('span'); ind.className = 'ind'; ind.setAttribute('aria-hidden', 'true');
    row.appendChild(ind);
    return function(){
      var a = row.querySelector(sel);
      if (!a || !a.offsetWidth) { ind.style.opacity = 0; return; }
      ind.style.opacity = 1;
      ind.style.width = a.offsetWidth + 'px';
      ind.style.transform = 'translateX(' + (a.offsetLeft) + 'px)';
    };
  }
  var navInd = slider(document.querySelector('.nav-links'), 'a.on');
  var tocInd = slider(document.querySelector('.toc .wrap'), 'a.on');
  if (navInd || tocInd) {
    new MutationObserver(function(){ if (navInd) navInd(); if (tocInd) tocInd(); })
      .observe(document.body, {subtree:true, attributes:true, attributeFilter:['class']});
    addEventListener('resize', function(){ if (navInd) navInd(); if (tocInd) tocInd(); });
  }

  /* arrows in buttons and links nudge on hover */
  document.querySelectorAll('.btn, .links a').forEach(function(a){
    a.innerHTML = a.innerHTML.replace(/\s?(→|↗)\s*$/, ' <span class="arr" aria-hidden="true">$1</span>');
  });

  /* impact numbers count up once, the first time they're on screen */
  if (!reduce && hasIO) {
    var nums = document.querySelectorAll('.impact-g b, .numbers .num b, .stat b');
    var co = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (!e.isIntersecting) return;
        co.unobserve(e.target);
        var el = e.target, txt = el.textContent, m = txt.match(/^([^0-9]*)([0-9][0-9,]*\.?[0-9]*)(.*)$/);
        if (!m) return;
        var end = parseFloat(m[2].replace(/,/g, '')), dec = (m[2].split('.')[1] || '').length, t0 = null;
        el.style.minWidth = el.offsetWidth + 'px';
        function tick(t){
          if (!t0) t0 = t;
          var k = Math.min(1, (t - t0) / 900), v = end * (1 - Math.pow(1 - k, 3));
          el.textContent = m[1] + v.toLocaleString('en-US', {minimumFractionDigits:dec, maximumFractionDigits:dec}) + m[3];
          if (k < 1) requestAnimationFrame(tick); else el.textContent = txt;
        }
        requestAnimationFrame(tick);
      });
    }, {threshold:.6});
    nums.forEach(function(n){ co.observe(n); });
  }

  /* mobile menu */
  var mb = document.querySelector('.menu-btn');
  if (mb && nav) {
    var setMenu = function(open){ nav.classList.toggle('menu-open', open); mb.setAttribute('aria-expanded', open); mb.setAttribute('aria-label', open ? 'Close menu' : 'Open menu'); };
    mb.addEventListener('click', function(){ setMenu(!nav.classList.contains('menu-open')); });
    nav.querySelectorAll('.nav-links a').forEach(function(a){ a.addEventListener('click', function(){ setMenu(false); }); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && nav.classList.contains('menu-open')) { setMenu(false); mb.focus(); } });
    document.addEventListener('click', function(e){ if (nav.classList.contains('menu-open') && !nav.contains(e.target)) setMenu(false); });
  }

  /* toast */
  var toastEl = null, toastT = null;
  function toast(msg){
    if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'toast'; toastEl.setAttribute('role', 'status'); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add('show');
    clearTimeout(toastT); toastT = setTimeout(function(){ toastEl.classList.remove('show'); }, 2200);
  }

  /* copy email */
  document.querySelectorAll('.copy-email').forEach(function(b){
    b.addEventListener('click', function(){
      var done = function(){
        b.textContent = 'Copied ✓'; b.classList.add('done'); toast('Email copied to your clipboard');
        setTimeout(function(){ b.textContent = 'Copy email'; b.classList.remove('done'); }, 1800);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(b.dataset.email).then(done, function(){ b.textContent = b.dataset.email; });
      else b.textContent = b.dataset.email;
    });
  });
})();
