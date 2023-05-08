from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as file:
                products_list = json.load(file)
                return products_list
        else:
            raise (ValueError("Arquivo inválido"))
