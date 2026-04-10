import os

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    # Read from environment variable (default = 10)
    n = int(os.getenv("N", 10))

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
