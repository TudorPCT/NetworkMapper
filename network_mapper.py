import re
import sys
import socket
from cidr import convert_cidr


def default_ip_list():
    f = open("common_ports.txt")
    file_content = f.read()
    ports = {int(port.split("-")[0]): port.split("-")[1] for port in re.findall(r"(\d+-\w+)", file_content)}
    return ports


def network_mapper(cidr_class, port_list=None):
    ip_list = convert_cidr(cidr_class)
    port_dict = default_ip_list()
    port_list = port_dict.keys() if port_list is None else port_list
    port_regex = re.compile("^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|"
                            "(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$")
    for ip in ip_list:
        for index, port in enumerate(port_list):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if port_regex.match(str(port)) and s.connect_ex((ip, port)) == 0:
                output = "{}:{}({})".format(ip, port, port_dict[port]) if port in port_dict.keys() \
                   else "{}:{}".format(ip, port) if index == 0 else str(port).ljust(len(ip))
                print(output)
            s.close()


def is_cidr_ip_class(cidr_ip_class):
    return re.match(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}"
        r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
        r"(/(3[0-2]|[1-2][0-9]|[0-9]))$",
        cidr_ip_class)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("[Error] - invalid number of arguments")
        sys.exit(0)
    elif not is_cidr_ip_class(sys.argv[1]):
        print("[Error] - invalid cidr ip class")
        sys.exit(0)

    if len(sys.argv) == 2:
        network_mapper(sys.argv[1])
    elif len(sys.argv) > 2:
        network_mapper(sys.argv[1], sys.argv[2:])
