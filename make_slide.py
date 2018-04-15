""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""

INDEX_TEMPLATE = r"""
<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script src="http://malsup.github.com/jquery.cycle2.js"></script>
<script src="http://malsup.github.io/jquery.cycle2.center.js"></script>

 <style>
.cycle-slideshow { width: 50%;  margin: auto; border: 1px solid #bbb; background: #ffc }
.cycle-slideshow img { width: 100%; height: auto }




  </style>




</head>
<body>
<h2>${header}</h2>
<p></p>
<div class="cycle-slideshow"   
    data-cycle-fx=scrollHorz
    data-cycle-center-horz=true
    data-cycle-center-vert=true>
% for name in names:
    <img  src="${directory}/${name}">
% endfor
</div> 
</body>
</html>
"""

EXCLUDED = ['index.html']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()
    fnames = [fname for fname in sorted(os.listdir(args.directory))
              if fname not in EXCLUDED]
    header = (args.header if args.header else os.path.basename(args.directory))
    print(Template(INDEX_TEMPLATE).render(names=fnames, header=header, directory=args.directory))


if __name__ == '__main__':
    main()