
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



parser = argparse.ArgumentParser()
parser.add_argument('-input','--input_html_file', default="",help="input html file name")
parser.add_argument('-codec','--input_codec', default="utf-8",help="input html file codec")
parser.add_argument('-wkdir','--work_dir', default=".",help="workdir")


args = parser.parse_args()

CMMN_HIDDEN_ATTRS = ['pl','depth', 'breadth','pbreadth','sibseq', 'samepl_total','samepl_sibseq', 'samepl_breadth']
CMMN_NORMAL_ATTRS = ['tag', 'text', 'tail','text_intag']
CMMN_CALC_ATTRS = ['outter_html']

def handle_each_ele(ele,root,wkdir):
    pl = ele['pl']
    tail = pl[-1]
    if(tail[0]=="<"):
        outter_html = "<!--" + ele['text'] +"-->"
    else:
        pth = elel.join(pl,"/")
        nds = engine.xpath(root,"/"+pth)
        nd = nds[ele['samepl_breadth']]
        outter_html = engine.beautify(nd)
    pl_str = elel.join(pl,"/")
    pl_str = "/"  + pl_str
    ele['pl'] = pl_str
    curr_dir = wkdir + pl_str
    fs.mkdir(curr_dir)
    for k in ele:
        v = ele[k]
        if(k in CMMN_HIDDEN_ATTRS):
            v=str(v)
            ele_dir = curr_dir + "/." + k
            fs.wfile(ele_dir,v)
        elif(k in CMMN_NORMAL_ATTRS):
            v=str(v)
            ele_dir = curr_dir + "/" + k
            fs.wfile(ele_dir,v)
        else:
            attrib = v
            if(attrib == None):
                attrib = {}
            else:
               pass
            for ak in attrib:
                av = attrib[ak]
                av = str(av)
                ele_dir = curr_dir + "/attrib." + ak
                fs.wfile(ele_dir,av)
        ele_dir = curr_dir + "/" + 'outter_html'
        fs.wfile(ele_dir,outter_html)


def main():
    html_str = fs.rfile(args.input_html_file)
    root = LXHTML(html_str)
    wfs = engine.WFS(root)
    mat = wfs.mat
    wkdir = args.work_dir
    elel.mat_mapv(mat,handle_each_ele,[root,wkdir])