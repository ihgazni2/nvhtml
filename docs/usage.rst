=====
Usage
=====

Command Line
------------

beautify
^^^^^^^^
    
    ::
    
        nvhtml_beauty -input opis.html
        vim opis.html.out.html
        
        # nvhtml_beauty -h
        usage: nvhtml_beauty [-h] [-input INPUT_HTML_FILE] [-output OUTPUT_HTML_FILE] [-codec INPUT_CODEC]

        optional arguments:
          -h,           --help                      show this help message and exit
          -input        --input_html_file           input html file name
          -output       --output_html_file          output html file name
          -codec        --input_codec               input html file codec


search with loc
^^^^^^^^^^^^^^^
     
    ::
        
        NVHTML-BENCH# nvhtml_loc -h
        usage: nvhtml_loc [-h] [-input INPUT_HTML_FILE] [-codec INPUT_CODEC]
                          [-loc MAT_LOC]
        
        optional arguments:
          -h,     --help                 show this help message and exit
          -input  --input_html_file      input html file name
          -codec  --input_codec          input html file codec
          -loc    --mat_loc              depth,breadth


        NVHTML-BENCH# nvhtml_loc -input opis.html -loc 11,2
        <------json-----
        {
         'pl':
               [
                'html',
                'body',
                'div',
                'div',
                'header',
                'div',
                'nav',
                'div',
                'ul',
                'li',
                'ul',
                'li'
               ],
         'breadth': 2,
         'depth': 11,
         'pbreadth': 2,
         'samepl_sibseq': 0,
         'samepl_breadth': 0,
         'tag': 'li',
         'sibseq': 0,
         'attrib':
                   {
                    'id': 'menu-item-22951',
                    'class': 'menu-item menu-item-type-post_type menu-item-object-page menu-item-22951'
                   },
         'text': None,
         'tail': '\n\t',
         'text_intag': ''
        }
        ------json---->
        
        <----------html--------------
        <li id="menu-item-22951" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-22951">
            <a href="https://opistobranquis.info/en/home/presentacio/">
                <span>
                    Presentation
                </span>
            </a>
        </li>
        
        <----------html--------------



        
tag search with depth
^^^^^^^^^^^^^^^^^^^^^
    
    ::
    
        NVHTML-BENCH# nvhtml_tag -h
        usage: nvhtml_tag [-h] [-input INPUT_HTML_FILE] [-codec INPUT_CODEC]
                          [-tag HTML_TAG] [-which WHICH_TAG]
                          [-sdepth START_LEVEL_DEPTH] [-edepth END_LEVEL_DEPTH]
        
        optional arguments:
          -h,                     --help                show this help message and exit
          -input                  --input_html_file     input html file name
          -codec                  --input_codec         input html file codec
          -tag                    --html_tag            html tag for search
          -which                  --which_tag           sequence of tag-array
          -sdepth                 --start_level_depth   start level depth
          -edepth                 --end_level_depth     end level depth
        NVHTML-BENCH#

        NVHTML-BENCH# nvhtml_tag -input opis.html.out.html -tag img -sdepth 3 -edepth 6
        <img alt="Twitter" src="https://opistobranquis.info/wp-content/themes/tempera/images/socials/Twitter.png">
        </img>
        
        <img alt="Facebook" src="https://opistobranquis.info/wp-content/themes/tempera/images/socials/Facebook.png">
        </img>
        
        <img alt="Twitter" src="https://opistobranquis.info/wp-content/themes/tempera/images/socials/Twitter.png">
        </img>
        
        <img alt="Facebook" src="https://opistobranquis.info/wp-content/themes/tempera/images/socials/Facebook.png">
        </img>
        
        <img style="float: right; display: none" class="loading" src="https://opistobranquis.info/wp-content/plugins/jetpack/modules/sharedaddy/images/loading.gif" alt="loading" width="16" height="16">
        </img>
        
        NVHTML-BENCH#    


search with tags-path
^^^^^^^^^^^^^^^^^^^^^
    
    ::
        
        NVHTML-BENCH# nvhtml_tgpth -input opis.html  -tgpth html.body.di
        [
         'div',
         'div',
         'div',
         'div'
        ]
        
        
        NVHTML-BENCH# nvhtml_tgpth -input opis.html  -tgpth html.body.div
        [
         0,
         1,
         2,
         3
        ]
        
        NVHTML-BENCH#
        NVHTML-BENCH# nvhtml_tgpth -input opis.html  -tgpth html.body.div.3
        <div id="cookie-banner">
        
            <div id="cookie-banner-container">
        
                <div class="left">
                                                Our website uses cookies. By accessing our website and
                    <br>
                    </br>
                    agreeing to this policy, you consent to our use of cookies.
                </div>
        
                <div class="right">
        
                    <a class="accept" href="#">
                        ACCEPT
                    </a>
        
                    <a class="more-info" href="https://opistobranquis.info/1HWEw">
                                                                MORE INFO
                    </a>
        
                </div>
        
            </div>
        </div>
        NVHTML-BENCH#


        usage: nvhtml_tgpth [-h] [-input INPUT_HTML_FILE] [-codec INPUT_CODEC]
                            [-tgpth TAG_PATH]
        
        optional arguments:
          -h,        --help                                  show this help message and exit
          -input     --input_html_file INPUT_HTML_FILE       input html file name
          -codec     --input_codec INPUT_CODEC               input html file codec
          -tgpth     --tag_path TAG_PATH                      html tag dot path


Examples
--------

tagsrch
^^^^^^^

    ::
    
        from lxml.etree import HTML as LXHTML
        from lxml.etree import XML as LXML
        from xdict.jprint import pdir,pobj
        from nvhtml import txt
        from nvhtml import lvsrch
        from nvhtml import fs
        from nvhtml import engine
        from nvhtml import utils
        import lxml.sax
        
    :: 
    
        html_str = fs.rfile("./test.html")
        root = LXHTML(html_str)
        eles = lvsrch.a(root,7,8,show=False)
        print(eles[0])
        print(eles[5])
        eles = lvsrch.a(root,7,8,which=0)
        eles = lvsrch.a(root,7,8,which=0,source=False)

.. image:: ./images/lvsrch.a.0.png


relation get
^^^^^^^^^^^^

:: 
    
    html_str = fs.rfile("./test.html")
    root = LXHTML(html_str)
    ele =  engine.xpath(root,"//div",5)
    
    engine.parent(ele)
    engine.grand_parent(ele)
    engine.ancestors(ele)
    engine.parent(ele)
    engine.grand_parent(ele)
    engine.ancestors(ele)
    engine.lsib(ele)
    engine.rsib(ele)
    engine.lcin(ele)
    engine.rcin(ele)
    engine.siblings(ele)
    engine.descendants(ele,5,6)
    
    engine.layer(ele)
    engine.breadth(ele)
    engine.depth(ele)
    engine.pathlist(ele)

.. image:: ./images/engine.0.png


description matrix
^^^^^^^^^^^^^^^^^^

:: 
  
    html_str = fs.rfile("./test.html")
    root = LXHTML(html_str)
    wfs = engine.WFS(root)
    pobj(wfs.mat[3][1])
    
.. image:: ./images/engine.1.png


width-first-traverse
^^^^^^^^^^^^^^^^^^^^
::

    html_str = fs.rfile("./test.html")
    root = LXHTML(html_str)
    pls = engine.wfspls(root)
    utils.parr(pls[:10])

.. image:: ./images/engine.2.png


depth-first-traverse
^^^^^^^^^^^^^^^^^^^^

::

    import lxml.sax
    html_str = fs.rfile("./test.html")
    root = LXHTML(html_str)
    dfs = engine.DFS()
    lxml.sax.saxify(root, dfs)
    utils.parr(dfs.pls[:5])
    utils.parr(dfs.pls[-10:])

.. image:: ./images/engine.3.png


beautify
^^^^^^^^

::

    html_str = fs.rfile("./test.html")
    root = LXHTML(html_str)
    html_str = engine.beautify(root)
    print(html_str[:480])

.. image:: ./images/engine.4.png

`lvsrch <./modules.html#module-lvsrch>`_
-----------------------------------------

.. code-block:: console

    [
     'a',
     'abbr',
     'acronym',
     'address',
     'applet',
     'area',
     'arguments',
     'article',
     'aside',
     'audio',
     'b',
     'base',
     'basefont',
     'bdi',
     'bdo',
     'big',
     'blockquote',
     'body',
     'br',
     'button',
     'canvas',
     'caption',
     'center',
     'cite',
     'code',
     'col',
     'colgroup',
     'command',
     'datalist',
     'dd',
     'del_',
     'details',
     'dfn',
     'dialog',
     'dir',
     'div',
     'dl',
     'dt',
     'elel',
     'em',
     'embed',
     'engine',
     'fieldset',
     'figcaption',
     'figure',
     'font',
     'footer',
     'form',
     'frame',
     'frameset',
     'h1',
     'h2',
     'h3',
     'h4',
     'h5',
     'h6',
     'head',
     'header',
     'hr',
     'html',
     'i',
     'iframe',
     'img',
     'input',
     'ins',
     'isindex',
     'kbd',
     'keygen',
     'label',
     'legend',
     'li',
     'link',
     'map',
     'mark',
     'menu',
     'menuitem',
     'meta',
     'meter',
     'nav',
     'noframes',
     'noscript',
     'object',
     'ol',
     'optgroup',
     'option',
     'output',
     'p',
     'param',
     'pre',
     'progress',
     'q',
     'rp',
     'rt',
     'ruby',
     's',
     'samp',
     'script',
     'section',
     'select',
     'small',
     'source',
     'span',
     'srch',
     'strike',
     'strong',
     'style',
     'sub',
     'summary',
     'sup',
     'table',
     'tbody',
     'td',
     'textarea',
     'tfoot',
     'th',
     'thead',
     'time',
     'title',
     'tr',
     'track',
     'tt',
     'u',
     'ul',
     'utils',
     'var',
     'video',
     'wbr',
     'xmp'
    ]


`engine <./modules.html#module-nvhtml.engine>`_
-----------------------------------------------

.. code-block:: console

    [
     'BEAUTIFY',
     'ContentHandler',
     'DFS',
     'WFS',
     'ancestor',
     'ancestors',
     'beautify',
     'between_levels_cond_func',
     'breadth',
     'child',
     'children',
     'copy',
     'default_wfs_handler',
     'depth',
     'descendants',
     'descendants_pls',
     'dfs_traverse',
     'dfspls',
     'disconnect',
     'elel',
     'extract_pls',
     'following_sibs',
     'grand_parent',
     'html',
     'init_cls_wfs_arguments',
     'is_leaf',
     'layer',
     'layer_wfs_handler',
     'lcin',
     'leaf_descendants',
     'leaf_descendants_pls',
     'loc',
     'loc2node',
     'lsib',
     'lxe',
     'lxml',
     'nonleaf_descendants',
     'nonleaf_descendants_pls',
     'parent',
     'pathlist',
     'plget',
     'preceding_sibs',
     'rcin',
     're',
     'rootnode',
     'rsib',
     'samepl_breadth',
     'samepl_siblings',
     'samepl_sibseq',
     'siblings',
     'sibseq',
     'source',
     'text_intag',
     'txtize',
     'utils',
     'wfs_traverse',
     'wfspls',
     'xpath',
     'xpath_levels'
    ]


