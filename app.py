import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai



load_dotenv()
api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=api_key)


# for m in genai.list_models():
#     print(m.name, "→", m.supported_generation_methods)


model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # ✅ Updated syntax
# response = model.generate_content("Say hello")
# print(response.text)


# Configure the Gemini SDK:
# Google Generative AI SDK (google-generativeai) is the Python package provided by Google to help you:

# Connect to Gemini models
# Send prompts
# Receive and process AI-generated responses
# Handle authentication (like API keys)
# Instead of writing complex code to hit REST APIs manually, the SDK does the heavy lifting for you.

# REST API stands for Representational State Transfer Application Programming Interface. It's a 
# way for two systems to talk to each other over the internet, usually using HTTP (like how your browser talks to websites).

#Streamlit
# ---- UI Layout ---- #
st.set_page_config(page_title="Foram's Recipe Recommender", page_icon="🍳", layout="centered")

st.title("🍳 Foram's Recipe Recommender")
st.markdown("Your AI sous-chef powered by Gemini 🔮")

# Sidebar filters
with st.sidebar:
    st.header("🍽️ Preferences")
    meal_type = st.selectbox("Meal Type", ["Any", "Breakfast", "Lunch", "Dinner", "Snack"])
    cuisine = st.multiselect("Cuisine Preferences", ["Indian", "Italian", "Chinese", "Mexican", "American"])
    diet = st.radio("Dietary Preference", ["None", "Vegan", "Vegetarian", "Gluten-Free"])

# Main input
user_input = st.text_input("Enter the ingredients you have or the type of meal you want:", placeholder="e.g., chicken, tomatoes, garlic")

if st.button("Get Recipe"):
    if user_input:
        with st.spinner("Cooking up your recipe..."):
            prompt = f"Give me a {meal_type.lower()} recipe using the following ingredients: {user_input}.\nCuisine: {', '.join(cuisine) if cuisine else 'Any'}, Diet: {diet}. Format the response with a title, ingredients, and steps."
            try:
                response = model.generate_content(prompt)
                if response.text:
                    st.markdown("### 🍽️ Recipe Suggestion")
                    st.write(response.text)
                else:
                    st.warning("Received an empty response. Try again.")
            except Exception as e:
                st.error(f"Error generating recipe: {e}")
    else:
        st.warning("Please enter some ingredients or a meal type.")
