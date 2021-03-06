import unittest
from typing import List, Any
from pathlib import Path
from snakeparse.api import SnakeParse, SnakeParser


class _DummyParser(SnakeParser):

    def parse_args(self, args: List[str]) -> Any:
        return 'parse_args: ' + ', '.join(args)

    def parse_args_file(self, args_file: Path) -> Any:
        return f'parse_args_file: {args_file}'

    def print_help(self) -> None:
        return 'print_help'


class SnakeParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = _DummyParser()
        self.parser.group = 'group'
        self.parser.description = 'description'

    def test_parse_args(self):
        args = ['1', 'A', 'B', 'C']
        self.assertEqual(self.parser.parse_args(args=args), 'parse_args: ' + ', '.join(args))

    def test_parse_config(self):
        args_file = Path('/some/path')
        config = { SnakeParse.ARGUMENT_FILE_NAME_KEY : args_file }
        retval = self.parser.parse_config(config=config)
        self.assertEqual(retval, f'parse_args_file: {args_file}')

    def test_print_help(self):
        self.assertEqual(self.parser.print_help(), 'print_help')

    def test_group(self):
        self.assertEqual(self.parser.group, 'group')
        self.assertIsNone(_DummyParser().group)

    def test_group_del(self):
        parser = _DummyParser()
        parser.group = 'group'
        self.assertEqual(parser.group, 'group')
        del parser.group
        self.assertIsNone(parser.group)

    def test_description(self):
        self.assertEqual(self.parser.description, 'description')
        self.assertIsNone(_DummyParser().description)

    def test_description_del(self):
        parser = _DummyParser()
        parser.description = 'description'
        self.assertEqual(parser.description, 'description')
        del parser.description
        self.assertIsNone(parser.description)

    # FIXME: broken
    #def test_parse_config_none_argfile(self):
    #    config = { SnakeParse.ARGUMENT_FILE_NAME_KEY : None }
    #    retval = self.parser.parse_config(config=config)
    #    self.assertEqual(len(vars(retval)), 0)


if __name__ == '__main__':
    unittest.main()
