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

parser = argparse.ArgumentParser()
parser.add_argument('-input','--input_html_file', default="",help="input html file name")
parser.add_argument('-output','--output_html_file', default="",help="output html file name")
parser.add_argument('-codec','--input_codec', default="utf-8",help="input html file codec")

parser.add_argument('-tag','--html_tag', default="",help="html tag necessary")
parser.add_argument('-which','--which_tag', default=None,help="sequence number in tag-array")


args = parser.parse_args()

def main():
    html_str = fs.rfile(args.input_html_file,codec=args.input_codec)
    root = LXHTML(html_str)
    entries = lvsrch.srch(args.html_tag,root,which=args.which_tag)
    fn = args.input_html_file+"."+args.html_tag +".html"
    fs.wfile(fn,html_str)




