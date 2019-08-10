from lxml.etree import HTML as LXHTML
# from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj
# from nvhtml import txt
# from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
# from nvhtml import utils
# import lxml.sax
from efdir import fs
import elist.elist as elel
import edict.edict as eded
import sqlite3
import qtable.qtable as qtb
import estring.estring as eses
from pandas.io import sql
import json
import os
import tytycss.tytycss as tyty
import jsbeautifier as jb
import copy
import xxurl.xxurl as xuxu

CMMN_COLUMNS = ['@tag@', '@text@', '@tail@','@text_intag@', '@pl@','@depth@', '@breadth@','@pbreadth@' '@sibseq@', '@samepl_total@','@samepl_sibseq@', '@samepl_breadth@']



def _size(wfs):
    sz = 0
    for i in range(wfs.mat.__len__()):
        layer = wfs.mat[i]
        for j in range(layer.__len__()):
            sz = sz + 1
    return(sz)

def _get_all_attrib_names(wfs):
    attr_names = set({})
    for i in range(wfs.mat.__len__()):
        layer = wfs.mat[i]
        for j in range(layer.__len__()):
            ele = layer[j]
            anames = list(ele['attrib'].keys())
            for name in anames:
                attr_names.add(name)
    return(list(attr_names))


def _get_attrib_name_freqs(wfs,attr_names):
    freqs = elel.init(attr_names.__len__(),0)
    for i in range(wfs.mat.__len__()):
        layer = wfs.mat[i]
        for j in range(layer.__len__()):
            ele = layer[j]
            anames = list(ele['attrib'].keys())
            for name in anames:
                index = attr_names.index(name)
                freqs[index] = freqs[index] + 1
    return(freqs)


def _sort_attr_names(wfs):
    attr_names = _get_all_attrib_names(wfs)
    freqs = _get_attrib_name_freqs(wfs,attr_names)
    attr_names,freqs= elel.batsorted(freqs,attr_names,freqs,reverse=True)
    return((attr_names,freqs))


def _jsonize_pl(pl):
    pl = elel.mapv(pl,lambda ele:str(ele))
    return(json.dumps(pl))




def _ele2vl(ele,columns):
    kl = columns
    vl =  elel.init(columns.__len__(),None)
    for k in ele:
        if(k == "attrib"):
            attribs = ele[k]
            for attr in attribs:
                i = kl.index(attr)
                vl[i] = attribs[attr]
        else:
            if("@"+k+"@" in kl):
                i = kl.index("@"+k+"@")
                if(k == "pl"):
                    vl[i] = _jsonize_pl(ele[k])
                else:
                    vl[i] = ele[k]
            else:
                pass
    return(vl)



def _get_fmt_wfs_mat(wfs,columns):
    wfs_list = elel.mat2wfs(wfs.mat)
    pls = elel.mapv(wfs_list,lambda ele:ele['pl'])
    mat = []
    c1d =0 
    for i in range(wfs.mat.__len__()):
        layer = wfs.mat[i]
        for j in range(layer.__len__()):
            ele = layer[j]
            ele["breadth"] = j
            ele["depth"] = i
            ele["c1d"] = c1d
            ele['samepl_total'] = pls.count(ele['pl'])
            entry = _ele2vl(ele,columns)
            mat.append(entry)
            c1d = c1d+1
    return(mat)








def _get_df(wfs,attr_names):
    columns = elel.concat(CMMN_COLUMNS,attr_names)
    wfsmat = _get_fmt_wfs_mat(wfs,columns)
    df = qtb.Qtable(mat=wfsmat,index=elel.init_range(0,wfsmat.__len__(),1),columns=columns)
    return(df)


##
def _attr(df_internal,attr):
    l = list(df_internal.loc[df_internal[attr].notnull()][attr])
    return(l)

# >>> df_internal.loc[df_internal['@tag@']=='style'].index
# Int64Index([41], dtype='int64')
# >>>



def _text(df_internal,strip=True):
    l = list(df_internal.loc[df_internal['@text@'].notnull()]['@text@'])
    if(strip):
        l = elel.mapv(l,lambda txt:eses.strip(txt,"\n\t\x20"))
        l = elel.cond_select_values_all(l,cond_func=lambda s:not(s==""))
    else:
        pass
    return(l)

def _tail(df_internal,strip=True):
    return(_text(df_internal,strip=strip,attr='@tail@'))


def _pl(df_internal):
    l = _attr(df_internal,'@pl@')
    return(l)

def _row(df_internal,rownum):
    return(df_internal.loc[rownum].dropna())

def _row2d(row):
    '''
        pobj(_row2d(_row(df_internal,35)))
    '''
    kl = list(row.index)
    vl = list(row.values)
    return(eded.kvlist2d(kl,vl))


def _col(df_internal,colname):
    return(df_internal[colname].dropna())


#####





#####


##


###

#####

def _to_sqlite(df_internal,dbname,tbname="HTML"):
    cnx = lite.connect(dbname)
    sql.to_sql(df_internal, name=tbname, con=cnx)
    return(cnx)

def _to_csv(df_internal,csvname):
    csv = df_internal.to_csv()
    fs.wfile(csvname,csv)


def _beautify_text(tag,text):
    if(tag == 'style'):
        text = tyty.beautify(text)
    elif(tag== 'script'):
        text = jb.beautify(text)
    else:
        pass
    return(text)


def _to_d4dir(d):
    nd = {}
    internal_attrnames = ['pl','tag','samepl_total','samepl_sibseq','samepl_breadth','sibseq','breadth','pbreadth','depth','c1d']
    nd['iattrib'] = {}
    for k in internal_attrnames:
        nd['iattrib'][k] = d[k]
    nd['iattrib']['pl'] = elel.mapv(nd['iattrib']['pl'],lambda ele:str(ele))
    nd['attrib'] = d['attrib']
    nd['text'] = _beautify_text(d['tag'],d['text'])
    nd['tail'] = d['tail']
    nd['text_intag'] = d['text_intag']
    # nd['outter_html'] = engine.beautify(d['node'])
    return(nd)


def _to_dirs(df_internal,wfs_list,wkdir="./"):
    nwfs_list = elel.mapv(wfs_list,_to_d4dir)
    for i in range(len(wfs_list)):
        dir_path = fs.pl2path(wfs_list[i]['pl'])
        samepl_total = wfs_list[i]['samepl_total']
        if(samepl_total >1):
            dir_path = os.path.join(dir_path,str(wfs_list[i]['samepl_breadth']))
        else:
            pass
        dir_path = os.path.join(wkdir,dir_path)
        fs.mkdirs(dir_path)
        d = nwfs_list[i]
        for k in d:
            path = os.path.join(dir_path,k)
            if(isinstance(d[k],str)):
                fs.wfile(path,d[k]+"\r\n")
            else:
                fs.wjson(path,d[k])

def _get_unique_pl(d):
    samepl_total = d['iattrib']['samepl_total']
    pl = copy.deepcopy(d['iattrib']['pl'])
    if(samepl_total == 1):
        pass
    else:
        pl.append(d['iattrib']['samepl_breadth'])
    return(pl)

def _rm_html_body(pl):
    try:
        if(pl[0]=='html'):
            pl = pl[1:]
        else:
            pass
    except:
        return(pl)
    else:
        try:
            if(pl[0]=='body'):
                pl = pl[1:]
            else:
                pass
        except:
            return(pl)
        else:
            return(pl)

def _flat_kv(wfs_list,only_attrib=True,sp="\x20",wkdir="./flatkv.json",**kwargs):
    if("rm_html_body" in kwargs):
        rm_html_body = kwargs['rm_html_body']
    else:
        rm_html_body = False
    wfs_list = elel.mat2wfs(wfs.mat)
    nwfs_list = elel.mapv(wfs_list,_to_d4dir)
    nd = {}
    for d in nwfs_list:
        pl = _get_unique_pl(d)
        if(rm_html_body):
            pl = _rm_html_body(pl)
        else:
            pass 
        k = elel.join(pl,sp)
        if(only_attrib):
            nd[k] = d['attrib']
        else:
            nd[k] = d
    if(rm_html_body):
        del nd['']
    else:
        pass 
    fs.wjson(wkdir,nd)
    return(nd)

######

#依赖lxml,反选出规则,再按照css (,,,,) priority 得到 最后输出

def _element_match_selector(sel_str,ele):
    sel = lxml.cssselect.CSSSelector(sel_str)
    l = sel.evaluate(ele)
    if(len(l)==0):
        return(False)
    else:
        return(True)

######

# import sys
# html_fn = sys.argv[1]



html_txt = fs.rfile('test.html')
root = LXHTML(html_txt)
wfs = engine.WFS(root)
attr_names,freqs = _sort_attr_names(wfs)
df = _get_df(wfs,attr_names)
df_internal = df.df
wfs_list = elel.mat2wfs(wfs.mat)
nwfs_list = elel.mapv(wfs_list,_to_d4dir)
flatkv = _flat_kv(wfs_list)
flatkv_full = _flat_kv(wfs_list,False,sp="\x20",wkdir="./flatkv_full.json")
_to_dirs(df_internal,wfs_list)







#nwfs_list search

def _in_text_search_wfs_list(nwfs_list,txt):
    def cond_func(ele,txt):
        if(ele['text']==None):
            return(False)
        else:
            return((txt in ele['text']))
    eles = elel.filter(nwfs_list,cond_func,txt)
    return(eles)













#####























