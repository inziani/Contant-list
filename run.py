from contacts import Contacts


def create_contact(fname, lname, phone, email):
    """Function to create a new contact """
    new_contact = Contacts(fname, lname, phone, email)
    return new_contact
