import os
from pathlib import Path
import re
from urllib.request import urlopen, urlretrieve
from collections import OrderedDict

from PIL import Image


def center_square_crop(im):
    # Do a center crop
    width, height = im.size
    if width > height:
        left = (width - height) / 2
        right = left + height
        top = 0
        bottom = height
    else:
        left = 0
        right = width
        top = (height - width) / 2
        bottom = top + width
    im = im.crop((left, top, right, bottom))

    return im


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix) :]
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

def find_urls(text):
    """
    1. Find all urls using regex: https://stackoverflow.com/a/840110/13837091
    2. Remove the trailing ")"
    3. Get unique URLs only (set comprehension -> list)
    """
    return list(
        OrderedDict.fromkeys(
            [s for s in re.findall("(?P<url>https?://[^\s)]+)", text)]
        )
    )

def get_non_alpha(text):
    for ch in text:
        if not ch.isalpha():
            return ch
    return None

def save_url_image(
    fname,
    profile,
    key,
    image_dir,
    size=(400, 400),
    crop_center=False,
    convert_to_jpg=False,
    jpg_quality=80,
):
    accepted_extensions = [
        "",
        "jpg",
        "jpeg",
        "png",
        "gif",
        "svg",
        "webp",
        "bmp",
        "tiff",
        "ico",
        "eps",
        "blp",

    ]
    if key not in profile:
        return None
    
    if profile[key] == "":
        return None

    urls = find_urls(profile[key])

    if len(urls) == 0:
        return None
    
    for url in urls:
        # Get the extension of the file
        ext = os.path.splitext(url)[1][1:]
        potential_sep_char = get_non_alpha(ext)
        if potential_sep_char is not None:
            ext = ext.partition(potential_sep_char)[0]
        
        if ext not in accepted_extensions:
            print(f"Extension {ext} not in accepted extensions: {accepted_extensions}")
            continue

        if ext == "jpeg":
            ext = "jpg"
        
        image_dir = Path(image_dir)
        # Download the image
        if ext != "":
            # file_path = os.path.join(image_dir, f"{fname}.{ext}")
            file_path = image_dir / f"{fname}.{ext}"
        else:
            file_path = image_dir / f"{fname}"

        image_dir.mkdir(parents=True, exist_ok=True)
        urlretrieve(url, str(file_path))

        if ext in ["svg", "gif"]:
            return "/" + str(file_path)
        else:
            try:
                im = Image.open(file_path)
                if crop_center:
                    im = center_square_crop(im)
                im.thumbnail(size)
            
            except Exception as e:
                print(f"Could not open {url} as image due to error: {e}")
                # Remove the file
                file_path.unlink()
                continue
            
            if ext == "jpg":
                im.save(file_path, quality=jpg_quality)
            elif ext == "":
                # In this case, we force the extension to be jpg
                file_path = file_path.with_suffix(".jpg")
                im.convert("RGB").save(file_path, quality=jpg_quality)
            
            elif convert_to_jpg:
                im = im.convert("RGB")
                # Remove ext from file_path
                file_path = Path(file_path).with_suffix(".jpg")
                im.save(file_path, quality=jpg_quality)
            
            else:
                im.save(file_path)

            return "/" + str(file_path)


def write_content_to_file(formatted, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, formatted["filename"]), "w") as f:
        f.write(formatted["content"])


def remove_items_with_values(dictionary, value):
    return {k: v for k, v in dictionary.items() if v != value}


def remove_keys(dictionary, keys_to_remove):
    keys_to_remove = set(keys_to_remove)

    return {k: v for k, v in dictionary.items() if k not in keys_to_remove}
