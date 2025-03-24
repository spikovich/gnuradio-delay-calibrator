#!/usr/bin/env python3
import sys
import unittest
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)

from tests import test

if __name__ == "__main__":
    unittest.main()