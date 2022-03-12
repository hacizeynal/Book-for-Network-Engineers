import yaml


def generate_config(template, input):
    return None


if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
        print(data)
    print(generate_config(template_file, data))
