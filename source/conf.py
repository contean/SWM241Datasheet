# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SWM241数据手册'
copyright = '2023, synwit'
author = 'synwit'
release = 'v1.0'



master_doc = 'index'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinxcontrib.excel_table']

templates_path = ['_templates']
exclude_patterns = []

language = '**zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['.']
html_use_index = True
html_show_sphinx = True
html_static_path = ['_static']

html_logo = '_static/logo.ico'


# Output file base name for HTML help builder.
 
latex_engine = 'xelatex'
# -- Options for LaTeX output ------------------------------------------------
 
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{xeCJK}
\setCJKmainfont[BoldFont=STZhongsong, ItalicFont=STKaiti]{STSong}
\setCJKsansfont[BoldFont=STHeiti]{STXihei}
\setCJKmonofont{STFangsong}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
\parindent 2em
\definecolor{VerbatimColor}{rgb}{0.95,0.95,0.95}
\setcounter{tocdepth}{3}
\renewcommand\familydefault{\ttdefault}
\renewcommand\CJKfamilydefault{\CJKrmdefault}
'''
}
 
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'SWM241.tex', 'PYTHON Documentation',
     'xxxx', 'manual'),
]
 
 
