import sys


def merge_names(first_names_path, last_names_path, output_file_path):
    names = {}
    with open(first_names_path) as first_names_file:
        for line in first_names_file:
            name, id = line.split()
            id = int(id)
            names[id] = name

    with open(last_names_path) as last_names_file:
        for line in last_names_file:
            surname, id = line.split()
            id = int(id)
            if id in names:
                names[id] += " " + surname

    with open(output_file_path, "w") as output_file:
        for id, name in sorted(list(names.items())):
            output_file.write(f"{name} {id}\n")


def main():
    if len(sys.argv) != 4:
        print(
            "Instructions: python names.py <first_names_file_path> <last_names_file_path> <output_file_path>"
        )
    else:
        merge_names(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
