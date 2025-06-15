import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """

Use the map below to **draw a polygon** (e.g., field boundary or affected area).
    The map is using **Esri World Imagery** as a basemap.
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Plant Disease Prediction Map")

# Create the interactive map
m = leafmap.Map(center=[38.14306249508979, -102.61118888854982], zoom=15.0, draw_export=True)
m.add_basemap("Esri.WorldImagery")  # Add satellite imagery
m.to_streamlit(height=600)



