import os

class DirectoryCleaner:
    files: list[str] = []

    def __init__(self, path: str) -> None:
        self.path = path
        self.get_files_in_path()

    def get_files_in_path(self) -> None:
        try:
            self.files = os.listdir(self.path)
        except FileNotFoundError:
            print("You provided wrong path...")

    def clean_directory(self) -> None:
        print("todo")