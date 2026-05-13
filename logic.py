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
    def remove_unnecessary_float(num: str) -> str:
        if "." in num:
            while num[-1] == "0":
                num = num.removesuffix("0")

            if num[-1] == ".":
                num = num.removesuffix(".")

        return num
    def solve_multiplication(term: str) -> str:
        while "*" in term:
            mul_index: int = term.find("*")
            num_1_str, num_1_start_index = get_left_num_as_str(term, mul_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, mul_index)

            # pars to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 * num_2)
            result_str = remove_unnecessary_float(result_str)

            term = term[:num_1_start_index] + result_str + term[num_2_end_index + 1:]

        return term
    def solve_division(term: str) -> str:
        while "/" in term:
            div_index: int = term.find("/")
            num_1_str, num_1_start_index = get_left_num_as_str(term, div_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, div_index)

            # parse to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 / num_2)
            result_str = remove_unnecessary_float(result_str)
            term = term[:num_1_start_index] + result_str + term[num_2_end_index + 1:]

        return term
    def solve_addition(term: str) -> str:
        while "+" in term:
            add_index: int = term.find("+")
            num_1_str, num_1_start_index = get_left_num_as_str(term, add_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, add_index)

            # parse to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 + num_2)
            result_str = remove_unnecessary_float(result_str)
            term = term[:num_1_start_index] + result_str + term[num_2_end_index + 1:]

        return term
    def solve_subtraction(term: str) -> str:
        while "-" in term:
            sub_index: int = term.find("-")
            num_1_str, num_1_start_index = get_left_num_as_str(term, sub_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, sub_index)

            # parse to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 - num_2)
            result_str = remove_unnecessary_float(result_str)

            term = term[:num_1_start_index] + result_str + term[num_2_end_index + 1:]

        return term

    # remove all spaces
    term = term.replace(" ", "")

    # check and solve brackets
    while "(" in term and ")" in term:
        index_start: int = term.rfind("(")
        index_end: int = term.find(")", index_start)

        bracket: str = term[index_start + 1:index_end]
        result: str = calculate_as_str(bracket)

        term = term[:index_start] + result + term[index_end + 1:]


    term = solve_multiplication(term)
    term = solve_division(term)
    term = solve_addition(term)
    term = solve_subtraction(term)

    return term