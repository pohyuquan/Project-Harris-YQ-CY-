import folium

m = folium.Map([41.789621, -87.596398],
               tiles='cartodbpositron',
               zoom_start=10, max_zoom=14, min_zoom=4)

folium.Marker(location=[41.789621, -87.596398], popup='University of Chicago').add_to(m)
folium.ClickForMarker(popup='Waypoint')

m.save("contact_us.html")
