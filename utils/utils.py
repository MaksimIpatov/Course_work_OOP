import json
from src.hh_api import Headhunter


def user_interact():
    """Метод взаимодействия с пользователем"""
    while True:
        print("ВЫберите действие!:")
        print("1.Получить интересующие вакансии, указать сколько!")
        print("2.Получить топ N вакансий по зарплате")
        print("3.Узнать о количестве(наличии) вакансий на hh с ключевым словом в описании")
        print("0. Close")
        choice = input("Выберите номер действия и введите:")
        hh_client = Headhunter()

        if choice == "1":
            query = input("Введите название интересующей вас вакансии: ")
            per_page_vacancy = input("Сколько вакансий показать?: ")
            vacancy_hh = hh_client.get_filter_vacancies(query, int(per_page_vacancy))
            print(vacancy_hh)

        elif choice == "2":
            n = input("Введите количество вакансий для поиска: ")
            query = input("Введите название интересующей вас вакансии: ")
            top_vacancies = hh_client.get_filter_vacancies(query, int(n))
            print(top_vacancies)

        elif choice == "3":
            keyword = input("Введите ключевое слово поиска!: ")
            per_page_vacancy = input("Наличие какого количества вакансий проверить?: ")
            filtered_vacancies = hh_client.get_vacancies(keyword.lower(), int(per_page_vacancy))
            print(f"В настоящее время на сайте hh.ru размещено не менее {len(filtered_vacancies)} вакансий с ключевым словом '{keyword}':")
        elif choice == "0":
            break
        else:
            print("Выбрано некорректное значение, выберите из 3 предложенных вариантов!")

if __name__ == '__main__':
    user_interact()




