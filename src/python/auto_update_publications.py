import datetime
from pathlib import Path

from ruamel.yaml import YAML

from . import add_publications_by_author

def main(save_dir="_posts/papers", site_data_dir="_data/"):
    site_data_dir = Path(site_data_dir)

    yaml = YAML()
    yaml.preserve_quotes = True
    with open(site_data_dir / "authors.yml") as f:
        authors = yaml.load(f)
    
    for author in authors.values():
        auto_update = author.get('auto_update_publications', False)
        author_id = author.get('semantic_scholar_id', False)

        if auto_update and author_id:
            year = int(datetime.datetime.now().year)
            parsed = {
                'start': year,
                'end': year,
                'author_id': author_id,
            }

            add_publications_by_author.main(parsed=parsed, save_dir=save_dir)


if __name__ == "__main__":
    main()