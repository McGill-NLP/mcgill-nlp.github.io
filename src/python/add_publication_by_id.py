import os
import json
import time
from urllib.request import urlopen

from ruamel.yaml import YAML

from . import parse_issue_body, write_content_to_file, remove_items_with_values
from .add_update_publication import generate_publication_post

def normalize_venue_names(venue):
    d = {
        'Annual Meeting of the Association for Computational Linguistics': 'ACL',
    }

    return d.get(venue, venue)

def fetch_content(parsed, max_retry=3):
    method = parsed["method"]
    identifier = parsed["identifier"]
    try:
        url = urlopen(
            f"https://api.semanticscholar.org/graph/v1/paper/{method}:{identifier}?fields=title,venue,year,publicationDate,authors.name,externalIds,url,abstract"
        )
        data = json.loads(url.read())
    except Exception as e:
        if max_retry > 0:
            # First, sleep for 20 second to avoid rate limiting
            time.sleep(20)
            return fetch_content(parsed, max_retry - 1)
        else:
            raise e

    return data


def create_attr_to_username_map(lab_members, attribute):
    """
    Given a dictionary where key is a lab member's username, and the values are
    a dictionary containing their information (see _posts/authors.yml), create
    a dictionary mapping the value of the given attribute to the username.
    """
    return {
        member_info[attribute]: username
        for username, member_info in lab_members.items()
        if attribute in member_info
    }


def filter_keys(d, keys):
    """
    Only keep the keys in the dictionary that are in the given list.
    """
    return {key: d[key] for key in keys if key in d}


def wrangle_fetched_content(parsed, paper_json):
    with open("_data/authors.yml") as f:
        yaml = YAML()
        yaml.preserve_quotes = True
        lab_members = yaml.load(f)

    parsed = remove_items_with_values(parsed, "_No response_")

    author_names = [data["name"] for data in paper_json["authors"]]
    paper_json["names"] = ", ".join(author_names)
    paper_json["tags"] = paper_json["venue"]
    paper_json["shorthand"] = str(paper_json["paperId"])
    paper_json["link"] = paper_json["url"]

    if paper_json["publicationDate"]:
        year, month, day = paper_json["publicationDate"].split("-")
    else:
        year, month, day = paper_json["year"], "01", "01"

    paper_json["year"] = parsed.get("year", year)
    paper_json["month"] = parsed.get("month", month)
    paper_json["day"] = parsed.get("day", day)

    if "ArXiv" in paper_json["externalIds"]:
        link = f"https://arxiv.org/abs/{paper_json['externalIds']['ArXiv']}"
        paper_json["link"] = link
        paper_json["shorthand"] = paper_json["externalIds"]["ArXiv"]
    elif "DOI" in paper_json["externalIds"]:
        paper_json["link"] = f"https://doi.org/{paper_json['externalIds']['DOI']}"
        paper_json["shorthand"] = paper_json["externalIds"]["DOI"]
    elif "ACL" in paper_json["externalIds"]:
        paper_json["shorthand"] = paper_json["externalIds"]["ACL"]

    for key in ["title", "names", "tags", "venue", "shorthand", "link"]:
        paper_json[key] = paper_json[key].replace("\n", " ")

    # Normalize the venue names
    if 'venue' in paper_json and paper_json["venue"] is not None:
        paper_json["venue"] = normalize_venue_names(paper_json["venue"])
    if 'tags' in paper_json:
        tags = [t.strip() for t in paper_json["tags"].split(", ")]
        normalized_tags = [normalize_venue_names(t) for t in tags]
        paper_json["tags"] = ",".join(normalized_tags)
    
    
    fullname_to_username = create_attr_to_username_map(lab_members, "name")
    member_id_to_username = create_attr_to_username_map(
        lab_members, "semantic_scholar_id"
    )

    for author in paper_json["authors"]:
        if author["authorId"] in member_id_to_username:
            paper_json["author"] = member_id_to_username[author["authorId"]]
            break

        if author["name"] in fullname_to_username:
            paper_json["author"] = fullname_to_username[author["name"]]
            break

    keys_to_keep = [
        # "paperId",
        # "externalIds",
        # "url",
        "title",
        "abstract",
        "venue",
        "year",
        # "openAccessPdf",
        # "publicationDate",
        # "authors",
        "names",
        "tags",
        "shorthand",
        "link",
        "month",
        "day",
        "author",
    ]

    paper_json = filter_keys(paper_json, keys_to_keep)

    return paper_json


def main(parsed, save_dir="_posts/papers"):
    paper_json = fetch_content(parsed)
    paper_json = wrangle_fetched_content(parsed, paper_json)  # in-place
    formatted = generate_publication_post(paper_json)
    write_content_to_file(formatted, save_dir)


if __name__ == "__main__":
    issue_body = os.environ["ISSUE_BODY"]
    parsed = parse_issue_body(issue_body)
    main(parsed)
