from Helpers.BaseTest import BaseTest
from Pages.HomePage import HomePage
from Pages.TablesPage import TablesPage
from hotdog.TestStep import TestStep
from time import sleep

class TablePageTests(BaseTest):

    def test_sort_first_table_by_last_name_alphabetical(self):
        home = HomePage(self.driver)
        table = TablesPage(self.driver)

        self.driver.get(self.page_url)
        home.sync()

        home.navigate_to_data_table_page()
        table.sync()

        sort_step = TestStep("Start table sort logic")
        unsorted_last_names = table.example_1_table.get_last_names()
        table.example_1_table.sort_table_by('last name')
        sorted_last_name = table.example_1_table.get_last_names()
        sort_step("Complete")
        alphabetical = sorted_last_name
        sleep(3)
        table_verification = TestStep("Verify last names are sorted and in alphabetical order")
        assert unsorted_last_names != sorted_last_name, "Table sort by last name didn't take place"
        self.assertAlphabetical(sorted_last_name)
        table_verification("Complete")
        sleep(3)
    def test_sort_first_table_by_last_name_reversedAlphabetical(self):
        home = HomePage(self.driver)
        table = TablesPage(self.driver)

        self.driver.get(self.page_url)
        home.sync()

        home.navigate_to_data_table_page()
        table.sync()

        sort_step = TestStep("Start table sort logic")
        unsorted_last_names = table.example_1_table.get_last_names()
        table.example_1_table.sort_table_by('last name')
        sorted_last_name = table.example_1_table.get_last_names()
        sort_step("Complete")
        alphabeticalReverse = list(reversed(sorted_last_name))
        sleep(5)

        new_reverAlph = list(alphabeticalReverse)  # or `new_list = old_list[:]`
        new_reverAlph.reverse()
        sleep(10)

        table_verification = TestStep("Verify last names are sorted and in alphabetical order")
        assert new_reverAlph != sorted_last_name, "Table sort by last name didn't take place"
        self.assertAlphabetical(new_reverAlph)
        table_verification("Complete List is reversed")
        sleep(10)
    # test first table last name reversed alphabetical
    # table page element verifcation




