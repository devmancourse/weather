import requests

cities = ["London", "svo", "Cherepovets"]
def get_weather(city):
    url = f"https://wttr.in/~{city}"
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.HTTPError:
        return "Ошибка выполнения запроса"
    


def main():
    for city in cities:
        print(get_weather(city).text)
        print(get_weather(city).raise_for_status)


if __name__ == "__main__":
    main()
