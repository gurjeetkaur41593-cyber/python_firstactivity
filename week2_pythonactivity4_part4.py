class MathSeries:
    def __init__(self, n=5):
        self.n = n

    def factorial_recursive(self, n=None):
        if n is None:
            n = self.n
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * self.factorial_recursive(n - 1)

    def fibonacci_recursive(self, n=None):
        if n is None:
            n = self.n
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def fibonacci_series(self, n=None):
        if n is None:
            n = self.n
        series = []
        for i in range(n + 1):
            series.append(self.fibonacci_recursive(i))
        return series


if __name__ == "__main__":
    # Create an object with n=5 (default)
    math_obj = MathSeries(n=5)

    # Print factorial
    print("Factorial (recursive):", math_obj.factorial_recursive())

    # Print nth Fibonacci value
    print("Fibonacci (recursive):", math_obj.fibonacci_recursive())

    # Print full Fibonacci series
    print("Full Fibonacci series:", math_obj.fibonacci_series())
