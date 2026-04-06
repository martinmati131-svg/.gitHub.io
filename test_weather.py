import requests
import sys

def test_juja_weather_api():
    # Juja Coordinates
    lat, lon = -1.1026, 37.0149
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Check if temperature data exists
        if "current" in data and "temperature_2m" in data["current"]:
            print(f"✅ Weather API is Online. Juja Temp: {data['current']['temperature_2m']}°C")
            return True
        else:
            print("❌ API Response format unexpected.")
            return False
            
    except Exception as e:
        print(f"❌ API Test Failed: {e}")
        return False

if __name__ == "__main__":
    if test_juja_weather_api():
        sys.exit(0) # Success
    else:
        sys.exit(1) # Failure - Stops the CI/CD pipeline
