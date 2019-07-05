import pandas as pd
import folium

df_volcano = pd.read_csv("Volcanoes.txt")

lat = list(df_volcano["LAT"])
lon = list(df_volcano["LON"])
elev = list(df_volcano["ELEV"])
name = list(df_volcano["NAME"])


def color_map(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'red'
    else:
        return 'orange'


html = """Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

m1 = folium.Map(location=[48, -102], zoom_start=3)

fgv = folium.FeatureGroup(name="Volcano Map")
for lat, lon, elev, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fgv.add_child(
        folium.CircleMarker(location=(lat, lon), popup=folium.Popup(iframe), radius=7, fill_color=color_map(elev),
                            color='grey',
                            fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

m1.add_child(fgv)
m1.add_child(fgp)
m1.add_child(folium.LayerControl())
m1.save("Map.html")
