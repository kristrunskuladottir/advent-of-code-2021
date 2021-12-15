from dataclasses import dataclass
import heapq
import sys
from typing import List


@dataclass
class Node():
    x: int
    y: int
    cost: int
    visited: bool = False
    tentative_distance: int = sys.maxsize

    # for priority queue
    def __lt__(self, other):
        return self.tentative_distance < other.tentative_distance


@dataclass
class RiskLevels():
    rows: List[List[Node]]
    unvisited_nodes: List[Node]

    @classmethod
    def create(cls, risk_levels: List[List[int]]) -> 'RiskLevels':
        unvisited_nodes = []
        rows = []
        for y in range(len(risk_levels)):
            new_row = []
            for x in range(len(risk_levels[0])):
                node = Node(x=x, y=y, cost=risk_levels[y][x])
                new_row.append(node)
                if x == 0 and y == 0:
                    new_row[-1].tentative_distance = 0
                    heapq.heappush(unvisited_nodes, new_row[-1])

            rows.append(new_row)

        return cls(rows=rows, unvisited_nodes=unvisited_nodes)

    def unvisited_neighbours(self, x: int, y: int) -> List[Node]:
        unvisited_neighbours = []

        if x > 0 and not self.rows[y][x - 1].visited:
            unvisited_neighbours.append(self.rows[y][x - 1])
        if x < len(self.rows[0]) - 1 and not self.rows[y][x + 1].visited:
            unvisited_neighbours.append(self.rows[y][x + 1])
        if y > 0 and not self.rows[y - 1][x].visited:
            unvisited_neighbours.append(self.rows[y - 1][x])
        if y < len(self.rows) - 1 and not self.rows[y + 1][x].visited:
            unvisited_neighbours.append(self.rows[y + 1][x])

        return unvisited_neighbours

    def calculate_tentative_distance(self, node: Node):
        for unvisited_neighbour in self.unvisited_neighbours(node.x, node.y):
            if node.tentative_distance + unvisited_neighbour.cost < unvisited_neighbour.tentative_distance:
                unvisited_neighbour.tentative_distance = node.tentative_distance + unvisited_neighbour.cost
                heapq.heappush(self.unvisited_nodes, unvisited_neighbour)

        node.visited = True


def dijkstra(risk_levels: RiskLevels) -> int:
    while not risk_levels.rows[-1][-1].visited:
        current_node = heapq.heappop(risk_levels.unvisited_nodes)
        risk_levels.calculate_tentative_distance(current_node)

    return risk_levels.rows[-1][-1].tentative_distance


def main() -> None:
    risk_levels = []
    with open('multiplied_input.txt', 'r') as f:
        for line in f:
            line = list(line.rstrip())
            risk_levels.append([int(risk) for risk in line])

    risk_levels = RiskLevels.create(risk_levels)

    shortest_way_cost = dijkstra(risk_levels)
    print('total risk', shortest_way_cost)


if __name__ == '__main__':
    main()
