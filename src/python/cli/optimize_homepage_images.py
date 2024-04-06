"""

To resize an image, you can use the following command:
```bash
python -m src.python.cli.optimize_homepage_images --source_dir assets/images/home/
```
"""
import argparse
from pathlib import Path
import shutil

from tqdm import tqdm
from PIL import Image

def main(source_dir: str):
    print(f"Optimizing images in {source_dir}")
    source_dir: Path = Path(source_dir)

    if not source_dir.exists():
        print(f"Directory {source_dir} does not exist.")
        return
    
    all_images = []
    for extension in ["jpg", "jpeg", "png", "webp"]:
        all_images.extend(list(source_dir.glob(f"*.{extension}")))
        
    # Allow jpg, jpeg, png, webp
    for image_path in tqdm(all_images):
        if str(image_path).endswith('.webp'):
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
        
        # First, we move the original image to the `move_originals_to` directory
        im.save(image_path.with_suffix(".webp"), "WEBP", quality=80)
        
        print(f"Optimized {image_path} and saved it as {image_path.with_suffix('.webp')}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize images")
    parser.add_argument("--source_dir", type=str, required=True, help="Source directory")
    args = parser.parse_args()
    main(args.source_dir)