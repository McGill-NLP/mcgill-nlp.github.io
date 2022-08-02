import unittest
from textwrap import dedent

import src.python.add_publication_by_id as mod



class TestAddPublicationById(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('tests/data/expected_post.md') as f:
            cls.expected = f.read()

    def test_add_publication_by_id(self):
        issue_body = dedent(
            """
            ### Method

            DOI

            ### Identifier

            10.18653/v1/2021.acl-long.416

            ### Month

            08

            ### Day

            01    
        """
        )
        parsed = mod.parse_issue_body(issue_body)
        mod.main(parsed)

        with open("_posts/papers/2020-08-01-2004.09456.md", "r") as f:
            content = f.read()

        self.assertEqual(content, self.expected)

if __name__ == "__main__":
    unittest.main()
