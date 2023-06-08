def check_brackets(text):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    for char in text:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or char != brackets[stack.pop()]:
                return False
    return not stack


def main():
    text = input("Input text: ")
    if check_brackets(text):
        print("Braces are balanced")
    else:
        print("Braces are not balanced")


if __name__ == "__main__":
    main()
