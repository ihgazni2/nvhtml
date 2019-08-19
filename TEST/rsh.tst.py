from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj
from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils
from nvhtml import rshtml
import lxml.sax
import argparse
from efdir import fs
import elist.elist as elel
import estring.estring as eses
import edict.edict as eded
import spaint.spaint as spaint
from xml.sax.handler import ContentHandler

import copy
import re



html_str = fs.rfile("opis.html")
root = LXHTML(html_str)
wfspls = engine.wfspls(root,drop_comment=True)
edfspls_sax = engine.edfspls_sax(root)

wfs = engine.wfs_traverse(root,drop_comment=True)
m = wfs.mat
m = engine.init_attr(m,"children",[])
m =  engine.fill_children_attr(m)


sdfsl = engine.sdfsl_from_mat(m)
edfsl = engine.edfsl_from_mat(m)

sdfspls = engine.sdfspls_etree(root)
edfspls = engine.edfspls_etree(root)

eplmat = engine.edfspls2plmat(edfspls)
wfspls2 = engine.edfspls2wfspls(edfspls)

splmat = engine.sdfspls2plmat(sdfspls)
wfspls3 = engine.sdfspls2wfspls(sdfspls)


sdfspls2 = engine.edfspls2sdfspls(edfspls)
edfspls2 = engine.sdfspls2edfspls(sdfspls)


######################################################





#######################################################


#step 0 
rsh = '''
html
    head
        meta
            -http-equiv X-UA-Compatible
            -content IE=edge,chrome=1
        meta
            -name viewport
            -content
                user-scalable=yes, 
                initial-scale=1.0, 
                minimum-scale=1.0, 
                maximum-scale=3.0
        meta
            -http-equiv Content-Type
            -content text/html; charset=UTF-8
        link
        link
    body
        div
            -id menu-item-27961
            -class
                qtranxs-lang-menu-item 
                menu-item-object-custom 
            .text
                |hello
                |hi
                |hao
                |hihihi
            .tail
                |this is a tail
            li
            li
        div
            li
        div
    #comment
        .text
            |this is a comment
'''






#####html_txt to 

html_txt = '''
<html>
    <head>
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        </meta>
        <meta name="viewport" content="user-scalable=yes, initial-scale=1.0, minimum-scale=1.0, maximum-scale=3.0">
        </meta>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </meta>
        <link>
        </link>
        <link>
        </link>
    </head>
    <body>
        <div id="menu-item-27961" class="qtranxs-lang-menu-item menu-item-object-custom">
            hello
            hi
            hao
            hihihi
            <li>
            </li>
            <li>
            </li>
        </div>
        this is a tail
        <div>
            <li>
            </li>
        </div>
        <div>
        </div>
    </body>
    <!--this is acomment-->
</html>
'''


# 'nvhtml_html2rsh=nvhtml.WFS.bin_nvhtml_html2rsh:main',
# 'nvhtml_rsh2html=nvhtml.WFS.bin_nvhtml_rsh2html:main'


rsh = rshtml.html2rsh(html_txt)
html = rshtml.rsh2html(rsh)
