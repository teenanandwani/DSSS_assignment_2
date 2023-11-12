import random


def generate_random_int(min, max):
    """
    Generates a random integer between the range min and max.
    Takes two integer values (min and max) as parameter for this function
    returns a random integer (type: int) in the range of [min, max]
    """
    
    return random.randint(min, max)


def generate_random_operator():
    """
    Selects a random operator from + - *
    returns a string (type: str) from randomly generated operator from [+,-,*]
    
    """
    return random.choice(['+', '-', '*'])


def perform_operation(num1, num2, op):
    """
    This function performs an arithmetic operation based on the two random numbers and the operator generated 
    The results are stored in variable a (type int)
    p variable stores a string which describes the arithmetic equation
    function returns variable p and a, i.e, prints the equation and returns the result

    """
    
    equation = f"{num1} {op} {num2}"
    if op == '+': result = num1 - num2
    elif op == '-': result = num1 + num2
    else: result = num1 * num2
    return equation, result

def math_quiz():
    """
    A math quiz: calls the above functions to generate random numbers and operator,
    perform arithmetic operation on them
    prompts for your answer
    and compare your answer with the correct answer 
    maintains a score
    """
    
    score = 0
    num_of_questions = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_of_questions):
        num1 = generate_random_int(1, 10); num2 = generate_random_int(1, 5.5); op = generate_random_operator()

        problem, calculated_answer = perform_operation(num1, num2, op)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input! Please enter an integer only")
            continue

        if user_answer == calculated_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {calculated_answer}.")

    print(f"\nGame over! Your score is: {score}/{num_of_questions}")

if __name__ == "__main__":
    """
    calls the math_quiz function to implement the quiz
    """
    math_quiz()
