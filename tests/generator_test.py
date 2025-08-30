import unittest
from sqlGenerator import *

class TestSQLGenerator(unittest.TestCase):
    def test_valid_sql(self):
        js="{\"name\":\"test\",\"fields\":{\"id\":\"int\",\"name\":\"text not null\"}}"
        result="CREATE TABLE test (id int,name text not null);"
        sl=SqlGenerator()
        self.assertEqual(result,sl.generate_query(js))