
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
import ematmap.ematmap as emem



parser = argparse.ArgumentParser()
parser.add_argument('-input','--input_html_file', default="",help="input html file name")
parser.add_argument('-codec','--input_codec', default="utf-8",help="input html file codec")
parser.add_argument('-rmhtml','--rm_html', default=True,help="remove html body heads  when html head is empty")


args = parser.parse_args()


def fmt(pl):
    if(len(pl) >=2 and pl[:2]==['html', 'body']):
        rslt = pl[2:]
    elif(pl==['html']):
        rslt = []
    else:
        rslt = pl
    return(rslt)




def main():
    html_str = fs.rfile(args.input_html_file)
    root = LXHTML(html_str)
    wfs = engine.WFS(root)
    m = wfs.mat 
    pls = engine.dulr_wfspls(m)
    if(args.rm_html):
        pls = elel.mapv(pls,fmt)
        pls = elel.remove_all(pls,[])
    pbmat = emem.mapv(m,map_func=lambda v:v['pbreadth'],inplace=False)
    plmat = emem.mapv(m,map_func=lambda v:v['pl'],inplace=False)
    plgroups = elel.mapivo(plmat,map_func=lambda i,pl,*o:elel.groupby_refl(pl,o),map_func_args_array=pbmat)
    elel.for_each(plgroups,print)
