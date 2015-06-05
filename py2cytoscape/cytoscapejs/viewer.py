import uuid
import json
import os

# ######## Default Values ###########

# Define default widget size
DEF_HEIGHT = 700
DEF_WIDTH = 1098 # Same as cell width of Jupyter

DEF_BACKGROUND_COLOR = '#FFFFFF'

HTML_TEMPLATE_FILE = 'template.html'
STYLE_FILE = 'default_style.json'

# Default network
DEF_NODES = [
    {'data': {'id': 'Network Data'}},
    {'data': {'id': 'Empty'}}
]

DEF_EDGES = [
    {'data': {'id': 'is', 'source': 'Network Data', 'target': 'Empty'}}
]

DEF_LAYOUT = 'preset'
DEF_STYLE = 'default'

PRESET_LAYOUTS = {
    'Preset': 'preset',
    'Circle': 'circle',
    'Concentric': 'concentric',
    'Breadthfirst': 'breadthfirst',
    'Spring': 'cose',
    'Grid': 'grid'
}


# Init styles
style_file = open(os.path.abspath(os.path.dirname(__file__)) + '/' + STYLE_FILE, 'r')
style_list = json.load(style_file)
styles = {}
for style in style_list:
    styles[style['title']] = style['style']


def render(network, style=DEF_STYLE, layout_algorithm=DEF_LAYOUT,
           background=DEF_BACKGROUND_COLOR, height=DEF_HEIGHT, width=DEF_WIDTH):
    from jinja2 import Template
    from IPython.core.display import display, HTML

    # Load style file if none available
    if style is None:
        style = styles['default2']
    elif isinstance(style, str):
        # Specified by name
        style = styles[style]

    if network is None:
        nodes = DEF_NODES
        edges = DEF_EDGES
    else:
        nodes = network['elements']['nodes']
        edges = network['elements']['edges']

    path = os.path.abspath(os.path.dirname(__file__)) + '/' + HTML_TEMPLATE_FILE
    template = Template(open(path).read())
    cyjs_widget = template.render(nodes=json.dumps(nodes), edges=json.dumps(edges), background=background,
                                  uuid="cy" + str(uuid.uuid4()), widget_width=str(width), widget_height=str(height),
                                  layout=layout_algorithm, style_json=json.dumps(style))

    return display(HTML(cyjs_widget))


# List of available layout algorithms
def get_layouts():
    return PRESET_LAYOUTS


def embed_share(url, width=DEF_WIDTH, height=DEF_HEIGHT):
    from IPython.core.display import display
    from IPython.lib.display import IFrame

    return display(IFrame(url, width, height))