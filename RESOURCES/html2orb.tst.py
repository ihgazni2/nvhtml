
from lxml import etree
#from xdict.jprint import pobj,pdir,parr
from efdir import fs
import requests
import xxurl.xxurl as xuxu
from nvhtml import engine
import elist.elist as elel


url = "https://www.w3school.com.cn/cssref/index.asp"

def url2orb(url):
    r=requests.get(url)
    html_txt = r.text
    r = engine.s2root(html_txt)
    html = ele2orb(r)
    return(html)


def tr_with_three_th(ele):
    if(ele.getparent()==None):
        trs = ele.xpath("//tr")
    else:
        trs = ele.xpath("tr")
    trs = elel.filter(trs,lambda tr:tr.xpath('th').__len__()==3)
    return(trs)

