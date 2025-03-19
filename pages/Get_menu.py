import streamlit as st
import pandas as pd
import numpy as np
import util
import streamlit.components.v1 as components
import pdfkit
st.page_link("pages/Get_menu.py", label="Generate Menu")
st.title("🍽️ Custom Restaurant Menu Builder")

cuisine=st.sidebar.selectbox("Select the cuisine for your Restaurant", (
    "North Indian", "South Indian", "Punjabi", "Bengali", "Gujarati",  
    "Rajasthani", "Maharashtrian", "Hyderabadi", "Kashmiri",  
    "Chettinad", "Goan", "Malabari", "Awadhi", "Bihari", "Odia",  
    "Assamese", "Naga", "Manipuri", "Mizo", "Sikkimese", "Uttarakhandi", "American", "Italian", "Mexican", 
    "Chinese", "Japanese", "Thai", "French", "Mediterranean", 
    "Middle Eastern", "Greek", "Spanish", "Korean", "Vietnamese", 
    "Brazilian", "Caribbean", "German", "Turkish"
))

st.sidebar.header("📝 Restaurant Setup")
restaurant_name = st.sidebar.text_input("Enter your Restaurant Name", placeholder="e.g. Tasty Bites")

if "menu_items" not in st.session_state:
    st.session_state.menu_items = []

menu_items = st.session_state.menu_items

st.sidebar.header("📌 Add Menu Items")
item_name = st.sidebar.text_input("Item Name", placeholder="e.g. Margherita Pizza")
item_price = st.sidebar.number_input("Price ($)", min_value=0.0, format="%.2f")
add_item = st.sidebar.button("➕ Add Item")

if add_item and item_name:
    menu_items.append({"name": item_name, "price": item_price})
    st.sidebar.success(f"Added {item_name}!")
    st.write(menu_items)

if menu_items:
    st.sidebar.write("### 📜 Menu Items")
    for item in menu_items:
        st.sidebar.write(f"🍽️ {item['name']} - ₹{item['price']:.2f}")
else:
    st.sidebar.info("No items in the menu yet. Add some from above!")

if st.sidebar.button("Generate you custom menu"):
    st.switch_page("pages.Get_menu")

    

if st.button("Generate menu"):
    menu_html = util.get_menu(cuisine, restaurant_name, menu_items)  
    components.html(menu_html, height=1000, scrolling=True)

    st.markdown("### Download Menu as PDF")
    
    if st.button("Download PDF"):
        pdfkit.from_string(menu_html, "menu.pdf")
        with open("menu.pdf", "rb") as f:
            st.download_button("Click to Download", f, file_name="menu.pdf", mime="application/pdf")




