import argparse
from pathlib import Path
import shutil


def replace_files(source_dir, target_dir, only_in_target=False):
    """
    Replace all files in target_dir with files in source_dir. If only_in_target is True,
    only replace files in target_dir that are also in source_dir.
    """
    print(
        f"Replacing files in {target_dir} with files in {source_dir} (only_in_target={only_in_target})"
    )
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    for fname in source_dir.iterdir():
        if only_in_target and fname.name not in target_dir.iterdir():
            print(f"Skipping {fname} because it is not in {target_dir}")
            continue

        print(f"Copying {fname} to {target_dir}")
        shutil.copy(fname, target_dir / fname.name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source_dir", help="The directory with the new files.")
    parser.add_argument("--target_dir", help="The directory with the old files.")
    parser.add_argument(
        "--only_in_target",
        help="Only replace files in target_dir that are also in source_dir.",
        default="true",
        choices=["true", "false"],
    )
    args = parser.parse_args()

    only_in_target = args.only_in_target == "true"

    replace_files(args.source_dir, args.target_dir, only_in_target=only_in_target)


if __name__ == "__main__":
    main()
