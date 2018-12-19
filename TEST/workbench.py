
from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj

from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine

html_str = fs.rfile("./test.html")
root = LXHTML(html_str)

handler = BEAUTIFY()
lxml.sax.saxify(root, handler)


txt.todirs(html_str)


