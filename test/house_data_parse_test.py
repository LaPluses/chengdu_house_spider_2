import unittest
from os import path
from src.data import HouseData
import json


class TestParse(unittest.TestCase):

    def test_parse_house_data(self):
        with open(path.join('test', 'test.html'), 'r') as f:
            html = f.read()
            all_house_data = HouseData.parse(html)
            s = json.dumps(all_house_data, ensure_ascii=False,
                           indent=4, cls=HouseData.Encoder)
            try:
                with open(path.join('test', 'test_all_house_data.json'), 'r') as f:
                    assert (f.read() == s)
            except FileNotFoundError:
                with open(path.join('test', 'test_all_house_data.json'), 'w') as f:
                    f.write(s)
