import streamlit as st
import random

st.set_page_config(page_title="Islamic Guidance", layout="centered")

st.title("Islamic Guidance & Reflection ✨")
st.markdown("""
Welcome to your spiritual companion. Explore uplifting Islamic quotes, make Du'a requests, and learn from the teachings of the Prophet Muhammad (PBUH).

🌙 **Feel at peace, stay connected with your faith.** 🌙
""")

page = st.radio("Navigate through:", ["Home", "Islamic Quotes", "Request Du'a", "Hadiths"])

if page == "Home":
    st.subheader("✨ Your Source of Islamic Reflection ✨")
    st.markdown("""
    Welcome to your **Islamic Guidance Portal**. Here you will find resources to help you reflect on faith and stay connected with the teachings of Islam.

    - 🌸 **Islamic Quotes**: Uplifting verses and sayings from the Quran and Hadith.
    - 🤲 **Du'a Requests**: Share your supplications, and let's make Du'a together.
    - 🕌 **Hadiths**: Learn from the sayings and actions of Prophet Muhammad (PBUH).

    📖 *"Indeed, with hardship comes ease."* — **Quran 94:6**

    Take a moment to reflect and connect with the beauty of your faith. ✨
    """)

elif page == "Islamic Quotes":
    st.subheader("Islamic Quotes for Reflection 🌙")
    quotes = [
        "The best of people are those that bring the most benefit to the rest of mankind. - Prophet Muhammad (PBUH)",
        "Whoever does good, Allah will reward him with more than what he has done. - Quran 16:97",
        "Indeed, with hardship comes ease. - Quran 94:6",
        "The believer is like a plant that grows when watered. - Imam Ali (AS)",
        "And hold firmly to the rope of Allah all together and do not become divided. - Quran 3:103"
    ]
    st.write(random.choice(quotes))

elif page == "Request Du'a":
    st.subheader("Submit Your Du'a Request 🤲")
    du_a_request = st.text_area("Write your Du'a request here", placeholder="Ask for blessings, forgiveness, or any need.")
    if st.button("Submit Du'a"):
        if du_a_request:
            st.success("🤲 Your Du'a has been submitted. May Allah grant your request, Ameen!")
        else:
            st.error("Please enter a Du'a request.")

elif page == "Hadiths":
    st.subheader("Hadiths from Prophet Muhammad (PBUH) 🌙")
    hadiths = [
        "The best of people are those that bring the most benefit to the rest of mankind. - Prophet Muhammad (PBUH)",
        "Whoever shows you the way to good, you should reward them. - Prophet Muhammad (PBUH)",
        "A believer is not one who eats his fill while his neighbor goes hungry. - Prophet Muhammad (PBUH)",
        "Seek knowledge from the cradle to the grave. - Prophet Muhammad (PBUH)",
        "The strong person is not the one who can overpower others, but the one who controls themselves when angry. - Prophet Muhammad (PBUH)",
        "The five daily prayers remove sins just as water removes dirt. - Prophet Muhammad (PBUH)",
        "Whoever builds a mosque for the sake of Allah, Allah will build for him a house in Paradise. - Prophet Muhammad (PBUH)",
        "None of you truly believes until he loves for his brother what he loves for himself. - Prophet Muhammad (PBUH)"
    ]
    st.write(random.choice(hadiths))

st.markdown("---")
st.markdown("Made with ❤️ by [Muhammad Rayyan]. Powered by Streamlit.")
