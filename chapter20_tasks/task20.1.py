"""
Task 20.1
Create generate_config function.
Function parameters:
* template - path to the template file (for example, "templates/for.txt")
* data_dict - a dictionary with values to be substituted into the template
The function should return the generated configuration string.
Check the operation of the function on the templates/for.txt template
and data from the data_files/for.yml file.
"""

import yaml
from jinja2 import Environment, FileSystemLoader
import os


def generate_config(template, input_dict):
    template_directory, main_template = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(template_directory),
        trim_blocks=True,
        lstrip_blocks=True)
    final_config = env.get_template(main_template)
    return final_config.render(input_dict)


if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
