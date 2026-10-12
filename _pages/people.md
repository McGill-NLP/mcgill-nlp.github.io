---
permalink: /people/
title: "People"
layout: splash_v2
header:
    overlay_image: /assets/images/logo/logo.png
    overlay_css: "background-size&#58; contain; background-repeat&#58; no-repeat;"
---

## Faculty, Staff & Postdoc

{% include card-authors-with-role.html authors=site.data.authors role="Faculty" render_current_role=true %}
{% include card-authors-with-role.html authors=site.data.authors role="Staff" render_current_role=true %}
{% include card-authors-with-role.html authors=site.data.authors role="Postdoc" render_current_role=true %}

## Students

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="PhD" heading="PhD" heading_id="phd" render_current_role=true %}

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="Master" heading="Masters" heading_id="masters" render_current_role=true %}

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="Undergraduate" heading="Undergraduate" heading_id="undergraduate" render_current_role=true %}

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="Intern" heading="Intern" heading_id="intern" render_current_role=true %}

---

# Past Members

## Faculty, Staff & Postdocs

{% include card-authors-with-role.html authors=site.data.authors roles="Faculty,Staff,Postdoc" render_current_role=false %}

## Alumni

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="PhD" heading="PhD" heading_id="phd-past" render_current_role=false %}

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="Master" heading="Masters" heading_id="masters-past" render_current_role=false %}

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="Undergraduate" heading="Undergraduate" heading_id="undergraduate-past" render_current_role=false %}

{% include card-authors-with-role.html authors=site.data.authors role="Student" title="Intern" heading="Interns" heading_id="interns-past" render_current_role=false %}

<br/>

<!-- # Updating the website

If you are part of the Complex Data Lab, please head to the [GitHub repository](https://github.com/ComplexData-MILA/ComplexDataLab-Mila-McGill), for instructions on adding/updating your publications, creating/updating your profile, updating other parts of the website and etc. -->