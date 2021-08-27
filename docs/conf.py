# Arquivo de configuração para o construtor de documentação Sphinx.
#
# Este arquivo contém apenas uma seleção das opções mais comuns. Por um completo
# lista veja a documentação:
# http://www.sphinx-doc.org/en/master/config

# -- Configuração de caminho --------------------------------------------------------------

# Se as extensões (ou módulos para documentar com autodoc) estiverem em outro diretório, 
# adicione esses diretórios a sys.path aqui. Se o diretório for relativo à raiz da documentação, 
# use os.path.abspath para torná-lo absoluto, como mostrado aqui.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
version = '1.0.1'

source_suffix = '.rst'
master_doc = 'index'

html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('overrides.css')  # também pode ser um URL

html_context = {
	"display_github": False, # Adicione o link Editar no Github 'em vez de' Ver o código-fonte da página
	"last_updated": True,
	"commit": False,
     }

# -- Informações do Projeto -----------------------------------------------------

project = 'Download de imagens do Google'
copyright = 'Github'
author = 'Github'


# -- Configuração geral ---------------------------------------------------

# Adicione quaisquer nomes de módulo de extensão Sphinx aqui, como strings. 
# Eles podem ser extensões que vêm com o Sphinx (chamadas 'sphinx.ext. *') 
# Ou seus personalizados.
extensions = [
]

# Adicione quaisquer caminhos que contenham modelos aqui, relativos a este diretório.
templates_path = ['_templates']

# Lista de padrões, em relação ao diretório de origem, que correspondem a arquivos 
# e diretórios a serem ignorados ao procurar por arquivos de origem.
# Este padrão também afeta html_static_path e html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Opções para saída HTML -------------------------------------------------

# O tema a ser usado para páginas de ajuda em HTML e HTML. 
# Consulte a documentação para obter uma lista de temas integrados.
#
html_theme = 'bizstyle'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'searchbox.html'] }

