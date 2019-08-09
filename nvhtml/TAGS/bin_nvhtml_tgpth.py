
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







def parse_dot_path(pth,root):
    '''
    '''
    node = root
    arr = pth.split(".")
    head = arr[0]
    tail = arr[-1]
    if(head == "."):
        xpath = "//"
    else:
        xpath = ""
    try:
        int(tail)
    except:
        arr = arr[:-1]
    else:
        tail = None
    for i in range(0,arr.__len__()-1):
        tag = arr[i]
        try:
            int(tag)
        except:
            xpath = xpath  + tag + "/"
        else:
            xpath = xpath.rstrip("/")
            nodes = engine.xpath(node,xpath)
            node = nodes[int(tag)]
            xpath = ""
    tag = arr[i]
    try:
        int(tag)
    except:
        xpath = xpath  + tag 
        nodes = engine.xpath(node,xpath)
    else:
        xpath = xpath.rstrip("/")
        nodes = engine.xpath(node,xpath)
        node = nodes[int(tag)]
        nodes = [node]
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
    nodes,tail = parse_dot_path(pth,root)
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


