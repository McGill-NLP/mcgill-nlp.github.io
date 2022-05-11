import os
from urllib.request import urlopen

from PIL import Image

def parse_issue_body(body):
    """
    Parse the body of the issue and return a dictionary of the parsed data.
    """
    parsed = {}
    k = None

    for line in body.split("\n"):
        if line.startswith("###"):
            k = line.removeprefix("###").strip().lower().replace(" ", "_")
            parsed[k] = ""
        else:
            if k is not None:
                parsed[k] += line.strip()

    return parsed

def save_url_image(fname, profile, key, path, ext='jpg', size=(700, 700)):
    if key in profile and profile[key].startswith("http"):
        file_path = f"{path}/{fname}.{ext}"
        os.makedirs(path, exist_ok=True)
        im = Image.open(urlopen(profile[key])).convert('RGB')
        im.thumbnail(size)
        im.save(file_path)
        profile[key] = "/" + file_path