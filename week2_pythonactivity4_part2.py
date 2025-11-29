class MathOperations:
    
    def factorial(self, n):
        """Recursive factorial"""
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        """Recursive Fibonacci"""
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    math_ops = MathOperations()

    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        num = int(input("Enter a number: "))
        ans = math_ops.factorial(num)

    elif choice == "2":
        num = int(input("Enter a number: "))
        ans = math_ops.fibonacci(num)

    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)
