import requests
import os


BASE_URL = "http://ip172-18-0-6-cvp77m291nsg0096ppg0-5000.direct.labs.play-with-docker.com"


def get_users():
    response = requests.get(f"{BASE_URL}/users")
    return response.json()

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    return response.json()

def add_user(name, email):
    data = {"name": name, "email": email}
    response = requests.post(f"{BASE_URL}/users", json=data)
    return response.json()

if __name__ == "__main__":
    print("Klientas paleistas")

    try:
        print("Visi vartotojai:", get_users())
    except Exception as e:
        print("Klaida gaunant visus vartotojus:", e)

    try:
        print("Vartotojas ID 1:", get_user(1))
    except Exception as e:
        print("Klaida gaunant vartotoją ID 1:", e)

    try:
        new_user = add_user("Petras", "petras@example.com")
        print("Pridėtas vartotojas:", new_user)
    except Exception as e:
        print("Klaida pridedant vartotoją:", e)

    try:
        print("Atnaujintas vartotojų sąrašas:", get_users())
    except Exception as e:
        print("Klaida gaunant atnaujintą sąrašą:", e)

