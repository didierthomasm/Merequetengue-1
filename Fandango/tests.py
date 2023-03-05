import unittest
import doctest

from django.test import TestCase
import Fandango.models


def load_tests(loader, tests, ignore):
    finder = doctest.DocTestFinder(verbose=True, exclude_empty=True)

    tests.addTests(doctest.DocTestSuite(module=Fandango.models, test_finder=finder))
    return tests
