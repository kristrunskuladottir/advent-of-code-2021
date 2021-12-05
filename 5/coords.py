from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Coordinate():
    x: int
    y: int

    @classmethod
    def create_from_string(cls, coordinate_input: str) -> 'Coordinate':
        # format of input: 'x,y' where x and y are integers
        coordinates = coordinate_input.split(',')
        return cls(x=int(coordinates[0]), y=int(coordinates[1]))


@dataclass(frozen=True)
class Line():
    start: Coordinate
    end: Coordinate

    @classmethod
    def create_from_string(cls, line_input: str) -> 'Line':
        # format of input: 'x1,y1 -> x2,y2' where x1, y1, x2, y2 are integers
        coordinates = line_input.split(' -> ')

        return cls(
            start=Coordinate.create_from_string(coordinates[0]),
            end=Coordinate.create_from_string(coordinates[1])
        )

    def is_horizontal(self) -> bool:
        return self.start.x == self.end.x

    def is_vertical(self) -> bool:
        return self.start.y == self.end.y

    def coordinates_covered(self) -> List[Coordinate]:
        covered = []
        if self.is_horizontal():
            bigger_y = self.start.y if self.start.y > self.end.y else self.end.y
            smaller_y = self.start.y if self.start.y < self.end.y else self.end.y

            while smaller_y <= bigger_y:
                covered.append(Coordinate(x=self.start.x, y=smaller_y))
                smaller_y += 1

        elif self.is_vertical():
            smaller_x = self.start.x if self.start.x < self.end.x else self.end.x
            bigger_x = self.start.x if self.start.x > self.end.x else self.end.x

            while smaller_x <= bigger_x:
                covered.append(Coordinate(x=smaller_x, y=self.start.y))
                smaller_x += 1

        else:
            # we have a diagonal line at 45°

            starting_x = self.start.x
            starting_y = self.start.y
            while starting_x != self.end.x and starting_y != self.end.y:
                covered.append(Coordinate(starting_x, starting_y))

                if starting_x < self.end.x:
                    starting_x += 1
                else:
                    starting_x -= 1

                if starting_y < self.end.y:
                    starting_y += 1
                else:
                    starting_y -= 1

            covered.append(self.end)

        return covered
