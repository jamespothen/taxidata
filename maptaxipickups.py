import folium

infile = open("taxipickup2011totals.csv", "r")


m = folium.Map(location=[40.783060, -73.971249], tiles="Stamen Toner", zoom_start=12)

for line in infile:
    longitude = float(line.split(",")[0].strip("\ufeff"))
    latitude = float(line.split(",")[1].strip("\ufeff"))

    print(longitude)
    print(latitude)
    print()

    folium.CircleMarker(
        location=[latitude, longitude],
        radius=0.5,
        color="#3186cc",
        fill=True,
        fill_color="#3186cc",
    ).add_to(m)

print("Saving map...")
m.save("pickups2011map.html")
print("Saved!")
infile.close()
