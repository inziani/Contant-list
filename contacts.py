class Contacts:
    """Class that generated new instances of contacts"""

    contact_list = list()

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        """ save contacts created on to the contact list in the Contacts class List object"""
        Contacts.contact_list.append(self)

    def delete_contact(self):
        """delete_contact method deletes saved contact from the contact_list"""

        Contacts.contact_list.remove(self)

    @classmethod
    def test_find_by_number(cls, number):
        """method takes in a number and returns a contact that matches that number
        Args:
            phone number to search for
        Returns:
            contact of the person that matches that number
            """
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True
        return False

    @classmethod
    def display_contacts(cls):
        """method that returns the contact list"""
        return cls.contact_list




