import unittest
import math

from vector_2d import Vector2D


class Particle:
    def __init__(self, position, momentum, mass):
        """
        Ininitialise the particle with a position and momentum vectors and a mass
        """
        self.position = position
        self.momentum = momentum
        self.mass = mass

    def get_velocity(self):
        """
        Return the velocity vector of the particle
        """
        return self.momentum/self.mass

    def get_energy(self):
        """
        Return kinetic enrgy of the particle
        """
        return self.momentum*self.momentum/(2*self.mass)

    # The ``@property`` modifies the function so that we can call it without the
    # parantheses, like a property, e.g. just ``particle.velocity``
    @property
    def velocity(self):
        return self.get_velocity()

    @property
    def energy(self):
        return self.get_energy()

class Complex:
    
    def __init__(self, real, imag):
        if not isinstance(real,(int,float)) or not isinstance(imag,(int,float)):
            raise ValueError("Both arguments must be numbers.")
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Cannot add Complex to " + str(type(other)))
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Cannot subtract " + str(type(other)) + " from Complex")
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __eq__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Cannot compare Complex and" + str(type(other)))
        return self.real == other.real and self.imag == other.imag

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        else:
            raise ValueError("Cannot multiply Complex with " + str(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)
    
    #@property
    def magnitude(self):
        return math.sqrt(self.real**2+self.imag**2)

    #@property
    def conjugate(self):
        return Complex(self.real, -self.imag)

    #@property
    def to_polar(self):
        return (self.magnitude(), math.atan(self.imag/self.real))


if __name__ == "__main__":
    unittest.main(module="test_exercise02_homework", verbosity=2)
