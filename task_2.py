from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    def validate_input_numbers(number: int) -> int:
        if 1 <= number <= 1000:
            return number
        else:
            raise ValueError(number)

    result_set = set()
    try:
        min = validate_input_numbers(min)
        max = validate_input_numbers(max)
        quantity = validate_input_numbers(quantity)

        while len(result_set) < quantity:
            result_set.add(randint(min, max))

    except ValueError as e:
        print(f"min, max or quantity is not a valid number. Expected number beetwen 1 and 1000!")
    except TypeError as e:
        print(f"min, max or quantity is not a number. Please input a number beetwen 1 and 1000!")

    return  sorted(list(result_set))

# print(get_numbers_ticket(1, 1000, 10))
# print(get_numbers_ticket(0, 1000, 10))
# print(get_numbers_ticket("1", 1000, 10))
# print(get_numbers_ticket(10, None, 100))