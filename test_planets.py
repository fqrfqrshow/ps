# -*- coding: utf-8 -*-
"""Модульные тесты для проекта планет."""

import unittest
from model import (
    BasePlanet,
    Planet,
    HabitablePlanet,
    MiningPlanet,
    parse_planet,
    parse_habitable_planet,
    parse_mining_planet,
    InvalidPlanetDataError,
    is_valid_date
)


class TestPlanetParsing(unittest.TestCase):
    """Тесты парсинга планет."""
    
    def test_valid_planet_parsing(self):
        """Тест корректного парсинга обычной планеты."""
        desc = '"Марс" 1659.09.03 3389.5 6.42e23'
        planet = parse_planet(desc)
        
        self.assertIsInstance(planet, Planet)
        self.assertEqual(planet.name, "Марс")
        self.assertEqual(planet.discovery_date, "1659.09.03")
        self.assertEqual(planet.radius, 3389.5)
        self.assertEqual(planet.mass, 6.42e23)
    
    def test_valid_habitable_planet_parsing(self):
        """Тест корректного парсинга обитаемой планеты."""
        desc = '"Земля" 0001.01.01 6371.0 5.97e24 15.0 0.9'
        planet = parse_habitable_planet(desc)
        
        self.assertIsInstance(planet, HabitablePlanet)
        self.assertEqual(planet.name, "Земля")
        self.assertEqual(planet.temperature, 15.0)
        self.assertEqual(planet.habitability_score, 0.9)
    
    def test_valid_mining_planet_parsing(self):
        """Тест корректного парсинга горнодобывающей планеты."""
        desc = '"Церера" 1801.01.01 946.0 9.4e20 "вода" "легкая"'
        planet = parse_mining_planet(desc)
        
        self.assertIsInstance(planet, MiningPlanet)
        self.assertEqual(planet.name, "Церера")
        self.assertEqual(planet.resource, "вода")
        self.assertEqual(planet.difficulty, "легкая")
    
    def test_invalid_date_format(self):
        """Тест с некорректным форматом даты."""
        desc = '"Марс" 1659-09-03 3389.5 6.42e23'
        
        with self.assertRaises(InvalidPlanetDataError):
            parse_planet(desc)
    
    def test_missing_fields(self):
        """Тест с недостаточным количеством полей."""
        desc = '"Марс" 1659.09.03 3389.5'
        
        with self.assertRaises(InvalidPlanetDataError):
            parse_planet(desc)
    
    def test_invalid_radius(self):
        """Тест с некорректным радиусом."""
        desc = '"Марс" 1659.09.03 -3389.5 6.42e23'
        
        with self.assertRaises(InvalidPlanetDataError):
            parse_planet(desc)
    
    def test_invalid_mass(self):
        """Тест с некорректной массой."""
        desc = '"Марс" 1659.09.03 3389.5 0'
        
        with self.assertRaises(InvalidPlanetDataError):
            parse_planet(desc)
    
    def test_habitable_invalid_temperature(self):
        """Тест с некорректной температурой."""
        desc = '"Земля" 0001.01.01 6371.0 5.97e24 invalid 0.9'
        
        with self.assertRaises(InvalidPlanetDataError):
            parse_habitable_planet(desc)
    
    def test_mining_empty_resource(self):
        """Тест с пустым ресурсом."""
        desc = '"Церера" 1801.01.01 946.0 9.4e20 "" "легкая"'
        
        with self.assertRaises(InvalidPlanetDataError):
            parse_mining_planet(desc)


class TestDateValidation(unittest.TestCase):
    """Тесты валидации дат."""
    
    def test_valid_dates(self):
        """Тест корректных дат."""
        self.assertTrue(is_valid_date("2023.12.31"))
        self.assertTrue(is_valid_date("0001.01.01"))
        self.assertTrue(is_valid_date("1999.02.28"))
    
    def test_invalid_dates(self):
        """Тест некорректных дат."""
        self.assertFalse(is_valid_date("2023-12-31"))
        self.assertFalse(is_valid_date("2023.13.01"))
        self.assertFalse(is_valid_date("2023.02.30"))
        self.assertFalse(is_valid_date("invalid"))
        self.assertFalse(is_valid_date(""))


class TestBasePlanet(unittest.TestCase):
    """Тесты базового класса планеты."""
    
    def test_get_data_method(self):
        """Тест метода get_data."""
        planet = BasePlanet("Марс", "1659.09.03", 3389.5, 6.42e23, 227900000)
        data = planet.get_data()
        
        expected = {
            "name": "Марс",
            "date": "1659.09.03",
            "radius": 3389.5,
            "mass": 6.42e23,
            "distance": 227900000
        }
        
        self.assertEqual(data, expected)


class TestHabitablePlanet(unittest.TestCase):
    """Тесты обитаемой планеты."""
    
    def test_get_data_with_temperature(self):
        """Тест получения данных с температурой."""
        planet = HabitablePlanet("Земля", "0001.01.01", 6371.0, 5.97e24, 15.0, 0.9)
        data = planet.get_data()
        
        self.assertIn("temperature", data)
        self.assertIn("habitability", data)
        self.assertEqual(data["temperature"], 15.0)
        self.assertEqual(data["habitability"], 0.9)


class TestMiningPlanet(unittest.TestCase):
    """Тесты горнодобывающей планеты."""
    
    def test_get_data_with_resource(self):
        """Тест получения данных с ресурсами."""
        planet = MiningPlanet("Церера", "1801.01.01", 946.0, 9.4e20, "вода", "легкая")
        data = planet.get_data()
        
        self.assertIn("resource", data)
        self.assertIn("difficulty", data)
        self.assertEqual(data["resource"], "вода")
        self.assertEqual(data["difficulty"], "легкая")


# ========================================================
# КЛАСС С ПРОВАЛЬНЫМИ ТЕСТАМИ ДЛЯ ПРОВЕРКИ GIT HOOK
# ========================================================

class TestFailForHookDemo(unittest.TestCase):
    """Демонстрационный класс с провальными тестами для проверки Git hook."""
    
    def test_this_will_always_fail(self):
        """Этот тест всегда падает - для проверки блокировки коммита."""
        self.assertEqual(1, 2)  # Очевидно неправильно!
    
    def test_another_failing_test(self):
        """Еще один провальный тест для надежности."""
        self.assertTrue(False)  # Тоже всегда падает
    
    def test_wrong_assertion(self):
        """Третий провальный тест."""
        self.assertGreater(1, 10)  # 1 не больше 10


# ========================================================


def run_tests():
    """Запуск всех тестов."""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == '__main__':
    unittest.main(verbosity=2)