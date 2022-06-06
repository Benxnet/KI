import json
from math import acos, cos, sin, pi

vertices = list()   #Liste mit den Knoten des Graphen

#Abstraktion eines Knotens/einer Stadt, diese kennt seine benachbarten Städte
class Vertex:
    def __init__(self, city_char, city_name, city_latitude, city_longtitude):
        assert isinstance(city_latitude, float)
        assert isinstance(city_longtitude, float)

        self.city_char = city_char
        self.city_name = city_name
        self.latitude = city_latitude
        self.longtitude = city_longtitude
        self.neighbours = list()

        self.from_neighbour = None
        self.cost = 0

    def add_neighbour(self, n, distance):
        assert isinstance(n, Vertex)
        self.neighbours.append((n, distance))


#Eigene Realisierung einer Queue-Datenstruktur
class Queue:
    __my_list__ = list()
    def enqueue(self, obj):
        assert isinstance(obj, Vertex)
        self.__my_list__.append(obj)

    def dequeue(self):
        minimum_city = None
        for current_city in self.__my_list__:
            if minimum_city == None or current_city.cost < minimum_city.cost:
                minimum_city = current_city
        self.__my_list__.remove(minimum_city)
        return minimum_city

    def is_empty(self):
        return len(self.__my_list__) == 0

    def is_inside(self, obj):
        assert isinstance(obj, Vertex)
        return obj in self.__my_list__

def get_distance_in_km(city1, city2):
    assert isinstance(city1, Vertex)
    assert isinstance(city2, Vertex)

    lat1 = city1.latitude / (180 / pi)
    lat2 = city2.latitude / (180 / pi)
    lon1 = city1.longtitude / (180 / pi)
    lon2 = city2.longtitude / (180 / pi)

    return 6378.388 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))

#Diese Funktion sucht einen Knoten aus der Liste, anhand dessen Zeichens
def get_Vertex(city_char):
    for vertex in vertices:
        if vertex.city_char == city_char:
            return vertex
    return None

def h(vertex, destination):
    assert isinstance(vertex, Vertex)
    result = int(get_distance_in_km(vertex, destination))
    print(str(result))
    print(vertex.city_name)
    return result

def A_Algorithm(origin, destination):
    assert isinstance(origin, Vertex)
    assert isinstance(destination, Vertex)

    frontier = Queue()
    explored = list()
    frontier.enqueue(origin)

    while True:
        assert not frontier.is_empty()
        current_city = frontier.dequeue()
        if current_city == destination:
            #Unser Ziel wurde gefunden
            #Verfolge den Pfad zurück
            path = list()
            while current_city != None:
                path.insert(0, current_city)
                current_city = current_city.from_neighbour
            return path

        explored.append(current_city)

        # Itteriere über alle Nachbarn des derzeitigen Knoten.
        # Ermittle für den Nachbarn die Kosten unter Anwendung einer Heuristik.
        for (neighbour, path_cost_to_neighbour) in current_city.neighbours:
            cost_of_neighbour = current_city.cost + path_cost_to_neighbour + h(neighbour, destination)

            if neighbour not in explored and not frontier.is_inside(neighbour):
                neighbour.cost = cost_of_neighbour
                neighbour.from_neighbour = current_city
                frontier.enqueue(neighbour)
            elif frontier.is_inside(neighbour) and neighbour.cost > cost_of_neighbour:
                neighbour.cost = cost_of_neighbour
                neighbour.from_neighbour = current_city


#Lese den Graphen aus der graph.json-Datei
with open('graph.json', 'r') as file_stream:
    json_dict = json.load(file_stream)
    (city_str, cities), (edge_str, edges) = json_dict.items()

    #Lese jetzt die Städte in eine Liste mit Tupeln
    for city in cities:
        new_city = Vertex(city.get("city_char"), city.get("city_name"), float(city.get("latitude")), float(city.get("longtitude")))
        vertices.append(new_city)

    #Lese jetzt die Kanten des Graphen in eine Adjazenzliste
    for edge_dict in edges:
        first_vertex = get_Vertex(edge_dict.get('a'))
        second_vertex = get_Vertex(edge_dict.get('b'))
        distance = int(edge_dict.get("distance"))

        first_vertex.add_neighbour(second_vertex, distance)
        second_vertex.add_neighbour(first_vertex, distance)

origin = None
dest = None
while origin == None:
    input_str = input("Start: ")
    for current in vertices:
        if current.city_name == input_str:
            origin = current

while dest == None:
    input_str = input("Ziel: ")
    for current in vertices:
        if current.city_name == input_str:
            dest = current

print("Berechne die Route von " + origin.city_name + " nach " + dest.city_name)
path = A_Algorithm(origin, dest)
for element in path:
    assert isinstance(element, Vertex)
    print(element.city_name + " -> ")
