
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


parser = argparse.ArgumentParser()
parser.add_argument('-input','--input_html_file', default="",help="input html file name")
parser.add_argument('-codec','--input_codec', default="utf-8",help="input html file codec")
parser.add_argument('-tgpth','--tag_path', default=".",help="html tag dot path")


def get_dot_path_segs(pth):
    '''
        >>> get_dot_path_segs(".a.b.3.c.d.5.e.f")
        (['//a/b', 3, 'c/d', 5, 'e'], 'f')
        >>>
        >>> get_dot_path_segs("a.b.3.c.d.5.e.f")
        (['/a/b', 3, 'c/d', 5, 'e'], 'f')
        >>>
        >>> get_dot_path_segs("a.b.3.c.d.5.e.f.")
        (['/a/b', 3, 'c/d', 5, 'e/f'], '')
        >>>
    '''
    arr =  pth.split(".")
    tail = arr[-1]
    arr  =  arr[:-1]
    segs = []
    if(arr[0] ==  ""):
        arr[0] =  "/"
    else:
        pass
    seg = ""
    for i in range(arr.__len__()):
        tag = arr[i]
        try:
            int(tag)
        except:
            seg  = seg + tag + "/"
        else:
            seg = seg.rstrip("/")
            segs.append(seg)
            segs.append(int(tag))
            seg = ""
    if(seg == ""):
        pass
    else:
        seg = seg.rstrip("/")
        segs.append(seg)
    if(segs[0][:2]=="//"):
        pass
    else:
        segs[0] = "/" + segs[0]
    return((segs,tail))




def get_pre_tail_nodes(pth,root):
    '''
    '''
    #
    segs,tail = get_dot_path_segs(pth)
    #
    node = root
    #
    for i in range(0,segs.__len__()):
        seg = segs[i]
        try:
            int(seg)
        except:
            xpath = seg
        else:
            nodes = engine.xpath(node,xpath)
            node = nodes[int(tag)]
            xpath = ""
    if(xpath ==  ""):
        nodes = [node]
    else:
        nodes = engine.xpath(node,xpath)
    return((nodes,tail))





##############################################
def get_next_layer_tags_via_xpath(root,xpath):
    eles = engine.xpath(root,xpath)
    arr = elel.mapv(eles,lambda ele:ele.getchildren())
    rslt = []
    for i in range(arr.__len__()):
        tmp = arr[i]
        rslt.extend(tmp)
    tags = elel.mapv(rslt,lambda ele:ele.tag)
    return(tags)
####################################################

def get_next_layer_tags(nodes):
    eles = elel.mapv(nodes,lambda ele:ele.getchildren())
    rslt = []
    for i in range(eles.__len__()):
        tmp = eles[i]
        rslt.extend(tmp)
    tags = elel.mapv(rslt,lambda ele:ele.tag)
    return(tags)





def get_seqs(tags,tail):
    seqs = elel.indexes_all(tags,tail)
    return(seqs)

def get_options(tags,tail):
    rslt = []
    for i in range(tags.__len__()):
        tag = tags[i]
        cond = tag.startswith(tail)
        rslt.append(tag)
    return(rslt)


args = parser.parse_args()


def main():
    html_str = fs.rfile(args.input_html_file)
    root = LXHTML(html_str)
    pth = args.tag_path
    #
    #print(pth)
    #
    nodes,tail = get_pre_tail_nodes(pth,root)
    #
    #print(nodes,tail)
    #
    if(tail == None):
        print(engine.beautify(nodes[0]))
    else:
        tags = get_next_layer_tags(nodes)
        seqs = get_seqs(tags,tail)
        lngth = seqs.__len__()
        if(lngth == 0):
            opts  = get_options(tags,tail)
            pobj(opts)
        elif(lngth == 1):
            breadth = seqs[0]
            nds = node.xpath(tail)
            elel.for_each(nds,lambda nd:print(engine.beautify(nd)))
        else:
            pobj(elel.elel.init_range(0,lngth,1))




#nvhtml_tgpth -input opis.html  -tgpth html.body.div
