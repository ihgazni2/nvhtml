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

args = parser.parse_args()

def main():
    html_str = fs.rfile(args.input_html_file)
    root = LXHTML(html_str)
    html_str = engine.beautify(root)
    fn = args.input_html_file+".out.html"
    fs.wfile(html_str,fn)




