#!/usr/bin/env python
#coding=utf-8

import jinja2

svg_template = """
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{{ width }}" height="{{ height }}">
  {% for circle in circles %}
  <circle cx="{{ circle.x }}" cy="{{ circle.y }}" r="{{ circle.r }}" stroke="black" stroke-width="2" fill="{{ circle.color }}" />
  {% endfor %}
</svg> 
"""

t = jinja2.Template(svg_template)
from collections import namedtuple
Circle = namedtuple("Circle", "x y r color")
circles = [Circle(x*10+5, y*10+5, 5, "red") 
           for x in range(10) for y in range(10)]

svg = t.render(width=150, height=150, circles=circles)

with file('test_svg.svg', 'w') as fid:
    fid.write(svg)
