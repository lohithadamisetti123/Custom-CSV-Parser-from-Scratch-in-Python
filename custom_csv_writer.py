class CustomCsvWriter:
    """
    Custom CSV writer implemented from scratch.
    Writes data to CSV format.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data):
        with open(self.file_path, "w", encoding="utf-8", newline="") as f:
            for row in data:
                line = self._format_row(row)
                f.write(line + "\n")

    def _format_row(self, row):
        formatted_fields = []

        for field in row:
            field = str(field)

            if self._needs_quotes(field):
                field = field.replace('"', '""')
                field = f'"{field}"'

            formatted_fields.append(field)

        return ",".join(formatted_fields)

    def _needs_quotes(self, field):
        return "," in field or '"' in field or "\n" in field
