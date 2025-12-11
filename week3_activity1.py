class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def read_file(self):
        """Reads the file and stores content."""
        try:
            with open(self.filename, "r", encoding="utf-8", errors="ignore") as file:
                self.content = file.read()
            print("File read successfully.\n")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return False
        return True

    def print_content(self):
        """Prints the file content."""
        if not self.content:
            print("No content to display. Read the file first.")
        else:
            print("---- File Content ----")
            print(self.content)
            print("----------------------")

    def count_stars(self):
        """Counts the number of '*' characters in the file."""
        if not self.content:
            print("Read the file first before counting.")
            return 0
        count = self.content.count('*')
        print(f"Number of '*' characters: {count}")
        return count


# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    # filename = FileProcessor('demo.txt')

    processor = FileProcessor('demo.txt')

    if processor.read_file():
        processor.print_content()
        processor.count_stars()
