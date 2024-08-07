import json
def user_interface():
    print('Введите запрос поиска')
    answer = input()
def filter_vacancies(key_word):
    with open("vacancies.json", "r", encoding="utf-8") as f:
        vacancies = json.load(f)
    filtered_vacancies = []
    for vacancy in vacancies:
        if key_word.lower() in vacancy['title'].lover():
            filtered_vacancies.append(vacancy)
    return filtered_vacancies

result = filter_vacancies("Python")
print(result)


