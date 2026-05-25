import streamlit as st
import requests
from datetime import datetime

api_key = "ee67c7c2b8de5452c7cb27021bb3ab7d"

st.title("🌤 Weather App (Streamlit Version)")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city == "":
        st.error("❌ Please enter a city name")

    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            weather = data["weather"][0]["main"]

            # Emoji
            if weather == "Clear":
                emoji = "☀"
            elif weather == "Rain":
                emoji = "🌧"
            elif weather == "Clouds":
                emoji = "☁"
            elif weather == "Thunderstorm":
                emoji = "⛈"
            else:
                emoji = "🌈"

            # Sunrise & Sunset
            sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p")
            sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p")

            # Rain check
            rain_data = data.get("rain")
            rain_status = "🌧 Rain Possible" if rain_data else "☀ Low Rain Chance"

            st.success(f"{emoji} Weather Report")

            st.write(f"📍 City: {city}")
            st.write(f"🌡 Temperature: {data['main']['temp']} °C")
            st.write(f"💧 Humidity: {data['main']['humidity']} %")
            st.write(f"🤗 Feels Like: {data['main']['feels_like']} °C")
            st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
            st.write(f"🌅 Sunrise: {sunrise}")
            st.write(f"🌇 Sunset: {sunset}")
            st.write(rain_status)

        else:
            st.error(f"❌ Error: {data.get('message', 'City not found')}")