# -*- coding: utf-8 -*-
"""Функции отображения данных о планетах."""


def display_planet(planet):
    """Отображает информацию о планете."""
    data = planet.get_data()
    output = f"{data['name']}: открыта {data['date']}, радиус {data['radius']} км, масса: {data['mass']}"
    
    if 'temperature' in data:
        output += f", температура: {data['temperature']}°C, шанс жизни: {data['habitability']}"
    
    if 'resource' in data:
        output += f", ресурс: {data['resource']}, сложность добычи: {data['difficulty']}"
    
    if data['distance']:
        output += f", расстояние до Солнца: {data['distance']} км"
    
    print(output)