"""
Task 20.2
Create template templates/cisco_router_base.txt.
The templates/cisco_router_base.txt template should include the content of the templates:
* templates/cisco_base.txt
* templates/alias.txt
* templates/eem_int_desc.txt
Template text cannot be copied.
Test the template templates/cisco_router_base.txt using the generate_config
function from task 20.1. Do not copy the code of the generate_config function.
As data, use the information from the data_files/router_info.yml file.
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
    data_file = "data_files/router_info.yml"
    template_file = "templates/cisco_router_base.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))

