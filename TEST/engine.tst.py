

from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from xdict.jprint import pdir,pobj

html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
node = engine.xpath_levels(root,"//a",5,6)[0]
pl = engine.pathlist(node)
pl



engine.pathlist(node)
engine.between_levels_cond_func(node, 3, 6)
engine.between_levels_cond_func(node, 7, 9)



from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj



from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine




html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
eles = engine.xpath(root,"//a")
ele =  engine.xpath(root,"//a",0)
ele1,ele2,ele3 = engine.xpath(root,"//a",1,2,3)


from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj



from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine

html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
#eles = engine.xpath_levels(root,"//a",start,end)
eles = engine.xpath_levels(root,"//a",5,6)
#eles = engine.xpath_levels(root,"//a",start)
eles = engine.xpath_levels(root,"//a",5)
#eles = engine.xpath_levels(root,"//a",start=0,end=ei)
eles = engine.xpath_levels(root,"//a",end=8)
#eles = engine.xpath_levels(root,"//a",start=7,end=last)
eles = engine.xpath_levels(root,"//a",start=7)
#eles = engine.xpath_levels(root,"//a",start=si,end=ei)
eles = engine.xpath_levels(root,"//a",start=7,end=9)





engine.plget(root,"a")
#()
engine.plget(root,"a",strict=False)
engine.plget(root,['html', 'body', 'div', 'div'])
engine.plget(root,'html', 'body', 'div', 'div')
#(<Element div at 0x21602c68dc8>, <Element div at 0x21602a9f748>, <Element div at 0x21602c68e48>, <Element div at 0x21602c68f48>, <Element div at 0x21602c68ec8>, <Element div at 0x21602c68f08>)
engine.plget(root,'html', 'body', 'div', 'div',whiches=[2,3,4])
#(<Element div at 0x21602c68e48>, <Element div at 0x21602c68f48>, <Element div at 0x21602c68ec8>)
engine.plget(root,'html', 'body', 'div', 'div',whiches=3)
#<Element div at 0x21602c68f48>



from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj

from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils

html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
ele1,ele2,ele3 = engine.xpath(root,"//a",1,2,3)
print(engine.source(ele1))
print(engine.source(ele2))


from nvhtml import utils
eles = list(engine.xpath(root,"//a",1,2,3))
txts = engine.txtize(eles)
utils.parr(txts)





html_str =  """<div>
    div-text
    <p>
        p-text
    </p>
    p-tail-in-div-closure
</div>"""

root = LXHTML(html_str)
ele = engine.xpath(root,"//div",0)
print(engine.text_intag(ele))
#>>> print(engine.text_intag(ele))
#
#    div-text
#
#    p-tail-in-div-closure
#
#>>>

from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj

from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils


html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
ele = engine.xpath(root,"//a",0)
engine.ancestors(ele)
# [<Element div at 0x21ec4c5d108>, <Element div at 0x21ec4c5d208>, <Element body at 0x21ec4c5d188>, <Element html at 0x21ec4ebe8c8>]
engine.ancestor(ele,1)
# <Element div at 0x21ec4c5d108>
engine.ancestors(ele,2,3)
# [<Element div at 0x21ec4c5d208>, <Element body at 0x21ec4c5d188>]
engine.ancestors(ele,start=2)
# [<Element div at 0x21ec4c5d208>, <Element body at 0x21ec4c5d188>, <Element html at 0x21ec4ebe8c8>]
engine.ancestors(ele,end=2)
# [<Element div at 0x21ec4c5d108>]
engine.ancestors(ele,start=2,end=4)
# [<Element div at 0x21ec4c5d208>, <Element body at 0x21ec4c5d188>]





html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
ele = engine.xpath(root,"//div",0)
childs = engine.children(ele)
childs
# [<Element div at 0x1a8609755c8>, <Element div at 0x1a860973988>, <Element div at 0x1a860973b48>, <Element div at 0x1a860973a88>, <!-- maincontent end -->, <Element div at 0x1a860973b08>, <Element div at 0x1a860973908>]
engine.children(ele,0)
# [<Element div at 0x1a8609755c8>]
engine.children(ele,4)
# [<!-- maincontent end -->]
engine.children(ele,6)
# [<Element div at 0x1a860973908>]
engine.children(ele,1,3,5)
# [<Element div at 0x1a860973988>, <Element div at 0x1a860973a88>, <Element div at 0x1a860973b08>]
engine.children(ele,[1,3,5])
# [<Element div at 0x1a860973988>, <Element div at 0x1a860973a88>, <Element div at 0x1a860973b08>]
engine.children(ele,start=1,end=4)
# [<Element div at 0x1a860973988>, <Element div at 0x1a860973b48>, <Element div at 0x1a860973a88>]

##



html_str = """
<html>
    <head>
    </head>
    <body>
        <div-out-1>
            <div id="0">b0</div>
            <div id="1">b1</div>
            <div id="2">b2</div>
            <div id="3">b3</div>
        </div-out-1>
        <div-out-2>
            <li id="0">l0</li>
            <li id="1">l1</li>
            <li id="2">l2</li>
            <li id="3">l3</li>
        </div-out-2>
    </body>
</html>
"""

root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-1/div",2)
ele.text
# 'b2'
engine.sibseq(ele)
# 2





root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-1/div",2)
sibs = engine.siblings(ele)
sibs
#[<Element div at 0x1d3f56f2808>, <Element div at 0x1d3f56f2848>, <Element div at 0x1d3f56f0308>, <Element div at 0x1d3f56f2888>]
engine.siblings(ele,0)
#[<Element div at 0x1d3f56f2808>]
engine.siblings(ele,3)
#[<Element div at 0x1d3f56f2888>]
engine.siblings(ele,1,2)
#[<Element div at 0x1d3f56f2848>, <Element div at 0x1d3f56f0308>]
engine.siblings(ele,[1,2,3])
#[<Element div at 0x1d3f56f2848>, <Element div at 0x1d3f56f0308>, <Element div at 0x1d3f56f2888>]
engine.siblings(ele,start=2,end=3)
#[<Element div at 0x1d3f56f0308>]



from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj

from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils


html_str = """
<html>
    <head>
    </head>
    <body>
        <div-out-1>
            <divx id="0">b0</divx>
            <divy id="1">b1</divy>
            <divx id="2">b2</divx>
            <divy id="3">b3</divy>
        </div-out-1>
        <div-out-2>
            <li id="0">l0</li>
            <li id="1">l1</li>
            <li id="2">l2</li>
            <li id="3">l3</li>
        </div-out-2>
    </body>
</html>
"""

root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-1/divx",0)
eles = engine.samepl_siblings(ele)
eles
# [<Element divx at 0x251425b9cc8>, <Element divx at 0x251425bf888>]
engine.pathlist(eles[0])
# engine.pathlist(eles[0])
engine.pathlist(eles[1])
# engine.pathlist(eles[1])




root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-1/divx",1)
engine.sibseq(ele)
# 2
engine.samepl_sibseq(ele)
# 1

##########################################################
##########################################################


root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-1/divx",1)
engine.lsib(ele)
# <divy id="1">b1</divy>
ele = engine.xpath(root,"//body/div-out-1/divx",0)
# <divx id="0">b0</divx>
engine.lsib(ele)
# None beacuse  <divx id="0">b0</divx>  is the left-most child of <div-out-1>




root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-1/divy",1)
# <divy id="3">b3</divy>
engine.rsib(ele)
# 
ele = engine.xpath(root,"//body/div-out-1/divy",0)
# <divy id="1">b1</divy>
print(engine.source(engine.rsib(ele)))
# <divx id="2">b2</divx>


from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj

from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils


html_str = """
<html>
    <head>
    </head>
    <body>
        <div-out-1>
            <divx id="0">b0</divx>
            <divy id="1">b1</divy>
            <divx id="2">b2</divx>
            <divy id="3">b3</divy>
        </div-out-1>
        <div-out-2>
            <li id="0">l0</li>
            <li id="1">l1</li>
            <li id="2">l2</li>
            <li id="3">l3</li>
        </div-out-2>
    </body>
</html>
"""

root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-2/li",0)
print(engine.source(engine.lcin(ele)))


root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-1/divy",1)
# <divy id="3">b3</divy>
print(engine.source(engine.rcin(ele)))
# <li id="0">l0</li>



##############

root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-2/li",0)
engine.breadth(ele)



###########################
###########################



html_str = """
<html>
    <head>
    </head>
    <body>
        <div-out-1>
            <divx id="10">b10</divx>
            <divy id="11">b11</divy>
            <divx id="12">b12</divx>
            <divy id="13">b13</divy>
        </div-out-1>
        <div-out-2>
            <divx id="20">b20</divx>
            <divy id="21">b21</divy>
            <divx id="22">b22</divx>
            <divy id="23">b23</divy>
        </div-out-2>
    </body>
</html>
"""

root = LXHTML(html_str)
ele = engine.xpath(root,"//body/div-out-2/divx",0)
engine.sampl_breadth(ele)
# 2




##########################
##########################
from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj

from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils


html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
engine.descendants(root).__len__()
# 867
engine.descendants(root,1,2)
# [<Element head at 0x2ec39e02f08>, <Element body at 0x2ec39e12148>]
engine.descendants(root,0,1)
# [<Element html at 0x2ec3a126608>]
eles = engine.descendants(root,5,7)
# start = 5 ,end =7, to get the nodes whose depth between 5 and 7 
engine.pathlist(eles[0])
# ['html', 'body', 'div', 'div', 'div', 'script']
engine.pathlist(eles[100])
# ['html', 'body', 'div', 'div', 'div', 'ul', 'li']





html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
# <Element html at 0x2ec3a13ee08>
ele = engine.xpath(root,"//body",0)
# <Element body at 0x2ec3a14da08>
ele.getparent()
# <Element html at 0x2ec3a13ee08>
engine.disconnect(ele)
# <Element body at 0x2ec3a14da08>
ele.getparent()
# None
root.getchildren()
# [<Element head at 0x2ec39e1f5c8>]




###
from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj

from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils


html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
wfs = engine.WFS(root)
pobj(wfs.mat[3][1])

{
 'pl':
       [
        'html',
        'body',
        'div',
        'div'
       ],
 'samepl_sibseq': 1,
 'samepl_breadth': 1,
 'tag': 'div',
 'sibseq': 1,
 'attrib':
           {
            'id': 'navfirst'
           },
 'text': '\r\n',
 'tail': '\r\n\r\n',
 'text_intag': '\r\n\r\n',
 'node': <Elementdivat0x24135ef9a88>
}
>>>










html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
pls = engine.wfspls(root)
utils.parr(pls[:10])
>>>
['html']
['html', 'head']
['html', 'body']
['html', 'head', <cyfunction Comment at 0x0000024135C12550>]
['html', 'head', 'script']
['html', 'head', 'script']
['html', 'head', 'meta']
['html', 'head', 'meta']
['html', 'head', 'meta']
['html', 'head', 'link']
>>>
utils.parr(pls[-10:])
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'span']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'a']
['html', 'body', 'div', 'div', 'div', 'table', 'tr', 'td', 'span']















html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
node = engine.loc2node(root,5,6)
node
# <Element li at 0x1c1502acd48>
engine.depth(node)
# 5
engine.breadth(node)
# 6



######################
######################




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
dfs = engine.DFS()
lxml.sax.saxify(root, dfs)
utils.parr(dfs.pls[:5])
>>>
['html', 'head', 'script']
['html', 'head', 'script']
['html', 'head', 'meta']
['html', 'head', 'meta']
['html', 'head', 'meta']
utils.parr(dfs.pls[-10:])
['html', 'body', 'div', 'div', 'div', 'script']
['html', 'body', 'div', 'div', 'div']
['html', 'body', 'div', 'div']
['html', 'body', 'div', 'div', 'p']
['html', 'body', 'div', 'div', 'p', 'a']
['html', 'body', 'div', 'div', 'p']
['html', 'body', 'div', 'div']
['html', 'body', 'div']
['html', 'body']
['html']
>>>
utils.parr(dfs.datas[-5:])
[(['html', 'body', 'div', 'div', 'p'], '\r\n使用条款和隐私条款。版权所有，保留一切权利。\r\n赞助商：'), (['html', 'body', 'div', 'div', 'p'], '。\r\n蒙ICP备06004630号\r\n')]
[(['html', 'body', 'div', 'div'], '\r\n'), (['html', 'body', 'div', 'div'], '\r\n\r\n'), (['html', 'body', 'div', 'div'], '\r\n')]
[(['html', 'body', 'div'], '\r\n\r\n'), (['html', 'body', 'div'], '\r\n\r\n'), (['html', 'body', 'div'], '\r\n\r\n'), (['html', 'body', 'div'], '\r\n\r\n'), (['html', 'body', 'div'], '\r\n'), (['html', 'body', 'div'], '\r\n\r\n'), (['html', 'body', 'div'], '\r\n\r\n'), (['html', 'body', 'div'], '\r\n\r\n\r\n')]
[(['html', 'body'], '\r\n\r\n'), (['html', 'body'], '\r\n'), (['html', 'body'], '\r\n\r\n')]
[(['html'], '\r\n'), (['html'], '\r\n\r\n'), (['html'], '\r\n\r\n')]
>>>
utils.parr(dfs.attribs[-5:])
{'id': 'p2'}
{'id': 'footer'}
{'id': 'wrapper'}
{'class': 'html'}
{'lang': 'zh-cn'}
>>>
dfs = engine.DFS(full_attrib=True)
lxml.sax.saxify(root, dfs)
utils.parr(dfs.attribs[-5:])
>>>
[('lang', 'zh-cn'), ('class', 'html'), ('id', 'wrapper'), ('id', 'footer'), ('id', 'p2')]
[('lang', 'zh-cn'), ('class', 'html'), ('id', 'wrapper'), ('id', 'footer')]
[('lang', 'zh-cn'), ('class', 'html'), ('id', 'wrapper')]
[('lang', 'zh-cn'), ('class', 'html')]
[('lang', 'zh-cn')]
>>>



###############
###############

import lxml.sax
html_str = fs.rfile("./test.html")
root = LXHTML(html_str)
html_str = engine.beautify(root)
print(html_str[:480])
>>>
<html lang="zh-cn">
    <head>
        <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-878633-1">
        </script>
        <script>
            window.dataLayer = window.dataLayer || [];
        </script>
        <meta charset="gbk">
        </meta>
        <meta name="robots" content="all">
        </meta>
        <meta name="author" content="w3school.com.cn">
        </meta>
        <link rel="stylesheet" type="text/css" href="/c5_20171220.css">
>>>
html_str = engine.beautify(root,fixed_indent=False)
print(html_str[:480])
print(html_str[:550])
<html lang="zh-cn">
      <head>
            <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-878633-1">
            </script>
            <script>
                    window.dataLayer = window.dataLayer || [];
            </script>
            <meta charset="gbk">
            </meta>
            <meta name="robots" content="all">
            </meta>
            <meta name="author" content="w3school.com.cn">
            </meta>
            <link rel="stylesheet" type="text/css" href="/c5_20171220.css">
>>>
