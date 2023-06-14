import googlemaps
import folium

def get_traffic_data(api_key, origin, destination):
    gmaps = googlemaps.Client(key=api_key)
    traffic_data = gmaps.directions(origin, destination, departure_time="now", traffic_model="best_guess")
    return traffic_data

def display_traffic_map(traffic_data):
    rio_coordinates = [-22.9068, -43.1729]
    traffic_map = folium.Map(location=rio_coordinates, zoom_start=12)

    for route in traffic_data:
        for leg in route['legs']:
            for step in leg['steps']:
                points = step['polyline']['points']
                decoded_points = googlemaps.convert.decode_polyline(points)
                traffic_map.add_child(folium.PolyLine(decoded_points, color='red'))

    return traffic_map

if __name__ == '__main__':
    api_key = ''
    origin = '-22.9068, -43.1729'  # Rio de Janeiro coordinates
    destination = '-22.9834, -43.2242'  # Leblon, Visconde de Albuquerque coordinates
    data = get_traffic_data(api_key, origin, destination)
    map = display_traffic_map(data)
    map.save('traffic_map.html')

