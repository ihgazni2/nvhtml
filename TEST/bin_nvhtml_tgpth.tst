
cd /opt/PY3/NVHTML-BENCH




from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj
from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils
import lxml.sax
import argparse
from efdir import fs
import elist.elist as elel
import estring.estring as eses
import spaint.spaint as spaint


html_str = fs.rfile("opis.html")
root = LXHTML(html_str)
m = engine.WFS(root).mat


