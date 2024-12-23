# Utility

## Resizing images

### Resizing bio images

To resize an image, you can use the following command:

```bash
python -m src.python.cli.optimize_images --source_dir assets/images/bio/
```

This will resize all images in `assets/images/bio/` to a resolution of 300x300 in webp format (they will be saved as '.avatar.webp').

### Resizing home images

To resize an image, you can use the following command:

```bash
python -m src.python.cli.optimize_homepage_images --source_dir assets/images/home/
```
