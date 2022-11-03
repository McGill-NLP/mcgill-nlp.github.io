import os
from pathlib import Path

from ruamel.yaml import YAML

from . import save_url_image, parse_issue_body, remove_keys, remove_items_with_values


def format_site_label(name):
    if name == "github":
        return "GitHub"
    elif name in ["twitter", "scholar", "website"]:
        return name.title()
    else:
        return name


def format_parsed_content(parsed):
    """
    Format the parsed content into a string.
    """
    parsed["alumni"] = parsed["status"] == "Alumni"

    parsed["links"] = [
        {"label": format_site_label(key), "url": parsed[key]}
        for key in ["website", "twitter", "github", "scholar"]
        if parsed[key] != "_No response_"
    ]

    parsed = remove_keys(
        parsed, 
        keys_to_remove=["status", "website", "twitter", "github", "scholar", "action"]
    )
    parsed = remove_items_with_values(parsed, "_No response_")
    
    return parsed

def merge_links(old_links, new_links):
    new_labels = {link["label"] for link in new_links}
    out_links = [
        link for link in old_links
        if link["label"] not in new_labels
    ]

    out_links.extend(new_links)

    return out_links

def sort_by_lastname(authors):
    lastname_to_user = {
        desc['name'].split()[-1] + user: user
        for user, desc in authors.items()
    }

    for key in sorted(lastname_to_user, reverse=True):
        user = lastname_to_user[key]
        desc = authors.pop(user)
        authors.insert(0, user, desc)

def main(parsed, site_data_dir="_data/", image_dir="assets/images/bio"):
    site_data_dir = Path(site_data_dir)
    profile = format_parsed_content(parsed)

    yaml = YAML()
    yaml.preserve_quotes = True
    with open(site_data_dir / "authors.yml") as f:
        authors = yaml.load(f)
    name_to_username = {authors[username]["name"]: username for username in authors}

    if parsed['action'] == 'Add member':
        if profile["name"] not in authors:
            username = profile["name"]
        else:
            n = 2
            while (k := f'{profile["name"]} {n}') in authors:
                n += 1
            username = k

        authors[username] = profile
    
    else:
        if profile['name'] not in name_to_username:
            raise ValueError(f'{profile["name"]} not in authors')
        
        username = name_to_username[profile['name']]
        profile['links'] = merge_links(authors[username].get('links', []), profile.get('links', []))
        authors[username].update(profile)
    
    save_url_image(fname=username, profile=authors[username], key="avatar", image_dir=image_dir)
    
    sort_by_lastname(authors)

    with open(site_data_dir / "authors.yml", "w") as f:
        yaml.dump(authors, f)

    return authors


if __name__ == "__main__":
    issue_body = os.environ["ISSUE_BODY"]
    parsed = parse_issue_body(issue_body)
    main(parsed)
