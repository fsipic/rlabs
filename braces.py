def check_braces(text):
    stack = []
    braces = {"(": ")", "[": "]", "{": "}"}
    for char in text:
        if char in braces:
            stack.append(char)
        elif char in braces.values():
            if not stack or char != braces[stack.pop()]:
                return False
    return not stack


def main():
    file_name = input("Enter filename: ")
    try:
        with open(file_name, "r") as file:
            text = file.read()
            if check_braces(text):
                print("Braces are balanced")
            else:
                print("Braces are not balanced")
    except IOError as error:
        print(f"An error occurred while opening the file: {error}")


if __name__ == "__main__":
    main()
