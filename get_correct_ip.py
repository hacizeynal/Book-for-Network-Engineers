from check_ip_function import check_ip

ip_address_full_list = [ '8.8.8.8', '1.8.8.8', '2.2.2' ]


def return_correct_ip(ip_address):
    correct_ip_address_list = [ ]
    for ip in ip_address:
        if check_ip(ip) is True:
            correct_ip_address_list.append(ip)
    return correct_ip_address_list


# def return_correct_ip(ip_address):
#     return [ ip for ip in ip_address_full_list if check_ip(ip) ]

print('Checking list of valid IP addresses from provided list')
correct_result = return_correct_ip(ip_address_full_list)
print(correct_result)
