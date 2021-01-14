from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from pcv import start, DEFAULTS_PATH, filters


class StartTests(TestCase):
    def test_initialize(self):
        with TemporaryDirectory() as tempdirname:
            temp_path = Path(tempdirname)
            start.initialize(destination=temp_path)
            # check directory contents recursively ('**')
            self.assertEqual(
                sorted(path.name for path in DEFAULTS_PATH.glob('**/*')),
                sorted(path.name for path in temp_path.glob('**/*')))


class FilterTests(TestCase):
    def test_to_iso_date(self):
        cases = [
            # (<input>, <expected output>)
            ('2021-12-13', '2021-12-13'),
            ('2021-12', '2021-12-01'),
            ('2021', '2021-01-01')
        ]
        for input_string, expected_output in cases:
            with self.subTest(input=input_string):
                self.assertEqual(
                    expected_output, filters.to_iso_date(input_string))
