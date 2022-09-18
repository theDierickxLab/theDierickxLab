---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# <i class="fas fa-users"></i>Team

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{% include section.html %}

{%
  include list.html
  data="members"
  component="portrait"
  filters="role: pi"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: phd"
%}
{%
  include list.html
  data="members"
  component="portrait"
  filters="role: programmer"
%}
{:.center}

{% include section.html background="images/banner.jpg" dark=true%}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

## Join

#### Post Dogtoral Researcher


{% include link.html type="external" link="pieterjan.dierickx@mpi-bn.mpg.de" text="Apply Now" icon="" style="button" %} {:.center}


{% include section.html %}

## Funding

Our work is made possible by funding from several organizations.
{:.center}

{%
  include gallery.html
  style="square"

  image1="images/CPI.png"
  link1="https://www.cpi-online.de/"
  tooltip1="The Cardio-Pulmonary Institute"

  image2="images/HERZ.png"
  link2="https://www.mpi-hlr.de/en"
  tooltip2="Max Planck Institute for Heart and Lung Research"

  image3="images/DZHK.png"
  link3="https://dzhk.de/en/"
  tooltip3="German Centre for Cardiovascular Research"

  image4="images/IMPRS.png"
  link4="https://nasa.gov/"
  tooltip4="https://imprs-mob.mpg.de/"

  image5="images/MPI.jpeg"
  link5="https://www.mpg.de/institutes?tab=institutes"
  tooltip5="Max Planck Institutes"
