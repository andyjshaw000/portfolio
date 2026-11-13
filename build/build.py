import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import PROJECTS, ORDER, m, TLDR

OUT = os.path.join(os.path.dirname(__file__), "..")
BYSLUG = {p["slug"]: p for p in PROJECTS}

def url(mid, w=1400, fill=None):
    """Wix image URL. GIFs are served as-is so they stay animated."""
    base = f"https://static.wixstatic.com/media/{mid}"
    if mid.endswith(".gif"):
        return base
    if fill:
        return f"{base}/v1/fill/w_{fill},h_{fill},al_c,q_85/{mid}"
    return f"{base}/v1/fit/w_{w},h_{w},q_85/{mid}"

def img(mid, alt="", w=1400, fill=None, lazy=True, zoom=True, cap=""):
    a = html.escape(alt or cap or "", quote=True)
    z = f' data-full="{url(mid, 2400)}" data-cap="{html.escape(cap, quote=True)}"' if zoom else ""
    return (f'<img data-wix src="{url(mid, w, fill)}" alt="{a}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async">'), z

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def nav(home=True):
    pre = "" if home else "index.html"
    return f"""<nav class="top">
  <div class="wrap nav-in">
    <a href="{pre or '#top'}" class="logo">Andy Shaw</a>
    <ul class="nav-links">
      <li><a href="{pre}#kndi">kndi</a></li>
      <li><a href="{pre}#meta">Meta</a></li>
      <li><a href="{pre}#work">Projects</a></li>
      <li><a href="{pre}#experience">Experience</a></li>
      <li><a href="{pre}#about">About</a></li>
      <li><a href="https://79f8e248-ca0f-4fcf-af31-76ef78ef797a.usrfiles.com/ugd/041fc2_833aa57dec1d47d5a1edbb8de85f2121.pdf" target="_blank" rel="noopener">Resume</a></li>
      <li><a href="{pre}#contact" class="cta">Get in touch</a></li>
    </ul>
  </div>
</nav>
"""

CONTACT = """<section class="contact" id="contact">
  <div class="wrap">
    <div class="label">Contact</div>
    <h2>Let's talk. <a href="mailto:andyjshaw000@gmail.com">andyjshaw000@gmail.com</a></h2>
    <div class="links">
      <a href="https://www.linkedin.com/in/andyjshaw000/" target="_blank" rel="noopener">LinkedIn ↗</a>
      <a href="https://github.com/andyjshaw000" target="_blank" rel="noopener">GitHub ↗</a>
      <a href="https://79f8e248-ca0f-4fcf-af31-76ef78ef797a.usrfiles.com/ugd/041fc2_833aa57dec1d47d5a1edbb8de85f2121.pdf" target="_blank" rel="noopener">Resume (PDF) ↗</a>
      <a href="https://kndi.app" target="_blank" rel="noopener">kndi.app ↗</a>
    </div>
  </div>
</section>
<footer><div class="wrap">© 2026 Andy Shaw</div></footer>
<script src="assets/site.js"></script>
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
        return f'<figure class="rv"><div class="ph"{z}>{tag}</div>{c}</figure>'
    if t == "figs":
        _, cols, items, cap, ar, contain = b
        cls = f"figs c{cols}" + (" contain" if contain else "")
        if cols == 1:
            cls += '" style="max-width:520px;margin-left:auto;margin-right:auto'
        out = [f'<div class="{cls} rv">']
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
        return (f'<div class="slider rv"><div class="track">{"".join(slides)}</div>'
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
            f'<a class="btn solid" href="{u}" target="_blank" rel="noopener">{l} ↗</a>' for l, u in p["links"]) + "</div>"
    cover_id = p.get("cover") or p["thumb"]
    ctag, cz = img(cover_id, alt=p["title"], w=2000, lazy=False, cap=p["title"])
    toc = "".join(f'<a href="#{anchor(h)}">{h}</a>' for h, _ in p["sections"])
    secs = []
    for h, blocks in p["sections"]:
        body = "".join(block(b) for b in blocks)
        secs.append(f'<section class="cs-sec" id="{anchor(h)}"><div class="wrap narrow"><h2 class="rv">{h}</h2>{body}</div></section>')
    nxt = ""
    if prev_p:
        nxt += f'<a href="{prev_p["slug"]}.html"><span>← Previous</span><b>{prev_p["title"]}</b></a>'
    else:
        nxt += '<a href="index.html#work"><span>← Back</span><b>All projects</b></a>'
    if next_p:
        nxt += f'<a class="r" href="{next_p["slug"]}.html"><span>Next →</span><b>{next_p["title"]}</b></a>'
    else:
        nxt += '<a class="r" href="index.html#work"><span>Back to</span><b>All projects</b></a>'
    return (HEAD.format(title=f'{p["title"]} | Andy Shaw', desc=html.escape(p["card"], quote=True)) + nav(False) +
f"""<div class="progress" aria-hidden="true"></div>
<header class="cs-hero wrap">
  <a class="back" href="index.html#work">← All projects</a>
  <div class="label">{p["where"]} · {p["kind"]}</div>
  <h1>{p["title"]}</h1>
  <p class="lede">{p["lede"]}</p>
  {links}
  <div class="facts">{facts}</div>
  {outcome}
</header>
<div class="wrap"><div class="cs-cover"><div class="ph"{cz} style="cursor:zoom-in">{ctag}</div></div></div>
<nav class="toc"><div class="wrap">{toc}</div></nav>
<main id="main">{"".join(secs)}</main>
<div class="wrap"><div class="cs-next">{nxt}</div></div>
""" + CONTACT)

def card(p):
    tag, _ = img(p["thumb"], alt=p["title"], fill=800, zoom=False)
    imp = f'<div class="impact">{p["impact"]}</div>' if p.get("impact") else ""
    pills = "".join(f"<span>{x}</span>" for x in p["pills"])
    return f"""<a class="proj rv" data-c="{p['cat']}" href="{p['slug']}.html">
  <div class="thumb">{tag}</div>
  <div class="body">
    <div class="where"><span>{p['where']}</span><span>{p['kind']}</span></div>
    <h4>{p['title']}</h4>
    <p>{p['card']}</p>
    {imp}
    <div class="pills">{pills}</div>
  </div>
</a>"""

def home():
    cards = "\n".join(card(BYSLUG[s]) for s in ORDER)
    ptag, _ = img(m("56a508aabfa1400493a7a92ebbedee1b", "jpg"), alt="Andy Shaw", w=900, zoom=False)
    return (HEAD.format(title="Andy Shaw | UX Research and Product",
                        desc="Andy Shaw. UX researcher at Meta Reality Labs and builder of kndi, an iOS app for planning festivals with friends. Open to PM, PjM, and UX research roles.")
            + nav(True) + f"""
<main id="main">
<header class="hero wrap" id="top">
  <div class="status"><span class="dot"></span>Open to PM, PjM, and UX research roles. Seattle or relocating.</div>
  <h1>I research how people use products, and I <em>build</em> them too.</h1>
  <p class="lede">I'm Andy. I lead UX research studies at <strong>Meta Reality Labs</strong> for AR/VR and smart glasses, and on the side I built and shipped <strong>kndi</strong>, an iPhone app for planning festivals with friends. Now I want a role where I help decide what gets built, not just test it after.</p>
  <div class="beads" aria-hidden="true">
    <span style="background:#E2552B"></span><span style="background:#F2A541"></span><span style="background:#F5D547"></span><span style="background:#5BC0A8"></span><span style="background:#4F8EF7"></span><span style="background:#9B6BF2"></span><span style="background:#EF6FB4"></span>
  </div>
</header>
<div class="strip" aria-label="Where I've worked and studied"><div class="strip-track">
  <span>Meta Reality Labs</span><i></i><span>Gopuff</span><i></i><span>User Research International</span><i></i><span>KUOW Public Radio</span><i></i><span>University of Washington</span><i></i><span>kndi</span><i></i>
  <span aria-hidden="true">Meta Reality Labs</span><i></i><span aria-hidden="true">Gopuff</span><i></i><span aria-hidden="true">User Research International</span><i></i><span aria-hidden="true">KUOW Public Radio</span><i></i><span aria-hidden="true">University of Washington</span><i></i><span aria-hidden="true">kndi</span><i></i>
</div></div>

<section id="kndi">
  <div class="wrap">
    <div class="label rv">Featured project</div>
    <h2 class="rv">From a group chat problem to a live app on the App Store.</h2>
    <div class="feature rv">
      <div class="feature-copy">
        <span class="tag">Side project · iOS · Live</span>
        <h3>kndi</h3>
        <div class="sub">Plan festivals with your friends.</div>
        <p>Planning a festival with a group usually means a messy group chat, five screenshots of the set times, and nobody knowing where to meet. kndi puts all of that in one place. Every event gets a group with chat, polls, a shared schedule, and an album, and you get a heads up when two sets you picked overlap.</p>
        <p>It also brings kandi trading into the app. You design digital beads and trade them by scanning each other's codes in person. The goal was never to replace the real thing. It's a way to keep the memory of who you met.</p>
        <ul class="did">
          <li><b>Product</b><span>Decided what to build and what to cut, based on how my friends and I actually plan shows.</span></li>
          <li><b>Build</b><span>Built and shipped the iOS app with a small group of friends, using AI coding tools to move fast.</span></li>
          <li><b>Growth</b><span>Wrote the go-to-market plan, focused on local network effects and Insomniac events, and worked on App Store discoverability.</span></li>
        </ul>
        <div class="stats">
          <div class="stat"><b>4.9</b><span>App Store rating</span></div>
          <div class="stat"><b data-count="6200">6,200+</b><span>events in 408 cities</span></div>
        </div>
        <div class="btns">
          <a class="btn solid" href="https://apps.apple.com/app/kndi/id6762342337" target="_blank" rel="noopener">View on the App Store ↗</a>
          <a class="btn" href="https://kndi.app" target="_blank" rel="noopener">kndi.app ↗</a>
        </div>
      </div>
      <div class="feature-art" aria-hidden="true">
        <div class="phone"><div class="screen">
          <div class="scr-top"><b>kndi</b><span class="chip">EDC LV</span></div>
          <div class="card">
            <div class="t">The Squad</div>
            <div class="m">6 friends · 3 days</div>
            <div class="sets">
              <div class="set"><span>Knock2 · 9:15</span><span class="av"><i style="background:#F2A541"></i><i style="background:#5BC0A8"></i><i style="background:#9B6BF2"></i></span></div>
              <div class="set clash"><span>ISOxo · 10:30</span><span class="chip">overlap</span></div>
              <div class="set"><span>Meet at the pin · 11:45</span><span class="av"><i style="background:#EF6FB4"></i><i style="background:#4F8EF7"></i></span></div>
            </div>
          </div>
          <div class="card">
            <div class="t">Your kandi</div>
            <div class="m">12 trades this weekend</div>
            <div class="kandi"><i style="background:#E2552B"></i><i style="background:#F2A541"></i><i style="background:#F5D547"></i><i style="background:#5BC0A8"></i><i style="background:#4F8EF7"></i><i style="background:#9B6BF2"></i><i style="background:#EF6FB4"></i><i style="background:#E2552B"></i><i style="background:#F2A541"></i><i style="background:#F5D547"></i><i style="background:#5BC0A8"></i><i style="background:#4F8EF7"></i></div>
          </div>
          <div class="card"><div class="t">Poll: Day 2 outfit theme</div><div class="m">4 of 6 voted</div></div>
        </div></div>
      </div>
    </div>
  </div>
</section>

<section id="meta">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <div class="label">Current role</div>
        <div class="meta-side">
          <b>Meta Reality Labs</b>
          UX Research Assistant<br>
          May 2024 to now<br>
          Redmond, via H10
        </div>
      </div>
      <div class="prose rv">
        <p>I joined Meta to support research studies. Four months in, I was promoted to lead all of the UX research studies on a larger team.</p>
        <p>I run studies end to end: writing the procedures, recruiting participants, piloting, collecting data in person, and doing the first round of cleaning and analysis in R and Python. That work goes straight to the research scientists who use it to shape product proposals for AR/VR and smart glasses.</p>
        <p class="note">Most of this work is under NDA, so I keep it high level here. I'm happy to walk through how I run a study when we talk.</p>
      </div>
    </div>
    <div class="numbers rv">
      <div class="num"><b data-count="300">300+</b><span>auditory perception experiments run</span></div>
      <div class="num"><b data-count="12">12+</b><span>research reports that influenced product direction</span></div>
      <div class="num"><b data-count="400">400+</b><span>user entries coded into 10+ personas and scenarios</span></div>
      <div class="num"><b data-count="8">8+</b><span>training sessions for vendor research assistants</span></div>
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <div class="label rv">Case studies</div>
    <h2 class="rv">Research, design, and code from Gopuff and UW.</h2>
    <div class="filters rv" role="group" aria-label="Filter projects">
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
    <div class="label rv">Experience</div>
    <h2 class="rv">About three years in UX research.</h2>
    <ul class="xp rv">
      <li><span class="when">May 2024 to now</span><div>
        <div class="role">UX Research Assistant</div>
        <div class="org">Meta Reality Labs, Redmond (via H10)</div>
        <ul>
          <li>Promoted after 4 months to lead all UX research studies on a larger team.</li>
          <li>Ran 300+ auditory perception experiments informing AR/VR and smart glasses products.</li>
          <li>Wrote 12+ research reports with statistical analysis that influenced product direction.</li>
          <li>Managed 100+ internal documents as the data collection team's documentation lead.</li>
        </ul></div></li>
      <li><span class="when">Ongoing</span><div>
        <div class="role">Founder and builder</div>
        <div class="org">kndi, iOS app</div>
        <ul>
          <li>Built and shipped an iPhone app for festival group planning and digital kandi trading.</li>
          <li>Owns product direction and the go-to-market plan.</li>
        </ul></div></li>
      <li><span class="when">Nov 2023 to May 2024</span><div>
        <div class="role">UX Moderator</div>
        <div class="org">User Research International, Redmond</div>
        <ul>
          <li>Led 80+ in-person usability tests, interviews, and benchmarks on consumer electronics hardware.</li>
          <li>Set up wearable and AR/VR research equipment, and recruited and screened participants.</li>
          <li>Helped write client reports with trends, insights, and recommendations.</li>
        </ul></div></li>
      <li><span class="when">Jun 2022 to Aug 2022</span><div>
        <div class="role">UX Researcher Intern</div>
        <div class="org">Gopuff, remote</div>
        <ul>
          <li>Ran 20+ interviews, usability tests, concept tests, and heuristic evaluations on the consumer app.</li>
          <li>Researched saving items for later to cut cart abandonment, projected to add $16M in annual revenue.</li>
          <li>Produced 40+ recommendations that guided app experiments. Bundling and product page work shipped.</li>
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
    <div class="portrait rv">{ptag}</div>
    <div class="rv">
      <div class="label">About</div>
      <h2 style="margin-bottom:28px">The planner of the group.</h2>
      <div class="prose">
        <p>I grew up in the Seattle area and studied HCDE at UW. In every group I'm in, I end up being the one who plans things and keeps everyone moving. I also work better when people are counting on me. That's a big part of why I'm moving toward product and program management.</p>
        <p>Research taught me to ask why before jumping to a fix. Building kndi taught me what comes after that: picking what to ship, cutting what doesn't matter, and seeing whether real people actually use it.</p>
        <p>Outside of work I run a weekly D&amp;D campaign as the Dungeon Master, go to a lot of EDM shows (which is where kndi came from), and play more League than I should.</p>
      </div>
      <div class="skills">
        <div><h5>Research</h5><p>Study design, interviews, usability tests, concept tests, surveys, heuristic evaluation, competitive analysis, personas</p></div>
        <div><h5>Data and code</h5><p>R, Python, SQL, JavaScript, Java, HTML/CSS, Git</p></div>
        <div><h5>Design</h5><p>Figma, Miro, wireframes, user flows, prototyping, Illustrator, Photoshop</p></div>
        <div><h5>Project management</h5><p>Research planning, prioritization, team training, documentation, shipping an app end to end</p></div>
      </div>
    </div>
  </div>
</section>
</main>
""" + CONTACT)

def main():
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(home())
    for p in PROJECTS:
        with open(os.path.join(OUT, f"{p['slug']}.html"), "w") as f:
            f.write(case_page(p))
    print("built", 1 + len(PROJECTS), "pages")

if __name__ == "__main__":
    main()
