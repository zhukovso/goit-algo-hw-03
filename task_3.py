import re

def normalize_phone(phone_number: str) -> str:
    try:
        cleaned_number = re.sub(r'[^\d]', '', phone_number)
        if not cleaned_number.startswith('+'):
            if cleaned_number.startswith('380'):
                cleaned_number = '+' + cleaned_number
            else:
                cleaned_number = '+38' + cleaned_number
        return cleaned_number
    except TypeError:
        print(f"{phone_number} is not a string.")


if __name__ == '__main__':

    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   "
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)