import unittest

#Comentando o descomentando la linea 4 o 5 se puede probar el código de discounterIA o discounterHuman
#from discounterIA import calculate_discount, apply_discount
from discounterHuman import calculate_discount, apply_discount


class TestCalculateDiscount(unittest.TestCase):
    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 10), 10)
        self.assertEqual(calculate_discount(200, 20), 40)
        self.assertEqual(calculate_discount(50, 0), 0)
        self.assertEqual(calculate_discount(0, 50), 0)
        self.assertEqual(calculate_discount(100, 100), 100)


class TestApplyDiscount(unittest.TestCase):
    def test_apply_discount(self):
        cart = [
            {'price': 100, 'discount': 10},
            {'price': 50, 'discount': 5},
            {'price': 75, 'discount': 15}
        ]
        self.assertEqual(apply_discount(cart), 201.25)

        cart = [
            {'price': 200, 'discount': 20},
            {'price': 100, 'discount': 10}
        ]
        self.assertEqual(apply_discount(cart), 250)

        cart = [
            {'price': 50, 'discount': 0},
            {'price': 75, 'discount': 0}
        ]
        self.assertEqual(apply_discount(cart), 125)

        cart = [
            {'price': 0, 'discount': 50}
        ]
        self.assertEqual(apply_discount(cart), 0)

        cart = [
            {'price': 100, 'discount': 100}
        ]
        self.assertEqual(apply_discount(cart), 0)

        cart = [
            {'price': 100, 'discount': -50},
            {'price': 100, 'discount': 150},
            {'price': 100, 'discount': 0},
            {'price': 100, 'discount': 33}
        ]
        self.assertEqual(apply_discount(cart), 267)

        cart = [
            {'price': 100, 'discount': -1}
        ]
        self.assertEqual(apply_discount(cart), 101)

        cart = [
            #       {'price': 100, 'discount': "a"}
            {'price': 100, 'discount': 200}

        ]
        self.assertEqual(apply_discount(cart), -100)

if __name__ == '__main__':
    unittest.main()