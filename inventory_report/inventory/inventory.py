import csv
import json
import xml.etree.ElementTree as ET
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        if path.endswith(".csv"):
            products_list = Inventory.read_file_csv(path)
        elif path.endswith(".json"):
            products_list = Inventory.read_file_json(path)
        elif path.endswith(".xml"):
            products_list = Inventory.read_file_xml(path)

        if type == "simples":
            return SimpleReport.generate(products_list)

        return CompleteReport.generate(products_list)

    @staticmethod
    def read_file_csv(path):
        with open(path) as file:
            products = csv.DictReader(file)
            products_list = [product for product in products]
            return products_list

    @staticmethod
    def read_file_json(path):
        with open(path) as file:
            products_list = json.load(file)
            return products_list

    @staticmethod
    def read_file_xml(path):
        with open(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            products_list = [
                {line.tag: line.text for line in record}
                for record in root.findall("record")
            ]
            return products_list
