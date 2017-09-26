#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# IsPrime2.py
# -----------

from unittest import main, TestCase

def is_prime (n: int) -> bool :
    assert n > 0
    if n == 2 :
        return True
    if (n == 1) or ((n % 2) == 0) :
        return False
    i = 3
    while (i * i) <= n :
        if (n % i) == 0 :
            return False
        i += 2
    return True

class MyUnitTests (TestCase) :
    def test_01 (self) :
        self.assertFalse(is_prime( 1))

    def test_02 (self) :
        self.assertTrue(is_prime( 2))

    def test_03 (self) :
        self.assertTrue(is_prime( 3))

    def test_04 (self) :
        self.assertFalse(is_prime( 4))

    def test_05 (self) :
        self.assertTrue(is_prime( 5))

    def test_07 (self) :
        self.assertTrue(is_prime( 7))

    def test_09 (self) :
        self.assertFalse(is_prime( 9))

    def test_27 (self) :
        self.assertFalse(is_prime(27))

    def test_29 (self) :
        self.assertTrue(is_prime(29))

if __name__ == "__main__" : # pragma: no cover
    main()
