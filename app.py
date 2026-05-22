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
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #d4af37;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #d4af37;
        color: black;
        border-radius: 12px;
        border: none;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        width: 100%;
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

