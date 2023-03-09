def compare(number_1, number_2):
    if number_1 == number_2:
        return "nums are equal"
    return (
        f"{number_1} is less than {number_2}"
        if number_2 < number_1
        else f"{number_1} is greater than {number_2}"
    )
