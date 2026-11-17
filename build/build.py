import html, os, sys, hashlib
sys.path.insert(0, os.path.dirname(__file__))
from content import PROJECTS, ORDER, m, TLDR

OUT = os.environ.get("OUT_DIR") or os.path.join(os.path.dirname(__file__), "..")
SRC = os.path.join(os.path.dirname(__file__), "..")
BYSLUG = {p["slug"]: p for p in PROJECTS}
def _ver():
    h = hashlib.md5()
    for f in ("assets/site.css", "assets/site.js"):
        h.update(open(os.path.join(SRC, f), "rb").read())
    return h.hexdigest()[:8]
V = _ver()
LD = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Andy Shaw","url":"https://andyjshaw000.github.io/portfolio/","jobTitle":"UX Researcher","worksFor":{"@type":"Organization","name":"Meta Reality Labs"},"address":{"@type":"PostalAddress","addressLocality":"Seattle","addressRegion":"WA","addressCountry":"US"},"alumniOf":{"@type":"CollegeOrUniversity","name":"University of Washington"},"knowsAbout":["Product management","Program management","UX research","Usability testing","React Native","SwiftUI","Python","R","SQL"],"sameAs":["https://www.linkedin.com/in/andyjshaw000/","https://github.com/andyjshaw000","https://kndi.app"]}</script>'''

# Contact email comes from the environment so it isn't stored in this script.
# Build with: PORTFOLIO_EMAIL=you@example.com python3 build/build.py
EMAIL = os.environ.get("PORTFOLIO_EMAIL", "").strip()
if not EMAIL:
    sys.exit("Set PORTFOLIO_EMAIL to the contact address shown on the site, then rerun.")

def url(mid, w=1400, fill=None):
    """Wix image URL. GIFs are served as-is so they stay animated."""
    if mid.startswith("assets/"):
        return mid
    base = f"https://static.wixstatic.com/media/{mid}"
    if mid.endswith(".gif"):
        return base
    if fill:
        return f"{base}/v1/fill/w_{fill},h_{fill},al_c,q_85/{mid}"
    return f"{base}/v1/fit/w_{w},h_{w},q_85/{mid}"

def vid(src, cap=""):
    poster = src[:-4] + ".jpg"
    a = html.escape(cap, quote=True)
    return (f'<video data-vid src="{src}" poster="{poster}" muted loop playsinline preload="none" aria-label="{a}"></video>'), ""

def img(mid, alt="", w=1400, fill=None, lazy=True, zoom=True, cap=""):
    if mid.endswith(".mp4"):
        return vid(mid, cap or alt)
    a = html.escape(alt or cap or "", quote=True)
    z = f' data-full="{url(mid, 2400)}" data-cap="{html.escape(cap, quote=True)}"' if zoom else ""
    return (f'<img data-wix src="{url(mid, w, fill)}" alt="{a}"'
            ' decoding="async">'), z

HEAD = """<!DOCTYPE html>
<html lang="en" data-theme="swiss">
<head>
<meta charset="UTF-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;600;700&family=Inter:wght@400;500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={v}">
<link rel="canonical" href="{canon}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta name="theme-color" content="#FFFFFF">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Andy Shaw">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="https://andyjshaw000.github.io/portfolio/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def nav(home=True):
    pre = "" if home else "index.html"
    return f"""<nav class="top">
  <div class="wrap nav-in">
    <a href="{pre or '#top'}" class="logo">Andy Shaw<i></i></a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
    <ul class="nav-links">
      <li><a href="{pre}#kndi">kndi</a></li>
      <li><a href="{pre}#meta">Meta</a></li>
      <li><a href="{pre}#work">Projects</a></li>
      <li><a href="{pre}#experience">Experience</a></li>
      <li><a href="{pre}#about">About</a></li>
      <li><a href="assets/Andy_Shaw_Resume.pdf" target="_blank" rel="noopener">Resume</a></li>
      <li><a href="{pre}#contact" class="cta">Get in touch</a></li>
    </ul>
  </div>
</nav>
"""

CONTACT = """<section class="contact" id="contact">
  <div class="wrap">
    <div class="label"><em>06</em>Contact</div>
    <h2>Let's talk. <a href="mailto:__EMAIL__">__EMAIL__</a></h2>
    <button class="copy-email" data-email="__EMAIL__">Copy email</button>
    <div class="links">
      <a href="https://www.linkedin.com/in/andyjshaw000/" target="_blank" rel="noopener">LinkedIn ↗</a>
      <a href="https://github.com/andyjshaw000" target="_blank" rel="noopener">GitHub ↗</a>
      <a href="assets/Andy_Shaw_Resume.pdf" target="_blank" rel="noopener">Resume (PDF) ↗</a>
      <a href="https://kndi.app" target="_blank" rel="noopener">kndi.app ↗</a>
    </div>
  </div>
</section>
<footer><div class="wrap foot"><span>© 2026 Andy Shaw</span><span><a href="index.html#work">Projects</a><a href="kndi.html">kndi</a><a href="https://www.linkedin.com/in/andyjshaw000/" target="_blank" rel="noopener">LinkedIn</a><a href="#top" class="foot-top">Back to top ↑</a></span></div></footer>
<script src="assets/site.js?v=__V__"></script>
</body>
</html>
"""

def ar_style(ar):
    return f' style="--ar:{ar}"' if ar else ""

def block(b):
    t = b[0]
    if t == "p":
        return f"<p>{b[1]}</p>"
    if t in ("ul", "ol"):
        return f"<{t}>" + "".join(f"<li>{x}</li>" for x in b[1]) + f"</{t}>"
    if t == "fig":
        _, mid, cap = b
        tag, z = img(mid, cap=cap, w=1800)
        c = f"<figcaption>{cap}</figcaption>" if cap else ""
        return f'<figure><div class="ph{" is-vid" if mid.endswith(".mp4") else ""}"{z}>{tag}</div>{c}</figure>'
    if t == "figs":
        _, cols, items, cap, ar, contain = b
        cls = f"figs c{cols}" + (" contain" if contain else "") + (" phones" if ar == "9/19.5" else "")
        out = [f'<div class="{cls}">']
        for mid, c in items:
            tag, z = img(mid, cap=c or cap, w=1200)
            fc = f"<figcaption>{c}</figcaption>" if c else ""
            style = ar_style(ar) if cols > 1 else ' style="aspect-ratio:auto"'
            out.append(f'<figure><div class="ph"{style}{z}>{tag}</div>{fc}</figure>')
        out.append("</div>")
        if cap:
            out.append(f'<div class="figs-cap">{cap}</div>')
        return "".join(out)
    if t == "slider":
        _, ids, cap, ar = b
        slides = []
        for i, mid in enumerate(ids):
            tag, z = img(mid, cap=f"{cap} ({i+1} of {len(ids)})", w=1600)
            slides.append(f'<div class="slide"{ar_style(ar)}{z}>{tag}</div>')
        return (f'<div class="slider"><div class="track">{"".join(slides)}</div>'
                f'<div class="ctrl"><span class="count"></span><span class="figs-cap" style="margin:0">{cap}</span>'
                f'<span class="arrows"><button class="pv" aria-label="Previous">←</button><button class="nx" aria-label="Next">→</button></span></div></div>')
    raise ValueError(t)

def anchor(s):
    return "".join(ch if ch.isalnum() else "-" for ch in s.lower()).strip("-").replace("--", "-")

def case_page(p):
    i = ORDER.index(p["slug"])
    prev_p = BYSLUG[ORDER[i - 1]] if i > 0 else None
    next_p = BYSLUG[ORDER[i + 1]] if i < len(ORDER) - 1 else None
    facts = "".join(f"<div><b>{k}</b><span>{v}</span></div>" for k, v in p["facts"])
    t = TLDR[p["slug"]]
    words = sum(len(str(b[1]).split()) for _, bl in p["sections"] for b in bl if b[0] in ("p","ul","ol"))
    mins = max(2, round(words / 220))
    outcome = (f'<div class="glance"><div class="glance-h"><span>At a glance</span><span>{mins} min read</span></div>'
               f'<div class="glance-g"><div><b>Problem</b><p>{t[0]}</p></div><div><b>What I did</b><p>{t[1]}</p></div>'
               f'<div class="result"><b>Result</b><p>{t[2]}</p></div></div></div>')
    links = ""
    if p.get("links"):
        links = '<div class="btns" style="margin-top:28px">' + "".join(
            f'<a class="btn{" solid" if i == 0 else ""}" href="{u}" target="_blank" rel="noopener">{l} ↗</a>' for i, (l, u) in enumerate(p["links"])) + "</div>"
    cover_id = p.get("cover") or p["thumb"]
    ctag, cz = img(cover_id, alt=p["title"], w=2000, lazy=False, cap=p["title"])
    if p.get("strip"):
        cells = "".join(f'<div class="cs-strip-cell" data-full="{u}" data-cap="kndi on the App Store">' + img(u, alt="kndi App Store screenshot", zoom=False, lazy=False)[0] + '</div>' for u in p["strip"])
        cover_html = f'<div class="wrap"><div class="cs-strip">{cells}</div></div>'
    else:
        cover_html = f'<div class="wrap"><div class="cs-cover"><div class="ph"{cz} style="cursor:zoom-in">{ctag}</div></div></div>'
    toc = "".join(f'<a href="#{anchor(h)}">{h}</a>' for h, _ in p["sections"])
    secs = []
    for h, blocks in p["sections"]:
        body = "".join(block(b) for b in blocks)
        secs.append(f'<section class="cs-sec" id="{anchor(h)}"><div class="wrap narrow"><h2>{h}</h2>{body}</div></section>')
    nxt = ""
    if prev_p:
        nxt += f'<a href="{prev_p["slug"]}.html"><span>← Previous</span><b>{prev_p["title"]}</b></a>'
    else:
        nxt += '<a href="index.html#work"><span>← Back</span><b>All projects</b></a>'
    if next_p:
        nxt += f'<a class="r" href="{next_p["slug"]}.html"><span>Next →</span><b>{next_p["title"]}</b></a>'
    else:
        nxt += '<a class="r" href="index.html#work"><span>Back to</span><b>All projects</b></a>'
    return (HEAD.format(ld="", v=V, canon="https://andyjshaw000.github.io/portfolio/"+p["slug"]+".html", title=f'{p["title"]} | Andy Shaw', desc=html.escape(p["card"], quote=True)) + nav(False) +
f"""<div class="progress" aria-hidden="true"></div>
<header class="cs-hero wrap" id="top">
  <a class="back" href="index.html#work">← All projects</a>
  <div class="label">{p["where"]} · {p["kind"]}</div>
  <h1>{p["title"]}</h1>
  <p class="lede">{p["lede"]}</p>
  {links}
  <div class="facts">{facts}</div>
  {outcome}
</header>
{cover_html}
<nav class="toc"><div class="wrap">{toc}</div></nav>
<main id="main">{"".join(secs)}</main>
<div class="wrap"><div class="cs-next">{nxt}</div></div>
""" + CONTACT)

def card(p):
    n = [x for x in ORDER if x != "kndi"].index(p["slug"]) + 1
    tag, _ = img(p["thumb"], alt=p["title"], fill=800, zoom=False)
    imp = f'<div class="impact">{p["impact"]}</div>' if p.get("impact") else ""
    pills = "".join(f"<span>{x}</span>" for x in p["pills"])
    return f"""<a class="proj" data-c="{p['cat']}" href="{p['slug']}.html">
  <div class="thumb">{tag}<span class="idx">{n:02d}</span></div>
  <div class="body">
    <div class="where"><span>{p['where']}</span><span>{p['kind']}</span></div>
    <h3 class="proj-t">{p['title']}</h3>
    <p>{p['card']}</p>
    {imp}
    <div class="pills">{pills}</div>
    <div class="more">Read case study <span>→</span></div>
  </div>
</a>"""

def home():
    cards = "\n".join(card(BYSLUG[s]) for s in ORDER if s != "kndi")
    ptag, _ = img(m("56a508aabfa1400493a7a92ebbedee1b", "jpg"), alt="Andy Shaw", w=900, zoom=False)
    return (HEAD.format(ld=LD, v=V, canon="https://andyjshaw000.github.io/portfolio/", title="Andy Shaw | Product Manager and UX Researcher in Seattle",
                        desc="Andy Shaw leads UX research studies at Meta Reality Labs and co-founded kndi, a live iOS app. Open to Product Manager, Program Manager, and UX Researcher roles in Seattle or remote.")
            + nav(True) + f"""
<main id="main">
<header class="hero wrap" id="top">
 <div class="gridlines" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
 <div class="hero-grid">
 <div class="hero-main">
  <div class="status"><span class="dot"></span>Open to Product Manager, Program Manager, and UX Researcher roles.</div>
  <h1>I research how people use products, and I <em>build</em> them too.</h1>
  <p class="lede">I'm Andy. I run UX research studies at <strong>Meta Reality Labs</strong> for AR/VR and smart glasses, and on the side I'm the top contributor on <strong>kndi</strong>, a live iPhone app for planning festivals with friends. Now I want a role where I help decide what gets built, not just test it after.</p>
  <div class="btns hero-cta">
    <a class="btn solid" href="#work">See my work ↓</a>
    <a class="btn" href="assets/Andy_Shaw_Resume.pdf" target="_blank" rel="noopener">Resume (PDF) ↗</a>
    <a class="btn" href="https://www.linkedin.com/in/andyjshaw000/" target="_blank" rel="noopener">LinkedIn ↗</a>
  </div>
 </div>
 <aside class="quick" aria-label="Quick facts">
  <div class="quick-h"><span>Quick facts</span><span class="beads" aria-hidden="true"><span style="background:#E2552B"></span><span style="background:#F2A541"></span><span style="background:#F5D547"></span><span style="background:#5BC0A8"></span><span style="background:#4F8EF7"></span><span style="background:#9B6BF2"></span><span style="background:#EF6FB4"></span></span></div>
  <dl>
    <div><dt>Now</dt><dd>UX Research at Meta Reality Labs</dd></div>
    <div><dt>Shipped</dt><dd><a href="#kndi">kndi</a>, live on the App Store</dd></div>
    <div><dt>Track record</dt><dd>300+ experiments run at Meta. Gopuff research shipped.</dd></div>
    <div><dt>Looking for</dt><dd>Product, program, or UX research roles</dd></div>
    <div><dt>Based in</dt><dd>Seattle. Open to relocating or remote.</dd></div>
    <div><dt>Available</dt><dd>December 2026</dd></div>
    <div><dt>School</dt><dd>UW HCDE, Cum Laude, Math minor</dd></div>
  </dl>
 </aside>
 </div>
</header>
<section class="impact" aria-label="Highlights">
  <div class="wrap impact-g">
    <a href="#meta"><b>3,500+</b><span>survey responses collected across 13 research programs</span><i>Meta</i></a>
    <a href="#meta"><b>4 mo.</b><span>to owning my team's UX research work</span><i>Meta</i></a>
    <a href="kndi.html"><b>72%</b><span>of all commits on a live iOS app, as top contributor of 6</span><i>kndi</i></a>
    <a href="bundling.html"><b>2</b><span>research projects that shipped in the Gopuff app</span><i>Gopuff</i></a>
  </div>
</section>
<div class="strip" aria-label="Where I've worked and studied"><div class="strip-track">
  <span>Meta Reality Labs</span><i></i><span>Gopuff</span><i></i><span>User Research International</span><i></i><span>KUOW Public Radio</span><i></i><span>University of Washington</span><i></i><span>kndi</span><i></i>
  <span aria-hidden="true">Meta Reality Labs</span><i></i><span aria-hidden="true">Gopuff</span><i></i><span aria-hidden="true">User Research International</span><i></i><span aria-hidden="true">KUOW Public Radio</span><i></i><span aria-hidden="true">University of Washington</span><i></i><span aria-hidden="true">kndi</span><i></i>
</div></div>

<section id="kndi">
  <div class="wrap">
    <div class="label"><em>01</em>Featured project</div>
    <h2>From a group chat problem to a live app on the App Store.</h2>
    <div class="feature">
      <div class="feature-copy">
        <span class="tag">Side project · iOS · Live</span>
        <h3>kndi</h3>
        <div class="sub">Plan festivals with your friends.</div>
        <p>Planning a festival with a group usually means a messy group chat, five screenshots of the set times, and nobody knowing where to meet. kndi puts all of that in one place. Every event gets a group with chat, polls, a shared schedule, and an album, and you get a heads up when two sets you picked overlap.</p>
        <p>It also brings kandi trading into the app. You design digital beads and trade them by scanning each other's codes in person. The goal was never to replace the real thing. It's a way to keep the memory of who you met.</p>
        <ul class="did">
          <li><b>Product</b><span>Decide what to build and what to cut. A cohort study of 251 signups showed new users who join a group on day one come back at 44% vs 15%, so onboarding now leads with groups.</span></li>
          <li><b>Build</b><span>Top contributor on a team of six: 72% of commits across the SwiftUI app and its React Native rebuild, including chat, the design system, kandi, and push.</span></li>
          <li><b>Launch</b><span>Led App Store submission, including the moderation policy and DMCA registration.</span></li>
        </ul>
        <div class="stats">
          <div class="stat"><b>4.9</b><span>App Store rating</span></div>
          <div class="stat"><b>~560</b><span>users</span></div>
          <div class="stat"><b>5,491</b><span>commits by me</span></div>
        </div>
        <div class="btns">
          <a class="btn solid" href="kndi.html">Read the case study →</a>
          <a class="btn" href="https://apps.apple.com/app/kndi/id6762342337" target="_blank" rel="noopener">App Store ↗</a>
          <a class="btn" href="https://kndi.app" target="_blank" rel="noopener">kndi.app ↗</a>
        </div>
      </div>
      <div class="feature-art" aria-hidden="true">
        <div class="phone real"><img src="assets/kndi/home.jpg" alt="kndi home screen"></div><div class="phone real back"><img src="assets/kndi/designer.jpg" alt=""></div>
      </div>
    </div>
  </div>
</section>

<section id="meta">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="label"><em>02</em>Current role</div>
        <h2 style="margin-bottom:28px">Leading research for AR/VR and smart glasses.</h2>
        <div class="meta-side">
          <b>Meta Reality Labs</b>
          Human Subjects Research Assistant II<br>
          (UX research)<br>
          May 2024 to now<br>
          Redmond, via H10
        </div>
      </div>
      <div class="prose">
        <p>I joined Meta to support research studies. Within four months, I took ownership of my team's UX research work instead of rotating across teams.</p>
        <p>I run studies end to end: writing the procedures, building screeners and surveys in Qualtrics, recruiting through Prolific or our internal pool, running sessions in the lab, and doing the first round of analysis in R and Python. That work goes straight to the research scientists who use it to shape product proposals for AR/VR and smart glasses.</p>
        <p>I care a lot about data you can trust. I build headphone screeners, catch trials, and hidden references into studies, which in one case narrowed 146 recruits to 98 reliable participants. I use the standard methods from audio research, like MUSHRA listening tests, MaxDiff, and paired comparisons, and I've run sessions in 8+ labs, including an anechoic chamber, plus people's homes and live cafeterias.</p>
        <p>I also own the team's documentation. I wrote 101 of the wiki's 113 revisions, consolidated 40+ documents into 10 role-based categories, and built a training curriculum so our panel studies no longer depend on one person.</p>
        <p class="note">Most of this work is under NDA, so I keep it high level here. I'm happy to walk through how I run a study when we talk.</p>
      </div>
    </div>
    <div class="numbers">
      <div class="num"><b>300+</b><span>auditory perception experiments run</span></div>
      <div class="num"><b>90</b><span>surveys built, collecting 3,500+ responses</span></div>
      <div class="num"><b>8</b><span>research reports I contributed to, one shaping a Meta AI app onboarding flow</span></div>
      <div class="num"><b>101</b><span>of the team wiki's 113 revisions written by me</span></div>
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <div class="label"><em>03</em>Case studies</div>
    <h2>Research, design, and code from Gopuff and UW.</h2>
    <div class="filters" role="group" aria-label="Filter projects">
      <button class="on" data-f="all">All</button>
      <button data-f="research">Research</button>
      <button data-f="design">Design</button>
      <button data-f="code">Code</button>
    </div>
    <div class="grid">
{cards}
    </div>
  </div>
</section>

<section id="experience">
  <div class="wrap">
    <div class="label"><em>04</em>Experience</div>
    <h2>About three years in UX research.</h2>
    <ul class="xp">
      <li><span class="when">May 2024 to now</span><div>
        <div class="role">Human Subjects Research Assistant II (UX research)</div>
        <div class="org">Meta Reality Labs, Redmond (contract via H10)</div>
        <ul>
          <li>Took ownership of my team's UX research work within four months, running studies from pilot to readout.</li>
          <li>Ran 300+ audio perception experiments and built 90 surveys that collected 3,500+ responses.</li>
          <li>Contributed to 8 research reports, including one that shaped an onboarding flow in the Meta AI app for smart glasses.</li>
          <li>Narrowed 146 recruits to 98 reliable participants with headphone screeners, catch trials, and hidden references.</li>
          <li>Built a training curriculum so panel studies no longer depend on one person, and wrote 101 of 113 wiki revisions.</li>
        </ul></div></li>
      <li><span class="when">Apr 2026 to now</span><div>
        <div class="role">Top contributor</div>
        <div class="org">kndi, iOS app (volunteer team of 6)</div>
        <ul>
          <li>Found in a cohort study of 251 signups that new users who join a group on day 0 come back in week 1 at 44% vs 15%, and reshaped onboarding around it.</li>
          <li>Grew the app to about 560 users while writing 72% of all commits (5,491 of 7,643) across the SwiftUI app and its React Native rebuild.</li>
          <li>Prioritized and fixed 172 of 214 issues from a full-stack audit, and led App Store submission.</li>
        </ul></div></li>
      <li><span class="when">Nov 2023 to May 2024</span><div>
        <div class="role">UX Moderator</div>
        <div class="org">User Research International, Redmond</div>
        <ul>
          <li>Led 80+ in-person usability tests, interviews, and benchmarks on consumer electronics hardware.</li>
          <li>Helped write client reports with trends, insights, and recommendations.</li>
        </ul></div></li>
      <li><span class="when">Jun 2022 to Aug 2022</span><div>
        <div class="role">UX Researcher Intern</div>
        <div class="org">Gopuff, remote</div>
        <ul>
          <li>Led discovery research on Save For Later, which the team projected at about $16M in annual revenue.</li>
          <li>Produced 40+ recommendations. Bundling and product page work shipped.</li>
        </ul></div></li>
      <li><span class="when">2019 to 2023</span><div>
        <div class="role">B.S. Human Centered Design &amp; Engineering, Cum Laude</div>
        <div class="org">University of Washington. HCI option, Mathematics minor</div>
      </div></li>
    </ul>
  </div>
</section>

<section id="about">
  <div class="wrap about-grid">
    <div class="portrait">{ptag}</div>
    <div>
      <div class="label"><em>05</em>About</div>
      <h2 style="margin-bottom:28px">The planner of the group.</h2>
      <div class="prose">
        <p>I grew up in the Seattle area and studied HCDE at UW. In every group I'm in, I end up being the one who plans things and keeps everyone moving. I also work better when people are counting on me. That's a big part of why I'm moving toward product and program management.</p>
        <p>Research taught me to ask why before jumping to a fix. Building kndi taught me what comes after that: picking what to ship, cutting what doesn't matter, and seeing whether real people actually use it.</p>
        <p>Outside of work I run a weekly D&amp;D campaign as the Dungeon Master, go to a lot of EDM shows (which is where kndi came from), and play more League than I should.</p>
      </div>
      <div class="skills">
        <div><h3 class="sk">Research</h3><p>Study design, interviews, usability tests, concept tests, surveys, heuristic evaluation, competitive analysis, personas</p></div>
        <div><h3 class="sk">Data and code</h3><p>R, Python, SQL, JavaScript, Java, HTML/CSS, Git</p></div>
        <div><h3 class="sk">Design</h3><p>Figma, Miro, wireframes, user flows, prototyping, Illustrator, Photoshop</p></div>
        <div><h3 class="sk">Project management</h3><p>Research planning, prioritization, team training, documentation, shipping an app end to end</p></div>
      </div>
    </div>
  </div>
</section>
</main>
""" + CONTACT)

def main():
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(home().replace("__V__", V).replace("__EMAIL__", EMAIL))
    for p in PROJECTS:
        with open(os.path.join(OUT, f"{p['slug']}.html"), "w") as f:
            f.write(case_page(p).replace("__V__", V).replace("__EMAIL__", EMAIL))
    SITE = "https://andyjshaw000.github.io/portfolio/"
    nf = (HEAD.format(ld="", v=V, canon=SITE, title="Page not found | Andy Shaw", desc="This page doesn't exist.").replace("<head>", '<head>\n<base href="/portfolio/">', 1)
          + nav(False) + """<main id="main"><header class="cs-hero wrap" id="top" style="min-height:60vh">
  <div class="label"><em>404</em>Page not found</div>
  <h1>That page doesn't exist.</h1>
  <p class="lede">The link might be old, or the page moved when this site replaced the Wix one.</p>
  <div class="btns" style="margin-top:28px"><a class="btn solid" href="index.html">Go to the home page</a><a class="btn" href="index.html#work">See case studies</a></div>
</header></main>
""" + CONTACT).replace("__V__", V).replace("__EMAIL__", EMAIL)
    with open(os.path.join(OUT, "404.html"), "w") as f:
        f.write(nf)
    urls = [SITE] + [SITE + p["slug"] + ".html" for p in PROJECTS]
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    print("built", 1 + len(PROJECTS), "pages + 404, sitemap, robots")

if __name__ == "__main__":
    main()
