# -*- coding: utf-8 -*-
"""Основная программа анализа планет."""

from model import Planet, parse_planet


def load_planets():
    """Загружает планеты из файла."""
    planets = []
    try:
        with open("planets.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    planet = parse_planet(line)
                    if planet:
                        planets.append(planet)
    except FileNotFoundError:
        print("Файл planets.txt не найден")
    return planets


def save_planets(planets):
    """Сохраняет планеты в файл."""
    with open("planets.txt", "w", encoding="utf-8") as f:
        for planet in planets:
            f.write(f'"{planet.name}" {planet.date} {planet.radius} {planet.mass}\n')


def show_all(planets):
    """Показывает все планеты."""
    if not planets:
        print("Список планет пуст")
    else:
        for i, planet in enumerate(planets, 1):
            print(f"{i}. ", end="")
            planet.display()


def add_planet(planets):
    """Добавляет новую планету."""
    name = input("Название планеты: ").strip()
    date = input("Дата открытия (ГГГГ.ММ.ДД): ").strip()
    
    try:
        radius = float(input("Радиус (км): "))
        mass = float(input("Масса (кг): "))
    except ValueError:
        print("Ошибка: радиус и масса должны быть числами")
        return planets
    
    planets.append(Planet(name, date, radius, mass))
    print(f"Планета '{name}' добавлена")
    return planets


def main():
    """Главное меню программы."""
    planets = load_planets()
    
    while True:
        print("\n" + "="*30)
        print("АНАЛИЗ ПЛАНЕТ")
        print("="*30)
        print("1. Вывести все планеты")
        print("2. Добавить планету")
        print("3. Выход")
        print("="*30)
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            show_all(planets)
        elif choice == "2":
            planets = add_planet(planets)
            save_planets(planets)
        elif choice == "3":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()