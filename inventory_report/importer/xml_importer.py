from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith(".xml"):
            with open(path) as file:
                tree = ET.parse(file)
                root = tree.getroot()
                products_list = [
                    {line.tag: line.text for line in record}
                    for record in root.findall("record")
                ]
                return products_list
        else:
            raise (ValueError("Arquivo inválido"))
