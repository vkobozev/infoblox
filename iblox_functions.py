from pyinfoblox import InfobloxWAPI
import urllib3
from cred import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
infoblox = InfobloxWAPI(username=USERNAME,
                        password=PASSWORD,
                        wapi=WAPI)


def get_info_by_ref(ref):
    return infoblox.record_host.get(objref=ref)


def get_info_by_name(hostname):
    return infoblox.record_host.get(name=hostname)


def get_info_by_ip(ip):
    return infoblox.ipv4address.get(ip_address=ip)


def get_ref_by_ip(ip):
    info = infoblox.ipv4address.get(ip_address=ip)[0]['objects'][0]
    return info


def get_ref_by_name(hostname):
    return infoblox.record_host.get(name=hostname)[0]['_ref']


def get_ip_ref_by_ip(ip):
    info = infoblox.ipv4address.get(ip_address=ip)[0]["_ref"]
    return info


def show_next_available_ip(network, number):
    netw = infoblox.network.get(network=network)
    result = infoblox.network.function(objref=netw[0]['_ref'], _function='next_available_ip', num=number)
    return result['ips']


def delete_host_by_ref(ref):
    delete_host = infoblox.record_host.delete(objref=ref)
    return delete_host


def create_host_with_fixed_ip(name, ip):
    new_host = infoblox.record_host.create(name=name, ipv4addrs=[{'ipv4addr': ip}], configure_for_dns=False)
    return new_host


def update_name(ref, newname):
    updated_host = infoblox.record_host.update(objref=ref, name=newname)
    return updated_host


def check_used_ip(ip):
    status = infoblox.ipv4address.get(ip_address=ip)[0]["status"]
    return status


def check_first_ten(container):
    list_unused = []
    dc_net = infoblox.networkcontainer.get(network_container=container)
    for subnet_cont in dc_net:
        dc_subnet = infoblox.network.get(network_container=subnet_cont["network"])
        for subnet in dc_subnet:
            dc_ip = infoblox.ipv4address.get(network=subnet["network"], _max_results=2000)
            for ip in dc_ip:
                oct_4 = int(ip['ip_address'].split(".")[-1])
                if oct_4 in range(11) and ip['status'] == 'UNUSED':
                    list_unused.append(ip['ip_address'])
    return list_unused


def get_list_unused_ip():
    list_unused = []
    containers = ['10.32.0.0/13', '10.40.0.0/13']
    for container in containers:
        dc_net = infoblox.networkcontainer.get(network_container=container)
        for subnet_cont in dc_net:
            dc_subnet = infoblox.network.get(network_container=subnet_cont["network"])
            for subnet in dc_subnet:
                dc_ip = infoblox.ipv4address.get(network=subnet["network"], _max_results=2000)
                for ip in dc_ip:
                    if ip['status'] == 'UNUSED':
                        list_unused.append(ip['ip_address'])
    return list_unused


if __name__ == '__main__':
    with open('../cp/list_unused_ip_iblox', 'w+') as f:
        f.write(str(get_list_unused_ip()))
