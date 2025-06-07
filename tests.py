from functions.get_file_content import get_file_content
from functions.run_file import run_python_file
from functions.write_file import write_file



def test():
    result = run_python_file("calculator", "main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print("")    

if __name__ == "__main__":
    test()