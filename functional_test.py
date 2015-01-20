from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

	# She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
	                 'Enter a to-do item')

	# She types 'Buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')


	# When she hits enter, the page updates, and now page lists
	# "1: Buy peacock feathers" as an item in a to-do lists table
        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element_by_id('id_list_table')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn("2: Use peacock feathers to make a fly", [row.text for row in rows])
	# self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table 00 its text was:\n%s" % (table.text,))
	
        # There is still a text box inviting her to add another
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')



