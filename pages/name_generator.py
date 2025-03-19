import streamlit as st
import Dishly
import util

st.sidebar.header("**Dishly**")
cuisine=st.sidebar.selectbox("Select the cuisine for your Restaurant", (
    "North Indian", "South Indian", "Punjabi", "Bengali", "Gujarati",  
    "Rajasthani", "Maharashtrian", "Hyderabadi", "Kashmiri",  
    "Chettinad", "Goan", "Malabari", "Awadhi", "Bihari", "Odia",  
    "Assamese", "Naga", "Manipuri", "Mizo", "Sikkimese", "Uttarakhandi", "American", "Italian", "Mexican", 
    "Chinese", "Japanese", "Thai", "French", "Mediterranean", 
    "Middle Eastern", "Greek", "Spanish", "Korean", "Vietnamese", 
    "Brazilian", "Caribbean", "German", "Turkish"
))

if st.sidebar.button("Get Name for Restaurant"):
        st.title(f"🧑‍🍳Some suggested Names for your {cuisine} Restaurant are :")
        st.write(util.get_name(cuisine))
st.sidebar.write("")
if st.sidebar.button("Get Menu Items for Restaurant"):
        st.title(f"🥗Some suggested Dishes for your {cuisine} Restaurant are :")
        st.write(util.get_menu_items(cuisine))

st.sidebar.empty()

