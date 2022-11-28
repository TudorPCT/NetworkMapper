def bin_to_int(num):
    result = 0
    for i in range(len(num)):
        result += int(num[-(i+1)]) * pow(2, i)
    return result


def build_ip(prefix, suffix):
    ip_bin = prefix + suffix
    ip = ".".join([str(bin_to_int(ip_bin[i:(i + 8)])) for i in range(0, 32, 8)])
    return ip


def convert_cidr(cidr):
    addr, bits = cidr.split('/')
    bits = int(bits)

    binary_addr = "".join(['{0:08b}'.format(int(num)) for num in addr.split('.')])

    addr_prefix = binary_addr[:bits]

    first_addr_suffix = bin_to_int(''.join(['0' for _ in range(32 - bits)]))
    last_addr_suffix = bin_to_int(''.join(['1' for _ in range(32 - bits)]))

    ip_list = []
    for i in range(first_addr_suffix, last_addr_suffix+1):
        ip_list.append(build_ip(addr_prefix, bin(i)[2:]))

    return ip_list
