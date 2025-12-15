class CustomCsvReader:
    """
    Custom CSV reader implemented from scratch.
    Reads CSV files in a streaming fashion.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, "r", encoding="utf-8")
        self.eof = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.eof:
            raise StopIteration

        row = self._read_row()
        if row is None:
            raise StopIteration

        return row

    def _read_row(self):
        row = []
        field = []
        in_quotes = False

        while True:
            char = self.file.read(1)

            if char == "":
                self.eof = True
                break

            if char == '"':
                if in_quotes:
                    next_char = self.file.read(1)
                    if next_char == '"':
                        field.append('"')
                    else:
                        in_quotes = False
                        if next_char:
                            self.file.seek(self.file.tell() - 1)
                else:
                    in_quotes = True

            elif char == "," and not in_quotes:
                row.append("".join(field))
                field = []

            elif char == "\n" and not in_quotes:
                break

            else:
                field.append(char)

        if field or row:
            row.append("".join(field))
            return row

        return None
