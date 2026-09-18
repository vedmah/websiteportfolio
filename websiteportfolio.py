"""
Vedant Mahajan — Glassmorphism Portfolio
-----------------------------------------
A modern, glass-styled single-file Streamlit portfolio with a hamburger
quick-nav menu, live-editable Projects and Certificates sections.

Run:
    streamlit run app.py

To add a new project or certificate, just add an entry to the
PROJECTS or CERTIFICATES lists below — no other code changes needed.
"""

import base64
import os
import streamlit as st

# ----------------------------------------------------------------------
# OFFICE IMAGE
# ----------------------------------------------------------------------
# Drop a real photo named "office.jpg" or "office.png" next to this file
# and it will be used automatically. Until then, a built-in glass-style
# office illustration is shown as a placeholder.
OFFICE_IMAGE_CANDIDATES = ["office.jpg", "office.jpeg", "office.png"]

def _find_office_image():
    here = os.path.dirname(os.path.abspath(__file__))
    for name in OFFICE_IMAGE_CANDIDATES:
        path = os.path.join(here, name)
        if os.path.exists(path):
            return path
    return None

def _office_image_data_uri():
    path = _find_office_image()
    if not path:
        return None
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mime = "jpeg" if ext in ("jpg", "jpeg") else "png"
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/{mime};base64,{encoded}"

# Built-in fallback illustration: an isometric office desk scene,
# drawn as inline SVG so no external file or network call is needed.
OFFICE_SVG_FALLBACK = """
<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="floor" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#2a1f55"/>
      <stop offset="100%" stop-color="#171233"/>
    </linearGradient>
    <linearGradient id="desk" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5b4bd6"/>
      <stop offset="100%" stop-color="#3d2f99"/>
    </linearGradient>
    <linearGradient id="screen" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#22d3ee"/>
      <stop offset="100%" stop-color="#7c5cff"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="600" height="360" rx="24" fill="url(#floor)"/>
  <ellipse cx="300" cy="300" rx="220" ry="30" fill="#000" opacity="0.25"/>

  <!-- window -->
  <rect x="40" y="40" width="150" height="180" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.18)"/>
  <line x1="115" y1="40" x2="115" y2="220" stroke="rgba(255,255,255,0.18)"/>
  <line x1="40" y1="130" x2="190" y2="130" stroke="rgba(255,255,255,0.18)"/>

  <!-- shelf -->
  <rect x="430" y="50" width="130" height="14" rx="4" fill="rgba(255,255,255,0.12)"/>
  <rect x="440" y="20" width="20" height="30" rx="3" fill="#22d3ee" opacity="0.7"/>
  <rect x="465" y="10" width="20" height="40" rx="3" fill="#7c5cff" opacity="0.7"/>
  <rect x="490" y="24" width="20" height="26" rx="3" fill="#ff8fd0" opacity="0.6"/>
  <circle cx="530" cy="35" r="14" fill="rgba(255,255,255,0.10)"/>

  <!-- desk -->
  <rect x="140" y="230" width="340" height="18" rx="6" fill="url(#desk)"/>
  <rect x="160" y="248" width="14" height="60" fill="#2a2260"/>
  <rect x="440" y="248" width="14" height="60" fill="#2a2260"/>

  <!-- monitor -->
  <rect x="255" y="150" width="110" height="72" rx="8" fill="#1c1440" stroke="rgba(255,255,255,0.15)"/>
  <rect x="265" y="160" width="90" height="52" rx="4" fill="url(#screen)"/>
  <rect x="300" y="222" width="20" height="14" fill="#1c1440"/>
  <rect x="285" y="234" width="50" height="6" rx="3" fill="#1c1440"/>

  <!-- keyboard + mouse -->
  <rect x="260" y="232" width="90" height="12" rx="4" fill="rgba(255,255,255,0.15)"/>
  <circle cx="370" cy="238" r="6" fill="rgba(255,255,255,0.15)"/>

  <!-- mug -->
  <rect x="190" y="216" width="22" height="20" rx="4" fill="#ff8fd0"/>
  <path d="M212 220 q10 0 10 8 q0 8 -10 8" fill="none" stroke="#ff8fd0" stroke-width="3"/>

  <!-- plant -->
  <rect x="400" y="214" width="24" height="22" rx="4" fill="#3d2f99"/>
  <circle cx="412" cy="200" r="10" fill="#22d3ee" opacity="0.8"/>
  <circle cx="402" cy="206" r="8" fill="#22d3ee" opacity="0.6"/>
  <circle cx="422" cy="206" r="8" fill="#22d3ee" opacity="0.6"/>

  <!-- chair -->
  <rect x="285" y="255" width="60" height="10" rx="4" fill="#2a2260"/>
  <rect x="300" y="264" width="10" height="40" fill="#2a2260"/>
  <ellipse cx="305" cy="308" rx="30" ry="8" fill="#000" opacity="0.2"/>
  <rect x="295" y="200" width="40" height="55" rx="14" fill="#5b4bd6" opacity="0.85"/>
</svg>
"""

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Vedant Mahajan | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# EDITABLE DATA — add your live projects & certificates here
# ----------------------------------------------------------------------
PROFILE = {
    "name": "Vedant Bhushan Mahajan",
    "title": "Python Developer • AI/ML Engineer",
    "tagline": "Building intelligent systems with Generative AI, ML, and clean Python engineering.",
    "location": "Pune, Maharashtra, India",
    "email": "your-email@example.com",          # <-- edit
    "github": "https://github.com/your-handle", # <-- edit
    "linkedin": "https://linkedin.com/in/your-handle",  # <-- edit
    "resume_link": "#",                          # <-- add a hosted resume link
}

SKILLS = [
    "Python", "SQL", "Machine Learning", "Deep Learning", "Generative AI",
    "LangChain", "FAISS", "HuggingFace", "AWS", "Azure", "DevOps", "Streamlit",
]

PROJECTS = [
    {
        "title": "DocuTrust",
        "description": "A Corrective RAG document Q&A platform using FAISS, "
                        "sentence-transformers, cross-encoder reranking, and the "
                        "Groq API for generation.",
        "tags": ["RAG", "FAISS", "Groq API", "NLP"],
        "live_link": "",     # <-- add live/demo URL
        "code_link": "",     # <-- add GitHub repo URL
    },
    {
        "title": "SmartHire",
        "description": "A resume screening system using TF-IDF + cosine similarity "
                        "with rule-based extraction for fast candidate shortlisting.",
        "tags": ["TF-IDF", "NLP", "Automation"],
        "live_link": "",
        "code_link": "",
    },
    {
        "title": "Mapparazzi",
        "description": "An Android Flutter app built for Pune Metro commuters, "
                        "with a presentation/documentation companion.",
        "tags": ["Flutter", "Android", "Transit"],
        "live_link": "",
        "code_link": "",
    },
    # Add more projects below — just copy the block above.
]

CERTIFICATES = [
    {
        "title": "Example Certificate Name",
        "issuer": "Issuing Organization",
        "date": "2026",
        "link": "",   # <-- add certificate verification/view URL
    },
    # Add more certificates below — just copy the block above.
]

NAV_ITEMS = ["Home", "About", "Skills", "Projects", "Certificates", "Contact"]

# ----------------------------------------------------------------------
# GLASSMORPHISM STYLES
# ----------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root{
    --bg-1:#0f1120;
    --bg-2:#1b1035;
    --accent:#7c5cff;
    --accent-2:#22d3ee;
    --glass-bg: rgba(255,255,255,0.06);
    --glass-border: rgba(255,255,255,0.14);
    --text-main:#f3f2ff;
    --text-muted:#b7b2d6;
}

html, body, [class*="css"]{
    font-family:'Poppins', sans-serif;
    color: var(--text-main);
}

.stApp{
    background:
        radial-gradient(circle at 15% 20%, rgba(124,92,255,0.35), transparent 45%),
        radial-gradient(circle at 85% 15%, rgba(34,211,238,0.25), transparent 40%),
        radial-gradient(circle at 50% 90%, rgba(255,92,180,0.18), transparent 45%),
        linear-gradient(160deg, var(--bg-1), var(--bg-2));
    background-attachment: fixed;
}

#MainMenu, footer, header {visibility: hidden;}

.block-container{
    padding-top: 1.2rem;
    max-width: 1150px;
}

/* ---------- GLASS CARD BASE ---------- */
.glass{
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    backdrop-filter: blur(18px) saturate(160%);
    -webkit-backdrop-filter: blur(18px) saturate(160%);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
}

/* ---------- NAVBAR ---------- */
.navbar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding: 0.9rem 1.5rem;
    margin-bottom: 1.6rem;
    position: sticky;
    top: 0.6rem;
    z-index: 999;
}
.navbar .brand{
    font-family:'Space Grotesk', sans-serif;
    font-weight:700;
    font-size:1.25rem;
    background: linear-gradient(90deg, var(--accent), var(--accent-2));
    -webkit-background-clip:text;
    -webkit-text-fill-color: transparent;
}
.nav-links{
    display:flex;
    gap: 0.4rem;
    flex-wrap: wrap;
}

/* Streamlit buttons restyled as pill nav links */
div[data-testid="stHorizontalBlock"] button{
    background: transparent !important;
    border: 1px solid transparent !important;
    color: var(--text-muted) !important;
    border-radius: 999px !important;
    padding: 0.35rem 1rem !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    transition: all 0.25s ease;
}
div[data-testid="stHorizontalBlock"] button:hover{
    background: rgba(255,255,255,0.10) !important;
    border: 1px solid var(--glass-border) !important;
    color: var(--text-main) !important;
}

/* Hamburger toggle button */
.hamburger-btn button{
    background: var(--glass-bg) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 12px !important;
    font-size: 1.2rem !important;
    padding: 0.3rem 0.7rem !important;
}

/* ---------- HERO ---------- */
.hero{
    padding: 3rem 2.2rem;
    margin-bottom: 1.8rem;
    text-align:center;
}
.hero h1{
    font-family:'Space Grotesk', sans-serif;
    font-size: 2.6rem;
    margin-bottom: 0.3rem;
}
.hero .title{
    font-size: 1.15rem;
    background: linear-gradient(90deg, var(--accent-2), var(--accent));
    -webkit-background-clip:text;
    -webkit-text-fill-color: transparent;
    font-weight:600;
    margin-bottom: 0.6rem;
}
.hero p.tagline{
    color: var(--text-muted);
    max-width: 620px;
    margin: 0 auto;
    line-height:1.6;
}

/* ---------- SECTION TITLES ---------- */
.section-title{
    font-family:'Space Grotesk', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    margin: 2.2rem 0 1rem 0;
    display:flex;
    align-items:center;
    gap:0.6rem;
}
.section-title::after{
    content:"";
    flex:1;
    height:1px;
    background: linear-gradient(90deg, var(--glass-border), transparent);
}

/* ---------- CARDS ---------- */
.card{
    padding: 1.4rem 1.5rem;
    margin-bottom: 1rem;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover{
    transform: translateY(-4px);
    box-shadow: 0 14px 40px rgba(124,92,255,0.25);
}
.card h4{
    margin: 0 0 0.4rem 0;
    font-family:'Space Grotesk', sans-serif;
    font-size: 1.15rem;
}
.card p{
    color: var(--text-muted);
    font-size: 0.93rem;
    line-height: 1.55;
    margin-bottom: 0.7rem;
}
.tag{
    display:inline-block;
    font-size: 0.72rem;
    padding: 0.18rem 0.6rem;
    margin: 0 0.3rem 0.3rem 0;
    border-radius: 999px;
    background: rgba(124,92,255,0.18);
    border: 1px solid rgba(124,92,255,0.35);
    color: #d6cfff;
}
.card-links a{
    font-size: 0.85rem;
    color: var(--accent-2);
    text-decoration:none;
    margin-right: 1rem;
    font-weight: 600;
}
.card-links a:hover{ text-decoration: underline; }

/* ---------- SKILL PILLS ---------- */
.skill-pill{
    display:inline-block;
    padding: 0.45rem 1rem;
    margin: 0.25rem;
    border-radius: 999px;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    font-size: 0.88rem;
    font-weight: 500;
}

/* ---------- CONTACT ---------- */
.contact-box{
    padding: 2rem;
    text-align:center;
}
.contact-box a{
    color: var(--accent-2);
    text-decoration:none;
    font-weight:600;
}

/* Mobile tweak */
@media (max-width: 640px){
    .hero h1{ font-size: 1.9rem; }
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# NAV STATE
# ----------------------------------------------------------------------
if "menu_open" not in st.session_state:
    st.session_state.menu_open = True
if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

def go_to(page):
    st.session_state.active_page = page

# ----------------------------------------------------------------------
# NAVBAR (glass bar + hamburger toggle + quick-nav pills)
# ----------------------------------------------------------------------
st.markdown('<div class="navbar glass">', unsafe_allow_html=True)
top_l, top_r = st.columns([0.15, 0.85])
with top_l:
    st.markdown(f'<div class="brand">✦ {PROFILE["name"].split()[0]}.dev</div>', unsafe_allow_html=True)
with top_r:
    ham_col, nav_col = st.columns([0.07, 0.93])
    with ham_col:
        st.markdown('<div class="hamburger-btn">', unsafe_allow_html=True)
        if st.button("☰", key="hamburger"):
            st.session_state.menu_open = not st.session_state.menu_open
        st.markdown('</div>', unsafe_allow_html=True)
    with nav_col:
        if st.session_state.menu_open:
            nav_cols = st.columns(len(NAV_ITEMS))
            for i, item in enumerate(NAV_ITEMS):
                with nav_cols[i]:
                    st.button(item, key=f"nav_{item}", on_click=go_to, args=(item,))
st.markdown('</div>', unsafe_allow_html=True)

page = st.session_state.active_page

# ----------------------------------------------------------------------
# HERO (always visible on Home, or as a compact header elsewhere)
# ----------------------------------------------------------------------
if page == "Home":
    office_uri = _office_image_data_uri()
    if office_uri:
        office_media_html = (
            f'<img src="{office_uri}" alt="Office" '
            f'style="width:100%; max-width:520px; border-radius:18px; '
            f'border:1px solid var(--glass-border); box-shadow:0 10px 34px rgba(0,0,0,0.35); '
            f'margin:1.2rem auto 0 auto; display:block;" />'
        )
    else:
        office_media_html = (
            f'<div style="max-width:480px; margin:1.2rem auto 0 auto; '
            f'border-radius:18px; overflow:hidden; border:1px solid var(--glass-border); '
            f'box-shadow:0 10px 34px rgba(0,0,0,0.35);">{OFFICE_SVG_FALLBACK}</div>'
        )

    st.markdown(f"""
    <div class="hero glass">
        <h1>Hi, I'm {PROFILE['name']} 👋</h1>
        <div class="title">{PROFILE['title']}</div>
        <p class="tagline">{PROFILE['tagline']}</p>
        <p style="color:var(--text-muted); margin-top:0.8rem; font-size:0.9rem;">📍 {PROFILE['location']}</p>
        {office_media_html}
    </div>
    """, unsafe_allow_html=True)
    if not office_uri:
        st.caption("Showing a placeholder illustration — drop a real photo named "
                   "`office.jpg` or `office.png` next to app.py to replace it.")

    st.markdown('<div class="section-title">Quick Links</div>', unsafe_allow_html=True)
    ql1, ql2, ql3, ql4 = st.columns(4)
    with ql1:
        st.markdown(f'<div class="card glass" style="text-align:center;">📄<br><a href="{PROFILE["resume_link"]}" target="_blank" style="color:var(--accent-2);font-weight:600;">Resume</a></div>', unsafe_allow_html=True)
    with ql2:
        st.markdown(f'<div class="card glass" style="text-align:center;">💻<br><a href="{PROFILE["github"]}" target="_blank" style="color:var(--accent-2);font-weight:600;">GitHub</a></div>', unsafe_allow_html=True)
    with ql3:
        st.markdown(f'<div class="card glass" style="text-align:center;">🔗<br><a href="{PROFILE["linkedin"]}" target="_blank" style="color:var(--accent-2);font-weight:600;">LinkedIn</a></div>', unsafe_allow_html=True)
    with ql4:
        st.markdown(f'<div class="card glass" style="text-align:center;">✉️<br><a href="mailto:{PROFILE["email"]}" style="color:var(--accent-2);font-weight:600;">Email</a></div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# ABOUT
# ----------------------------------------------------------------------
if page in ("Home", "About"):
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card glass">
        <p>I'm a Python Developer and AI/ML Engineer with a background spanning
        Python development, Generative AI, machine learning, web development,
        application support, software testing, and data science. I hold an MCA
        (First Class with Distinction) from Pune University and a B.Sc. in
        Statistics, and I enjoy turning research-grade AI ideas into clean,
        shippable products.</p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SKILLS
# ----------------------------------------------------------------------
if page in ("Home", "Skills"):
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    pills_html = "".join(f'<span class="skill-pill">{s}</span>' for s in SKILLS)
    st.markdown(f'<div class="card glass">{pills_html}</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# PROJECTS
# ----------------------------------------------------------------------
if page in ("Home", "Projects"):
    st.markdown('<div class="section-title">Live Projects</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for idx, proj in enumerate(PROJECTS):
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in proj["tags"])
        links_html = ""
        if proj.get("live_link"):
            links_html += f'<a href="{proj["live_link"]}" target="_blank">🚀 Live Demo</a>'
        if proj.get("code_link"):
            links_html += f'<a href="{proj["code_link"]}" target="_blank">💻 Code</a>'
        if not links_html:
            links_html = '<span style="color:var(--text-muted); font-size:0.85rem;">Links coming soon</span>'
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card glass">
                <h4>{proj['title']}</h4>
                <p>{proj['description']}</p>
                <div>{tags_html}</div>
                <div class="card-links" style="margin-top:0.6rem;">{links_html}</div>
            </div>
            """, unsafe_allow_html=True)

# ----------------------------------------------------------------------
# CERTIFICATES
# ----------------------------------------------------------------------
if page in ("Home", "Certificates"):
    st.markdown('<div class="section-title">Certificates</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, cert in enumerate(CERTIFICATES):
        link_html = (f'<a href="{cert["link"]}" target="_blank">🔎 View Certificate</a>'
                     if cert.get("link") else
                     '<span style="color:var(--text-muted); font-size:0.85rem;">Link coming soon</span>')
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="card glass">
                <h4>{cert['title']}</h4>
                <p>{cert['issuer']} · {cert['date']}</p>
                <div class="card-links">{link_html}</div>
            </div>
            """, unsafe_allow_html=True)

# ----------------------------------------------------------------------
# CONTACT
# ----------------------------------------------------------------------
if page in ("Home", "Contact"):
    st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="contact-box glass">
        <p style="color:var(--text-muted); margin-bottom:1rem;">
            Open to Python / AI-ML roles and collaborations.
        </p>
        <a href="mailto:{PROFILE['email']}">{PROFILE['email']}</a> &nbsp;|&nbsp;
        <a href="{PROFILE['github']}" target="_blank">GitHub</a> &nbsp;|&nbsp;
        <a href="{PROFILE['linkedin']}" target="_blank">LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; color:var(--text-muted); font-size:0.8rem; margin-top:2.5rem; padding-bottom:1.5rem;">
    Built with Streamlit · © {PROFILE['name']}
</div>
""", unsafe_allow_html=True)
