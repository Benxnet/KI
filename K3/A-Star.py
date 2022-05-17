import json
import math
import time


class AStar:
    def __init__(self):
        with open("europa.json", "r") as file:
            self.adjazenzliste = json.loads(file.read())

        self.koordinaten = {"a": {"x": 2, "y": 3},
                            "b": {"x": 3, "y": 3},
                            "c": {"x": 1, "y": 1},
                            "d": {"x": 5, "y": 3},
                            "e": {"x": 3, "y": 1},
                            "f": {"x": 2, "y": 2},
                            "g": {"x": 5, "y": 4},
                            "h": {"x": 3, "y": 4},
                            "i": {"x": 1, "y": 3},
                            "j": {"x": 4, "y": 2}
                            }

        self.distance = {"a": math.inf,
                         "b": math.inf,
                         "c": math.inf,
                         "d": math.inf,
                         "e": math.inf,
                         "f": math.inf,
                         "g": math.inf,
                         "h": math.inf,
                         "i": math.inf,
                         "j": math.inf
                         }
        self.ziel = ""
        self.start = ""
        self.frontier = []

    def aStarAlg(self, start, ziel):
        self.start = start
        self.ziel = ziel
        self.distance[start] = 0
        self.frontier.append(start)
        explored = list()

        while len(self.frontier) != 0:  # if EMPTY?( _frontier ) then
            v = self.getLowestCost()  # _node ← POP ( _frontier ) /* chooses the lowest-cost node in frontier */
            print("Explore:" + v)
            if v == self.ziel:  # if _problem.GOAL-TEST ( _node.STATE ) then
                return self.solution()  # return SOLUTION ( _node )
            self.frontier.remove(v)  # add _node.STATE to _explored
            explored.append(v)
            for knoten in self.adjazenzliste[v].keys():  # for each _action in _problem.ACTIONS ( _node.STATE ) do

                if self.distance[knoten] == math.inf or self.distance[knoten] > self.distance[v] + \
                        self.adjazenzliste[v][
                            knoten] and knoten not in explored:  # if _child.STATE is not in _explored or _frontier then bzw günstigsten

                    self.distance[knoten] = self.distance[v] + self.adjazenzliste[v][knoten]  # kosten

                    self.frontier.append(knoten)  # _frontier ← INSERT ( _child, _frontier )

    def getLowestCost(self):
        cheap = self.frontier[0]
        for knoten in self.frontier:
            if self.distance[knoten] + self.heuristic(knoten) < self.distance[cheap]:
                cheap = knoten
        return cheap

    def solution(self):
        distance = self.distance[self.ziel]
        solution = []
        cur_node = self.ziel
        while cur_node != self.start:
            for nachbar in self.adjazenzliste[cur_node].keys():
                tmp = distance - self.adjazenzliste[cur_node][nachbar]
                if tmp == self.distance[nachbar]:
                    distance -= self.adjazenzliste[cur_node][nachbar]
                    solution.append(cur_node)
                    cur_node = nachbar
                    break
        solution.append(self.start)
        solution.reverse()
        return solution

    def heuristic(self, knoten):
        delta_x = self.koordinaten[knoten]["x"] - self.koordinaten[self.ziel]["x"]  # abstand x
        delta_y = self.koordinaten[knoten]["y"] - self.koordinaten[self.ziel]["y"]  # abstand y
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2)) * 200  # Hypotenuse oder luftlinie


if __name__ == "__main__":
    search = AStar()
    start = ""
    ziel = ""
    while start not in {"a", "b", "c", "d", "e", "f2", "g", "h", "i", "j"}:
        start = input("Start: ")
    while ziel not in {"a", "b", "c", "d", "e", "f2", "g", "h", "i", "j"}:
        ziel = input("Ziel: ")
    print(search.aStarAlg(start, ziel))
