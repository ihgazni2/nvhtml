import edict.edict as eded
import efuntool.efuntool as eftl
import copy
import elist.elist as elel

# 下面这两个更新到efuntool


# 下面这两个更新到efuntool

#def de_args_kwargs(kl,dflt_vl,*args,**kwargs):

import  efuntool.efuntool as eftl

eftl.self_args_kwargs
eftl.de_args_kwargs

NODE_KL = ['_tag','_row','_children']
NODE_DFLT_VL = ['view',True,[]]


NODE_TYPE = type(Node())

def is_node(obj):
    return(isinstance(obj,NODE_TYPE))


class Node():
    def __init__(self,*args,**kwargs):
        '''
            #这种方法定义的不会触发__setattr__
        '''
        dflt_vl = copy.deepcopy(NODE_DFLT_VL)
        d = de_args_kwargs(NODE_KL,dflt_vl,*args,**kwargs)
        eded._update(self.__dict__,d,deepcopy=0)
    def __repr__(self):
        return(self._tag)
    def __setattr__(self,an,*args):
        tag_or_node = eftl.optional_arg('view',*args)
        if(an[0]=='_'):
            raise(NameError('attribute name cant start with "_"'))
        elif(is_node(tag_or_node)):
            self.__dict__['_children'].append(tag_or_node)
        else:
            nd = Node(tag_or_node)
            self.__dict__['_children'].append(nd)


def get_fstch(nd):
    children = nd.getchildren()
    return(None if(children.__len__() == 0) else children[0])

def get_rsib(nd):
    return(nd.getnext())

def is_root(nd):
    return(nd.getparent() == None)

def is_leaf(nd):
    return(nd.getchildren().__len__() == 0)


def get_rsib_of_fst_ances_with_rsib_including_self(nd):
    rsib = get_rsib(nd)
    while(rsib  == None):
        if(is_root(nd)):
            return(None)
        else:
            pnd = nd.getparent()
            rsib = get_rsib(pnd)
            nd = pnd
    return(rsib)


def get_sdfs_next(nd):
    fstch = get_fstch(nd)
    if(fstch != None):
        return(fstch)
    else:
        rsib = get_rsib_of_fst_ances_with_rsib_including_self(nd)
        return(rsib)

def get_sdfsndl2(nd):
    sdfsndl = [nd]
    while(nd!= None):
        nd = get_sdfs_next(nd)
        sdfsndl.append(nd)
    return(sdfsndl[:-1])


def get_sdfsndl(nd):
    sdfsndl = ([nd] +list(r.iterdescendants()))
    return(sdfsndl)



from lxml import etree
from xdict.jprint import pobj,pdir,parr
from efdir import fs
html_txt = fs.rfile('tst.html')
r = etree.HTML(html_txt)


def is_comment(ele):
    return(isinstance(ele,lxml.etree._Comment))

def is_comment_tag(tag):
    cond = isinstance(tag,str)
    if(not(cond)):
        if(tag.__name__ == 'Comment'):
            return(True)
        else:
            return(False)
    else:
        return(False)


def tag2an(tag):
    cond = is_comment_tag(tag)
    if(cond):
        return('Comment')
    else:
        return(tag.replace('-','_'))

def an2tag(an):
    return(an.replace('_','-'))


def group_children_by_tag_and_set(children,orb):
    st=set({})
    for i in range(len(children)):
        child = children[i]
        ele = child.__dict__['_ele']
        tag = ele.tag
        an = tag2an(tag)
        if(an in st):
            eles = orb.__dict__[an]
            eles.append(child)
        else:
            orb.__dict__[an] = [child]
            st.add(an)


def ele2orb(ele):
    rorb = Orb(ele)
    unhandled = [rorb]
    next_unhandled = []
    while(len(unhandled) >0):
        for i in range(len(unhandled)):
            orb = unhandled[i]
            ele = orb.__dict__['_ele']
            ele_children = ele.getchildren()
            children = elel.mapv(ele_children,Orb)
            if(len(children) == 0):
                setattr(orb,"",None)
            else:
                pass
            group_children_by_tag_and_set(children,orb)
            next_unhandled = next_unhandled + children
        unhandled = next_unhandled
        next_unhandled = []
    return(rorb)


class List():
    _list = []
    def __init__(self):
        setattr(self," ","")
    def __repr__(self):
        return(self._list.__repr__())

class Dict():
    _dict = {}
    def __init__(self):
        setattr(self," ","")
    def __repr__(self):
        return(self._dict.__repr__())


import re

def split_an(an):
    for i in range(len(an)):
        ch = an[i]
        if(ch in "0123456789"):
            break
        else:
            pass
    if(i == (len(an) -1) and not(ch in "0123456789")):
        ran = an
        seqs= []
    else:
        ran = an[:i]
        seqs = an[i:].split('_')
        seqs = elel.mapv(seqs,int)
    return(ran,seqs)


class Orb(object):
    #singleton _dict = {} 自定义的有singleton效果
    # __dict__ 没有singleton 效果,并且不会触发__setattr__
    def __init__(self,ele):
        self.__dict__['_ele'] = ele
    def __repr__(self):
        return(self.__dict__['_ele'].__repr__())
    def __getattribute__(self,an):
        #*args 在这个函数里 无法 使用 会随结果一起返回
        if(an[0]=="_"):
            return(object.__getattribute__(self,an))
        else:
            an,seqs = split_an(an)
            arr = self.__dict__[an]
            if(len(seqs) == 0):
                return(arr)
            elif(len(seqs) == 1):
                return(arr[seqs[0]])
            else:
                return(elel.select_seqs(arr,seqs))


class tst(object):
    __dict = {}
    def __init__(self):
        self.__dict['ctrl'] = {}
    def __setitem__(self,k,v):
        self.__dict['ctrl'][k] = v
    def __repr__(self):
        return(self.__dict['ctrl'].__repr__())


class tst2():
    __dict = {}
    def __init__(self):
        self.__dict['ctrl'] = {}



class tst3():
    __u = {}

'''
>>> class tst3():
...     __u = {}
...
>>> k = tst3()
>>>
>>> k._tst3__u
{}
>>>
'''


class tst4():
    ___u = {}

#####################3
class tst():
    def __getattribute__(self,*args):
        print(args)
    def __setattr__(self,*args):
        print(args)


class Orb(object):
    def __init__(self,ele):
        self.__dict__['__ctrl'] = {}
        self.__dict__['__ele'] = ele
    def __setitem__(self,k,v):
        self.__dict__['__ctrl'][k] = v
    def __getitem__(self,k):
        return(self.__dict__['__ctrl'][k])
    def __repr__(self):
        return(self.__dict__['__ctrl'].__repr__())


####

def get_tags(eles):
    tags = elel.mapv(eles,lambda ele:ele.tag)
    return(tags)

def get_keys(eles):
    tags = get_tags(eles)
    if(len(tags) == 0):
        return([])
    else:
        return(elel.uniqualize(tags))


def ele2wmat(ele):
    wmat = []
    orb = rele2orb(ele)
    unhandled = [orb]
    next_unhandled = []
    while(len(unhandled) >0):
        lyr = []
        wmat.append(lyr)
        for i in range(len(unhandled)):
            orb = unhandled[i]
            lyr.append(orb)
            depth = orb.depth + 1
            pbreadth = orb.breadth
            lngth = len(next_unhandled)
            ele_children = orb.ele.getchildren()
            orb.keys = get_keys(ele_children)
            children = elel.mapiv(ele_children,lambda i,ele:ele2orb(ele,depth,lngth+i,pbreadth))
            orb.group = group_children_by_tag(children)
            next_unhandled = next_unhandled + children
        unhandled = next_unhandled
        next_unhandled = []
    return(wmat)



def leaf_ele2nd(leaf_ele):
    nd = Node()
    tag = leaf_ele.tag.replace('-','_')
    nd['ele'] = leaf_ele
    return(nd)


class Node(dict):
    pass



import elist.elist as elel

wmat = ele2wmat(r)
depth = len(wmat)
lst_lyr = wmat[depth-1]
unhandled = elel.mapv(lst_lyr,leaf_ele2nd)

while(depth >0):





    ele_lyr = wmat[i]
    tags = get_tags(ele_lyr)
    ans = elel.uniqualize(tags)
    for an in ans:
        setattr(nd,an,[])
        unhandled



for i in range(len(wmat)):



    for an in ans:
        setattr(nd,an,[])

