from datetime import date
import statistics


class SimpleReport:
    @staticmethod
    def generate(products_list):
        today = date.today().strftime("%Y-%m-%d")

        older_manufacturing = [
            product["data_de_fabricacao"] for product in products_list
        ]
        nearest_expiration = [
            product["data_de_validade"]
            for product in products_list
            if product["data_de_validade"] > today
        ]
        companies_data = [
            product["nome_da_empresa"] for product in products_list
        ]
        return (
            f"Data de fabricação mais antiga: {min(older_manufacturing)}\n"
            f"Data de validade mais próxima: {min(nearest_expiration)}\n"
            f"Empresa com mais produtos: {statistics.mode(companies_data)}"
        )
