# Creating Pages under _posts

## Teaching
To write a course description, create a new file called `<YYYY>-<MM>-<DD>-<shorthand>.md` in the [`_posts/teaching` directory](_posts/teaching). Note that `<shorthand>` will determine the URL of the file, so choose carefully.

```yaml
---
title: "COMP XYZ - Semester YYYY"  # Add course code, followed by the semester it's taught
author: Reihaneh Rabbany  # Name of the instructor
categories:
  - Teaching  # Used to list all posts describing a course in /teaching/
tags:
  - Winter 2022  # Semester
  - Course Name  # Course Name
---
```

Then, add content relevant to the course using markdown below the `---`, e.g.:

```markdown
* **Course codes:** COMP XXX (Semester Code)
* **Instructors:**  XXX
* **Location:** XXX
* **Time:** XXX
* **Course Website:** [here](url)

# Overview
Course Overview

```

### Deleting a post

You may want to delete posts forever. Then, delete the file in `_posts/`. If you simply want to hide it, you can prepend the file name with `hide`. For example, to hide the file `2016-03-09-COMP-XYZ.md`, you can rename it to `hide-2016-03-09-COMP-XYZ.md`.

## Create a profile page

> [!NOTE]
> *If you are having a hard time in this section, try to copy from someone else's profile and modify it.*

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
