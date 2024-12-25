import requests
import folium
import webbrowser

# Step 1: Get public IP
def get_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json()["ip"]
    except:
        print("Failed to get IP")
        return None

# Step 2: Get location data
def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return data if data["status"] == "success" else None
    except:
        print("Failed to get location")
        return None

# Step 3: Show map
def show_map(lat, lon, city):
    my_map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup=city).add_to(my_map)
    my_map.save("map.html")
    webbrowser.open("map.html")

# Main program
def main():
    print("Getting your location...")
    ip = get_ip()
    if not ip:
        return print("Could not get IP.")

    location = get_location(ip)
    if not location:
        return print("Could not get location.")

    print(f"City: {location['city']}, Country: {location['country']}")
    print(f"Coordinates: {location['lat']}, {location['lon']}")
    show_map(location["lat"], location["lon"], location["city"])

main()
