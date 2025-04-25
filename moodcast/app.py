import streamlit as st
from sentiment_analyzer import get_sentiment
from weather_fetcher import get_weather
from spotify_recommender import get_recommendations
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MoodCast 🎶", page_icon="🌤️")

st.title("🌤️ MoodCast - Music Recommender 🎧")
st.markdown("Get music suggestions based on your mood and weather!")

# Inputs
city = st.text_input("📍 Enter your city:")
mood_input = st.text_area("🧠 Describe your current mood:")

if st.button("Get Recommendations"):
    if city and mood_input:
        with st.spinner("Analyzing..."):
            mood, confidence = get_sentiment(mood_input)
            weather_desc, temperature, humidity = get_weather(city)
            tracks = get_recommendations(mood, weather_desc)

        st.success(f"Detected Mood: **{mood}** ({confidence:.2%} confidence)")
        st.info(f"Weather in {city}: **{weather_desc.capitalize()}**, {temperature}°C")

        st.subheader("🎵 Music Recommendations:")
        for i, track in enumerate(tracks, 1):
            st.write(f"{i}. [{track['name']}]({track['url']}) by {', '.join(track['artists'])}")
    else:
        st.warning("Please enter both city and mood.")


