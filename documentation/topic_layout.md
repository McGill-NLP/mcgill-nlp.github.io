# Topic Layout

## Requirements

Create a markdown file under `_research_directions\{{RESEARCH DIRECTION}}`. The file name of this markdown file should be the **Topic Key**.

**Topic Key**: 
The key to this research direction. This should be one word and lowercase. Please use `-` to concatenate. Note, the markdown file for the page needs to be this name. This will correspond to the url, tie with tagging team members (e.g. information-integrity) and potentially papers to show on the page.


## Components within the --- 

**title**: The title for this page (e.g Information Integrity)
**layout**: Keep it as `splash`
**category**: Keep it as `{{RESEARCH DIRECTION}}`
**order**: Integer. The order within the home page.
**header**:
    - **overlay_filter**: The overlay on top of the image. For example, a purple gradient can be described as: `linear-gradient(rgba(157, 110, 219, 0.3), rgba(157, 110, 219, 1))`
    - **overlay_image**: The underlying image, used both on the research direction main page & the research direction gallery view on the home page
**one-liner**: The one-liner / question shown on the home page.
**excerpt**:  Text for the header banner for the main research page – mainly used to describe what we do / or the team in two lines. (e.g. Our team creates tools and datasets to foster a safe, open space for online public discourse. We hope to empower researchers and the public to understand and navigate today’s digital landscape.)


## Layout
We then create one of the following layout:

``` 
{{ INTRO }}

{{ Selected Publications }} 

{{ Funding }}
```