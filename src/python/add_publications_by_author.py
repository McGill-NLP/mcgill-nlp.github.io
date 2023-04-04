import os
import json
from urllib.request import urlopen

from . import parse_issue_body, write_content_to_file
from .add_update_publication import generate_publication_post
from .add_publication_by_id import wrangle_fetched_content


def fetch_content(parsed):
    url = urlopen(
        f"https://api.semanticscholar.org/graph/v1/author/{parsed['author_id']}?fields=papers.title,papers.venue,papers.year,papers.publicationDate,papers.authors,papers.externalIds,papers.url,papers.abstract,papers.externalIds"
    )
    data = json.loads(url.read())

    return data


def main(parsed, save_dir="_posts/papers", use_ignore_list=True):
    ignore_list_fname = "records/semantic_paper_ids_ignored.json"

    if use_ignore_list and os.path.exists(ignore_list_fname):
        with open(ignore_list_fname) as f:
            ignored_ids = set(json.loads(f.read()))
    else:
        ignored_ids = set()

    fetched = fetch_content(parsed)
    cleaned = []

    for paper_json in fetched["papers"]:
        paper_id = paper_json['paperId']

        start = int(parsed["start"])
        end = int(parsed["end"])
        if paper_json['publicationDate']:
            year = int(paper_json['publicationDate'].split('-')[0])
        else:
            year = int(paper_json["year"])

        if year >= start and year <= end and paper_id not in ignored_ids:
            ignored_ids.add(paper_id)
            paper_json = wrangle_fetched_content(parsed, paper_json)  # in-place
            formatted = generate_publication_post(paper_json)
            cleaned.append(formatted)
            write_content_to_file(formatted, save_dir)

    with open(ignore_list_fname, "w") as f:
        json.dump(sorted(ignored_ids), f, indent=2)

    return {'cleaned': cleaned, 'ignored': ignored_ids}


if __name__ == "__main__":
    issue_body = os.environ['ISSUE_BODY']
    parsed = parse_issue_body(issue_body)
    main(parsed)
