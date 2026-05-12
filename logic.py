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
    # remove all spaces
    term = term.replace(" ", "")

    while any(op in term for op in ["*", "/", "+", "-"]):
        # check for multiplication
        if "*" in term:
            mul_index: int = term.find("*")
            num_1_str, num_1_start_index = get_left_num_as_str(term, mul_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, mul_index)

            # pars to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 * num_2)
            if "." in result_str:
                while result_str[-1] == "0":
                    result_str = result_str.removesuffix("0")

                if result_str[-1] == ".":
                    result_str = result_str.removesuffix(".")


            term = f"{term[:num_1_start_index]}{result_str}{term[num_2_end_index + 1:]}"


        # check for division
        if "/" in term:
            div_index: int = term.find("/")
            num_1_str, num_1_start_index = get_left_num_as_str(term, div_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, div_index)

            # parse to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 / num_2)
            if "." in result_str:
                while result_str[-1] == "0":
                    result_str = result_str.removesuffix("0")

                if result_str[-1] == ".":
                    result_str = result_str.removesuffix(".")

            term = f"{term[:num_1_start_index]}{result_str}{term[num_2_end_index + 1:]}"


        # check for addition
        if "+" in term:
            add_index: int = term.find("+")
            num_1_str, num_1_start_index = get_left_num_as_str(term, add_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, add_index)

            # parse to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 + num_2)
            if "." in result_str:
                while result_str[-1] == "0":
                    result_str = result_str.removesuffix("0")

                if result_str[-1] == ".":
                    result_str = result_str.removesuffix(".")

            term = f"{term[:num_1_start_index]}{result_str}{term[num_2_end_index + 1:]}"


        # check for subtraction
        if "-" in term:
            sub_index: int = term.find("-")
            num_1_str, num_1_start_index = get_left_num_as_str(term, sub_index)
            num_2_str, num_2_end_index = get_right_num_as_str(term, sub_index)

            # parse to float
            num_1 = float(num_1_str)
            num_2 = float(num_2_str)

            # get result and replace in term
            result_str = str(num_1 - num_2)
            if "." in result_str:
                while result_str[-1] == "0":
                    result_str = result_str.removesuffix("0")

                if result_str[-1] == ".":
                    result_str = result_str.removesuffix(".")

            term = f"{term[:num_1_start_index]}{result_str}{term[num_2_end_index + 1:]}"

    return term