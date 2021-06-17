# This lab report 1 is submitted by:::
#   Name: Ashish Pokhrel
#   Class: C.E.
#   Registration no: 022446-17
#   Roll: 38


import keyword

def check_keyword(arg):
    keyword_list = keyword.kwlist

    if arg in keyword_list:
        return True
    else:
        return False


def is_valid_delimiter(arg):
    del_list = [" ", "(", ")", "[", "]", "{", "}", ",", ":", ".", 
                "`", "=", ";", "+=", "-=", "*=", "/=", "%=", 
                "**=", "&=", "|=", "^=", ">>=", "<<="]

    if arg in del_list:
        return True
    else:
        return False


def is_separator(arg):
    sep_list = [".", ",", ";", "(", ")", "{", "}", "[", "]"]

    if arg in sep_list:
        return True
    else:
        return False


def is_valid_operator(arg):
    op_list = ["+", "-", "*", "**", "/", "%", "<<", ">>", 
                "&", "|", "^", "~", ">", "<=", ">=", "==", 
                "!=", "<>", "="]

    if arg in op_list:
        return True 
    else:
        return False

def is_valid_integer(arg):    
    if len(arg) == 0:
        return False

    int_list = [str(x) for x in list(range(10))]

    for x in arg:
        if x not in int_list:
            return False

    return True 


def search_token(arg, tokens):
    if arg in tokens:
        return True
    else:
        return False


def detect_token(arg):
    left, right = 0,0
    length = len(arg) - 1
    tokens = []

    while (right <= length and left <= right):
        if (not is_valid_delimiter(arg[right])):
            right += 1

        if (is_valid_delimiter(arg[right]) and left == right):
            if (is_valid_operator(arg[right])):
                if (not search_token(arg[right], tokens)):
                    tokens.append(arg[right])
                    print(f"operator: {arg[right]}")

            elif (is_separator(arg[right])):
                if(not search_token(arg[right], tokens)):
                    tokens.append(arg[right])
                    print(f"separator: {arg[right]}")

            right += 1
            left = right


        elif (is_valid_delimiter(arg[right]) and left != right or 
                (right == length and left != right)):
            
            sub = arg[left:right]

            if (not search_token(sub, tokens)):
                if (check_keyword(sub)):
                    tokens.append(sub)
                    print(f"keyword: {sub}")

                elif (is_valid_integer(sub)):
                    tokens.append(sub)
                    print(f"literal: {sub}")

                else:
                    tokens.append(sub)
                    print(f"identifier: {sub}")

            left = right



if __name__ == "__main__":
    file = open('File1.txt', 'r')
    filestr = str(file.read())

    ign_list = [" ", "\n"]

    code = ""

    for x in filestr:
        if x not in ign_list:
            code += x
        else:
            code += " "

    print("The tokens in the given code are listed below: \n")
    detect_token(code)