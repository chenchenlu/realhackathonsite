from flask import Flask
import folium 
import pandas

app = Flask(__name__)
data=pandas.read_csv('Benches_Coordinates.csv')

LAT=list(data['Latitude'])
LON=list(data['Longitude'])
name=list(data['Name'])
start_coords = [42.447285, -76.484052]
# capacity=list(data['capacity'])
website=list(data['Website'])
# picture=list(data['picture'])

fg=folium.Map(location=start_coords, zoom_start=17)
# fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))


 
for lt,ln,nm,ws in zip(LAT,LON,name,website):
 	fg.add_child(folium.Marker(location=[lt,ln],popup="<b>Name  : </b>"+nm + "<br><b>Directions: </b><a href="+ws+">click here</a>",icon=folium.Icon(color='green')))


fg.save('/Users/jialichen/Desktop/hackathon_site/cumap.html')
