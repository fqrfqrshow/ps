# -*- coding: utf-8 -*-
"""Основная программа для анализа планет."""

from model import parse_planet, parse_habitable_planet, parse_mining_planet, InvalidPlanetDataError
from view import display_planet


def process_line(line):
    """Обрабатывает строку с описанием планеты."""
    line = line.strip()
    if not line or line.startswith('#'):
        return None
    
    try:
        # Пробуем парсить как обитаемую планету
        try:
            return parse_habitable_planet(line)
        except InvalidPlanetDataError:
            pass
        
        # Пробуем парсить как горнодобывающую планету
        try:
            return parse_mining_planet(line)
        except InvalidPlanetDataError:
            pass
        
        # Пробуем парсить как обычную планету
        try:
            return parse_planet(line)
        except InvalidPlanetDataError:
            pass
        
        print(f"Не удалось определить тип планеты для строки: {line}")
        return None
        
    except Exception as e:
        print(f"Ошибка при обработке строки '{line}': {e}")
        return None


def main():
    """Основная функция программы."""
    try:
        with open("planets.txt", "r", encoding="utf-8") as f:
            for line in f:
                planet = process_line(line)
                if planet:
                    display_planet(planet)
    except FileNotFoundError:
        print("Ошибка: Файл planets.txt не найден.")
    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()