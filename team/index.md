---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team


{% include section.html %}


{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{%
  include link.html
  link="research"
  text="See what we've published"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{%
  include link.html
  link="tools"
  text="Browse our tools"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="resources"
  title="Our Resources"
  flip=true
  text=text
%}

{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include link.html
  link="team"
  text="Meet our team"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Our Team"
  text=text
%}




  


 {% include section.html %} 
  
## Our lab is supported by
{:.center}

{%
  include gallery.html
  style="flexbox"

  image1="images/CPI.png"
  link1="https://www.cpi-online.de/"
  tooltip1="The Cardio-Pulmonary Institute"

  image2="images/HERZ.png"
  link2="https://www.mpi-hlr.de/en"
  tooltip2="Max Planck Institute for Heart and Lung Research"

  image3="images/dzhk.png"
  link3="https://dzhk.de/en/"
  tooltip3="German Centre for Cardiovascular Research"

  image4="images/IMPRS.png"
  link4="https://imprs-mob.mpg.de/"
  tooltip4="IMPRS for Molecular Organ Biology"

  
  %}
