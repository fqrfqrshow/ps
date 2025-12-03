# -*- coding: utf-8 -*-
"""Модели данных для планет."""

from datetime import datetime


class Planet:
    def __init__(self, name, date, radius, mass):
        self.name = name
        self.date = date
        self.radius = radius
        self.mass = mass
    
    def display(self):
        print(f"{self.name}: открыта {self.date}, радиус {self.radius} км, масса {self.mass} кг")


def parse_planet(line):
    """Парсит строку с данными планеты."""
    parts = line.strip().split()
    if len(parts) < 4:
        return None
    
    name = parts[0].strip('"')
    date = parts[1]
    radius = float(parts[2])
    mass = float(parts[3])
    
    # Проверка даты
    try:
        datetime.strptime(date, "%Y.%m.%d")
    except ValueError:
        return None
    
    return Planet(name, date, radius, mass)