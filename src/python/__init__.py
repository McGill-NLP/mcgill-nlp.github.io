import os
from urllib.request import urlopen

from PIL import Image

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever

def parse_issue_body(body):
    """
    Parse the body of the issue and return a dictionary of the parsed data.
    """
    parsed = {}
    k = None

    for line in body.split("\n"):
        if line.startswith("###"):
            k = remove_prefix(line, prefix="###").strip().lower().replace(" ", "_")
            parsed[k] = ""
        else:
            if k is not None:
                parsed[k] += line.strip()

    return parsed

def save_url_image(fname, profile, key, image_dir, ext='jpg', size=(700, 700)):
    if key in profile and profile[key].startswith("http"):
        file_path = os.path.join(image_dir, f"{fname}.{ext}")
        os.makedirs(image_dir, exist_ok=True)
        im = Image.open(urlopen(profile[key])).convert('RGB')
        im.thumbnail(size)
        im.save(file_path)
        profile[key] = "/" + file_path


def write_content_to_file(formatted, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, formatted["filename"]), "w") as f:
        f.write(formatted["content"])


def remove_items_with_values(dictionary, value):
    return {
        k: v
        for k, v in dictionary.items()
        if v != value
    }

def remove_keys(dictionary, keys_to_remove):
    keys_to_remove = set(keys_to_remove)
    
    return {
        k: v for k, v in dictionary.items()
        if k not in keys_to_remove
    }