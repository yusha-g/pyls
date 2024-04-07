class InvalidPath(Exception):
    def __init__(self, file_name: str) -> None:
        self.message=f"error: cannot access {file_name}: No such file or directory"
        super().__init__(self.message)