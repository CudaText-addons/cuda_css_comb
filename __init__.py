import sys
import os
import json
from cudatext import *
from . import format_proc
from .node_proc import *

format_proc.INI = 'cuda_css_comb.json'
format_proc.MSG = '[CSScomb] '

tool_js = os.path.join(os.path.dirname(__file__), 'csscomb.js')

def get_syntax():
    lexer = ed.get_prop(PROP_LEXER_FILE)
    syntax = 'scss' if lexer=='SCSS' else 'less' if lexer=='LESS' else 'css'
    return syntax
    
def get_config():
    fn = format_proc.ini_filename()
    text = open(fn).read()
    j = json.loads(text)
    return json.dumps(j)

def do_format(text):
    return run_node(text, [tool_js, get_syntax(), get_config()]) 


class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        try:
            format_proc.run(do_format)
        except Exception as e:
            msg_box('Error while running Node.js \n'+str(e), MB_OK+MB_ICONERROR)
