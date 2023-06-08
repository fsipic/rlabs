import sys


def check_brackets(file_path):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    with open(file_path, "r") as f:
        text = f.read()
        for char in text:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or char != brackets[stack.pop()]:
                    return False
        return not stack


def main():
    if len(sys.argv) != 2:
        print("Instructions: python brackets.py <input_file_path>")
    else:
        result = check_brackets(sys.argv[1])
        if result:
            print("Braces are balanced")
        else:
            print("Braces are not balanced")


if __name__ == "__main__":
    main()
