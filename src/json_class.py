import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class FileAbstractClass(ABC):
    """Абстрактный класс от ABC"""

    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(FileAbstractClass):
    """Класс для работы с файлом vacancies.json"""

    def __init__(self, filename="vacancies.json"):
        self.filename = f"data/{filename}"

    def write_data(self, vacancies):
        """Метод выполняет добавление новые данные в файл vacancies.json, без дублей"""
        with open(self.filename, "r", encoding="utf-8") as f:
            existing_vacancies = json.load(f)
        """Множество для хранения уникальных идентификаторов вакансий, используя url"""
        existing_urls = {vacancy['url'] for vacancy in existing_vacancies}
        """Добавить только новые вакансии, которых еще нет в существующих вакансиях"""
        new_vacancies = [vacancy for vacancy in vacancies if vacancy['url'] not in existing_urls]
        """Объединяем существующие и новые вакансии"""
        updated_vacancies = existing_vacancies + new_vacancies
        return updated_vacancies

    def get_vacancies(self, updated_vacancies=None):
        """Запись обновленных данных обратно в файл"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(updated_vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self):
        """Метод удаляет записи вакансий"""
        with open(self.filename, mode="w") as f:
            f.truncate()
