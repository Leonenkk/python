def is_very_long(password):
    return len(password) > 8


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_element(password):
    return any(not char.isdigit() and not char.isalpha() for char in password)


def list_of_functions(password):
    return [
        has_letters(password),
        has_lower_letters(password),
        has_upper_letters(password),
        has_digit(password),
        is_very_long(password),
        has_element(password)
    ]


def rate_password(function_list):
    score = 0
    for element in function_list:
        if element:
            score += 2
    return score


def main():
    password = input('Введите пароль: ')
    function_list=list_of_functions(password)
    score=rate_password(function_list)
    print(f'Рейтинг пароля: {score}')


if __name__ == '__main__':
    main()
