import unittest
import pyperclip
from contacts import Contacts


class MyTestCase(unittest.TestCase):
    """ Test class that defines test cases for the contact class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases"""

    def setUp(self):
        """set up method to run before each test cases"""
        self.new_contact = Contacts('Valentine', 'Robai', '0712345678', 'ValentineRobai.Inziani@gmail.com')

    def test_contacts_init(self):
        self.assertEqual(self.new_contact.first_name, 'Valentine')
        self.assertEqual(self.new_contact.last_name, 'Robai')
        self.assertEqual(self.new_contact.phone_number, '0712345678')
        self.assertEqual(self.new_contact.email, 'ValentineRobai.Inziani@gmail.com')

    def test_save_contact(self):
        """test_save_contact test case to test if the contact object is saved into the contact list"""
        self.new_contact.save_contact()
        self.assertEqual(len(Contacts.contact_list), 1)

    def tearDown(self):
        """tear down method does clean up after each test case has run"""

        Contacts.contact_list = []

    def test_save_multiple_contacts(self):
        """test_save_multiple_contact to check if we can save multiple contacts to the list"""
        self.new_contact.save_contact()
        test_contact = Contacts('Test', 'User', '071234786', 'test@yahoo.com')
        test_contact.save_contact()
        self.assertEqual(len(Contacts.contact_list), 2)

    def test_delete_contact(self):
        """test_delete_contact to test if we can remove a contact from our contact list"""

        self.new_contact.save_contact()
        test_contact = Contacts('Test', 'User', '071234786', 'test@yahoo.com')
        test_contact.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contacts.contact_list), 1)

    def text_find_contact_by_number(self):
        """test to check if we can find a contact by phone number and display information"""
        self.new_contact.save_contact()
        test_contact = Contacts('Test', 'User', '071234786', 'test@yahoo.com')
        test_contact.save_contact()

        found_contact = Contacts.find_by_number('0711223344')
        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        """test to check if we can return Boolean "if we cannot find the contact"""
        self.new_contact.save_contact()
        test_contact = Contacts('Test', 'User', '071234786', 'test@yahoo.com')
        test_contact.save_contact()

        contact_exists = Contacts.contact_exists('0711223344')

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        """method that returns a list of all contacts saved"""

        self.assertEqual(Contacts.display_contacts(), Contacts.contact_list)

    @classmethod
    def copy_emails(clscls, number):
        contact_found = Contacts.find_by_number(number)
        pyperclip.copy(contact_found.email)


if __name__ == '__main__':
    unittest.main()
