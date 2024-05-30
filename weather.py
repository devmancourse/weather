import requests


def weather(city):
    response = requests.get(f"https://wttr.in/~{city}")
    return response.text 


if __name__ == "__main__":
    city = input("Enter city: ")
    print(weather(city))
