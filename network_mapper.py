import re
import sys
from cidr import convert_cidr


def default_ip_list():
    f = open("common_ports.txt")
    file_content = f.read()
    ports = {int(port.split("-")[0]): port.split("-")[1] for port in re.findall("(\d+-{1}\w+)", file_content)}
    return ports


def network_mapper(cidr_class, port_list=None):
    ip_list = convert_cidr(cidr_class)
    port_list = default_ip_list() if port_list is None else port_list
    print(ip_list)
    print(port_list)


def is_cidr_ip_class(cidr_ip_class):
    return re.match(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}"
        r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
        r"(\/(3[0-2]|[1-2][0-9]|[0-9]))$",
        cidr_ip_class)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("[Error] - invalid number of arguments")
        sys.exit(0)
    elif not is_cidr_ip_class(sys.argv[1]):
        print("[Error] - invalid cidr class")
        sys.exit(0)

    if len(sys.argv) == 2:
        network_mapper(sys.argv[1])
    elif len(sys.argv) > 2:
        network_mapper(sys.argv[1], sys.argv[2:])
