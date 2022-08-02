# McGill NLP Website

This is the source code of the [group website](https://mcgill-nlp.github.io/), which was built using [Jekyll](https://github.com/jekyll/jekyll) and [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes).

## Quickstart

For certain contributions, it is possible to fill GitHub forms and everything will be automated without requiring to fork or modify the codebase. This currently works for:
* Adding or updating the profile of a lab member
* Adding a paper written by a lab member
  * With manual information entry
  * With a URL (for limited number of websites)
* Adding all papers by a certain author within a time frame

To get started, [click here to open the issue forms](https://github.com/McGill-NLP/mcgill-nlp.github.io/issues/new/choose).

Note: if you made a mistake but already submitted the form, please see how to correct it in [FAQ](#FAQ).

> If you are looking to build a project website/webpage for your paper, check out the [project page template](https://github.com/McGill-NLP/project-page-template), which has the same style as this website.

## Steps to contribute

For any type of contribution, please follow these steps:
1. [Fork](https://github.com/McGill-NLP/mcgill-nlp.github.io/fork) the repository.
2. Add your contribution by editing the desired files.
3. Create a pull request: Click on the [Pull Request](https://github.com/McGill-NLP/mcgill-nlp.github.io/pulls) tab and select "New pull request". Select the repository you forked and modified.
4. Wait for a team member to review and merge your pull request.

## Add new member profile

Navigate to [_data/authors.yml](./_data/authors.yml) and add the desired information at the end of the file. It has to follow the following template:

```yaml
John Doe:  # Your full name; this will be used for post `author`
  name: "John Doe"
  role: "PhD"   # One of: "Faculty", "Postdoc", "PhD", "Master", "Undergraduate", "Intern"
  avatar: "/assets/images/bio/placeholder/default.jpg"  # Path to image of you (place in assets/images/bio)
  advisor: "John Doe Sr." # The advisor or advisors of the new member
  date: "Sep 2030"  # Start date. Must be in the "MMM YYYY" format, or "Fall"/"Winter".
  bio: "Just some cool student" # Describe the new member (optional)
  note: "Co-advised by Amasa L." # Additional notes (optional)
  alumni: false # Whether the new member is an alumni
  new_role: "Professing at Leland Junior S. University" # If an alumni, their new role
  links:
    - label: "Website"
      url: "https://john-doe.github.io/" # Link to website
    - label: "GitHub"
      url: "https://github.com/john-doe" # Link to Github profile
    - label: "Twitter"
      url: "https://twitter.com/john-doe" # Link to Twitter profile
    - label: "Scholar"
      icon: "fas fa-fw fa-graduation-cap" # Font Awesome icon
      url: "https://scholar.google.com/citations?user=<user_id>" # Link to Google Scholar profile
```

This will look like this:

![Demo of user profile](.github/images/demo-profile.jpg)

`John Doe`: Replace `John Doe` with your full name. This will be what you will use when writing a blog post or a publication abstract, and is required for certain automatic forms. Note that if someone already has the same name, you can append your start date, but that might break some automations.

`avatar`: Note that the `avatar` field links to an image located in `assets/images/bio`. You will need to upload the image to the repository before it shows up. Make sure you choose a picture in `jpg` (to save space), an aspect ratio of 1:1, resolution of about 300x300, and mainly centered around the face. In a hurry, you may use the default image.

`icon`: An icon that can be found in the [Font Awesome v5 free library](https://fontawesome.com/v5/search?m=free). V6 (most recent) will not work. In the HTML snippet, copy the string after `class=`. For example, if your string is `<i class="fab fa-accessible-icon"></i>`, then only copy `"fas fa-graduation-cap"` for the Google Scholar icon. This is optional only when `label` is "Website", "GitHub", "LinkedIn", or "Twitter". Otherwise, that link will not appear under your name in `/people/`.

### Modifying a member's profile

Has a member graduated? Does a member wish to have a new profile picture or bio? You can modify the profile of a member by editing the `_data/authors.yml` file.

### Deleting a member

If you wish to delete a member (e.g. added by mistake, duplicates, etc.) you can directly delete their "block" (everything indented after their name) in the `_data/authors.yml` file.


## Front matters and YAML

For any type of page or post (publication, blog post, course description), we use something called ["Front Matters"](https://jekyllrb.com/docs/front-matter/) to tell Jekyll about the purpose of the file. This is a block of YAML text at the beginning of the file. The rest of the file is regular [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

## Modify pages

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

## Creating a post

You may want to add new content: blog post, a new publication (abstract/more information), or a course description. These are all grouped under *posts* (in fact, anything that isn't a page is a post). This section will cover how to work with them.

### Publication

To add a *publication*, create a new file called `<YYYY>-<MM>-<DD>-<shorthand>.md` in the [`_posts/papers` directory](_posts/papers). Note that `<shorthand>` will determine the URL of the file, so choose carefully.

Every file should start with the following:
```yaml
---
title: "My cool paper" # Add official title
author: <full name> # Add name to show profile in sidebar
categories: Publications # Used to list all posts about publications in /publications/
names: "Firstname lastname, Firstname lastname, ..." # names of all authors
link: https://arxiv.org/abs/1234.5678 # link to paper
code: https://github.com/McGill-NLP/example  # link to code (optional)
webpage: https://mcgill-nlp.github.io/project  # link to project (optional)
video: https://youtube.com  # link to video (optional)
twitter: https://twitter.com/username  # link to twitter thread (optional)
demo: https://project-demo.com  # link to interactive demo (optional)
thumbnail: /assets/images/papers/figure.jpg  # link to a thumbnail (optional)
venue: ACL 2022  # venue and year of the paper
tags: ACL # tag of the paper (exclude year, use shorthand)
---
```

Then, it should be followed with the content in markdown:

```markdown

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

In our cool paper, we propose a new state-of-the-art method to detect if an image is a hotdot or...
```

It will look like this in `/publications/`:

![Showing new post in the publication page](.github/images/demo-publication.jpg)


Notes:
* `author`: This links to one of the authors in `_data/authors.yml`. If the author is missing, this will not work.
* `{{ page.names }}` is a Jekyll snippet that will display the names of all authors (which was defined right above). This will save you from repeating yourself.
* `{{ page.venue }}` is a Jekyll snippet, just like `{{ page.names }}`.
* `include display-publication-links.html` will display the icons and links to code, webpage, tweets, etc. `pub=page` refers to the page object, which is handled by Jekyll.
* `thumbnail` links to a image located in `assets/images/papers`. If you don't have one, remove that line. You will need to upload the image to the repository before it shows up. Make sure you choose a picture:
  * in `jpg` (to save space), 
  * an aspect ratio of 4:3 (landscape), 
  * resolution of about 800x600, 
  * taken from your paper.

### Blog

To write a blog post, create a new file called `<YYYY>-<MM>-<DD>-<shorthand>.md` in the [`_posts/blog` directory](_posts/blog). Note that `<shorthand>` will determine the URL of the file, so choose carefully.

Every file should start with the following:
```yaml
---
title: "My cool blog post" # Add title
author: <username> # Add your name (see above)
categories: # Used to list all blog posts in /blog/
  - Blog
tags: # Choose tag(s) not clashing with a conference name (optional)
  - Pytorch
excerpt_separator: "<!--more-->"  # Separate the excerpt from the body (optional)
last_modified_at: "2016-03-09" # Add modification date if relevant (optional)
---
```

Followed by the content in markdown:

```markdown
*Your summary here will be previewed on `/publications/`*

<!--more-->

Some starting statement

## Section in the paper

More content.
```

### Teaching
To write a course description, create a new file called `<YYYY>-<MM>-<DD>-<shorthand>.md` in the [`_posts/teaching` directory](_posts/teaching). Note that `<shorthand>` will determine the URL of the file, so choose carefully.

```yaml
---
title: "COMP XYZ - Semester YYYY"  # Add course code, followed by the semester it's taught
author: Siva Reddy  # Name of the instructor
categories:
  - Teaching  # Used to list all posts describing a course in /teaching/
tags:
  - Winter 2022  # Semester
link: "https://docs.google.com/document/d/..." # Link to an external course description
---
```

Then, add content relevant to the course using markdown below the `---`, e.g.:

```markdown
*summary here*

## Syllabus

Content of syllabus here

```


### Deleting a post

You may want to delete posts forever. Then, delete the file in `_posts/`. If you simply want to hide it, you can prepend the file name with `hide`. For example, to hide the file `2016-03-09-COMP-XYZ.md`, you can rename it to `hide-2016-03-09-COMP-XYZ.md`.


## Create a profile page

To have your own profile, you can create a new file called `<username>.md` in the [`_pages_/profiles` directory](_pages_/profiles). Note that `<username>` will determine the URL of the file, so choose carefully. You will need to add the following at the top:
```yaml
---
title: John Doe  # Add your name
permalink: /people/john/  # Add your username
layout: archive
classes:
    - wide
    - no-sidebar
---
```
Then, you can add any content you like using markdown:

```markdown
Welcome to John Doe's personal profile!

## Publications

<div>
  {% include posts-publication.html taxonomy="Publications" author="John Doe" %}
</div>

## Teaching

<div>
  {% include posts-category.html taxonomy="Teaching" author="John Doe" %}
</div>

## Blog posts

<div>
  {% include posts-category.html taxonomy="Blog" author="John Doe" %}
</div>

## Contact

Here's how to contact John Doe: ...
```

Note that by using `{% include posts-publication.html taxonomy="Publications" author="John Doe" %}`, you can display all posts about publications by filtering for "John Doe" in the `names` field of each publication. If you choose `{% include posts-category.html taxonomy="Teaching" author="John Doe" %}`, you can display all posts about teaching instead, and `taxonomy="Blog"` will display all posts about blog posts. Note that `posts-publication.html` and `posts-category.html` are special html files in `_includes/` that generate a list of post following a specific format. That's a Jekyll feature and is considered as an advanced feature, so you don't have to worry and can just directly use it like above.

Then, you can update `_data/authors.yml` to include a link to your profile page, e.g.:
```yaml
John Doe:
  name: "John Doe"
  # ...
  links:
    - label: "Page"
      url: "/people/siva"
      icon: "fas fa-fw fa-user"
    - label: "Github"
      url: "..."
    #...
```

## Advanced

This section is meant for the maintainer(s) or developers of the site. Please consult the faculty members for more information on how to become a maintainer.

### Setup

You will need to install ruby and gem to use `jekyll` locally. This is only if you want to compile and run this site locally. If you want to modify a markdown file or a yaml file, you don't need to do that; please refer to the sections above for instructions.

For the instructions, see [Jekyll quickstart](https://jekyllrb.com/docs/).

To run the site locally, use the last command in the quickstart:
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

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.

### Running tests

There are some tests for the python scripts. You can run them by running the following command in the root folder:
```bash
python -m unittest
```

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
