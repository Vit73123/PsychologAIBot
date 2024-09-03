def age_name(age: int) -> str:
    if 2 <= age % 10 <= 4:
        return 'года'
    elif age % 10 == 1 and (age - 11) % 10 == 0:
        return 'год'
    else:
        return 'лет'


if __name__ == '__main__':
    # grades = [(str(i), str(grade)) for i, grade in enumerate(range(-3, 4))]
    # print(grades)
    age = 1001
    print(f'{age} {age_name(age)}')
