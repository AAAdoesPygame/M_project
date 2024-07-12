import os
import subprocess
import platform


def find_program(program_name):
    """
    Finds the full path of a program.
    """
    if platform.system() == "Windows":
        # Check common program directories
        common_paths = [
            "C:\\Program Files",
            "C:\\Program Files (x86)"
        ]
        for path in common_paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower() == program_name.lower() + ".exe":
                        return os.path.join(root, file)
        # Check system PATH
        path_var = os.getenv("PATH")
        for path in path_var.split(';'):
            full_path = os.path.join(path, program_name + ".exe")
            if os.path.exists(full_path):
                return full_path
    else:
        which_cmd = "which"
        try:
            result = subprocess.run([which_cmd, program_name], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
        except FileNotFoundError:
            pass
    return None


def find_file(file_name, search_path):
    """
    Recursively search for a file starting from the specified path.
    """
    for root, dirs, files in os.walk(search_path):
        print(f"Searching in: {root}")
        if file_name in files:
            return os.path.join(root, file_name)
    return None


def open_file_with_program(program, file_path):
    """
    Opens the specified file with the specified program.
    """
    try:
        if platform.system() == "Windows":
            subprocess.run([program, file_path])
        else:
            subprocess.run([program, file_path])
    except Exception as e:
        print(f"An error occurred while trying to open the file: {e}")


def main():
    program_name = input("Enter the name of the program (e.g., Audacity): ").strip()
    file_name = input("Enter the name of the file (with extension): ").strip()

    search_path = "C:\\"

    print("Searching for the file...")
    file_path = find_file(file_name, search_path)

    if not file_path:
        print(f"File '{file_name}' not found on the C drive.")
        return

    print("Searching for the program...")
    program_path = find_program(program_name)

    if program_path:
        print(f"Program found: {program_path}")
        print(f"File found: {file_path}")
        open_file_with_program(program_path, file_path)
    else:
        print(f"Program '{program_name}' not found in common directories or PATH.")


if __name__ == "__main__":
    main()

