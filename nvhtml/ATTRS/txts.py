from nvhtml.ATTR.attrsrch import *

def cls(root,*args,**kwargs):
    clses = srcha4txts(root,"class",*args,**kwargs)
    return(clses)
