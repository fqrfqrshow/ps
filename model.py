# -*- coding: utf-8 -*-
"""Модели данных для планет."""

from datetime import datetime
import shlex


class InvalidPlanetDataError(Exception):
    """Исключение для ошибок при парсинге данных о планете."""
    pass


class BasePlanet:
    """Базовый класс планеты."""
    
    def __init__(self, name, discovery_date, radius, mass, distance_to_sun=None):
        self.name = name
        self.discovery_date = discovery_date
        self.radius = radius
        self.mass = mass
        self.distance_to_sun = distance_to_sun
    
    def get_data(self):
        """Возвращает данные планеты в виде словаря."""
        return {
            "name": self.name,
            "date": self.discovery_date,
            "radius": self.radius,
            "mass": self.mass,
            "distance": self.distance_to_sun
        }


class Planet(BasePlanet):
    """Класс обычной планеты."""
    pass


class HabitablePlanet(BasePlanet):
    """Класс обитаемой планеты."""
    
    def __init__(self, name, discovery_date, radius, mass, temperature, habitability_score, distance_to_sun=None):
        super().__init__(name, discovery_date, radius, mass, distance_to_sun)
        self.temperature = temperature
        self.habitability_score = habitability_score
    
    def get_data(self):
        data = super().get_data()
        data.update({
            "temperature": self.temperature,
            "habitability": self.habitability_score
        })
        return data


class MiningPlanet(BasePlanet):
    """Класс горнодобывающей планеты."""
    
    def __init__(self, name, discovery_date, radius, mass, resource, difficulty, distance_to_sun=None):
        super().__init__(name, discovery_date, radius, mass, distance_to_sun)
        self.resource = resource
        self.difficulty = difficulty
    
    def get_data(self):
        data = super().get_data()
        data.update({
            "resource": self.resource,
            "difficulty": self.difficulty
        })
        return data


def is_valid_date(date_str):
    """Проверка корректности даты."""
    try:
        datetime.strptime(date_str, "%Y.%m.%d")
        return True
    except ValueError:
        return False


def parse_planet(description):
    """Парсинг обычной планеты."""
    try:
        parts = shlex.split(description)
    except ValueError:
        raise InvalidPlanetDataError("Ошибка разбора строки")
    
    if len(parts) < 4:
        raise InvalidPlanetDataError("Недостаточно данных")
    
    name = parts[0]
    date = parts[1]
    
    try:
        radius = float(parts[2])
        mass = float(parts[3])
    except ValueError:
        raise InvalidPlanetDataError("Ошибка преобразования чисел")
    
    if not is_valid_date(date) or radius <= 0 or mass <= 0:
        raise InvalidPlanetDataError("Неверные значения")
    
    return Planet(name, date, radius, mass)


def parse_habitable_planet(description):
    """Парсинг обитаемой планеты."""
    try:
        parts = shlex.split(description)
    except ValueError:
        raise InvalidPlanetDataError("Ошибка разбора строки")
    
    if len(parts) < 6:
        raise InvalidPlanetDataError("Недостаточно данных")
    
    name = parts[0]
    date = parts[1]
    
    try:
        radius = float(parts[2])
        mass = float(parts[3])
        temperature = float(parts[4])
        score = float(parts[5])
    except ValueError:
        raise InvalidPlanetDataError("Ошибка преобразования чисел")
    
    if not is_valid_date(date) or radius <= 0 or mass <= 0:
        raise InvalidPlanetDataError("Неверные значения")
    
    return HabitablePlanet(name, date, radius, mass, temperature, score)


def parse_mining_planet(description):
    """Парсинг горнодобывающей планеты."""
    try:
        parts = shlex.split(description)
    except ValueError:
        raise InvalidPlanetDataError("Ошибка разбора строки")
    
    if len(parts) < 6:
        raise InvalidPlanetDataError("Недостаточно данных")
    
    name = parts[0]
    date = parts[1]
    
    try:
        radius = float(parts[2])
        mass = float(parts[3])
    except ValueError:
        raise InvalidPlanetDataError("Ошибка преобразования чисел")
    
    resource = parts[4]
    difficulty = parts[5]
    
    if not resource:
        raise InvalidPlanetDataError("Пустой ресурс")
    if not difficulty:
        raise InvalidPlanetDataError("Пустая сложность")
    if not is_valid_date(date) or radius <= 0 or mass <= 0:
        raise InvalidPlanetDataError("Неверные значения")
    
    return MiningPlanet(name, date, radius, mass, resource, difficulty)