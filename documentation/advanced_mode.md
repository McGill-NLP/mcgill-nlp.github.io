# Advanced Information

We are using minimal-mistakes & Jekyll. 

For any type of page or post (publication, blog post, course description), we use something called ["Front Matters"](https://jekyllrb.com/docs/front-matter/) to tell Jekyll about the purpose of the file. This is a block of YAML text at the beginning of the file. The rest of the file is regular [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

Guide: https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/
Layout / YAML Front-matter: https://mmistakes.github.io/minimal-mistakes/docs/layouts/

## Creating Modules

For our custom Front Matter / modules, you can find the **html** page under `_includes`. 

For the CSS, we write it in **SASS**, and put it under `_sass/custom`.  We then add a `@include custom/{module-name}.scss`.

We try not to have many custom **javascript**, but if there is, it is under `_includes/head/custom.html`


## Important Dependecies

It is layed out such that we do not repeat yourself (DRY). Hence, we make use of the file layout & file name.

### Research Directions (on the Home Page)

On the home page (`_pages/home.md`), we have the following line:
> {% include research-directions.html category="research-directions"%}

Here, it automatically collects any `.md` files under `_research_directions`. Please note, these files should follow a similar layout outlined [here](./research_direction_layout.md)


### Topics (on the research direction page)

Within the research_direction, you may find the following:
> {% include sub_research-directions.html category="temporal-graph-learning" %}

Here, it automatically finds any `.md` files under `_research_directions/{RESEARCH DIRECTION}`. Please note, these files should follow a similar layout outlined [here](./topic_layout.md)

E.g. If the `RESEARCH DIRECTION` is `temporal-graph-learning`, then you should make a directory under `_research_directions` called `temporal-graph-learning`. When using calling `sub_research-directions.html`, also pass in `temporal-graph-learning`. 

### Selected Publications (on research direction / topic pages)

This is used within `RESEARCH DIRECTION` page or `TOPIC` page. 

> {% include posts-highlighted-publications.html taxonomy="TGA" %}

Here, we automatically collect papers (md files under `_posts`). Within these md files, we search for those with categories that match the given taxonomy. 

E.g. For the topic _Temporal Graph Applications_, we use the key `TGA`. Hence, we add `TGA` as one of the categories for a paper we want to shown on the _Temporal Graph Applications_ page.







## Modify pages

> [!WARNING]
> *This section is for advanced users. You will likely not need it unless you are intend to maintain this website or fix specific issues with page rendering*

To modify a page, navigate to [_pages](_pages/) and update the desired file. If you add a new file, you will also need to edit the [_data/navigation.yml](_data/navigation.yml) file with the correct relative URL.

The following pages are mostly likely to be frequently updated:

* [home](_pages/home.md)
* [contact](_pages/contact.md)

The following pages are not likely to be frequently updated:

* [people](_pages/people.md)
* [publications](_pages/publications.md)
* [blog](_pages/blog.md)
* [teaching](_pages/teaching.md)

Note: If you want to add new content to one of the pages above, please refer to the section on [creating a post](#creating-a-post).

The following files are only meant to be modified by the site maintainer in rare cases:

* [404](_pages/404.md)
* [category-archive](_pages/category-archive.md)
* [tag-archive](_pages/tag-archive.md)
* [year-archive](_pages/year-archive.md)

### Removing a page

To remove a page, delete the desired file in `_pages/` and delete the corresponding entry in [_data/navigation.yml](_data/navigation.yml).


## Maintaining / Local Development

> [!WARNING]
> *This section is meant for the maintainer(s) or developers of the site. Please consult the faculty members for more information on how to become a maintainer.*

### Setup

#### Codespace

Most of the dependencies (`jekyll`, `ruby`, `gem`, Python `requirements.txt`, etc.) are already installed thanks to automations in `.devcontainer/devcontainer.json`. You can simply open the repo in a codespace and start working.

#### Local

You will need to install the python dependencies by running (from inside project directory):

```
pip3 install --user -r src/python/requirements.txt
```

You will need to install ruby and gem to use `jekyll` locally. This is only if you want to compile and run this site locally. If you want to modify a markdown file or a yaml file, you don't need to do that; please refer to the sections above for instructions. For the instructions, see [Jekyll installation](https://jekyllrb.com/docs/installation/) (e.g. [on Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/)).

### Running the site in development mode

To run the site locally (or remotely on Codespaces), use the last command in the quickstart:

```bash
bundle exec jekyll serve
```

We use the `minimal-mistakes` theme. Specifically, we use the `remote-theme` installation method, which is why the repo doesn't contain all of the html, css, and yaml files required for the theme. To learn more, read [this minimal-mistakes doc section](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/#remote-theme-method). Note we are using a specific version of the theme, which can be found on `_config.yml`.

### Editing SCSS

If you need to modify some CSS attributes directly, you need to use [sass](https://sass-lang.com/documentation/syntax), or directly write CSS (which is still valid). You can create a new file in [_sass/custom](_sass/custom) and import it inside [_sass/main.scss](_sass/main.scss). Note that all files in [_sass/custom](_sass/custom) were added by the maintainers of this repo, in addition to the original styling provided by minimal-mistakes.

Here's a brief description:

* [_sass/custom/display-publications.scss](_sass/custom/display-publications.scss): Some custom CSS for styling the publications on `/publications/`, which did not have the same format in the original minimal-mistakes theme.
* [_sass/custom/no-sidebar.scss](_sass/custom/no-sidebar.scss): This adds an option to shift the page to the left side when there's no sidebar. Search for `no-sidebar` in [_config.yml](_config.yml) to see how to use it, or read [this post](https://mmistakes.github.io/minimal-mistakes/docs/layouts/#layout-based-and-user-defined-classes).
* [_sass/custom/people-card.scss](_sass/custom/people-card.scss): This is a custom CSS for styling the "cards" for each member in `/people/`.
* [_sass/custom/skin.scss](_sass/custom/skin.scss): This is a custom CSS for styling the skin of the website.

### Custom `_includes/`

`_includes/` contains HTML and MD files that can be called from any page. It's something specific to Jekyll. To use it in your page, simply create an HTML file at  `_includes/my-file.html` and add the following to the front matter of your page:

```
{% include "my-file.html" %}
```

We have 5 custom `include` HTML files for this website. You may take a look at their usage by searching `include <name>.html` across the codebase.

### Custom `_layouts/`

You can create custom html layouts in `_layouts/`. For example, you can create a file called `my-layout.html`. It should contain a front matter block, followed by the HTML content:

```html
---
layout: archive
---

{{ content }}

<div>
  {% include ... %}
</div>
```

To use them, simply specify, in the front matters of a page in `_page/`:

```yaml
---
layout: publication
---
```

Example: In our case, we have a custom `publications.html` layout for the `/publications/` page.

### Github Actions

We use Github Actions to automate processes. You can find the files in [`.github/workflows/`](.github/workflows/), and see their status in the "Actions" tab. This requires you to use YAML.

### Python scripts

Some Python scripts are ran inside the actions. You can find them in [`src/python/`](src/python). If you want to run them locally, you can use the following command:

```bash
pip install -r src/python/requirements.txt
python src/python/<script>.py
```

Replace `<script>` with the name of the script. If you want to add some library, you can add it to the requirements.txt file. Make sure to include the full version: `<library>==<version>`, or else it might break automation. For example, if you want to use the `requests` library, you can add it to the requirements.txt file as `requests==2.18.4`.

### Issue forms

To modify an issue form, simply edit the corresponding form in [`.github/ISSUE_TEMPLATE`](.github/ISSUE_TEMPLATE). Note that if you make some major change, you might need to modify the python scripts. Thus, it is recommended to test that on a fork in order to avoid breaking the automation on the main repo.

### Troubleshooting

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

* [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
* [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
* [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.

### Running tests

There are some tests for the python scripts. You can run them by running the following command in the root folder:

```bash
python -m unittest
```