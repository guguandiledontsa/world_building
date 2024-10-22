from dataclasses import dataclass, field
from math import inf


@dataclass(frozen=True)
class FuelTank:
    level: float = field(default=-inf)
    cost: float = field(default=0.25)
    volume: float = field(default=100)

    def __post_init__(self):
        if self.level > self.volume:
            raise ValueError("Fuel tank level cannot be greater than volume")
        if self.level < 0:
            object.__setattr__(self, "level", self.volume)
        if self.cost <= 0 or self.volume <= 0:
            raise ValueError("Cost and volume must be positive.")

    def drop_fuel(self, distance: float):
        new_level = self.level - (distance * self.cost)
        if new_level < 0:
            raise ValueError("Fuel tank level cannot be negative")
        return FuelTank(level=new_level, cost=self.cost, volume=self.volume)

    def refuel(self):
        # takes time can stop mid-way
        ...
        if self.is_full():
            raise ValueError("Fuel tank is full")

        return FuelTank(level=self.volume, cost=self.cost, volume=self.volume)

    def is_empty(self):
        return self.level == 0

    def is_full(self):
        return self.level == self.volume
