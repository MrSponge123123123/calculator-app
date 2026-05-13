from typing import Literal


def get_left_num_as_str(term:str, sign_index: int) -> list:
    digits: list[str] = []
    offset: int = -1

    while sign_index + offset >= 0 and (term[sign_index + offset].isdigit() or term[sign_index + offset] == "."):
        digits.append(term[sign_index + offset])
        offset -= 1

    digit_str: str = ""
    for d in digits:
        digit_str = d + digit_str

    return digit_str, sign_index + offset + 1


def get_right_num_as_str(term:str, sign_index: int) -> list:
    digits: list[str] = []
    offset: int = 1

    while sign_index + offset < len(term) and (term[sign_index + offset].isdigit() or term[sign_index + offset] == "."):
        digits.append(term[sign_index + offset])
        offset += 1

    digit_str: str = ""
    for d in digits:
        digit_str += d

    return digit_str, sign_index + offset - 1


def calculate_as_str(term: str) -> str:
    def split_term(term: str) -> list:
        split_term: list = []

        number: str = ""
        for index in range(len(term)):
            # check if - is for a neg number
            if term[index] == "-" and term[index + 1].isdigit() and (index - 1 == -1 or (
                    not term[index - 1].isdigit() or (term[index - 1] == "(" or term[index - 1] == ")"))):
                number += term[index]
                continue

            if term[index].isdigit() or term[index] == ".":
                number += term[index]
                continue

            # add number to split term if there is no digit left
            if number:
                split_term.append(number)
                number = ""

            # add operator or parentheses to split term
            split_term.append(term[index])

        if number:
            split_term.append(number)

        return split_term
    def remove_unnecessary_float(num: str) -> str:
        if "." in num:
            while num[-1] == "0":
                num = num.removesuffix("0")

            if num[-1] == ".":
                num = num.removesuffix(".")

        return num
    def solve(split_term: list, operator: Literal["*", "/", "+", "-"]) -> str:
        while operator in split_term:
            operator_index: int = split_term.index(operator)
            num_1_str = split_term[operator_index - 1]
            num_2_str = split_term[operator_index + 1]

            # parse to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result = 0
            if operator == "/":
                result = num_1 / num_2
            elif operator == "*":
                result = num_1 * num_2
            elif operator == "+":
                result = num_1 + num_2
            elif operator == "-":
                result = num_1 - num_2

            result_str = remove_unnecessary_float(str(result))

            split_term = split_term[:operator_index - 1] + [result_str] + split_term[operator_index + 2:]

        return split_term
    def solve_parentheses(split_term: list) -> list:
        def rindex(split_term: list, item) -> int:
            for i in range(len(split_term) - 1, -1):
                if split_term[i] == item:
                    return i
            return -1

        while "(" in split_term and ")" in split_term:
            index_start: int = rindex(split_term, "(")
            index_end: int = split_term.index(")", index_start)

            inner: str = split_term[index_start + 1:index_end]
            result: str = calculate_as_str(inner)

            split_term = split_term[:index_start] + [result] + term[index_end + 1:]

        return term

    # remove all spaces
    term = term.replace(" ", "")

    # solve term
    split_term = split_term(term)
    split_term = solve(split_term, "*")
    split_term = solve(split_term, "/")
    split_term = solve(split_term, "+")
    split_term = solve(split_term, "-")

    return split_term[0]