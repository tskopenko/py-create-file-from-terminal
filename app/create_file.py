import sys
import os
from datetime import datetime


def create_directory(way: str) -> None:
    os.makedirs(way)
    current_directory = os.getcwd()
    os.chdir(os.path.join(current_directory, way))


def create_file(name: str) -> None:
    count_lines = 1
    file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_content += "\n" + str(count_lines) + " " + line
        count_lines += 1
    with open(name, "w") as file:
        file.write(file_content)


def main() -> None:
    command = sys.argv

    if "-d" in command:
        if "-f" not in command:
            path = os.path.join(*command[2:])
        else:
            path = os.path.join(*command[2:-2])
        create_directory(path)
    if "-f" in command:
        file_name = command[-1]
        create_file(file_name)
