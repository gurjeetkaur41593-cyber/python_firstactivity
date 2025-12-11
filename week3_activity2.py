class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    # ---- Write Mode ----
    def write_file(self, content):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(content)
            print("✔ Content written successfully.")
        except Exception as e:
            print("Error writing file:", e)

    # ---- Append Mode ----
    def append_file(self, content):
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(content)
            print("✔ Content appended successfully.")
        except Exception as e:
            print("Error appending to file:", e)

    # ---- Read Mode ----
    def read_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read()
                print("----- File Content -----")
                print(data)
                print("\n*** End of File Reached ***")
                return data
        except Exception as e:
            print("Error reading file:", e)

    # ---- Count '*' characters ----
    def count_stars(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read()
                star_count = data.count("*")
                print(f"Total '*' characters: {star_count}")
                return star_count
        except Exception as e:
            print("Error counting stars:", e)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    handler = FileHandler("demo.txt")

    # Write content
    handler.write_file("Hello * World\nThis is a test * file.\n")

    # Append more content
    handler.append_file("Appending more text ** here.\n")

    # Read file content
    file_content = handler.read_file()

    # Count '*' characters
    handler.count_stars()
