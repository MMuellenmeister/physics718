import unittest
from math import pi, sqrt

from exercise02_homework import Complex, Particle
from vector_2d import Vector2D


# You can put interactive code here that will run when the file is run as a script
# Feel free to instantiate classes here and print outputs for debugging.
class TestParticle(unittest.TestCase):
    def setUp(self):
        self.pos = Vector2D(3, 4)
        self.mom = Vector2D(-0.5, 1)
        self.mass = 2.5
        self.part = Particle(self.pos, self.mom, self.mass)

    def test_init(self):
        "1. a) Test particle initialisation"
        self.assertEqual(self.part.mass, self.mass)
        self.assertEqual(self.part.momentum, self.mom)
        self.assertEqual(self.part.position, self.pos)

    def test_get_velocity(self):
        "1. b) get_velocity"
        self.assertEqual(self.part.get_velocity(), Vector2D(-0.2, 0.4))

    def test_get_energy(self):
        "1. c)  get_energy"
        self.assertAlmostEqual(self.part.get_energy(), 0.25)

    def test_property_functions(self):
        "1. d)  Property functions"
        self.assertEqual(self.part.get_energy(), self.part.energy)
        self.assertEqual(self.part.get_velocity(), self.part.velocity)


class TestComplex(unittest.TestCase):
    def test_init(self):
        "2. a) test __init__"
        c = Complex(42, 13)
        self.assertEqual(c.real, 42)
        self.assertEqual(c.imag, 13)

    def test_equal(self):
        "2 b) test =="
        c1 = Complex(42, 13)
        c2 = Complex(c1.real, c1.imag)
        self.assertEqual(c1, c2)

    def test_add(self):
        "2 b) test +"
        c1 = Complex(1, 1.5)
        c2 = Complex(-1, 2)
        sum_our = c2 + c1
        sum_python = complex(c2.real, c2.imag) + complex(c1.real, c1.imag)
        self.assertEqual(sum_our, Complex(sum_python.real, sum_python.imag))

    def test_substract(self):
        "2 b) test -"
        c1 = Complex(1, 1.5)
        c2 = Complex(-1, 2)
        sub_our = c2 - c1
        sub_python = complex(c2.real, c2.imag) - complex(c1.real, c1.imag)
        self.assertEqual(sub_our, Complex(sub_python.real, sub_python.imag))

    def test_magnitude(self):
        "2 c) test magnitude"
        c = Complex(1, 1.5)
        self.assertEqual(c.magnitude(), Vector2D(c.real, c.imag).magnitude())

    def test_conjugate(self):
        "2 c) test conjugate"
        c = Complex(1, 1.5)
        self.assertEqual(c.conjugate(), Complex(1, -1.5))

    def test_to_polar(self):
        "2 c) test to_polar"
        c = Complex(1, 1)
        r, phi = c.to_polar()
        self.assertAlmostEqual(phi, pi / 4)
        self.assertAlmostEqual(r, sqrt(2))

    def test_mul_with_scalar(self):
        "2 d) test multiplication with scalar"
        self.assertEqual(Complex(1, 1.5) * 2, Complex(2, 3))
        self.assertEqual(2.0 * Complex(1, 1.5), Complex(2, 3))

    def test_mul_two_complex_numbers(self):
        "2 d) test multiplication of two complex numbers"
        c1 = Complex(1, 1.5)
        c2 = Complex(-1, 2)
        prod_our = c2 * c1
        prod_python = complex(c2.real, c2.imag) * complex(c1.real, c1.imag)
        self.assertEqual(prod_our, Complex(prod_python.real, prod_python.imag))


if __name__ == "__main__":
    unittest.main(verbosity=2)
