import re


def parse_sh_version(sh_ver_output):
    regex = (
        "Cisco IOS .*? Version (?P<ios>\S+), .*"
        "uptime is (?P<uptime>[\w, ]+)\n.*"
        'image file is "(?P<image>\S+)".*'
    )
    match = re.search(regex, sh_ver_output, re.DOTALL, )
    if match:
        return match.group("ios", "image", "uptime")


print(parse_sh_version("show_version_r3.txt"))
