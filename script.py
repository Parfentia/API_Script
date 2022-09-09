import requests
import json


# Обработка get запроса
def api_request(x):
    data = {'num': x[0]}
    response = requests.get("http://rosreestr.subnets.ru/?get=num&format=json", params=data)
    obj = json.loads(response.text)
    key = "error"
    if key in obj:
        return "Error"
    else:
        return obj["0"]["operator"]


# Вывод в файл
def output_in_file(answer, file_path):
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(answer)


file_path = input("Введите путь к файлу: ")
answer = ""
with open(file_path, "r", encoding='utf-8') as file:
    all_text = file.read()
    lines = all_text.split(",")
    for line in lines:
        line = line.replace("\n", "")
        element = line.split("/")
        answer += element[0] + "/" + element[1] + "/"
        get_answer = api_request(element)
        if get_answer == "Error":
            answer += "No answer/2"
        elif element[1] == get_answer:
            answer += get_answer + "/1"
        else:
            answer += get_answer + "/0"
        answer += "\n"
    output_in_file(answer, "answer.txt")
