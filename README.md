# RAGHAV-SEO-STUDIO
Generate instant SEO-ready marketing content for each new project launch.
import streamlit as st
from utils.grok_client import generate_seo

st.title("🏢 Real Estate SEO Generator")

project_name = st.text_input("Project Name")

city = st.selectbox(
    "City",
    ["Mumbai","Pune","Bangalore","Delhi","Jaipur"]
)

micro_market = st.text_input("Micro Market")

project_type = st.selectbox(
    "Project Type",
    ["Residential","Commercial","Mixed"]
)

configuration = st.multiselect(
    "Configuration",
    ["1BHK","2BHK","3BHK","4BHK","Office","Retail"]
)

landmarks = st.text_input("Nearby Landmarks")

brand_positioning = st.selectbox(
    "Brand Positioning",
    ["Luxury","Premium","Affordable","Ultra Luxury"]
)

usp = st.text_area("USP")

if st.button("Generate SEO Content"):
    result = generate_seo(
        project_name,
        city,
        micro_market,
        project_type,
        configuration,
        landmarks,
        brand_positioning,
        usp
    )
    
    st.markdown(result)
