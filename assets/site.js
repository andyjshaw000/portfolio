(function(){
  'use strict';
  var root = document.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;
  if (!reduce) root.classList.add('anim-hero', 'anim-count', 'anim-marquee', 'anim-tilt', 'anim-more');
  function onSeen(els, cb, opts){
    if (!hasIO) { els.forEach(cb); return; }
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { cb(e.target); io.unobserve(e.target); } }); }, opts || {threshold:.1});
    els.forEach(function(el){ io.observe(el); });
  }

  /* nav border on scroll, reading progress, back to top */
  var nav = document.querySelector('nav.top');
  var bar = document.querySelector('.progress');
  var top = document.createElement('button');
  top.className = 'to-top'; top.setAttribute('aria-label', 'Back to top'); top.textContent = '↑';
  document.body.appendChild(top);
  top.addEventListener('click', function(){ scrollTo({top:0, behavior: reduce ? 'auto' : 'smooth'}); });
  addEventListener('scroll', function(){
    if (nav) nav.classList.toggle('scrolled', scrollY > 10);
    var h = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.width = (h > 0 ? scrollY / h * 100 : 0) + '%';
    top.classList.toggle('show', scrollY > 900);
  }, {passive:true});

  /* scroll reveals and staggered groups */
  ['.grid .proj', '.numbers .num', '.xp > li', '.glance-g > div', '.skills > div', '.figs figure', '.did li'].forEach(function(sel){
    var parents = [], groups = [];
    document.querySelectorAll(sel).forEach(function(el){
      var i = parents.indexOf(el.parentElement);
      if (i < 0) { parents.push(el.parentElement); groups.push([]); i = parents.length - 1; }
      groups[i].push(el);
    });
    groups.forEach(function(g){ g.forEach(function(el, i){ el.classList.add('st'); el.style.setProperty('--d', (i % 6) * 0.07 + 's'); }); });
  });
  onSeen(document.querySelectorAll('.rv, .st, .label'), function(el){ el.classList.add('in'); }, {threshold:.08});

  /* image wipe: observe the unclipped parent, since a fully clipped element never reads as visible */
  var wipes = document.querySelectorAll('figure .ph, .cs-cover');
  wipes.forEach(function(el){ el.classList.add('wipe'); });
  if (hasIO) {
    var wo = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { e.target._wipe.classList.add('in'); wo.unobserve(e.target); } }); }, {threshold:.05});
    wipes.forEach(function(el){ var host = el.parentElement || el; host._wipe = el; wo.observe(host); });
  } else wipes.forEach(function(el){ el.classList.add('in'); });

  /* images: fade in on load, placeholder on failure */
  document.querySelectorAll('img[data-wix]').forEach(function(img){
    function fail(){ if (img.parentElement) img.parentElement.classList.add('failed'); }
    img.addEventListener('error', fail);
    img.addEventListener('load', function(){ img.classList.add('ok'); });
    if (img.complete) { if (img.naturalWidth === 0) fail(); else img.classList.add('ok'); }
  });

  /* hero words rise in */
  var h1 = document.querySelector('.hero h1');
  if (h1 && !reduce) {
    var n = 0;
    (function wrap(node){
      Array.prototype.slice.call(node.childNodes).forEach(function(c){
        if (c.nodeType === 3) {
          var frag = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(function(part){
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var s = document.createElement('span'); s.className = 'w'; s.textContent = part;
            s.style.animationDelay = (0.08 * n++) + 's'; frag.appendChild(s);
          });
          node.replaceChild(frag, c);
        } else if (c.nodeType === 1) wrap(c);
      });
    })(h1);
  }

  /* numbers count up */
  onSeen(document.querySelectorAll('[data-count]'), function(el){
    if (reduce) return;
    var target = +el.dataset.count, t0 = null, plus = /\+\s*$/.test(el.textContent) ? '+' : '';
    function step(ts){ if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / 1400); el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))).toLocaleString('en-US') + plus; if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }, {threshold:.6});

  /* card tilt and magnetic buttons */
  if (!reduce && matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.proj').forEach(function(c){
      c.addEventListener('mousemove', function(e){
        var r = c.getBoundingClientRect();
        c.style.setProperty('--ry', ((e.clientX - r.left) / r.width - .5) * 8 + 'deg');
        c.style.setProperty('--rx', -((e.clientY - r.top) / r.height - .5) * 8 + 'deg');
      });
      c.addEventListener('mouseleave', function(){ c.style.removeProperty('--rx'); c.style.removeProperty('--ry'); });
    });
    document.querySelectorAll('.btn, .nav-links .cta').forEach(function(b){
      b.addEventListener('mousemove', function(e){ var r = b.getBoundingClientRect(); b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * .18) + 'px,' + ((e.clientY - r.top - r.height / 2) * .25) + 'px)'; });
      b.addEventListener('mouseleave', function(){ b.style.transform = ''; });
    });
  }

  /* cover parallax */
  var cover = document.querySelector('.cs-cover img');
  if (cover && !reduce) addEventListener('scroll', function(){ cover.style.transform = 'scale(1.08) translateY(' + (Math.min(scrollY, 900) * 0.06) + 'px)'; }, {passive:true});

  /* page transitions */
  if (!reduce) {
    document.body.classList.add('page-in');
    document.querySelectorAll('a[href$=".html"], a[href*=".html#"]').forEach(function(a){
      if (a.target === '_blank') return;
      a.addEventListener('click', function(e){
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
        e.preventDefault(); document.body.classList.add('page-out');
        var href = a.getAttribute('href');
        setTimeout(function(){ location.href = href; }, 220);
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
      var f = b.dataset.f;
      document.querySelectorAll('.proj').forEach(function(p){ p.classList.toggle('hide', f !== 'all' && p.dataset.c.split(' ').indexOf(f) < 0); });
    });
  });

  /* sliders */
  document.querySelectorAll('.slider').forEach(function(s){
    var track = s.querySelector('.track'), slides = s.querySelectorAll('.slide'), count = s.querySelector('.count');
    function step(){ return slides[0].getBoundingClientRect().width + 16; }
    function upd(){ if (count) count.textContent = (Math.round(track.scrollLeft / step()) + 1) + ' / ' + slides.length; }
    track.addEventListener('scroll', function(){ requestAnimationFrame(upd); }, {passive:true});
    s.querySelector('.pv').addEventListener('click', function(){ track.scrollBy({left:-step(), behavior:'smooth'}); });
    s.querySelector('.nx').addEventListener('click', function(){ track.scrollBy({left:step(), behavior:'smooth'}); });
    upd();
  });

  /* lightbox: keyboard accessible, focus managed */
  var zoomables = Array.prototype.slice.call(document.querySelectorAll('[data-full]'));
  if (zoomables.length) {
    var lb = document.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Image viewer'); lb.tabIndex = -1;
    lb.innerHTML = '<img alt=""><div class="cap" aria-live="polite"></div><button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous image">←</button><button class="nx" aria-label="Next image">→</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.cap'), closeBtn = lb.querySelector('.x'), cur = 0, opener = null;
    function show(i){
      cur = (i + zoomables.length) % zoomables.length;
      var el = zoomables[cur];
      lbImg.src = el.dataset.full; lbImg.alt = el.dataset.cap || '';
      lbCap.textContent = el.dataset.cap || '';
      if (!lb.classList.contains('open')) { opener = document.activeElement; lb.classList.add('open'); document.body.style.overflow = 'hidden'; closeBtn.focus(); }
    }
    function close(){ lb.classList.remove('open'); lbImg.src = ''; document.body.style.overflow = ''; if (opener && opener.focus) opener.focus(); }
    zoomables.forEach(function(el, i){
      el.tabIndex = 0; el.setAttribute('role', 'button');
      el.setAttribute('aria-label', 'Enlarge image' + (el.dataset.cap ? ': ' + el.dataset.cap : ''));
      el.addEventListener('click', function(){ if (!el.classList.contains('failed')) show(i); });
      el.addEventListener('keydown', function(e){ if ((e.key === 'Enter' || e.key === ' ') && !el.classList.contains('failed')) { e.preventDefault(); show(i); } });
    });
    closeBtn.addEventListener('click', close);
    lb.querySelector('.pv').addEventListener('click', function(e){ e.stopPropagation(); show(cur - 1); });
    lb.querySelector('.nx').addEventListener('click', function(e){ e.stopPropagation(); show(cur + 1); });
    lb.addEventListener('click', function(e){ if (e.target === lb) close(); });
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
          a.scrollIntoView({block:'nearest', inline:'center'});
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

  /* mobile menu */
  var mb = document.querySelector('.menu-btn');
  if (mb && nav) {
    function setMenu(open){ nav.classList.toggle('menu-open', open); mb.setAttribute('aria-expanded', open); mb.setAttribute('aria-label', open ? 'Close menu' : 'Open menu'); }
    mb.addEventListener('click', function(){ setMenu(!nav.classList.contains('menu-open')); });
    nav.querySelectorAll('.nav-links a').forEach(function(a){ a.addEventListener('click', function(){ setMenu(false); }); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && nav.classList.contains('menu-open')) { setMenu(false); mb.focus(); } });
  }

  /* copy email */
  document.querySelectorAll('.copy-email').forEach(function(b){
    b.addEventListener('click', function(){
      var done = function(){ b.textContent = 'Copied'; setTimeout(function(){ b.textContent = 'Copy email'; }, 1800); };
      if (navigator.clipboard) navigator.clipboard.writeText(b.dataset.email).then(done, function(){ b.textContent = b.dataset.email; });
      else b.textContent = b.dataset.email;
    });
  });
})();
