# Complex Data Lab Website

### [➡️ Click Here to Add Your Profile or Paper ⬅️](https://github.com/ComplexData-MILA/ComplexDataLab-Mila-McGill/issues/new/choose)

<br>

This is the source code of [Complex Data Lab Website](https://complexdatalab.com/), which was forked from [McGill-NLP](https://github.com/McGill-NLP/mcgill-nlp.github.io). Internally, it is built using [Jekyll](https://github.com/jekyll/jekyll) and [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes).

## Quickstart

> [!IMPORTANT]
> You should probably read this section!

For certain contributions, it is possible to fill GitHub forms and everything will be automated without requiring to fork or modify the codebase. This currently works for:

* Adding or updating the profile of a lab member
* Adding a paper written by a lab member
  * With manual information entry
  * With a URL (for limited number of websites)
* Adding all papers by a certain author within a time frame

To get started, [click here to open the issue forms](https://github.com/ComplexData-MILA/ComplexDataLab-Mila-McGill/issues/new/choose).

> [!NOTE]
>
> * *If you made a mistake but already submitted the form, please see how to correct it in [FAQ](#faq).*
> * *If you are looking to build a project website/webpage for your paper, check out the [project page template](https://github.com/McGill-NLP/project-page-template), which has the same style as this website.*

## Steps to contribute

For other types of contribution (not covered by the issue form), please follow these steps:

1. [Fork](https://github.com/ComplexData-MILA/ComplexDataLab-Mila-McGill/fork) the repository.
2. Add your contribution by editing the desired files.
3. Create a pull request: Click on the [Pull Request](https://github.com/ComplexData-MILA/ComplexDataLab-Mila-McGill/pulls) tab and select "New pull request". Select the repository you forked and modified.
4. Wait for a team member to review and merge your pull request.

## Quick Guides

| Name | Page | 
| :-- | :-- | 
| Adding members / contributors | [here](./documentation/members.md) |
| Utility (e.g. image-resizing) | [here](./documentation/utility.md) | 
| Creating pages under _post (paper publications, blogs, teaching) | [here](./documentation/creating-posts.md) |
| Modifying pages / dependicies / Local setup | [here](./documentation/advanced_mode.md) | 


## FAQ

> I created a post but it doesn't show up. What's wrong?

Make sure it is in the right directory, and that the file name is correct. The file name should be `<YYYY>-<MM>-<DD>-<shorthand>.md`; this is not a convention or a preference, it is actually **needed** to render that file.

> I made a mistake when filling the form. How can I fix it?

After you fill the form, an issue is created with an appropriate *tag*. Then, a pull request (which is a "proposal" to make a change) is automatically created from that *tag*, based on the content of the issue. But if you made a mistake, then that PR is incorrect. So you should try to close it, or request the PR to be closed in a reply. Then, all you need to do is to modify the issue's content (makes sure the formatting stays the same, that's very important!). Once it's updated, you can remove the *tag*, refresh the page, then add back the same *tag*. This will create a new pull request, and a maintainer will review it.

> When using `src/python/add_publications_by_author.py`, it keeps adding a paper I already added (or I want to ignore). How can I make it stop doing that?

Add the semantic scholar paper ID to the list in `records/semantic_paper_ids_ignored.json`.

> When filling out the form, how do I upload my profile picture or a thumbnail without having to use an external source, like imgur?

1. Open a [new blank issue](https://github.com/McGill-NLP/mcgill-nlp.github.io/issues/new).
2. Click on "Attach files by dragging & dropping, selecting, or pasting them".
3. Upload your picture.
4. Copy only the URL link (i.e. `https://user-images.githubusercontent.com/...png` only). Ignore the rest (i.e. `![text]()`).
5. Keep the link, but cancel the new issue. Paste that link in the form.

> The tests in `test_add_publications_by_author.py` are failing. What should I do?

Sometimes, semantic scholar will update the content of the paper. In that case, the failed tests have saved the new versions of those papers in `tests/scratch/_posts/papers`, and you will need to replace the old versions in `tests/data/add_publication_by_author/<author_name>` with the new versions in `tests/scratch/_posts/papers`. You can do that by running the following command:

```bash
python -m src.python.cli.replace_files_in_test_dir --source_dir tests/scratch/_posts/papers --target_dir tests/data/add_publications_by_author/siva
python -m src.python.cli.replace_files_in_test_dir --source_dir tests/scratch/_posts/papers --target_dir tests/data/add_publications_by_author/jackie
python -m src.python.cli.replace_files_in_test_dir --source_dir tests/scratch/_posts/papers --target_dir tests/data/add_publications_by_author/tim
```

> Does Semantic Scholar require an API key? I am getting an HTTP 429 error.

Although it is possible to make requests to Semantic Scholar without an API key, it is recommend to use one if available. Please set the environment variable `SEMANTIC_SCHOLAR_API_KEY` to your API key and it will be automatically used. For mcgill-nlp.github.io, we have set it up as a [*GitHub Repository Secret*](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository); please look at `.github/workflows/auto-update-publications.yml` to see how the environment variable is assigned. You can update Github Repository secrets for Actions at [this settings page](https://github.com/McGill-NLP/mcgill-nlp.github.io/settings/secrets/actions/).
