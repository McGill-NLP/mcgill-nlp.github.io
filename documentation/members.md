## Add new member profile

> [!NOTE]
> *Have you tried using issue forms? They should be faster and easier for most of the (simpler) scenarios. This section is only if you need to make custom changes not covered by the forms.*

Navigate to [_data/authors.yml](./_data/authors.yml) and add the desired information at the end of the file. It has to follow the following template:

```yaml
John Doe:  # Your full name; this will be used for post `author`
  name: "John Doe"
  role: "PhD"   # One of: "Faculty", "Adjunct Faculty", "Postdoc", "PhD", "Master", "Undergraduate", "Intern"
  avatar: "/assets/images/bio/placeholder/default.jpg"  # Path to image of you (place in assets/images/bio)
  advisor: "John Doe Sr." # The advisor or advisors of the new member
  date: "Sep 2030"  # Start date. Must be in the "MMM YYYY" format, or "Fall"/"Winter".
  bio: "Just some cool student" # Describe the new member (optional)
  note: "Co-advised by Amasa L." # Additional notes (optional)
  alumni: false # Whether the new member is an alumni
  new_role: "Professing at Leland Junior S. University" # If an alumni, their new role
  auto_update_publications: false. # Whether to automatically look for new papers published by this author every 2 weeks
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