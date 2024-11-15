import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to fetch weather data for a specific city using its URL
def get_weather_data(url):
    try:
        # Send HTTP request to get the page content
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract city name
            city_name = soup.find('span', class_='styles--locationName--zoGXR')
            
            # Extract temperature
            temp = soup.find('span', class_='styles--temperature--aIAgZ')
            
            # If both city name and temperature are found, return their text
            if city_name and temp:
                weather_info = {
                    'City': city_name.text.strip(),
                    'Temperature': temp.text.strip()
                }
                return weather_info
            else:
                return {"Error": "Weather data not found"}
        else:
            return {"Error": "Failed to retrieve data"}
    
    except Exception as e:
        return {"Error": f"Exception occurred: {str(e)}"}

# URL for Karachi's weather page
karachi_url = 'https://weather.com/weather/today/l/0ee297022f3da5058fdc66e432a545093212ba9de0b471f2e15d3aae60e5744a'

# URL for Faisalabad's weather page
faisalabad_url = 'https://weather.com/weather/today/l/60a7f149e5614edc0cbad0e18f3c59fad074023ec4f5d483d9d58762bb07f587'

# URL for Lahore's weather page (add Lahore's URL)
lahore_url = 'https://weather.com/weather/today/l/600747e08521c7c7642ee7d2c87ee6e6b126ea4048677df1c2367181527dd1ed'

# Fetch weather data for Karachi, Faisalabad, and Lahore
karachi_weather = get_weather_data(karachi_url)
faisalabad_weather = get_weather_data(faisalabad_url)
lahore_weather = get_weather_data(lahore_url)

# Streamlit UI
st.title('Weather Data for Karachi, Faisalabad, and Lahore')

# Display Karachi weather info
if "Error" not in karachi_weather:
    st.subheader(f"Weather in {karachi_weather['City']}")
    st.write(f"Temperature: {karachi_weather['Temperature']}")
else:
    st.write(karachi_weather['Error'])

# Display Faisalabad weather info
if "Error" not in faisalabad_weather:
    st.subheader(f"Weather in {faisalabad_weather['City']}")
    st.write(f"Temperature: {faisalabad_weather['Temperature']}")
else:
    st.write(faisalabad_weather['Error'])

# Display Lahore weather info
if "Error" not in lahore_weather:
    st.subheader(f"Weather in {lahore_weather['City']}")
    st.write(f"Temperature: {lahore_weather['Temperature']}")
else:
    st.write(lahore_weather['Error'])