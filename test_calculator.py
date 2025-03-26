import unittest
import json
from calc_app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.get('/calculate?num1=10&num2=5&operation=add')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 15.0)

    def test_subtraction(self):
        response = self.app.get('/calculate?num1=10&num2=5&operation=subtract')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 5.0)

    def test_multiplication(self):
        response = self.app.get('/calculate?num1=10&num2=5&operation=multiply')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 50.0)

    def test_division(self):
        response = self.app.get('/calculate?num1=10&num2=5&operation=divide')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 2.0)

    def test_divide_by_zero(self):
        response = self.app.get('/calculate?num1=10&num2=0&operation=divide')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Cannot divide by zero")

    def test_invalid_operation(self):
        response = self.app.get('/calculate?num1=10&num2=5&operation=modulus')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid operation")

    def test_invalid_input(self):
        response = self.app.get('/calculate?num1=abc&num2=5&operation=add')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid input")

if __name__ == '__main__':
    unittest.main()
