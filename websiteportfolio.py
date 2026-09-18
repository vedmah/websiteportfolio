import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Vedant Mahajan | 3D Portfolio",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Injection of Modern Glassmorphism CSS & Custom Styles
glass_css = """
<style>
/* Gradient Background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

/* Glassmorphic Container Cards */
div.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    padding: 24px;
    margin-bottom: 20px;
    transition: transform 0.3s ease, border-color 0.3s ease;
}

div.glass-card:hover {
    transform: translateY(-4px);
    border-color: rgba(99, 102, 241, 0.4);
}

/* Header & Typography */
h1, h2, h3 {
    color: #ffffff !important;
    font-weight: 700;
}

.gradient-text {
    background: linear-gradient(90deg, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Glass Pill Buttons */
.glass-btn {
    display: inline-block;
    padding: 8px 18px;
    background: rgba(99, 102, 241, 0.2);
    border: 1px solid rgba(129, 140, 248, 0.4);
    color: #e0e7ff !important;
    text-decoration: none !important;
    border-radius: 20px;
    font-size: 0.88rem;
    font-weight: 500;
    backdrop-filter: blur(8px);
    transition: all 0.2s ease-in-out;
}

.glass-btn:hover {
    background: rgba(99, 102, 241, 0.4);
    box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
}

/* Hide default streamlit margins/header padding for sleek full-width feel */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
"""
st.markdown(glass_css, unsafe_allow_html=True)

# 3. Top Navigation Bar with Quick Hamburger Menu
if "current_nav" not in st.session_state:
    st.session_state.current_nav = "🏠 Overview & 3D Space"

top_col1, top_col2 = st.columns([3, 1])

with top_col1:
    st.markdown("<h2 style='margin:0;'>Vedant Mahajan <span class='gradient-text'>| 3D & Web Portfolio</span></h2>", unsafe_allow_html=True)

with top_col2:
    nav_selection = st.selectbox(
        "☰ Quick Navigation Menu",
        options=["🏠 Overview & 3D Space", "🚀 Live Projects", "📜 Certificates", "📩 Contact"],
        index=["🏠 Overview & 3D Space", "🚀 Live Projects", "📜 Certificates", "📩 Contact"].index(st.session_state.current_nav),
        key="nav_menu"
    )
    st.session_state.current_nav = nav_selection

st.markdown("---")

# 4. PAGE SECTIONS

# --- SECTION 1: OVERVIEW & 3D OFFICE SPACE ---
if st.session_state.current_nav == "🏠 Overview & 3D Space":
    
    st.markdown("""
    <div class="glass-card">
        <h3>👋 Welcome to my Glassmorphic Space</h3>
        <p style="color: #cbd5e1;">
            I am a Front-End Developer & AI/Data Science Practitioner skilled in building interactive, sleek modern web UI experience, Streamlit platforms, and custom 3D web spaces.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 class='gradient-text'>🏢 3D Interactive Office View</h3>", unsafe_allow_html=True)
    
    # 3D Model / Spline Embed Container inside Glass Card
    st.markdown("""
    <div class="glass-card">
        <p style="color: #94a3b8; font-size:0.9rem;">Interact with the 3D canvas below (Orbit, pan, and click objects):</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Replace URL below with your actual Spline, Three.js, or Sketchfab 3D embed URL
    three_d_embed_url = "https://my.spline.design/3dtextcubescopy-4a3bd095ca1ba8cbfd9ebfa6043efbfb/"
    st.components.v1.iframe(three_d_embed_url, height=520, scrolling=False)


# --- SECTION 2: LIVE PROJECTS ---
elif st.session_state.current_nav == "🚀 Live Projects":
    st.markdown("<h3 class='gradient-text'>🚀 Featured Live Projects</h3>", unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("""
        <div class="glass-card">
            <h4>📐 Architectural & Interior 3D Site</h4>
            <p style="color: #cbd5e1; font-size:0.9rem;">
                An interactive web app featuring 3D layouts, urban planning assets, and responsive interior visualization components.
            </p>
            <p style="color: #818cf8; font-size:0.8rem; font-weight:600;">Tech: WordPress, Elementor, Three.js, CSS3</p>
            <a href="https://github.com" target="_blank" class="glass-btn">🔗 Live Demo</a>
            <a href="https://github.com" target="_blank" class="glass-btn" style="margin-left:8px;">💻 Source Code</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h4>📊 ML & Streamlit AI Tool</h4>
            <p style="color: #cbd5e1; font-size:0.9rem;">
                Multi-variable regression analytics suite equipped with Ridge/Lasso regularization tuning and real-time visualization controls.
            </p>
            <p style="color: #818cf8; font-size:0.8rem; font-weight:600;">Tech: Python, Streamlit, Scikit-Learn, Pandas</p>
            <a href="https://streamlit.io" target="_blank" class="glass-btn">🔗 Live App</a>
        </div>
        """, unsafe_allow_html=True)

    with col_p2:
        st.markdown("""
        <div class="glass-card">
            <h4>🚇 Integrated Metro Map Platform</h4>
            <p style="color: #cbd5e1; font-size:0.9rem;">
                An offline mobile-ready web tool facilitating route lookup, fare calculation, and transit visual mapping for urban rail systems.
            </p>
            <p style="color: #818cf8; font-size:0.8rem; font-weight:600;">Tech: HTML5, JavaScript, PWA, CSS Glassmorphism</p>
            <a href="https://github.com" target="_blank" class="glass-btn">🔗 View Project</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h4>🤖 Corrective RAG AI Platform</h4>
            <p style="color: #cbd5e1; font-size:0.9rem;">
                Retrieval-Augmented Generation agent capable of verifying query responses, filtering document context, and dynamically correcting hallucinated outputs.
            </p>
            <p style="color: #818cf8; font-size:0.8rem; font-weight:600;">Tech: Python, LLM APIs, LangChain, VectorDB</p>
            <a href="https://github.com" target="_blank" class="glass-btn">🔗 Repo & Docs</a>
        </div>
        """, unsafe_allow_html=True)


# --- SECTION 3: CERTIFICATES ---
elif st.session_state.current_nav == "📜 Certificates":
    st.markdown("<h3 class='gradient-text'>📜 Professional Certifications & Achievements</h3>", unsafe_allow_html=True)
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        <div class="glass-card">
            <h4>☁️ Azure Cloud Master</h4>
            <p style="color: #94a3b8; font-size:0.85rem;">Issued by Azurelib</p>
            <p style="color: #cbd5e1; font-size:0.88rem;">Validated expertise in cloud infrastructure, container services, and enterprise deployments.</p>
            <a href="https://credential.net" target="_blank" class="glass-btn">Verify Credential</a>
        </div>
        """, unsafe_allow_html=True)
        
    with cert2:
        st.markdown("""
        <div class="glass-card">
            <h4>⚡ AWS Cloud Certified</h4>
            <p style="color: #94a3b8; font-size:0.85rem;">Cloud Master Certification</p>
            <p style="color: #cbd5e1; font-size:0.88rem;">Mastery in AWS core architectures, serverless computing, and cloud deployment pipelines.</p>
            <a href="https://aws.amazon.com" target="_blank" class="glass-btn">Verify Credential</a>
        </div>
        """, unsafe_allow_html=True)

    with cert3:
        st.markdown("""
        <div class="glass-card">
            <h4>🤖 AI & Data Science Specialist</h4>
            <p style="color: #94a3b8; font-size:0.85rem;">FutureSkills Prime / AI Bootcamps</p>
            <p style="color: #cbd5e1; font-size:0.88rem;">Certified in Machine Learning workflows, LLMs, prompt engineering, and data analytics.</p>
            <a href="https://futureskillsprime.in" target="_blank" class="glass-btn">Verify Credential</a>
        </div>
        """, unsafe_allow_html=True)


# --- SECTION 4: CONTACT ---
elif st.session_state.current_nav == "📩 Contact":
    st.markdown("<h3 class='gradient-text'>📩 Get In Touch</h3>", unsafe_allow_html=True)
    
    c_left, c_right = st.columns([2, 1])
    
    with c_left:
        st.markdown("""
        <div class="glass-card">
            <h4>Send a Direct Message</h4>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Thank you! Your message has been received.")
                
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c_right:
        st.markdown("""
        <div class="glass-card">
            <h4>Connect Directly</h4>
            <p style="color: #cbd5e1; font-size:0.9rem;">💼 <b>LinkedIn:</b> linkedin.com/in/vedantmahajan</p>
            <p style="color: #cbd5e1; font-size:0.9rem;">💻 <b>GitHub:</b> github.com/vedantmahajan</p>
            <p style="color: #cbd5e1; font-size:0.9rem;">📍 <b>Location:</b> Pune, Maharashtra, India</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><hr><p style='text-align: center; color: #64748b; font-size: 0.85rem;'>Designed with 🧊 Glassmorphism & Streamlit | Vedant Mahajan</p>", unsafe_allow_html=True)
