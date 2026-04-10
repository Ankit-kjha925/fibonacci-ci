def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    n = int(input())  # You can modify or make dynamic
    print("Hello, World!")
    fib_series = fibonacci(n)

    return {
        "message": "Hello, World!",
        "n": n,
        "fibonacci": fib_series
    }


if __name__ == "__main__":
    result = main()
    print(result)
