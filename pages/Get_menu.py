import streamlit as st
import streamlit.components.v1 as components
import os
import util

# Use the existing "menus" folder inside your project
SAVE_DIR = "menus"
os.makedirs(SAVE_DIR, exist_ok=True)  # Ensure the folder exists

st.title("🍽️ Custom Restaurant Menu Builder")

# Sidebar Inputs
cuisine = st.sidebar.selectbox("Select Cuisine", ["Italian", "Chinese", "Indian", "Mexican"])
restaurant_name = st.sidebar.text_input("Enter Restaurant Name", placeholder="e.g. Tasty Bites")

if "menu_items" not in st.session_state:
    st.session_state.menu_items = []

menu_items = st.session_state.menu_items

# Add Menu Items
item_name = st.sidebar.text_input("Item Name", placeholder="e.g. Margherita Pizza")
item_price = st.sidebar.number_input("Price (₹)", min_value=0.0, format="%.2f")
if st.sidebar.button("➕ Add Item"):
    menu_items.append({"name": item_name, "price": item_price})
    st.sidebar.success(f"Added {item_name}!")

# Display Menu Items
if menu_items:
    st.sidebar.write("### 📜 Menu Items")
    for item in menu_items:
        st.sidebar.write(f"🍽️ {item['name']} - ₹{item['price']:.2f}")

# Generate Menu
if st.button("Generate Menu"):
    menu_html = util.get_menu(cuisine, restaurant_name, menu_items)
    st.session_state.menu_html = menu_html  # Store in session state
    components.html(menu_html, height=1000, width=1000, scrolling=True)

    # **Save to Existing "menus/" Folder**
    file_path = os.path.join(SAVE_DIR, f"{restaurant_name}_menu.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(menu_html)

# **Download from "menus/" Folder**
if "menu_html" in st.session_state:
    file_path = os.path.join(SAVE_DIR, f"{restaurant_name}_menu.html")

    with open(file_path, "rb") as f:
        st.download_button("📥 Download Menu (HTML)", f, file_name=f"{restaurant_name}_menu.html", mime="text/html")
