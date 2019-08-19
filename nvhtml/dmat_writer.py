from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
import lxml.etree

from nvhtml import engine

def fill_nd(nd,ele):
    for k in ele['attrib']:
        v = ele['attrib'][k]
        nd.set(k,v)
    nd.text = ele['text']
    nd.tail = ele['tail']
    return((nd,ele))

def fill_dmat_child_nd(ele,dmat):
    chlocs = ele['children']
    pnd = ele['nd']
    for i in range(len(chlocs)):
        loc = chlocs[i]
        chele = dmat[loc[0]][loc[1]]
        chtag = chele['tag']
        if(chtag  == "<comment>"):
            comment = lxml.etree.Comment(chele['text'])
            pnd.insert(i,comment)
            chnd = engine.child(pnd,i)
        else:
            chnd = lxml.etree.SubElement(pnd,chtag)
        chele['nd'] = chnd


def creat_root_nd(root_ele,dmat):
    tag = root_ele['tag']
    root = lxml.etree.Element(tag)
    root,root_ele = fill_nd(root,root_ele)
    root_ele['nd'] = root
    fill_dmat_child_nd(root_ele,dmat)
    return(root)

def dmat2etree(dmat):
    lngth = len(dmat)
    ######
    root_ele = dmat[0][0]
    root = creat_root_nd(root_ele,dmat)
    ######
    for i in range(1,lngth):
        layer = dmat[i]
        for j in range(len(layer)):
            ele = layer[j]
            nd = ele['nd']
            nd,ele = fill_nd(nd,ele)
            fill_dmat_child_nd(ele,dmat)
    ######
    return(root)

def dmat2html(dmat):
    r = dmat2etree(dmat)
    return(engine.beautify(r))
