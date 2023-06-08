import sqlite3
import sys


def merge_names(first_names_path, last_names_path, output_file_path):
    conn = sqlite3.connect("names.db")

    conn.execute(
        "CREATE TABLE IF NOT EXISTS names (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)"
    )

    with open(first_names_path) as first_names_file:
        for line in first_names_file:
            name, id = line.split()
            id = int(id)
            conn.execute(
                f"INSERT OR REPLACE INTO names (id, first_name) VALUES ('{id}', '{name}')"
            )

    with open(last_names_path) as last_names_file:
        for line in last_names_file:
            name, id = line.split()
            id = int(id)
            conn.execute(f"UPDATE names SET last_name = '{name}' WHERE id = '{id}'")

    conn.commit()
    with open(output_file_path, "w") as output_file:
        result = conn.execute("SELECT * FROM names ORDER BY id")
        for row in result:
            output_file.write(f"{row[1]} {row[2]} {row[0]}\n")

    conn.close()


def main():
    if len(sys.argv) != 4:
        print(
            "Instructions: python names_extension.py <first_names_file_path> <last_names_file_path> <output_file_path>"
        )
    else:
        merge_names(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
