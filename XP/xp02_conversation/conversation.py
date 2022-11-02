"""Converstaion."""
import re
import math


class Student:
    """Student class which interacts with the server."""

    def __init__(self, biggest_number: int):
        """
        Constructor.

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
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        pass

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
        pass

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
            elif list(str(num)) == sorted(list(str(num)), reverse=True):
                decreasing_list.append(num)
            else:
                neither_list.append(num)
        if increasing:
            if to_be:
                self.possible_answers = set(increasing_list)
            else:
                self.possible_answers = set(decreasing_list + neither_list)
        else:
            if to_be:
                self.possible_answers = set(decreasing_list)
            else:
                self.possible_answers = set(increasing_list + neither_list)


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
    pass


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
    pass


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
                fibonacci_numbers.pop(1)
                break
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
            catalan_list.pop(0)
            break
    if catalan_list == [1, 1]:
        catalan_list.pop(1)
    return catalan_list


def catalan(num):
    if num <= 1:
        return 1
    result = 0
    for i in range(num):
        result += catalan(i) * catalan(num - i - 1)
    return result


regex_a = r'((?:- )?\d+)x2'
regex_b = r'((?:- )?\d+)x(?!2)'
regex_c = r'(?<!x)((?:- )?\d+)(?!x)'

if __name__ == '__main__':

    def print_regex_results(regex, f):
        for match in re.finditer(regex, f):
            print(match.group(1))


    f = "3x2 - 4x + 1"

    print_regex_results(regex_a, f)  # 3
    print_regex_results(regex_b, f)  # - 4
    print_regex_results(regex_c, f)  # 1

    f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4"

    print("x2")
    print_regex_results(regex_a, f2)  # 3, - 2
    print("x")
    print_regex_results(regex_b, f2)  # 4, - 7
    print("c")
    print_regex_results(regex_c, f2)  # 5, 4

    print(find_primes_in_range(498))

    print(find_catalan_numbers(2))
