# MoodCast-Weather-Music-Matcher

# MoodCast - Weather Based Mood and Music Recommender 🎭🌦️🎶

MoodCast is a simple, fun app that detects your mood using text sentiment analysis, 
fetches current weather, and recommends the perfect Spotify playlist based on both! 🎵✨

---

## 🚀 Features

- 📝 **Sentiment Analysis** using HuggingFace Transformers
- 🌦️ **Weather Detection** via OpenWeatherMap API
- 🎶 **Spotify Playlist Recommendation** tailored to mood and weather
- ⚡ Built with **Python** and **Streamlit** for a fast, interactive web experience

---
## This project helped me explore:

-API integration & modular design in Python
-Combining emotion AI with real-time data
-Clean UI/UX using Streamlit for demos

---
## 🏛️ Project Structure

moodcast/
├── app.py                  👈 Streamlit main app
├── sentiment_analyzer.py   👈 Sentiment using HuggingFace
├── weather_fetcher.py      👈 Weather via OpenWeatherMap
├── spotify_recommender.py  👈 Spotify playlist suggester
├── .env                    👈 Your API keys
├── requirements.txt

---
## Launch the Streamlit app:
streamlit run app.py

## 📚 Built With
Python 
Streamlit
HuggingFace Transformers 
OpenWeatherMap API 
Spotify Web API 
