import os
import json
import unittest
import shutil
from textwrap import dedent

import src.python.add_publications_by_author as mod


class TestAddPublicationsByAuthor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.save_dir = "tests/scratch/_posts/papers"
        shutil.move('records/semantic_paper_ids_ignored.json', 'records/old_semantic_scholar_paper_ids.json')
    
    @classmethod
    def tearDownClass(cls):
        shutil.move('records/old_semantic_scholar_paper_ids.json', 'records/semantic_paper_ids_ignored.json')


    def tearDown(self) -> None:
        if os.path.exists(self.save_dir):
            shutil.rmtree(self.save_dir)

    def add_publication_and_verify_all(self, author):
        with open(f"tests/data/add_publications_by_author/{author}/in.md") as f:
            issue_body = f.read()
        
        parsed = mod.parse_issue_body(issue_body)
        out = mod.main(parsed, save_dir=self.save_dir)
        papers = out["cleaned"]
        file2paper = {x["filename"]: x for x in papers}

        out_dir = f"tests/data/add_publications_by_author/{author}/out"

        for file in os.listdir(out_dir):
            with open(os.path.join(out_dir, file)) as f:
                expected_paper = f.read()
            error_msg = f"\n\nWe did not find this paper in the list of all papers by {author}: {file}\nList of all papers: {file2paper.keys()}"
            self.assertIn(file, list(file2paper.keys()), msg=error_msg)
            self.assertEqual(file2paper[file]["content"], expected_paper)

        with open("records/semantic_paper_ids_ignored.json") as f:
            ignored = set(json.load(f))

        # test if the paper was added to the list of ignored papers in semantic scholar IDs file
        for paper_id in out["ignored"]:
            self.assertIn(paper_id, ignored)

    def test_main_siva(self):
        self.add_publication_and_verify_all("siva")
    
    def test_main_tim(self):
        self.add_publication_and_verify_all("timothy")

    def test_main_jackie(self):
        self.add_publication_and_verify_all("jackie")


if __name__ == "__main__":
    unittest.main()
