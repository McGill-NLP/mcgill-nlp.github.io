"""
To resize an image, you can use the following command:
```bash
python -m src.python.cli.optimize_images --source_dir assets/images/bio/ --move_originals_to assets/originals/bio/
```

This will resize all images in `assets/images/bio/` to a resolution of 300x300, and move the original images to `assets/originals/bio/`. You can replace `assets/images/bio/` with the directory of your choice. Note that this will only work for `jpg` images.
"""
import argparse
from pathlib import Path
import shutil

from tqdm import tqdm
from PIL import Image

def main(source_dir: str, move_originals_to: str):
    print(f"Optimizing images in {source_dir} and moving the originals to {move_originals_to}")
    source_dir: Path = Path(source_dir)
    move_originals_to: Path = Path(move_originals_to)
    move_originals_to.mkdir(parents=True, exist_ok=True)

    if not source_dir.exists():
        print(f"Directory {source_dir} does not exist.")
        return
    
    all_images = []
    for extension in ["jpg", "jpeg", "png", "webp"]:
        all_images.extend(list(source_dir.glob(f"*.{extension}")))
        
    # Allow jpg, jpeg, png, webp
    for image_path in tqdm(all_images):
        if str(image_path).endswith('avatar.webp'):
            print(f"Skipping {image_path} as it is already a thumbnail.")
            continue
        
        # First, get the extension of the image
        img_ext = image_path.suffix.lower()
        if img_ext not in [".jpg", ".jpeg", ".png", ".webp"]:
            print(f"Skipping {image_path} as it is not a jpg or jpeg image.")
            continue
        
        im = Image.open(image_path)
        
        # Remove transparency if it's a png
        if img_ext == ".png":
            im = im.convert("RGB")
        
        # If the image is not square, we crop it to make it square
        if im.width != im.height:
            size = min(im.width, im.height)
            left = (im.width - size) / 2
            top = (im.height - size) / 2
            right = (im.width + size) / 2
            bottom = (im.height + size) / 2
            im = im.crop((left, top, right, bottom))
        
        im.thumbnail((300, 300))
        
        # First, we move the original image to the `move_originals_to` directory
        im.save(image_path.with_suffix(".avatar.webp"), "WEBP", quality=80)
        
        print(f"Optimized {image_path} and saved it as {image_path.with_suffix('.thumbnail.webp')}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize images")
    parser.add_argument("--source_dir", type=str, required=True, help="Source directory")
    parser.add_argument("--move_originals_to", type=str, required=True, help="Move originals to")
    args = parser.parse_args()
    main(args.source_dir, args.move_originals_to)