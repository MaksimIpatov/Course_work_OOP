from abc import ABC, abstractmethod
import requests

class AbstractAPI(ABC):
    """Абстрактный класс от ABC"""
    @abstractmethod
    def get_response(self, text, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, text, per_page):
        pass

    @abstractmethod
    def get_filter_vacancies(self, text, per_page):
        pass
class Headhunter(AbstractAPI):
    """Класс для работы с API HH"""
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_response(self, text: str, per_page: int):
        """ Метод выполняет запрос на API сайта hh.ru"""
        params = {"text": text, "per_page": per_page}
        response = requests.get(self.__url, params=params)
        return response

    def get_vacancies(self, text: str, per_page: int=20) -> list:
        """Метод возвращает запрошенную вакансию, к примеру python"""
        vacancies = self.get_response(text, per_page).json()["items"]
        return vacancies

    def get_filter_vacancies(self, text: str, per_page: int) -> list:
        """"Метод поиска с ключевым словом в описании для всех вакансий"""
        filter_vacancies = []
        vacancies = self.get_vacancies(text, per_page)
        for vacancy in vacancies:
            filter_vacancies.append({
                "name": vacancy["name"],
                "salary": vacancy["salary"],
                "url": vacancy.get("url", None),
                "employer": vacancy["employer"]["name"]
            })
        return filter_vacancies

# hh = Headhunter()
# data = hh.get_filter_vacancies("python", 100)
# for elem in data:
#     print(elem["salary"])
