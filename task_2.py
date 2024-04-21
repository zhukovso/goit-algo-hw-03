from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    def validate_input_numbers(number: int) -> int:
        if 1 <= number <= 1000:
            return number
        else:
            raise ValueError(number)

    # result_set = set()
    try:
        # min = validate_input_numbers(min)
        # max = validate_input_numbers(max)
        # quantity = validate_input_numbers(quantity)

        # while len(result_set) < quantity:
        #     result_set.add(randint(min, max))

        return sorted(sample(range(validate_input_numbers(min), validate_input_numbers(max)), validate_input_numbers(quantity)))

    except ValueError as e:
        print(f"{e.args[0]} is not a valid number of min, max or quantity. Expected number beetwen 1 and 1000!")
    except TypeError as e:
        print(f"min, max or quantity is not a number. Please input a number beetwen 1 and 1000!")

    # return  sorted(list(result_set))

if __name__ == '__main__':
    print(get_numbers_ticket(1, 1000, 10))
    print(get_numbers_ticket(0, 1000, 10))
    print(get_numbers_ticket("1", 1000, 10))
    print(get_numbers_ticket(10, None, 100))