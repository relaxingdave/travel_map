#
# https://openrouteservice.org/example-avoid-obstacles-while-routing/

import json
import requests

import folium
# import pyproj
# from shapely import geometry
# from shapely.geometry import Point, LineString, Polygon, MultiPolygon

from openrouteservice import client

# create folium map


# ESRI satellite map
# m = folium.Map(
# 	location= [-4.103753, -81.044672],
# 	zoom_start=6,
# 	attr="ESRI")

# tile = folium.TileLayer(
#         tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#         attr='Esri',
#         name='Esri Satellite',
#         overlay=False,
#         control=True
#        ).add_to(m)

# mapbox satellite map
# tile ="https://api.mapbox.com/styles/v1/horstibo/cjzfzikmy07ao1cnsdetakzcp/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiaG9yc3RpYm8iLCJhIjoiY2p6Zzd0N2k4MGhndTNubnJlbjJpYXA0aiJ9.CH9pLMpXzoH9igV5pGn0jQ"
tile = "https://api.mapbox.com/styles/v1/horstibo/cjzfzikmy07ao1cnsdetakzcp/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiaG9yc3RpYm8iLCJhIjoiY2p6Zzd0N2k4MGhndTNubnJlbjJpYXA0aiJ9.CH9pLMpXzoH9igV5pGn0jQ"
m = folium.Map(
    location=[-4.103753, -81.044672],
    zoom_start=6,
    tiles=tile,
    attr='Mapbox')


def style_function(color):
    return lambda feature: dict(color=color,
                                weight=3,
                                opacity=0.5)


request_params = {
    'coordinates': [[12.108259, 54.081919], [12.072063, 54.103684]],
    'format_out': 'geojson',
    'profile': 'driving-car',
    'preference': 'shortest',
    'instructions': 'false'
}

api_key = '5b3ce3597851110001cf6248b560c2165259434bb980d7e91b7fdcab'
clnt = client.Client(key=api_key)  # Create client with api key
route_normal = clnt.directions(**request_params)
folium.features.GeoJson(data=route_normal,
                        name='Route without construction sites',
                        style_function=style_function('#FF0000'),
                        overlay=True).add_to(m)

names_dict = {1: "Quito",
              2: "Ipiales",
              3: "Nationalpark XX",
              4: "Campingplatz La Bonanza",
              5: "Salento",
              6: "Manizales",
              7: "Medellin",
              8: "Guatapé",
              9: "Isla Múcura",
              10: "Tolú",
              11: "Cartagena",
              12: "Minca",
              13: "Palomino",
              14: "Tayrona Nationalpark",
              15: "Barichara",
              16: "Salzkathedrale Zipaquira",
              17: "Bogotá",
              18: "San Agustín",
              19: "Polizeistation bei Popayán",
              20: "Laguna de la Cocha",
              21: "Ipiales",
              22: "Ibarra",
              23: "Otavalo",
              24: "Quito",
              25: "Mindo",
              26: "Santa Marianita",
              27: "Guayaquil",
              28: "Galapagos-Inseln",
              29: "Guayaquil",
              30: "Laguna de Quilotoa",
              31: "Insilivi",
              32: "Chimborazo",
              33: "Banyos",
              34: "Misahuallí",
              35: "Limón",
              36: "Cuenca",
              37: "Mancora",
              38: "Trujillo",
              39: "Caraz"}

tooltip_dict = {1: 'Start der Reise in Quito',
                2: "Erster Stopp in Kolumbien: Ipiales",
                3: "Übernachtung am Nationalpark Chimayoy",
                4: "Campingplatz La Bonanza",
                5: "Salento",
                6: "Thermalbad in Manizales",
                7: "Medellin",
                8: "Guatapé",
                9: "Isla Múcura",
                10: "Tolú",
                11: "Cartagena",
                12: "Minca",
                13: "Palomino",
                14: "Tayrona Nationalpark",
                15: "Barichara",
                16: "Salzkathedrale Zipaquira",
                17: "Bogotá",
                18: "San Agustín",
                19: "Polizeistation in Coconuco",
                20: "Laguna de la Cocha",
                21: "Ipiales",
                22: "Ibarra",
                23: "Otavalo",
                24: "Quito",
                25: "Mindo",
                26: "Santa Marianita",
                27: "Guayaquil",
                28: "Galapagos-Inseln",
                29: "Guayaquil",
                30: "Laguna de Quilotoa",
                31: "Insilivi",
                32: "Chimborazo",
                33: "Banyos",
                34: "Misahuallí",
                35: "Limón",
                36: "Cuenca",
                37: "Mancora",
                38: "Trujillo",
                39: "Caraz"
                }

coordinates_dict = {1: [-0.148817, -78.441441],
                    2: [0.805646, -77.585560],
                    3: [1.262471, -77.285087],
                    4: [2.614479, -76.464835],
                    5: [4.635837, -75.571897],
                    6: [5.020810, -75.436550],
                    7: [6.230270, -75.490612],
                    8: [6.222607, -75.247956],
                    9: [9.782041, -75.872093],
                    10: [9.527937, -75.582389],
                    11: [10.392408, -75.478310],
                    12: [11.142307, -74.116795],
                    13: [11.262063, -73.582315],
                    14: [11.306578, -74.065735],
                    15: [6.635837, -73.223497],
                    16: [5.021684, -74.006458],
                    17: [4.711236, -74.076193],
                    18: [1.879869, -76.270277],
                    19: [2.354453, -76.495912],
                    20: [1.045381, -77.149888],
                    21: [0.825578, -77.641045],
                    22: [0.346814, -78.132687],
                    23: [0.234532, -78.260937],
                    24: [-0.148817, -78.441441],
                    25: [-0.054427, -78.775578],
                    26: [-0.993734, -80.855599],
                    27: [-2.189082, -79.896047],
                    28: [-0.742243, -90.316072],
                    29: [-2.189082, -79.896047],
                    30: [-0.871530, -78.899970],
                    31: [-0.699945, -78.886296],
                    32: [-1.471576, -78.822819],
                    33: [-1.392466, -78.426375],
                    34: [-1.033614, -77.669724],
                    35: [-2.963455, -78.427225],
                    36: [-2.900669, -79.006375],
                    37: [-4.103753, -81.044672],
                    38: [-8.106723, -79.032320],
                    39: [-9.051385, -77.794601]
                    }

url_dict = {}  # needs to be filled with links to blog posts

# for loop
coord_len = len(coordinates_dict)

for i in (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22,
        23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39):
    folium.Marker(coordinates_dict[i],
                  # folium.Popup("""<a href=" ['https://www.google.de/] "target="_blank"> [Quito Post]' </a>"""),
                  tooltip=tooltip_dict[i]).add_to(m)

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

folium.PolyLine(route).add_to(m)

m.save('newtest.html')
