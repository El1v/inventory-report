from .importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith(".csv"):
            with open(path) as file:
                products = csv.DictReader(file)
                products_list = [product for product in products]
                return products_list
        else:
            raise (ValueError("Arquivo inválido"))
