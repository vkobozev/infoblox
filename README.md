Here you can find some usefull functions which help you to operate with Infoblox IPAM system.

cred.py - put here your credentials and url of the system
iblox_logging.py - here I put logging configuration


Here are some examples.


In [1]: import iblox_functions as i

In [2]: i.get_info_by_ip("172.20.20.220")
Out[2]: 
[{'_ref': 'ipv4address/Li5pcHY0X2FkZHJlc3MkMTcyLjIwLjIwLjIyMC8w:172.20.20.220',
  'ip_address': '172.20.20.220',
  'is_conflict': False,
  'mac_address': '',
  'names': [],
  'network': '172.20.20.0/24',
  'network_view': 'default',
  'objects': [],
  'status': 'UNUSED',
  'types': [],
  'usage': []}]

In [4]: i.create_host_with_fixed_ip("vkobozev-test","172.20.20.220")
Out[4]: 'record:host/ZG5zLmhvc3QkLm5vbl9ETlNfaG9zdF9yb290LjAuMTUyNzY3NjQ1MzEyNy52a29ib3pldi10ZXN0:vkobozev-test/%20'

In [5]: i.get_info_by_ref('record:host/ZG5zLmhvc3QkLm5vbl9ETlNfaG9zdF9yb290LjAuMTUyNzY3NjQ1MzEyNy52a29ib3pldi10ZXN0:vkobozev-test/%20')
Out[5]: 
{'_ref': 'record:host/ZG5zLmhvc3QkLm5vbl9ETlNfaG9zdF9yb290LjAuMTUyNzY3NjQ1MzEyNy52a29ib3pldi10ZXN0:vkobozev-test/%20',
 'ipv4addrs': [{'_ref': 'record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQubm9uX0ROU19ob3N0X3Jvb3QuMC4xNTI3Njc2NDUzMTI3LnZrb2JvemV2LXRlc3QuMTcyLjIwLjIwLjIyMC4:172.20.20.220/vkobozev-test/%20',
   'configure_for_dhcp': False,
   'host': 'vkobozev-test',
   'ipv4addr': '172.20.20.220'}],
 'name': 'vkobozev-test',
 'view': ' '}

In [6]: i.delete_host_by_ref('record:host/ZG5zLmhvc3QkLm5vbl9ETlNfaG9zdF9yb290LjAuMTUyNzY3NjQ1MzEyNy52a29ib3pldi10ZXN0:vkobozev-test/%20')
Out[6]: 'record:host/ZG5zLmhvc3QkLm5vbl9ETlNfaG9zdF9yb290LjAuMTUyNzY3NjQ1MzEyNy52a29ib3pldi10ZXN0:vkobozev-test/%20'

In [7]: i.get_info_by_ip("172.20.20.220")
Out[7]: 
[{'_ref': 'ipv4address/Li5pcHY0X2FkZHJlc3MkMTcyLjIwLjIwLjIyMC8w:172.20.20.220',
  'ip_address': '172.20.20.220',
  'is_conflict': False,
  'mac_address': '',
  'names': [],
  'network': '172.20.20.0/24',
  'network_view': 'default',
  'objects': [],
  'status': 'UNUSED',
  'types': [],
  'usage': []}]
