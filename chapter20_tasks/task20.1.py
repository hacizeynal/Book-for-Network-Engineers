import yaml
from jinja2 import Environment, FileSystemLoader
import os


def generate_config(template, input_dict):
    template_directory, template_itself = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(template_directory),
        trim_blocks=True,
        lstrip_blocks=True)
    k = env.get_template(template_itself)
    return k.render(input_dict)


if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
