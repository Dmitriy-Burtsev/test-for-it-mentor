def main(input: str) -> str:
    parts = input.split()
    if len(parts) != 3:
        raise Exception("Неправильный формат входных данных")
    a_str, operator, b_str = parts
    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        raise Exception("Операнды должны быть целыми числами")
    if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise Exception("Числа должны быть от 1 до 10 включительно")
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a // b  # Целочисленное деление
    else:
        raise Exception("Недопустимый оператор")
    return str(result)
if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите арифметическое выражение : ")
            output = main(user_input)
            print(output)
        except Exception as e:
            print("throws Exception:", e)
            break


