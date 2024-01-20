from dataclasses import dataclass


@dataclass
class Point:
    lon: float
    lat: float

location = Point(3.12, 5.33)
print(location.__annotations__)