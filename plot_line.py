#!/usr/bin/env python
#coding=utf-8

import jinja2

svg_template = """
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{{ width }}" height="{{ height }}">
  <path d="{{ line }}" fill="none" stroke="green" stroke-width="3" />
</svg> 
"""

class Line2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        coords = zip(self.x, self.y)
        return " ".join(["M{} {}".format(*coords[0])]+["L{} {}".format(x, y)
                  for x, y in coords])


t = jinja2.Template(svg_template)
import numpy as np
l = Line2D(np.arange(10)*10, np.random.rand(10)*100)
svg = t.render(width=100, height = 100, line=l)

with file('test_svg.svg', 'w') as fid:
    fid.write(svg)
