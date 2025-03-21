import streamlit as st
import os
import util

# Initialize session state for dish items
if "dish_items" not in st.session_state:
    st.session_state.dish_items = []

st.title("🍽️ Ingredient-Based Dish Recommender")

st.sidebar.header("📝 Add Available Ingredients")
item_name = st.sidebar.text_input("Item Name", placeholder="e.g. Paneer, Carrot, Rice")

# Add item only if it's not empty and not already added
if st.sidebar.button("➕ Add Item"):
    if item_name.strip() and item_name not in [item["name"] for item in st.session_state.dish_items]:
        st.session_state.dish_items.append({"name": item_name})
        st.sidebar.success(f"Added {item_name}!")
    elif not item_name.strip():
        st.sidebar.warning("⚠️ Please enter an ingredient name.")
    else:
        st.sidebar.warning("⚠️ This item is already added.")

# Display added ingredients with remove option
if st.session_state.dish_items:
    st.sidebar.write("### 📜 Your Ingredients")
    for item in st.session_state.dish_items:
        col1, col2 = st.sidebar.columns([3, 1])
        col1.write(f"🍽️ {item['name']}")
        if col2.button("❌", key=item["name"]):
            st.session_state.dish_items.remove(item)

if st.sidebar.button("🍛 Get Dish Suggestions"):
    st.write(util.get_dishes(st.session_state.dish_items))