from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from pcv import start, DEFAULTS_PATH


class StartTests(TestCase):
    def test_initialize(self):
        with TemporaryDirectory() as tempdirname:
            temp_path = Path(tempdirname)
            start.initialize(destination=temp_path)
            # check directory contents recursively ('**')
            self.assertEqual(
                sorted(path.name for path in DEFAULTS_PATH.glob('**/*')),
                sorted(path.name for path in temp_path.glob('**/*')))
