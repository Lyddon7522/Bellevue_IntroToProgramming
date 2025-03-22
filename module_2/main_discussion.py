def main():
    n = 20

    result = does_it_fiz_buzz(n)
    print(result)

def does_it_fiz_buzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


if __name__ == "__main__":
    main()