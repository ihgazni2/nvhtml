import os

from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj
from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils
from nvhtml import htmldb 

import lxml.sax
import argparse
from efdir import fs
import elist.elist as elel
import edict.edict as eded
import estring.estring as eses
import spaint.spaint as spaint
from lxml.etree import tostring as nd2str


parser = argparse.ArgumentParser()
parser.add_argument('-input','--input_html_file', default="",help="input html file name")
parser.add_argument('-codec','--input_codec', default="utf-8",help="input html file codec")
parser.add_argument('-wkdir','--work_dir', default=".",help="workdir")
parser.add_argument('-dbname','--database_name', default="sqlite.db",help="database name")
#parser.add_argument('-beautify','--beautify', default=False,help="beautify")
parser.add_argument('-tbname','--table_name', default="tb_html",help="tbale name")

args = parser.parse_args()



def main():
    html_str = fs.rfile(args.input_html_file)
    root = LXHTML(html_str)
    wfs = engine.WFS(root)
    mat = wfs.mat
    attr_names,freqs= htmldb.sort_attr_names(mat)
    mat = htmldb.fmt_mat(mat,root)
    columns = elel.concat(htmldb.CMMN_COLUMNS,attr_names)
    dfmat = htmldb.get_dfmat(mat,columns)
    df = htmldb.get_df(dfmat,columns)
    dbname = args.work_dir+"/" +args.input_html_file +"." + args.database_name
    os.system("rm "+dbname)
    tbname = args.table_name
    cnx = htmldb.df2sqlite(df,dbname,tbname)
    cnx.close()
    print("db: ",dbname)
    print("table: ",tbname)
