"""Builds assets/Andy_Shaw_Resume.pdf from the latest General resume (Nov 2026, with the kndi update).

The contact email comes from PORTFOLIO_EMAIL so it isn't stored in this script.
Run: PORTFOLIO_EMAIL=you@example.com python3 build/resume.py
"""
import asyncio
import html
import os
import sys

from playwright.async_api import async_playwright

EMAIL = os.environ.get("PORTFOLIO_EMAIL", "").strip()
if not EMAIL:
    sys.exit("Set PORTFOLIO_EMAIL to the contact address for the resume, then rerun.")
OUT = os.environ.get("OUT_DIR") or os.path.join(os.path.dirname(__file__), "..")

SUMMARY = ("UX researcher with three years running studies end to end and turning findings into product decisions. "
           "At Meta Reality Labs, ran 300+ audio perception experiments and built 90 surveys that collected 3,500+ responses. "
           "Leads product for kndi, an iOS app with ~560 users.")

JOBS = [
    ("Human Subjects Research Assistant II", "Meta Reality Labs (contract via H10)", "Redmond, WA", "May 2024 - Nov 2026", [
        "Helped move several features from prototyping into development by contributing to 8 research reports, one of which shaped an onboarding flow in the Meta AI app for smart glasses.",
        "Owned the team's UX research work within four months, running studies independently from pilot to readout.",
        "Collected 3,500+ responses across 13 research programs by building 90 survey instruments in Qualtrics.",
        "Measured audio quality and effort with standard methods (MUSHRA, ITU-T P.800, P.835, NASA-TLX, SSQ12).",
        "Narrowed 146 recruits to 98 reliable participants by building in headphone screeners, catch trials, and hidden references, and sized samples with power analysis.",
        "Kept crowdsourced studies at 40 to 60 completions a week by running them end to end on Prolific and Qualtrics.",
        "Built a tiered training curriculum and roles matrix so panel studies no longer depended on one person, then trained other assistants into it.",
        "Consolidated 40+ documents into 10 role-based categories and wrote 101 of 113 revisions of the team wiki.",
        "Automated document status tracking with an LLM and built a team knowledge chatbot and meeting-notes digest.",
    ]),
    ("UX Moderator", "User Research International", "Redmond, WA", "Nov 2023 - May 2024", [
        "Moderated 80+ usability studies, interviews, and benchmarks on prototype electronics for major tech clients.",
        "Turned session data into client reports with prioritized findings and design recommendations.",
    ]),
    ("UX Research Intern", "Gopuff", "Remote", "Jun 2022 - Aug 2022", [
        "Led discovery research on Save For Later, a feature the team projected at about $16M in annual revenue.",
        "Ran 4 mixed-methods studies at once with interviews, concept tests, usability tests, and competitive analysis.",
    ]),
]

PROJECT = ("Product Owner and Lead Engineer", "kndi, iOS app for festival crews (volunteer team)", "kndi.app", "Apr 2026 - Present", [
    "Found that new users who join a group on day 0 return in week 1 at 44% vs 15%, from a cohort study of 251 signups, and reshaped onboarding around it.",
    "Grew the app to ~560 users, leading product and engineering with AI coding tools (72% of all commits).",
    "Led the rebuild from SwiftUI to React Native for iOS and Android, keeping parity across ~40 feature areas.",
])

EDUCATION = [
    "B.S. in Human Centered Design &amp; Engineering (Human-Computer Interaction), Minor in Mathematics",
    "Cum Laude  ·  GPA 3.88  ·  Dean's List  ·  Annual Dean's List 2021-2022",
    "Coursework: Usability Research, User Research, HCI, Data Visualization, Statistics, Directed Research (2 quarters)",
]

SKILLS = [
    ("Research", "Experimental design, cohort analysis, power analysis, surveys, interviews, usability testing"),
    ("Operations", "Prolific, Qualtrics, Ethnio, Dscout, UserTesting, REDCap, recruiting and screening, ethics review"),
    ("Technical", "SQL, PostHog, R, Python, React Native, Supabase, Git, Figma, Excel, AI coding tools"),
    ("Audio", "Max/MSP, IRCAM Spat5, SenseLab, ambisonics, binaural rendering, multichannel capture, Audacity, Reaper"),
]


def esc(t):
    return html.escape(t, quote=False).replace("&amp;amp;", "&amp;")


def job(title, org, loc, dates, bullets):
    lis = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    return (f'<div class="job"><div class="row"><b>{esc(title)}</b><span>{esc(dates)}</span></div>'
            f'<div class="sub">{esc(org)}  ·  {esc(loc)}</div><ul>{lis}</ul></div>')


def page():
    contact1 = f"Lynnwood, WA  ·  {html.escape(EMAIL)}"
    contact2 = "linkedin.com/in/andyjshaw000  ·  github.com/andyjshaw000  ·  andyjshaw000.github.io/portfolio"
    jobs = "".join(job(*j) for j in JOBS)
    edu = "".join(f'<div class="{"" if i == 0 else "muted"}">{e}</div>' for i, e in enumerate(EDUCATION))
    skills = "".join(f"<div><b>{k}:</b>  {esc(v)}</div>" for k, v in SKILLS)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0.5in 0.72in; }}
body {{ font-family: Arial, Helvetica, sans-serif; font-size: 9.6pt; line-height: 1.32; color: #111; margin: 0; }}
h1 {{ font-size: 18pt; margin: 0 0 2px; text-align: center; letter-spacing: .5px; }}
.contact {{ text-align: center; color: #333; }}
h2 {{ font-size: 10pt; letter-spacing: 1px; border-bottom: 1px solid #111; margin: 9px 0 4px; padding-bottom: 1px; }}
.row {{ display: flex; justify-content: space-between; }}
.row span {{ color: #444; }}
.sub {{ font-style: italic; color: #333; }}
.job {{ margin-bottom: 5px; }}
ul {{ margin: 2px 0 0; padding-left: 16px; }}
li {{ margin: 0 0 1px; }}
.muted {{ color: #444; }}
a {{ color: inherit; text-decoration: none; }}
</style></head><body>
<h1>Andy Shaw</h1>
<div class="contact">{contact1}</div>
<div class="contact">{contact2}</div>
<h2>SUMMARY</h2><div>{esc(SUMMARY)}</div>
<h2>EXPERIENCE</h2>{jobs}
<h2>PROJECTS</h2>{job(*PROJECT)}
<h2>EDUCATION</h2><div class="row"><b>University of Washington</b><span>June 2023</span></div>{edu}
<h2>SKILLS</h2>{skills}
</body></html>"""


async def main():
    out = os.path.join(OUT, "assets", "Andy_Shaw_Resume.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.set_content(page(), wait_until="load")
        await pg.pdf(path=out, format="Letter", print_background=True, prefer_css_page_size=True)
        await b.close()
    print("wrote", out)


if __name__ == "__main__":
    asyncio.run(main())
