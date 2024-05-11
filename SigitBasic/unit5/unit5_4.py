def func(num1: float, num2: float) -> float:
   """
   Performs a mathematical addition operation on two numbers.

   Args:
       num1 (float): The first number.
       num2 (float): The second number.

   Returns:
       float: The result of the addition operation.
   """
   result = num1 + num2
   return result

def main():
   num1 = 3.5
   num2 = 2.7
   result = func(num1, num2)
   print(f"The result of the operation on {num1} and {num2} is: {result}\n")

   help(func)

if __name__ == "__main__":
   main()