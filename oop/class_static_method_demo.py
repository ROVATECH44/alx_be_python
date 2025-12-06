# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition without needing class or instance reference."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: performs multiplication and references class attributes."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Demo usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")
