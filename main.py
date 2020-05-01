import folium
from openrouteservice import client

from route_params import names_dict, tooltip_dict, coordinates_dict

DEFAULT_LOC = [-4.103753, -81.044672]
api_key = '5b3ce3597851110001cf6248b560c2165259434bb980d7e91b7fdcab'
clnt = client.Client(key=api_key)  # Create client with api key


def style_route(color):
    return lambda feature: dict(color=color,
                                weight=3,
                                opacity=0.5)


# TODO create points directly from coordinates

route = [(-0.148817, -78.441441),
         (0.805646, -77.585560),
         (1.262471, -77.285087),
         (2.614479, -76.464835),
         (4.635837, -75.571897),
         (5.020810, -75.436550),
         (6.230270, -75.490612),
         (6.222607, -75.247956),
         (9.782041, -75.872093),
         (9.527937, -75.582389),
         (10.392408, -75.478310),
         (11.142307, -74.116795),
         (11.262063, -73.582315),
         (11.306578, -74.065735),
         (6.635837, -73.223497),
         (5.021684, -74.006458),
         (4.711236, -74.076193),
         (1.879869, -76.270277),
         (2.354453, -76.495912),
         (1.045381, -77.149888),
         (0.825578, -77.641045),
         (0.346814, -78.132687),
         (0.234532, -78.260937),
         (-0.148817, -78.441441),
         (-0.054427, -78.775578),
         (-0.993734, -80.855599),
         (-2.189082, -79.896047),
         (-0.742243, -90.316072),
         (-2.189082, -79.896047),
         (-0.871530, -78.899970),
         (-0.699945, -78.886296),
         (-1.471576, -78.822819),
         (-1.392466, -78.426375),
         (-1.033614, -77.669724),
         (-2.963455, -78.427225),
         (-2.900669, -79.006375),
         (-4.103753, -81.044672),
         (-8.106723, -79.032320),
         (-9.051385, -77.794601)
         ]

# lon and lat are switched in open route service

# TODO create coordinates list, this can be used: list(reversed(site_coords)
# TODO hiearchy of labels higher than route and circles
# TODO create loop for creating coordinates
request_params = {
    'coordinates': route,
    'format_out': 'geojson',
    'profile': 'driving-car',
    'preference': 'shortest',
    'instructions': 'false'
}


# mapbox satellite map
tile = "https://api.mapbox.com/styles/v1/horstibo/cjzfzikmy07ao1cnsdetakzcp/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiaG9yc3RpYm8iLCJhIjoiY2p6Zzd0N2k4MGhndTNubnJlbjJpYXA0aiJ9.CH9pLMpXzoH9igV5pGn0jQ"
m = folium.Map(
    location=DEFAULT_LOC,
    zoom_start=5,
    tiles=tile,
    attr='Mapbox')


route_normal = clnt.directions(**request_params)
folium.features.GeoJson(data=route_normal,
                        name='Route without construction sites',
                        style_function=style_route('#FF0000'),
                        overlay=True).add_to(m)

# for loop
coord_len = len(coordinates_dict)

for i in (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22,
        23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39):

    folium.CircleMarker(
        radius=3,
        location=coordinates_dict[i],
        popup=tooltip_dict[i],
        color='crimson',
        fill=True,
    ).add_to(m)


# folium.PolyLine(route).add_to(m)

m.save('newtest.html')
