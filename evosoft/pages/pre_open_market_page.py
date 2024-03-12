import csv

from pages.base_page import BasePage
from pages.locators import LocatorsPreOpenMarket


class PreOpenManagePage(BasePage):

    def scroll_to_table(self):
        self.scroll_to_element(LocatorsPreOpenMarket.TABLE)

    def parser_data(self):
        table = self.browser.find_element(*LocatorsPreOpenMarket.TABLE)
        rows = table.find_elements(*LocatorsPreOpenMarket.ROWS)

        with open('output.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            csv_writer.writerow(['Имя', 'Цена'])

            for row in rows:
                name = row.find_element(*LocatorsPreOpenMarket.NAME).text
                price = row.find_element(*LocatorsPreOpenMarket.PRICE).text
                csv_writer.writerow([name, price])
