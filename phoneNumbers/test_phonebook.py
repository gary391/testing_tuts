import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number) # number vs number looked up

    # Test case of a name that is not present in the phonebook and the test case should raise a key error

    def test_missing_name(self):
        phonebook = PhoneBook() # Instance of the class that is under the test
        with self.assertRaises(KeyError): # Check to see if a key error is being raised
            phonebook.lookup("missing_name") #Using a context manager - This means that unit test will ensure that lines
                                        # enclosed with the with statement will throw a key error, and if they do,
                                        # then the test will pass.
