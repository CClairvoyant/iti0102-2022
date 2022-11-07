"""Conversation."""
import re
import math


class Student:
    """Student class which interacts with the server."""

    def __init__(self, biggest_number: int):
        """
        Construct the class.

        Save the biggest number into a variable that is attainable later on.
        Create a collection of all possible results [possible_answers] <- dont rename that (can be a list or a set)
        :param biggest_number: biggest possible number(inclusive) to guess
        NB: calculating using sets is much faster compared to lists
        """
        self.possible_answers = set([all_possible_answers for all_possible_answers in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple
        possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        if re.search("quadratic", sentence):
            if re.search("bigger", sentence):
                if re.search("times", sentence):
                    self.deal_with_quadratic_equation(re.search(r"(?<=\").+(?=\")", sentence).group(), True, float(
                        re.search(r"(?<=where ).+(?= times)", sentence).group()), True)
                elif re.search("divided", sentence):
                    self.deal_with_quadratic_equation(re.search(r"(?<=\").+(?=\")", sentence).group(), True, 1 / (
                        float(re.search(r"(?<=divided by ).+(?= and)", sentence).group())), True)
                else:
                    self.deal_with_quadratic_equation(re.search(r"(?<=\").+(?=\")", sentence).group(), False, 1, True)
            elif re.search("smaller", sentence):
                if re.search("times", sentence):
                    self.deal_with_quadratic_equation(re.search(r"(?<=\").+(?=\")", sentence).group(), True, float(
                        re.search(r"(?<=where ).+(?= times)", sentence).group()), False)
                elif re.search("divided", sentence):
                    self.deal_with_quadratic_equation(re.search(r"(?<=\").+(?=\")", sentence).group(), True, 1 / (
                        float(re.search(r"(?<=divided by ).+(?= and)", sentence).group())), False)
                else:
                    self.deal_with_quadratic_equation(re.search(r"(?<=\").+(?=\")", sentence).group(), False, 1, False)
        elif re.search("binary", sentence):
            if re.search("one in its binary", sentence) or re.search("ones in its binary", sentence):
                self.deal_with_number_of_ones(int(re.search(r"\d+(?= ones? in its binary)", sentence).group()))
            else:
                self.deal_with_number_of_zeroes(int(re.search(r"\d+(?= zeroe?s? in its binary)", sentence).group()))
        elif re.search("prime", sentence):
            self.deal_with_primes(not bool(re.search("doesn't|does not|isn't|is not", sentence)))
        elif re.search("composite", sentence):
            self.deal_with_composites(not bool(re.search("doesn't|does not|isn't|is not", sentence)))
        elif re.search("decimal", sentence):
            self.deal_with_dec_value(re.search(r"(?<=\").+(?=\")", sentence).group())
        elif re.search("hex", sentence):
            self.deal_with_hex_value(re.search(r"(?<=\").+(?=\")", sentence).group())
        elif re.search("fibonacci", sentence):
            self.deal_with_fibonacci_sequence(not bool(re.search("doesn't|does not|isn't|is not", sentence)))
        elif re.search("catalan", sentence):
            self.deal_with_catalan_sequence(not bool(re.search("doesn't|does not|isn't|is not", sentence)))
        elif re.search("order", sentence):
            self.deal_with_number_order(bool(re.search("increasing", sentence)),
                                        not bool(re.search("doesn't|does not|isn't|is not", sentence)))
        else:
            return "Something's really wrong."
        if len(self.possible_answers) == 1:
            answer = list(self.possible_answers)[0]
            return f"The number I needed to guess was {answer}."
        if len(self.possible_answers) == 0:
            return sentence
        return f"Possible answers are {sorted(self.possible_answers)}."

    def intersect_possible_answers(self, update: list):
        """
        Logical AND between two sets.

        :param update: new list to be put into conjunction with self.possible_answers
        conjunction between self.possible_answers and update
        https://en.wikipedia.org/wiki/Logical_conjunction
        """
        self.possible_answers.intersection_update(set(update))

    def exclude_possible_answers(self, update: list):
        """
        Logical SUBTRACTION between two sets.

        :param update: new list to be excluded from self.possible_answers
        update excluded from self.possible_answers
        """
        self.possible_answers.difference_update(set(update))

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int):
        """
        Filter possible_answers to match the amount of zeroes in its binary form.

        :param amount_of_zeroes: number of zeroes in the correct number's binary form
        """
        temp_list = []
        for num in self.possible_answers:
            if bin(num)[2:].count("0") == amount_of_zeroes:
                temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_number_of_ones(self, amount_of_ones: int):
        """
        Filter possible answers to match the amount of ones in its binary form.

        :param amount_of_ones: number of zeroes in the correct number's binary form
        """
        temp_list = []
        for num in self.possible_answers:
            if bin(num)[2:].count("1") == amount_of_ones:
                temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_primes(self, is_prime: bool):
        """
        Filter possible answers to either keep or remove all primes.

        Call find_primes_in_range to get all composite numbers in range.
        :param is_prime: boolean whether the number is prime or not
        """
        prime_list = find_primes_in_range(max(self.possible_answers))
        temp_list = []
        if is_prime:
            for num in self.possible_answers:
                if num in prime_list:
                    temp_list.append(num)
        else:
            for num in self.possible_answers:
                if num not in prime_list:
                    temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_composites(self, is_composite: bool):
        """
        Filter possible answers to either keep or remove all composites.

        Call find_composites_in_range to get all composite numbers in range.
        :param is_composite: boolean whether the number is composite or not
        """
        composite_list = find_composites_in_range(max(self.possible_answers))
        temp_list = []
        if is_composite:
            for num in self.possible_answers:
                if num in composite_list:
                    temp_list.append(num)
        else:
            for num in self.possible_answers:
                if num not in composite_list:
                    temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_dec_value(self, decimal_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: decimal value within the number like 9 in 192
        """
        temp_list = []
        for num in self.possible_answers:
            if decimal_value in str(num):
                temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_hex_value(self, hex_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the hex_value in them.

        :param hex_value: hex value within the number like e in fe2
        """
        temp_list = []
        for num in self.possible_answers:
            if hex_value in hex(num)[2:]:
                temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        Regex can be used here.
        Call quadratic_equation_solver with variables a, b, c.
        deal_with_dec_value should be called.
        :param equation: the quadratic equation
        :param to_multiply: whether it is necessary to multiply or divide with a given multiplicative
        :param multiplicative: the multiplicative to multiply or divide with
        :param is_bigger: to use the bigger or smaller result of the quadratic equation(min or max from [x1, x2])
        """
        answers = quadratic_equation_solver(equation)
        if type(answers) is not float:
            if is_bigger:
                answer = answers[-1]
            else:
                answer = answers[0]
        else:
            answer = answers
        if to_multiply:
            answer = answer * multiplicative
        answer = normal_round(answer)
        if answer not in self.possible_answers:
            self.possible_answers = equation
        else:
            self.deal_with_dec_value(str(answer))

    def deal_with_fibonacci_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        fibo_nums = find_fibonacci_numbers(max(self.possible_answers))
        temp_list = []
        if is_in:
            for num in self.possible_answers:
                if num in fibo_nums:
                    temp_list.append(num)
        else:
            for num in self.possible_answers:
                if num not in fibo_nums:
                    temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        catalan_nums = find_catalan_numbers(max(self.possible_answers))
        temp_list = []
        if is_in:
            for num in self.possible_answers:
                if num in catalan_nums:
                    temp_list.append(num)
        else:
            for num in self.possible_answers:
                if num not in catalan_nums:
                    temp_list.append(num)
        self.possible_answers = set(temp_list)

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        increasing_list = []
        decreasing_list = []
        neither_list = []
        for num in self.possible_answers:
            if list(str(num)) == sorted(list(str(num))):
                increasing_list.append(num)
            if list(str(num)) == sorted(list(str(num)), reverse=True):
                decreasing_list.append(num)
            if list(str(num)) != sorted(list(str(num))) and list(str(num)) != sorted(list(str(num)), reverse=True):
                neither_list.append(num)
        if increasing:
            if to_be:
                self.possible_answers = set(increasing_list)
            else:
                self.possible_answers = set(decreasing_list + neither_list).difference(set(increasing_list))
        else:
            if to_be:
                self.possible_answers = set(decreasing_list)
            else:
                self.possible_answers = set(increasing_list + neither_list).difference(set(decreasing_list))


def normalize_quadratic_equation(equation: str):
    """
    Normalize the quadratic equation.

    normalize_quadratic_equation("x2 + 2x = 3") => "x2 + 2x - 3 = 0"
    normalize_quadratic_equation("0 = 3 + 1x2") => "x2 + 3 = 0"
    normalize_quadratic_equation("2x + 2 = 2x2") => "2x2 - 2x - 2 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2") => "14x2 - x - 10 = 0"

    :param equation: quadratic equation to be normalized
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return: normalized equation
    """
    x2_list = []
    x_list = []
    num_list = []
    if equation[-3:] != "= 0":
        while equation[-1] != "=":
            if "= + " in equation:
                equation = equation.replace("= + ", "= ")
            if re.search(r"(?<==)( (?:- )?\d+)x2", equation):
                if "-" in re.search(r"(?<==)( (?:- )?\d+)x2", equation).group():
                    x2_list.append(int(re.search(r"(?<==)( (?:- )?\d+)x2", equation).group()[2:-2]))
                else:
                    x2_list.append(int("-" + re.search(r"(?<==)( (?:- )?\d+)x2", equation).group()[1:-2]))
                equation = equation.replace("=" + re.search(r"(?<==)( (?:- )?\d+)x2", equation).group(), "=")
            elif re.search(r"(?<== )x2", equation):
                x2_list.append(-1)
                equation = equation.replace("= x2", "=")
            elif re.search(r"(?<== - )x2", equation):
                x2_list.append(1)
                equation = equation.replace("= - x2", "=")
            elif "= x" in equation or "= x1" in equation:
                x_list.append(-1)
                if "= x1" in equation:
                    equation = equation.replace("= x1", "=")
                else:
                    equation = equation.replace("= x", "=")
            elif "= - x" in equation or "= - x1" in equation:
                x_list.append(1)
                if "= - x1" in equation:
                    equation = equation.replace("= - x1", "=")
                else:
                    equation = equation.replace("= - x", "=")
            elif re.search(r"(?<==)( (?:- )?\d+)x(?!2)", equation):
                if "-" in re.search(r"(?<==)( (?:- )?\d+)x(?!2)", equation).group():
                    x_list.append(int(re.search(r"(?<==)( (?:- )?\d+)x(?!2)", equation).group()[2:-1]))
                else:
                    x_list.append(int("-" + re.search(r"(?<==)( (?:- )?\d+)x(?!2)", equation).group()[1:-1]))
                equation = equation.replace("=" + re.search(r"(?<==)( (?:- )?\d+)x(?!2)", equation).group(), "=")
            elif re.search(r"(?<==)( (?:- )?\d+)(?!x)", equation):
                if "-" in re.search(r"(?<==)( (?:- )?\d+)(?!x)", equation).group():
                    num_list.append(int(re.search(r"(?<==)( (?:- )?\d+)(?!x)", equation).group()[2:]))
                else:
                    num_list.append(int("-" + re.search(r"(?<==)( (?:- )?\d+)(?!x)", equation).group()[1:]))
                equation = equation.replace("=" + re.search(r"(?<==)( (?:- )?\d+)(?!x)", equation).group(), "=")
        equation = equation + " 0"
    while equation != "= 0":
        if equation[:2] == "+ ":
            equation = equation[2:]
        if equation[:2] == "- ":
            equation = equation[2:]
            first_space = equation.find(" ")
            if re.search(r"(\d+)(?=x2)", equation[:first_space]):
                x2_list.append(int("-" + re.search(r"(\d+)(?=x2)", equation[:first_space]).group()))
                equation = equation[first_space + 1:]
            elif equation[:2] == "x2":
                x2_list.append(-1)
                equation = equation[3:]
            elif equation[0] == "x" or equation[:2] == "x1":
                x_list.append(-1)
                if equation[:2] == "x1":
                    equation = equation[3:]
                else:
                    equation = equation[2:]
            elif re.search(r"(\d+)(?=x[ |1])", equation[:first_space + 1]):
                x_list.append(int("-" + re.search(r"(\d+)(?=x)", equation[:first_space]).group()))
                equation = equation[first_space + 1:]
            elif re.search(r"(\d+)(?!x)", equation[:first_space]):
                num_list.append(int("-" + re.search(r"(\d+)(?!x)", equation[:first_space]).group()))
                equation = equation[first_space + 1:]
        else:
            first_space = equation.find(" ")
            if re.search(r"(\d+)(?=x2)", equation[:first_space]):
                x2_list.append(int(re.search(r"(\d+)(?=x2)", equation[:first_space]).group()))
                equation = equation[first_space + 1:]
            elif equation[:2] == "x2":
                x2_list.append(1)
                equation = equation[3:]
            elif equation[0] == "x" or equation[:2] == "x1":
                x_list.append(1)
                if equation[:2] == "x1":
                    equation = equation[3:]
                else:
                    equation = equation[2:]
            elif re.search(r"(\d+)(?=x[ |1])", equation[:first_space + 1]):
                x_list.append(int(re.search(r"(\d+)(?=x)", equation[:first_space]).group()))
                equation = equation[first_space + 1:]
            elif re.search(r"(\d+)(?!x)", equation[:first_space]):
                num_list.append(int(re.search(r"(\d+)(?!x)", equation[:first_space]).group()))
                equation = equation[first_space + 1:]
    x2_sum = sum(x2_list)
    x_sum = sum(x_list)
    num_sum = sum(num_list)
    if x2_sum < 0:
        x2_sum = -x2_sum
        x_sum = -x_sum
        num_sum = -num_sum
    if not x2_sum and x_sum < 0:
        x_sum = -x_sum
        num_sum = -num_sum
    if not x2_sum and not x_sum and num_sum < 0:
        num_sum = -num_sum
    if num_list and num_sum > 0:
        equation = f"+ {num_sum} " + equation
    if num_list and num_sum < 0:
        equation = f"- {-num_sum} " + equation
    if x_list and x_sum == 1:
        equation = "+ x " + equation
    if x_list and x_sum == -1:
        equation = "- x " + equation
    if x_list and x_sum > 1:
        equation = f"+ {x_sum}x " + equation
    if x_list and x_sum < -1:
        equation = f"- {-x_sum}x " + equation
    if x2_list and x2_sum == 1:
        equation = "x2 " + equation
    if x2_list and x2_sum > 1:
        equation = f"{x2_sum}x2 " + equation
    if equation[0] == "+":
        equation = equation[2:]
    return equation


def quadratic_equation_solver(equation: str):
    """
    Solve the normalized quadratic equation.

    :param equation: quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return:
    if there are no solutions, return None.
    if there is exactly 1 solution, return it.
    if there are 2 solutions, return them in a tuple, where smaller is first
    all numbers are returned as floats.
    """
    equation = normalize_quadratic_equation(equation)
    x2 = 0
    x = 0
    num = 0
    while equation != "= 0":
        if equation[:2] == "+ ":
            equation = equation[2:]
        if equation[:2] == "- ":
            equation = equation[2:]
            first_space = equation.find(" ")
            if equation[first_space - 2:first_space] == "x2":
                if equation[0].isdigit():
                    x2 = int("-" + equation[:first_space - 2])
                    equation = equation[first_space + 1:]
                else:
                    x2 = -1
                    equation = equation[3:]
            elif equation[first_space - 1:first_space] == "x":
                if equation[0].isdigit():
                    x = int("-" + equation[:first_space - 1:])
                    equation = equation[first_space + 1:]
                else:
                    x = -1
                    equation = equation[2:]
            elif equation[first_space - 2:first_space] == "x1":
                if equation[0].isdigit():
                    x = int("-" + equation[:first_space - 2])
                    equation = equation[first_space + 1:]
                else:
                    x = -1
                    equation = equation[3:]
            elif equation[:first_space].isdigit():
                num = int("-" + equation[:first_space])
                equation = equation[first_space + 1:]
        else:
            first_space = equation.find(" ")
            if equation[first_space - 2:first_space] == "x2":
                if equation[0].isdigit():
                    x2 = int(equation[:first_space - 2])
                    equation = equation[first_space + 1:]
                else:
                    x2 = 1
                    equation = equation[3:]
            elif equation[first_space - 1:first_space] == "x":
                if equation[0].isdigit():
                    x = int(equation[:first_space - 1:])
                    equation = equation[first_space + 1:]
                else:
                    x = 1
                    equation = equation[2:]
            elif equation[first_space - 2:first_space] == "x1":
                if equation[0].isdigit():
                    x = int(equation[:first_space - 2])
                    equation = equation[first_space + 1:]
                else:
                    x = 1
                    equation = equation[3:]
            elif equation[:first_space].isdigit():
                num = int(equation[:first_space])
                equation = equation[first_space + 1:]
    if x2 and x ** 2 - 4 * x2 * num >= 0:
        solution1 = (-x + math.sqrt(x ** 2 - 4 * x2 * num)) / (2 * x2)
        solution2 = (-x - math.sqrt(x ** 2 - 4 * x2 * num)) / (2 * x2)
        if solution1 != solution2:
            return tuple(sorted([solution1, solution2]))
        else:
            return solution1
    elif not x2 and x:
        return -num / x
    return None


def find_primes_in_range(biggest_number: int):
    """
    Find all primes in range(end inclusive).

    :param biggest_number: all primes in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :return: list of primes
    """
    list_of_primes = []
    for num in range(2, biggest_number + 1):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            list_of_primes.append(num)
    return list_of_primes


def find_composites_in_range(biggest_number: int):
    """
    Find all composites in range(end inclusive).

    Call find_primes_in_range from this method to get all composites
    :return: list of composites
    :param biggest_number: all composites in range of biggest_number(included)
    """
    composite_list = list(range(biggest_number + 1))
    prime_list = find_primes_in_range(biggest_number)
    for prime in prime_list:
        composite_list.remove(prime)
    if 0 in composite_list:
        composite_list.remove(0)
    if 1 in composite_list:
        composite_list.remove(1)
    return composite_list


def find_fibonacci_numbers(biggest_number: int):
    """
    Find all Fibonacci numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all fibonacci numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :return: list of fibonacci numbers
    """
    if biggest_number > 1:
        fibonacci_numbers = [0, 1]
        for i in range(2, biggest_number):
            fibonacci_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
            if fibonacci_number <= biggest_number:
                fibonacci_numbers.append(fibonacci_number)
            else:
                return fibonacci_numbers
        else:
            return fibonacci_numbers
    else:
        return list(range(biggest_number + 1))


def find_catalan_numbers(biggest_number: int):
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """
    catalan_list = []
    for num in range(biggest_number):
        if catalan(num) <= biggest_number:
            catalan_list.append(catalan(num))
        else:
            break
    return catalan_list


def catalan(num):
    """Find catalan number."""
    if num <= 1:
        return 1
    result = 0
    for i in range(num):
        result += catalan(i) * catalan(num - i - 1)
    return result


def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


# regex_a = "(.*)"
# regex_b = "(.*)"
# regex_c = "(.*)"

regex_a = r'((?<!.)(?:- )?\d+(?=x2)(?!x2\d)|(?<= )(?:- )?\d+(?=x2)(?!x2\d)|(?:- |\+ )(?=x2)(?!x2\d))'
regex_b = r'((?<!.)(?:- )?\d+(?=x1? |x1?$)|(?<= )(?:- )?\d+(?=x1? |x1?$)|(?:- |\+ )(?=x1? |x1?$))'
regex_c = r'((?<= )(?:- )?\d+(?!.)|(?<= )(?:- )?\d+(?= )|(?<!.)(?:- )?\d+(?= )|(?<!.)(?:- )?\d+(?!.))'

if __name__ == '__main__':

    def print_regex_results(regex, f):
        for match in re.finditer(regex, f):
            print(match.group(1))


    f = "- x - 7 + 3x2"

    # print_regex_results(regex_a, f)  # 3
    # print_regex_results(regex_b, f)  # - 4
    # print_regex_results(regex_c, f)  # 1
    #
    # f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4"
    #
    # print("x2")
    # print_regex_results(regex_a, f2)  # 3, - 2
    # print("x")
    # print_regex_results(regex_b, f2)  # 4, - 7
    # print("c")
    # print_regex_results(regex_c, f2)  # 5, 4

    print(quadratic_equation_solver("x2 + 2x = 3"))  # => "x2 + 2x - 3 = 0"
    print(quadratic_equation_solver("0 = 3 + 1x2"))  # => "x2 + 3 = 0"
    print(quadratic_equation_solver("2x + 2 = 2x2"))  # => "2x2 - 2x - 2 = 0"
    print(quadratic_equation_solver("0x2 - 2x = 1"))  # => "2x + 1 = 0"
    print(quadratic_equation_solver("0x2 - 2x = 1"))  # => "2x + 1 = 0"
    print(quadratic_equation_solver("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2"))  # => "14x2 - x - 10 = 0"
    print(quadratic_equation_solver("- x2 - 4x + 5 = 0"))  # => "- x2 - 4x + 5 = 0" => (-5.0, 1.0)
    print(quadratic_equation_solver("9x2 + 12x + 4 = 0"))
    print(quadratic_equation_solver("3x2 + 0 + 27x = 0"))
    print(quadratic_equation_solver("- x2 - 2x + 3 = 0"))
    print(quadratic_equation_solver("2x2 + 3x - 1 = 0"))
    print(quadratic_equation_solver("67x + 32x2 - 60x2 + 74x2 - 76 - 98 + 95 + 18x - 98x - 86x + 17 - 68x2 + 100x + 181 = 98"))

    hm = Student(100)
    print(hm.decision_branch("This number, that you need to guess is composite."))
    print(hm.decision_branch("Number includes decimal value: \"4\"."))
    print(hm.decision_branch("Number is not in increasing order."))
    print(hm.decision_branch("The aforementioned number does not occur to be in increasing order."))
    print(hm.decision_branch("Number is made up of 4 ones in its binary form."))

    u = Student(56)
    print(u.decision_branch(
        "This number is comprised dasdas of a digit where 3.0000 times the bigger result for the following quadratic equation:\"67x + 32x2 - 60x2 + 74x2 - 76 - 98 + 95 + 18x - 98x - 86x + 17 - 68x2 + 100x + 181 = 98\" is rounded to closest integer."))
    print(u.decision_branch(
        "The given ungabunga number includes a digit where 0.5625 times the bigger result for the following quadratic equation:\"59x2 - 57x + 97x2 + 45x + 87 + 67 + 41x = - 58x + 87 - 61 + 82x + 4x + 48 + 159x2\" is rounded to closest integer."))
    print(u.decision_branch(
        "Number includes sadsada a digit, where the bigger result for the following quadratic equation:\"- 39 + 41x + 75x + 54 - 67x + 171 - 70x2 - 27 - 90 - 48x = 0\" is divided by 0.3333 and is rounded to closest integer."))
    print(u.decision_branch(
        "This number, that you need to guess includes a digit where -4.9020 times the smaller result for the following quadratic equation:\"47x2 + 1x - 33x2 - 29 + 93 + 69x2 - 115 = - 38x2 + 71x2\" is rounded to closest integer."))

    uf = Student(100)
    print(uf.decision_branch(
        "I am losing my mind, because the aforementioned number involves a digit, where the smaller result for the following quadratic equation:\"- 17x2 + 79x2 = 97x + 2x2 + 117x2 - 46x - 61x + 27x - 18x - 42 - 46x2\" is divided by -0.2121 and is rounded to closest integer."))
    print(uf.decision_branch(
        "This number contains a digit, where the bigger result for the following quadratic equation:\"- 52x + 69x = - 67x2 - 49x2 + 145x - 41x2 + 3x2 - 58x - 71x + 10 - 86x2 + 175x2\" is divided by 0.3846 and is rounded to closest integer."))

    uga = Student(1000)
    print(uga.decision_branch(
        "This number I am going insane includes a digit, where the bigger result for the following quadratic equation:\"- 44 - 48x2 - 85 + 340 + 69x2 = 48 + 90x - 91x + 86x2 + 97\" is divided by 0.2031 and is rounded to closest integer."))
    print(uga.decision_branch(
        "This number I am going insane includes a digit, where the bigger result for the following quadratic equation:\"- 44 - 48x2 - 85 + 340 + 69x2 = 48 + 90x - 91x + 86x2 + 97\" is divided by 0.2031 and is rounded to closest integer."))


    ugabuga = Student(1000)
    ugabuga.deal_with_quadratic_equation("- 44 - 48x2 - 85 + 340 + -x2 = 48 + 90x - 91x + 86x2 + 97", True, -5.0000, True)
    print(ugabuga.possible_answers)
    # ugugagaga
