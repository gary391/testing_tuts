import unittest
from unittest.mock import patch
from unit_testing_corey.employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
# Instead of creating the employee object for each individual test, we can create
# two employee object,and reuse them through the code, this can be done using setUp and
# tearDone method.

# Note these should be camel cased.
# The setup method will be run before every single function
# The tearDown method will run after the end of each single test.


    def setUp(self):
        print('setUp')
        # For access these employee object with in our test, we have to
        # make them as instance attribute by adding a self before the
        # object variable. The self keyword means the emp_1 is attached
        # to the instance of the class(self). It can be accessed anywhere in the
        # class using self.

        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        """ Check if the email address is updated correctly after the name change."""
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        """Check if the full name is updated correctly after the name change."""
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        """Check if the pay is being applied to the employees"""
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """Using patch as context manager, we pass in the method we want to mock
        which is requests.get method in the employee module not the overall
        request.get, and assign a name to it as mocked_get and use this instead of
        calling in the request.get
        """
        print('test_monthly_schedule')
        with patch('unit_testing_corey.employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            # Here we are calling the method, and pass in month.
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()