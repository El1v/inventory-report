from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products_list):

        simple_report = SimpleReport.generate(products_list)
        companies_data = [
            product["nome_da_empresa"] for product in products_list
        ]
        companies_counter = Counter(companies_data)
        report = ""
        for companie, quantity in companies_counter.items():
            report += f"- {companie}: {quantity}\n"

        return (
            f"{simple_report}"
            f"\nProdutos estocados por empresa:\n"
            f"{report}"
        )
