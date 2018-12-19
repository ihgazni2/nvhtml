from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj
from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils
import lxml.sax


html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
eles = lvsrch.a(root,7,8,show=False)
print(eles[0])
print(eles[5])
eles = lvsrch.a(root,7,8,which=0)
eles = lvsrch.a(root,7,8,which=0,source=False)

