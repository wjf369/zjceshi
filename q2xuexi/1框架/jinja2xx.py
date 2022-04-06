# from jinja2 import Template
# template = Template('Hello {{ name }}!')
# print (template.render(name='World'))

from jinja2 import Environment
from jinja2 import FileSystemLoader

env = Environment(loader=PackageLoader('/path/to/templates', 'utf-8'))
template = env.get_template('mytemplate.html')
template.render(the='variables', go='here')