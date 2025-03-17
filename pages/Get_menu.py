import streamlit as st
import pandas as pd
import numpy as np
import util

st.title("🍽️ Custom Restaurant Menu Builder")

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

if menu_items:
    st.sidebar.write("### 📜 Menu Items")
    for item in menu_items:
        st.sidebar.write(f"🍽️ {item['name']} - 💲{item['price']:.2f}")
else:
    st.sidebar.info("No items in the menu yet. Add some from above!")

if st.sidebar.button("Generate you custom menu"):
    st.switch_page("pages.Get_menu")