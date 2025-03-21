import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

# Set page configuration
st.set_page_config(page_title="Dishly - Your Restaurant Business Partner", page_icon="🍽", layout="centered")# Title and Subtitle
st.title("🍽 Welcome to Dishly – Your Ultimate Restaurant Business Partner!")
st.markdown(
    """
    Starting a new restaurant business? **Dishly** is here to help!  
    Whether you’re looking for the perfect **restaurant name**, a **customized menu**,  
    or **dish recommendations** based on available ingredients, we’ve got you covered. 🚀  
    """
)

# Features Section
st.subheader("What Dishly Offers:")
st.markdown(
    """
    - 🍽 **Unique Restaurant Name Ideas** – Stand out with a catchy and memorable name.  
    - 📜 **Personalized Menu Creation** – Design a menu that suits your vision and target audience.  
    - 🥗 **Smart Dish Suggestions** – Enter the ingredients you have, and we’ll suggest the best dishes along with their recipes.  
    """
)

# Call to Action
st.markdown("### Ready to bring your restaurant vision to life?")
st.button("🚀 Get Started Now")
