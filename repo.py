import json
from os import path

class Repo:
    def __init__(self, filename: str) -> None:
        self.__filename = filename
    
    def save_items(self, data) -> None:
        with open(self.__filename, 'w') as file:
            json.dump(data, file)

    def get_items(self) -> dict[str, str | float | int]:
        with open(self.__filename, "r") as file:
            data = json.load(file)
            return data

def main():
    cur_path: str = path.abspath(__file__)
    dir = path.dirname(cur_path)
    test_path = path.join(dir, 'test.json')
    repo = Repo(test_path)
    repo.save_items([1,2,3])
    repo.get_items()
    print(repo.get_items())

if __name__ == "__main__":
    main()