import streamlit as st
from openai import OpenAI

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="RAGHAV REALTY SEO Generator",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 RAGHAV REALTY AI SEO Generator")
st.markdown("Generate SEO titles, meta descriptions, keywords & hashtags instantly.")

# ----------------------------
# API CONFIG
# ----------------------------
client = OpenAI(
    api_key=st.secrets["GROK_API_KEY"],
    base_url="https://api.x.ai/v1"
)

# ----------------------------
# FORM INPUTS
# ----------------------------
with st.form("seo_form"):

    project_name = st.text_input("Project Name")

    city = st.selectbox(
        "City",
        [
            "Mumbai",
            "Pune",
            "Delhi",
            "Bangalore",
            "Jaipur",
            "Ahmedabad"
        ]
    )

    micro_market = st.text_input(
        "Micro Market (e.g. Andheri East)"
    )

    project_type = st.selectbox(
        "Project Type",
        [
            "Residential",
            "Commercial",
            "Mixed"
        ]
    )

    configuration = st.multiselect(
        "Configuration",
        [
            "1 BHK",
            "2 BHK",
            "3 BHK",
            "4 BHK",
            "Office",
            "Retail"
        ]
    )

    landmarks = st.text_input(
        "Nearby Landmarks (optional)"
    )

    brand_positioning = st.selectbox(
        "Brand Positioning",
        [
            "Luxury",
            "Premium",
            "Affordable",
            "Ultra Luxury"
        ]
    )

    usp = st.text_area(
        "USP (Unique Selling Proposition)"
    )

    submit = st.form_submit_button(
        "Generate SEO Content"
    )

# ----------------------------
# GENERATE OUTPUT
# ----------------------------
if submit:

    prompt = f"""
    You are an expert real estate SEO strategist.

    Generate:

    1. 5 SEO Titles
    2. 3 Meta Descriptions
    3. 10 SEO Keywords
    4. 10 Social Media Hashtags

    Project Details:

    Project Name: {project_name}
    City: {city}
    Micro Market: {micro_market}
    Project Type: {project_type}
    Configuration: {configuration}
    Nearby Landmarks: {landmarks}
    Brand Positioning: {brand_positioning}
    USP: {usp}

    Make content optimized for:
    - Google SEO
    - Instagram discoverability
    - LinkedIn engagement
    """

    with st.spinner("Generating AI SEO content..."):

        response = client.chat.completions.create(
            model="grok-3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

    st.success("Generated successfully!")
    st.markdown(result)
