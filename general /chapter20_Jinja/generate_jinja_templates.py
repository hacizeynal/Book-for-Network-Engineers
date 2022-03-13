from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

# python generate_jinja_templates.py templates/for.txt data_files/for.yml

template_directory, template_file = os.path.split(sys.argv [ 1 ])
# assigned to template and templates will be assigned to template_dir

vars_file = sys.argv [ 2 ]  # means third element in list
print(vars_file)

env = Environment(
    loader=FileSystemLoader(template_directory),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template(template_file)
with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)
    print(vars_dict)

print(template.render(vars_dict))  # render will take * args or **kwargs as argument
