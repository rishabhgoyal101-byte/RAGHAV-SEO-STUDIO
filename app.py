import streamlit as st
from groq import Groq

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
    .stTextInput input, .stTextArea textarea {
        border-radius: 10px;
    }
    .block-container {
        padding-top: 2rem;
        max-width: 1000px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------
st.markdown('<div class="main-title">RAGHAV REALTY</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered SEO & Hashtag Generator for New Project Launches</div>', unsafe_allow_html=True)

# ----------------------------
# API CONFIG
# ----------------------------
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

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

# ----------------------------
# GENERATE OUTPUT
# ----------------------------
if submit:
    prompt = f"""
    You are an expert luxury real estate SEO strategist for India.

    Generate:
    1. 5 SEO Titles
    2. 3 Meta Descriptions
    3. 10 SEO Keywords
    4. 10 Premium Social Media Hashtags

    Project Details:
    Project Name: {project_name}
    City: {city}
    Micro Market: {micro_market}
    Project Type: {project_type}
    Configuration: {configuration}
    Nearby Landmarks: {landmarks}
    Brand Positioning: {brand_positioning}
    USP: {usp}

    Use premium, luxury-focused language optimized for Google SEO and social media.
    """

    with st.spinner("Generating premium SEO content..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content

    st.success("SEO content generated successfully!")
    st.markdown(result)
