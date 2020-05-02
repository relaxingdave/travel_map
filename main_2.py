import folium
from openrouteservice import client

from route_params import (tooltip_dict, coordinates_dict, blog_list,
    blog_links, blog_names)

DEFAULT_LOC = [-4.103753, -81.044672]
api_key = '5b3ce3597851110001cf6248b560c2165259434bb980d7e91b7fdcab'
clnt = client.Client(key=api_key)  # Create client with api key

# split route into parts since only 6000 km can be queried
# highest number should be last stop of total route + 1
split_tuples = [
    range(1, 10),
    range(10, 20),
    range(20, 30),
    range(30, 40)
]

def style_route(color):
    return lambda feature: dict(color=color,
                                weight=3,
                                opacity=0.5)


# TODO hiearchy of labels higher than route and circles
# TODO hack to search for complete route. now, routes between e.g. 9 and 10 missing! slightly modify start for 10?

# initialize mapbox satellite map
tile = "https://api.mapbox.com/styles/v1/horstibo/cjzfzikmy07ao1cnsdetakzcp/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiaG9yc3RpYm8iLCJhIjoiY2p6Zzd0N2k4MGhndTNubnJlbjJpYXA0aiJ9.CH9pLMpXzoH9igV5pGn0jQ"
m = folium.Map(
    location=DEFAULT_LOC,
    zoom_start=5,
    tiles=tile,
    attr='Mapbox')


# circles for stays
coord_len = len(coordinates_dict)
for i in (list(range(1, coord_len))):

    folium.CircleMarker(
        radius=4,
        location=coordinates_dict[i],
        popup=tooltip_dict[i],
        color='crimson',
        fill=True,
    ).add_to(m)


# create markers and links to log articles.
# coordinates has to be selected by blog_list entry (the coordinate), whilst
# blog_names and links are only lists of the blog articles.
for n, b in enumerate(blog_list):
    marker_name = "Artikel " + tooltip_dict[b]
    folium.Marker(
        coordinates_dict[b],
        folium.Popup(f"""<a href="{blog_links[n]} "target="_blank"> {blog_names[n]} </a>"""),
        tooltip=blog_names[n]).add_to(m)


# iterate over coordinate splits (maximum of 6000km is processed by ors)
for s in split_tuples:
    selected_keys = list(s)

    # coordinates have to be in reversed order for ors
    # radius is the maximum distance from the location to a road
    route_points = []
    radiuses = []

    # iterate over coordinates
    for key in selected_keys:
        coordinates_dict[key].reverse()
        route_points.append(coordinates_dict[key])
        radiuses.append(2000)

    # compute route for split
    request_params = {
        'coordinates': route_points,
        'radiuses': radiuses,
        'format_out': 'geojson',
        'profile': 'driving-car',
        'preference': 'shortest',
        'instructions': 'false'
    }
    route = clnt.directions(**request_params)
    folium.features.GeoJson(data=route,
                            name='Route',
                            style_function=style_route('#FF0000'),
                            overlay=True).add_to(m)

m.save('newtest.html')
