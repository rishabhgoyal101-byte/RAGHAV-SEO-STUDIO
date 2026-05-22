import streamlit as st
from groq import Groq
from pptx import Presentation
from io import BytesIO

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="RAGHAV REALTY SEO Generator",
    page_icon="🏢",
    layout="wide"
)

# ----------------------------
# CUSTOM PREMIUM STYLING
# ----------------------------
st.markdown("""
<style>
    /* RAGHAV REALTY website-inspired palette:
       warm ivory, soft beige, deep brown, premium gold */

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #f7f1e6 !important;
        background-image:
            radial-gradient(circle at top left, rgba(190, 143, 66, 0.18), transparent 30%),
            linear-gradient(180deg, #fff8ec 0%, #f4ead8 50%, #eadcc5 100%) !important;
        color: #2b2118 !important;
        font-family: "Georgia", "Times New Roman", serif !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    [data-testid="stToolbar"] {
        right: 2rem !important;
    }

    [data-testid="stMainBlockContainer"], .block-container {
        background: rgba(255, 252, 245, 0.78) !important;
        border: 1px solid rgba(180, 132, 57, 0.24) !important;
        border-radius: 28px !important;
        padding: 2.2rem 2.4rem !important;
        max-width: 1120px !important;
        box-shadow: 0 24px 70px rgba(80, 55, 25, 0.12) !important;
    }

    .main-title {
        font-size: 2.9rem !important;
        font-weight: 800 !important;
        color: #8b5e2a !important;
        text-align: center !important;
        letter-spacing: 4px !important;
        text-transform: uppercase !important;
        margin-bottom: 0.25rem !important;
    }

    .subtitle {
        text-align: center !important;
        color: #6d5133 !important;
        margin-bottom: 2rem !important;
        letter-spacing: 1px !important;
        font-size: 1.08rem !important;
        font-family: "Arial", sans-serif !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, div, label, .stMarkdown {
        color: #2b2118 !important;
    }

    label {
        font-family: "Arial", sans-serif !important;
        font-weight: 700 !important;
        color: #5b4228 !important;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #fffaf2 !important;
        color: #2b2118 !important;
        border: 1px solid rgba(139, 94, 42, 0.42) !important;
        border-radius: 14px !important;
        font-family: "Arial", sans-serif !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border: 1px solid #b88945 !important;
        box-shadow: 0 0 0 2px rgba(184, 137, 69, 0.18) !important;
    }

    [data-baseweb="select"] > div {
        background-color: #fffaf2 !important;
        color: #2b2118 !important;
        border: 1px solid rgba(139, 94, 42, 0.42) !important;
        border-radius: 14px !important;
        font-family: "Arial", sans-serif !important;
    }

    [data-baseweb="select"] * {
        color: #2b2118 !important;
    }

    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(135deg, #8b5e2a 0%, #c79b52 100%) !important;
        color: #fff8ec !important;
        border-radius: 999px !important;
        border: none !important;
        padding: 0.9rem 1.6rem !important;
        font-weight: 800 !important;
        width: 100% !important;
        font-family: "Arial", sans-serif !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 12px 30px rgba(139, 94, 42, 0.24) !important;
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #6f461d 0%, #b88945 100%) !important;
        color: #ffffff !important;
        transform: translateY(-1px);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 12px !important;
        border-bottom: 1px solid rgba(139, 94, 42, 0.25) !important;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #fff6e8 !important;
        color: #8b5e2a !important;
        border-radius: 999px !important;
        border: 1px solid rgba(139, 94, 42, 0.28) !important;
        padding: 12px 26px !important;
        font-weight: 800 !important;
        font-family: "Arial", sans-serif !important;
    }

    .stTabs [aria-selected="true"] {
        background: #8b5e2a !important;
        color: #fff8ec !important;
    }

    [data-testid="stAlert"] {
        background-color: rgba(255, 248, 236, 0.92) !important;
        border: 1px solid rgba(139, 94, 42, 0.35) !important;
        color: #2b2118 !important;
        border-radius: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER + LOGO
# ----------------------------
# Upload your logo file as logo.png in the same folder
st.image("logo.png", width=180)
st.markdown('<div class="main-title">RAGHAV REALTY</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered SEO & Hashtag Generator for New Project Launches</div>', unsafe_allow_html=True)

# ----------------------------
# API CONFIG
# ----------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ----------------------------
# FORM
# ----------------------------
with st.form("seo_form"):
    col1, col2 = st.columns(2)

    with col1:
        project_name = st.text_input("Project Name")
        city = st.selectbox("City", ["Mumbai", "Pune", "Delhi", "Bangalore", "Jaipur", "Ahmedabad"])
        micro_market = st.text_input("Micro Market")
        project_type = st.selectbox("Project Type", ["Residential", "Commercial", "Mixed"])

    with col2:
        configuration = st.multiselect("Configuration", ["1 BHK", "2 BHK", "3 BHK", "4 BHK", "Office", "Retail"])
        landmarks = st.text_input("Nearby Landmarks")
        brand_positioning = st.selectbox("Brand Positioning", ["Luxury", "Premium", "Affordable", "Ultra Luxury"])

    usp = st.text_area("USP (Unique Selling Proposition)")
    submit = st.form_submit_button("Generate Premium SEO Content")


def create_ppt(seo_text, hashtag_text):
    prs = Presentation()

    slide1 = prs.slides.add_slide(prs.slide_layouts[5])
    slide1.shapes.title.text = "SEO Content"
    slide1.placeholders[0].text = seo_text

    slide2 = prs.slides.add_slide(prs.slide_layouts[5])
    slide2.shapes.title.text = "Hashtags"
    slide2.placeholders[0].text = hashtag_text

    output = BytesIO()
    prs.save(output)
    output.seek(0)
    return output

# ----------------------------
# GENERATE OUTPUT
# ----------------------------
if submit:
    prompt = f"""
    You are an expert luxury real estate SEO strategist for India.

    Generate in two clearly labeled sections:
    SECTION 1: SEO
    - 5 SEO Titles
    - 3 Meta Descriptions
    - 10 SEO Keywords

    SECTION 2: HASHTAGS
    - 10 Premium Social Media Hashtags

    Project Details:
    Project Name: {project_name}
    City: {city}
    Micro Market: {micro_market}
    Project Type: {project_type}
    Configuration: {configuration}
    Nearby Landmarks: {landmarks}
    Brand Positioning: {brand_positioning}
    USP: {usp}
    """

    with st.spinner("Generating premium SEO content..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1000
            )

            result = response.choices[0].message.content

            # Basic split between SEO and hashtags
            parts = result.split("SECTION 2:") if "SECTION 2:" in result else [result, ""]
            seo_content = parts[0]
            hashtag_content = parts[1]

            tab1, tab2 = st.tabs(["SEO", "Hashtags"])
            with tab1:
                st.markdown(seo_content)
            with tab2:
                st.markdown(hashtag_content)

            ppt_file = create_ppt(seo_content, hashtag_content)
            st.download_button(
                label="Download as PPT",
                data=ppt_file,
                file_name=f"{project_name}_seo_hashtags.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )

        except Exception as e:
            st.error("Groq API Error:")
            st.code(str(e))

