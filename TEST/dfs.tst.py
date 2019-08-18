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
