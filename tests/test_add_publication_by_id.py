import unittest
from textwrap import dedent

import src.python.add_publication_by_id as mod



class TestAddPublicationById(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('tests/data/add_publication_by_id/2020-08-01-2004.09456.md') as f:
            cls.expected_out = f.read()

    def test_add_publication_by_id(self):
        with open('tests/data/add_publication_by_id/in.md') as f:
            issue_body = f.read()
        parsed = mod.parse_issue_body(issue_body)
        mod.main(parsed)

        with open("_posts/papers/2020-08-01-2004.09456.md", "r") as f:
            content = f.read()

        self.assertEqual(content, self.expected_out)

if __name__ == "__main__":
    unittest.main()
