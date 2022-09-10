from typing import List, Dict, Any
import names
import re
import random


class UserDataGenerator:
    def __init__(self):  # C++ konstruktor inicjalizujący
        self.user_data = []

    def generate_data(self, number_of_users: int) -> List[Dict[str, Any]]:  # Any oznacza dowolny, różny typ danych
        for i in range(number_of_users):
            # Dictionary / JSON
            # Słownik/JSON składa się z pary key value
            user = {
                'user_id': i + 1,
                'user_name': re.split(" ", names.get_full_name())[0],  # re.split zwraca listę zawierającą imię i
                # nazwisko, natomiast [0] wskazuje na pierwszy element listy - imię
                'user_last_name': re.split(" ", names.get_full_name())[1],
                'user_age': random.randint(18, 50)
            }
            self.user_data.append(user)  # Append dodaje nowy element na koniec listy
        return self.user_data


if __name__ == '__main__':
    generate_user_data = UserDataGenerator()
    sample_data = generate_user_data.generate_data(number_of_users=10)

    # Display generated users
    for user in sample_data:
        print(user)

# Prefix: column_user_name  - prefix jest statycznym ciągiem znaków na początku w nazwenictwie technicznym
# Sufix: user_name_column  - sufix jest statycznym ciągiem znaków na końcu
