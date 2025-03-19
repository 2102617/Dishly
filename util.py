import os
import key 
from langchain_groq import ChatGroq
from transformers import pipeline

llm1=ChatGroq(
    model_name="llama3-8b-8192",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=3,
    api_key=key.Dishly_key
    )
# Test the model
def get_name(cuisine):
    return llm1.invoke(f"Generate a unique and catchy {cuisine} restaurant name that is creative, memorable, and suitable for a modern dining experience.").content

def get_menu_items(cuisine):
    return llm1.invoke(f"List the food items for a traditional {cuisine} restaurant.. Include a variety of dishes under the categories: Appetizers, Main Courses, Desserts, and Beverages.") 

def get_menu(cuisine, name, items):
    prompt = f"""
Generate a **fully styled and visually appealing restaurant menu** for a {cuisine} restaurant named "{name}" in **HTML format** with **inline CSS**.

### **Requirements:**
- A **prominent header** displaying "{name}" in a stylish font.
- **Only display** the following dishes: {items}, with:
  - **Dish Name** (bold and readable)
  - **Short Description** (concise and engaging)
  - **Price** (formatted properly with currency symbol)
  - **Image URL** (in a proper `<img>` tag with appropriate size & aspect ratio)
  - **Valid Image URLs** from reliable sources (DO NOT generate non-working or fake URLs).
  - Example image URLs:
    - Use `https://source.unsplash.com/300x200/?food,{cuisine}`
- Ensure all images are:
  - Availbale for public display
  - Displayed at a consistent size (e.g., width: 150px, height: auto)
  - Aligned properly with the menu items
- The menu should have:
  - A **color scheme** complementing {cuisine} cuisine (use warm, inviting colors)
  - **Well-structured layout** with clear section spacing
  - **Hover effects** for improved UI experience
  - **Padding, borders, and alignment** for readability
- The output must be **fully structured HTML with inline CSS**, directly renderable in `components.html(menu_html, height=1000, scrolling=True)`.
- **NO explanations, no preamble/postamble. Only return valid HTML.**

### **Output Format:**
- Start directly with `<html>`, no introductory text.
- End directly after `</html>`, with no extra content.
"""

    response = llm1.invoke(prompt)
    return response.content
