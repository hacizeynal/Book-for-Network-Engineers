from jinja2 import Environment, FileSystemLoader
import yaml

directory_for_environment = Environment(loader=FileSystemLoader('templates'))
template = directory_for_environment.get_template('router_template.txt')

with open('routers_info.yml') as f:
    routers = yaml.safe_load(f)


for router in routers:
    r1_conf = router['name'] + '_r1.txt'
    with open(r1_conf, 'w') as f:
        f.write(template.render(router))

