# STAMINA talks

Each file in this folder is one talk on the [STAMINA page](../stamina/index.html).
The page is built from these files by Jekyll (`_includes/stamina-talk.html` renders one talk).

**Add a talk:** copy `_template.md` to `YYYY-MM-DD-lastname.md`, fill in the fields, and commit.

**After the talk:** add the YouTube link under `links: recording:`.

A talk is listed under *Upcoming* until the day after its date, then under *Past*,
grouped by term (Jan–Jun = Spring, Jul–Dec = Fall; override with `term:`).
The site rebuilds on every push to `main` and every Wednesday, so talks move to *Past* on their own.

**Preview locally** (from the repo root, before pushing):

```bash
bundle exec jekyll build            # ~35 s; writes the site to _site/
python3 -m http.server 4000 -d _site
# open http://localhost:4000/stamina/ ; re-run the build after each edit, then refresh
```

(`jekyll serve` / `build --watch` crash on WSL with Ruby 3.0 + Jekyll 3.9 —
"no implicit conversion of Hash into Integer" in pathutil — so use the two commands above.)
