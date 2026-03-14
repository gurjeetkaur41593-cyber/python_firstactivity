from abc import ABC, abstractmethod
import csv
import json
import xml.etree.ElementTree as ET

# -----------------------------
# Abstract Base Class
# -----------------------------
class Exporter(ABC):

    @abstractmethod
    def export(self, data):
        pass


# -----------------------------
# CSV Exporter
# -----------------------------
class CSVExporter(Exporter):

    def export(self, data):
        with open("dataCSV.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print("✅ Data exported to CSV format")


# -----------------------------
# JSON Exporter
# -----------------------------
class JSONExporter(Exporter):

    def export(self, data):
        with open("dataJSON.json", "w") as file:
            json.dump(data, file, indent=4)
        print("✅ Data exported to JSON format")


# -----------------------------
# XML Exporter
# -----------------------------
class XMLExporter(Exporter):

    def export(self, data):
        root = ET.Element("dataset")

        for item in data:
            record = ET.SubElement(root, "record")
            for key, value in item.items():
                element = ET.SubElement(record, key)
                element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write("dataXML.xml")
        print("✅ Data exported to XML format")


# -----------------------------
# Factory Class
# -----------------------------
class ExporterFactory:

    @staticmethod
    def get_exporter(format_type):
        if format_type == "csv":
            return CSVExporter()
        elif format_type == "json":
            return JSONExporter()
        elif format_type == "xml":
            return XMLExporter()
        else:
            raise ValueError("❌ Invalid export format selected")


# -----------------------------
# Main Program (Runtime Selection)
# -----------------------------
def main():

    # Sample dataset
    data = [
        {"id": 1, "name": "Alice", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Charlie", "age": 28}
    ]

    print("\nSelect export format:")
    print("1. CSV")
    print("2. JSON")
    print("3. XML")

    choice = input("Enter your choice (1/2/3): ")

    format_map = {
        "1": "csv",
        "2": "json",
        "3": "xml"
    }

    exporter = ExporterFactory.get_exporter(format_map.get(choice))
    exporter.export(data)


# Program entry point
if __name__ == "__main__":
    main()
