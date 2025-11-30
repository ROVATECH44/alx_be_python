def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        result = num / den
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Non-numeric input provided."


print(safe_divide(10, 2))       # Result: 5.0
print(safe_divide(10, 0))       # Error: Cannot divide by zero.
print(safe_divide("ten", 2))    # Error: Non-numeric input provided.
print(safe_divide("10", "2"))   # Result: 5.0
