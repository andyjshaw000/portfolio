(function(){
  var nav = document.querySelector('nav.top');
  if (nav) addEventListener('scroll', function(){ nav.classList.toggle('scrolled', scrollY > 10); }, {passive:true});

  // reveal on scroll
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, {threshold:.08});
    document.querySelectorAll('.rv').forEach(function(el){ io.observe(el); });
  } else {
    document.querySelectorAll('.rv').forEach(function(el){ el.classList.add('in'); });
  }

  // image fallback
  document.querySelectorAll('img[data-wix]').forEach(function(img){
    function fail(){ var p = img.parentElement; if (p) p.classList.add('failed'); }
    img.addEventListener('error', fail);
    img.addEventListener('load', function(){ img.classList.add('ok'); });
    if (img.complete) { if (img.naturalWidth === 0) fail(); else img.classList.add('ok'); }
  });

  // project filters
  var fb = document.querySelectorAll('.filters button');
  fb.forEach(function(b){
    b.addEventListener('click', function(){
      fb.forEach(function(x){ x.classList.remove('on'); });
      b.classList.add('on');
      var f = b.dataset.f;
      document.querySelectorAll('.proj').forEach(function(p){
        p.classList.toggle('hide', f !== 'all' && p.dataset.c.split(' ').indexOf(f) < 0);
      });
    });
  });

  // sliders
  document.querySelectorAll('.slider').forEach(function(s){
    var track = s.querySelector('.track');
    var slides = s.querySelectorAll('.slide');
    var count = s.querySelector('.count');
    function idx(){ var w = slides[0].getBoundingClientRect().width + 16; return Math.round(track.scrollLeft / w); }
    function upd(){ if (count) count.textContent = (idx() + 1) + ' / ' + slides.length; }
    track.addEventListener('scroll', function(){ window.requestAnimationFrame(upd); }, {passive:true});
    s.querySelector('.pv').addEventListener('click', function(){ var w = slides[0].getBoundingClientRect().width + 16; track.scrollBy({left:-w, behavior:'smooth'}); });
    s.querySelector('.nx').addEventListener('click', function(){ var w = slides[0].getBoundingClientRect().width + 16; track.scrollBy({left:w, behavior:'smooth'}); });
    upd();
  });

  // lightbox
  var zoomables = Array.prototype.slice.call(document.querySelectorAll('[data-full]'));
  if (zoomables.length) {
    var lb = document.createElement('div');
    lb.className = 'lb';
    lb.innerHTML = '<img alt=""><div class="cap"></div><button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous">←</button><button class="nx" aria-label="Next">→</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.cap'), cur = 0;
    function show(i){
      cur = (i + zoomables.length) % zoomables.length;
      var el = zoomables[cur];
      lbImg.src = el.dataset.full;
      lbCap.textContent = el.dataset.cap || '';
      lb.classList.add('open');
    }
    function close(){ lb.classList.remove('open'); lbImg.src = ''; }
    zoomables.forEach(function(el, i){
      el.addEventListener('click', function(){ if (!el.classList.contains('failed')) show(i); });
    });
    lb.querySelector('.x').addEventListener('click', close);
    lb.querySelector('.pv').addEventListener('click', function(e){ e.stopPropagation(); show(cur - 1); });
    lb.querySelector('.nx').addEventListener('click', function(e){ e.stopPropagation(); show(cur + 1); });
    lb.addEventListener('click', function(e){ if (e.target === lb) close(); });
    document.addEventListener('keydown', function(e){
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(cur - 1);
      if (e.key === 'ArrowRight') show(cur + 1);
    });
  }

  // case study section nav highlight
  var tocLinks = document.querySelectorAll('.toc a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function(a){ map[a.getAttribute('href').slice(1)] = a; });
    var so = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (e.isIntersecting) {
          tocLinks.forEach(function(a){ a.classList.remove('on'); });
          var a = map[e.target.id]; if (a) a.classList.add('on');
        }
      });
    }, {rootMargin:'-40% 0px -55% 0px'});
    document.querySelectorAll('.cs-sec[id]').forEach(function(s){ so.observe(s); });
  }
})();

/* ================= v2: design lab, animations, UX ================= */
(function(){
  var root = document.documentElement;
  var LAB_ON = true; // set to false once a design is picked
  var FONTS = {
    midnight: 'family=Unbounded:wght@400;500;600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500',
    swiss: 'family=Inter+Tight:wght@500;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500',
    soft: 'family=Fraunces:opsz,wght@9..144,400;9..144,500&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500'
  };
  var THEMES = [
    {id:'editorial', name:'Warm Editorial', sw:['#F6F3EE','#1B1A17','#E2552B']},
    {id:'midnight', name:'Midnight Rave', sw:['#0E0C13','#FF5FA2','#9B6BF2']},
    {id:'swiss', name:'Swiss Grid', sw:['#FFFFFF','#0A0A0A','#1F4BFF']},
    {id:'soft', name:'Soft Product', sw:['#F6F4FF','#1E1B3A','#6C4CF5']}
  ];
  var ANIMS = [
    {id:'anim-hero', name:'Hero text reveal', d:'Headline words rise in one by one'},
    {id:'anim-count', name:'Counting numbers', d:'Stats count up when they scroll in'},
    {id:'anim-marquee', name:'Scrolling logo strip', d:'Companies glide across under the hero'},
    {id:'anim-tilt', name:'3D card tilt', d:'Project cards tilt toward your cursor'},
    {id:'anim-beads', name:'Kandi bead cursor', d:'Colored beads trail your mouse'}
  ];
  var DEFAULTS = {theme:'editorial', 'anim-hero':true, 'anim-count':true, 'anim-marquee':true, 'anim-tilt':false, 'anim-beads':false};
  var state = {};
  try { state = JSON.parse(localStorage.getItem('andy-lab') || '{}'); } catch(e) { state = {}; }
  for (var k in DEFAULTS) if (!(k in state)) state[k] = DEFAULTS[k];
  function save(){ try { localStorage.setItem('andy-lab', JSON.stringify(state)); } catch(e) {} }

  function loadFonts(t){
    if (!FONTS[t] || document.getElementById('font-' + t)) return;
    var l = document.createElement('link');
    l.id = 'font-' + t; l.rel = 'stylesheet';
    l.href = 'https://fonts.googleapis.com/css2?' + FONTS[t] + '&display=swap';
    document.head.appendChild(l);
  }
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function apply(){
    if (state.theme === 'editorial') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', state.theme);
    loadFonts(state.theme);
    ANIMS.forEach(function(a){ root.classList.toggle(a.id, !!state[a.id] && !reduce); });
  }
  apply();

  // hero words
  var h1 = document.querySelector('.hero h1');
  if (h1) {
    var i = 0;
    (function wrap(node){
      Array.prototype.slice.call(node.childNodes).forEach(function(n){
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function(part){
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var s = document.createElement('span'); s.className = 'w'; s.textContent = part;
            s.style.animationDelay = (0.08 * i++) + 's'; frag.appendChild(s);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) wrap(n);
      });
    })(h1);
  }

  // count up
  function countUp(el){
    if (!root.classList.contains('anim-count')) return;
    var target = +el.dataset.count, t0 = null, dur = 1400;
    function fmt(v){ return Math.round(v).toLocaleString('en-US') + '+'; }
    function step(ts){ if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / dur); el.textContent = fmt(target * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { countUp(e.target); co.unobserve(e.target); } }); }, {threshold:.6});
    document.querySelectorAll('[data-count]').forEach(function(el){ co.observe(el); });
  }

  // tilt
  document.querySelectorAll('.proj').forEach(function(c){
    c.addEventListener('mousemove', function(e){
      if (!root.classList.contains('anim-tilt')) return;
      var r = c.getBoundingClientRect();
      c.style.setProperty('--ry', ((e.clientX - r.left) / r.width - .5) * 8 + 'deg');
      c.style.setProperty('--rx', -((e.clientY - r.top) / r.height - .5) * 8 + 'deg');
    });
    c.addEventListener('mouseleave', function(){ c.style.removeProperty('--rx'); c.style.removeProperty('--ry'); });
  });

  // bead cursor
  var BEADS = ['#E2552B','#F2A541','#F5D547','#5BC0A8','#4F8EF7','#9B6BF2','#EF6FB4'], bi = 0, last = 0;
  document.addEventListener('mousemove', function(e){
    if (!root.classList.contains('anim-beads')) return;
    var now = Date.now(); if (now - last < 45) return; last = now;
    var b = document.createElement('div'); b.className = 'bead';
    b.style.left = e.clientX + 'px'; b.style.top = e.clientY + 'px'; b.style.background = BEADS[bi++ % BEADS.length];
    document.body.appendChild(b);
    requestAnimationFrame(function(){ b.style.opacity = '0'; b.style.transform = 'translate(-50%,-50%) translateY(14px) scale(.4)'; });
    setTimeout(function(){ b.remove(); }, 650);
  }, {passive:true});

  // reading progress + back to top
  var bar = document.querySelector('.progress');
  var top = document.createElement('button'); top.className = 'to-top'; top.setAttribute('aria-label','Back to top'); top.textContent = '↑';
  document.body.appendChild(top);
  top.addEventListener('click', function(){ scrollTo({top:0, behavior:'smooth'}); });
  addEventListener('scroll', function(){
    var h = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.width = (h > 0 ? scrollY / h * 100 : 0) + '%';
    top.classList.toggle('show', scrollY > 900);
  }, {passive:true});

  // lab panel
  if (!LAB_ON) return;
  var btn = document.createElement('button'); btn.className = 'lab-btn'; btn.textContent = '✦ Design lab';
  var panel = document.createElement('div'); panel.className = 'lab'; panel.setAttribute('role','dialog'); panel.setAttribute('aria-label','Design lab');
  var html = '<h6>Design system</h6><div class="themes">';
  THEMES.forEach(function(t){
    html += '<button data-t="' + t.id + '"><span class="sw">' + t.sw.map(function(c){ return '<i style="background:' + c + '"></i>'; }).join('') + '</span>' + t.name + '</button>';
  });
  html += '</div><h6>Animations</h6><div>';
  ANIMS.forEach(function(a){
    html += '<label><span>' + a.name + '<small>' + a.d + '</small></span><input type="checkbox" data-a="' + a.id + '"></label>';
  });
  html += '</div><div class="hint">Your picks carry across pages. Tell Claude which combo you want and the lab gets removed.</div>';
  panel.innerHTML = html;
  document.body.appendChild(panel); document.body.appendChild(btn);
  function sync(){
    panel.querySelectorAll('[data-t]').forEach(function(b){ b.classList.toggle('on', b.dataset.t === state.theme); });
    panel.querySelectorAll('[data-a]').forEach(function(c){ c.checked = !!state[c.dataset.a]; });
  }
  sync();
  btn.addEventListener('click', function(){ panel.classList.toggle('open'); });
  panel.addEventListener('click', function(e){
    var t = e.target.closest('[data-t]');
    if (t) { state.theme = t.dataset.t; save(); apply(); sync(); }
  });
  panel.addEventListener('change', function(e){
    var a = e.target.dataset.a; if (!a) return;
    state[a] = e.target.checked; save(); apply();
    if (a === 'anim-hero' && state[a]) { document.querySelectorAll('.hero h1 .w').forEach(function(w){ w.style.animation = 'none'; void w.offsetWidth; w.style.animation = ''; }); }
  });
})();
