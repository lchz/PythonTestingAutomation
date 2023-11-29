# import pytest
from Code.code import *


class TestPythonWithPytest:
    def test_add(self):
        assert add(5, 4) == 9

    def test_multiply(self):
        assert multiply(3, 4) == 12

    def test_power(self):
        assert power(2, 8) == 256
