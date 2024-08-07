import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy

class FileAbstractClass(ABC):
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
    def __init__(self, filename="vacancies.json"):
        self.filename = f"data/{filename}"

    def write_data(self, vacancies):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)


    def get_vacancies(self) -> list[Vacancy]:
        with open(self.filename, encoding="utf-8") as f:
            data = json.load(f)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies


    def delete_vacancy(self):
        with open(self.filename, mode="w") as f:
            f.truncate()


