import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """

Use the map below to **draw a polygon** (e.g., field boundary or affected area).
    The map is using **Esri World Imagery** as a basemap.

A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Plant Disease Prediction Map")

# Create the interactive map
m = leafmap.Map(center=[38.5, -98.0], zoom=5, draw_export=True)
m.add_basemap("Esri.WorldImagery")  # Add satellite imagery
m.to_streamlit(height=600)



