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

    def get_new_path(self, file_name: str, dir_name: str) -> str:
        return f"{self.path}/{dir_name}/{file_name}"

    def create_dir(self, dir_name: str) -> None:
        dir_path = f"{self.path}/{dir_name}"
        if (os.path.isdir(dir_path)):
            return
        os.mkdir(dir_path)

    def clean_directory(self) -> None:
        for file in self.files:
            file_path = f"{self.path}/{file}"
            if file.endswith(".txt"):
                self.create_dir("notes")
                os.rename(file_path, self.get_new_path(file, "notes"))
            elif file.endswith(".pdf"):
                self.create_dir("documents")
                os.rename(file_path, self.get_new_path(file, "documents"))
            elif file.endswith(tuple([".svg", ".png", ".jpg", ".jpeg", ".gif"])):
                self.create_dir("images")
                os.rename(file_path, self.get_new_path(file, "images"))
            elif file.endswith(tuple([".mp4", ".wav"])):
                self.create_dir("videos")
                os.rename(file_path, self.get_new_path(file, "videos"))
            elif file.endswith(".exe"):
                self.create_dir("apps")
                os.rename(file_path, self.get_new_path(file, "apps"))
            else:
                self.create_dir("others")
                os.rename(file_path, self.get_new_path(file, "others"))