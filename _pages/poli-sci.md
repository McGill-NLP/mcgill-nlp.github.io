---
title: Politics & Online Media
layout: single
permalink: /poli-sci/
classes:
    - wide
    - no-sidebar
---

<div class="research-directions__wrapper">
   {% assign poli_sci_projects = site.projects | where_exp: "item", "item.path contains 'poli-sci/'" %}
  {% for project in poli_sci_projects %}
    <div class="research-directions__item">
      <a class="archive__item" href="{{ project.url | relative_url }}">
        {% if project.header.teaser %}
          <div class="archive__item-teaser">
            <img src="{{ project.header.teaser | relative_url }}" alt="{% if project.header.alt %}{{ project.header.alt }}{% endif %}">
          </div>
        {% endif %}

        <div class="archive__item-body">
          <h2 class="archive__item-title">{{ project.title }}</h2>
          {% if project.excerpt %}
            <div class="archive__item-excerpt">
              {{ project.excerpt }}
            </div>
          {% endif %}
        </div>
      </a>
    </div>
  {% endfor %}
</div>