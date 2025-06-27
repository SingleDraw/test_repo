#!/usr/bin/env python3

import os
import json
import sys
from dotenv import load_dotenv
load_dotenv('/ansible/.host.env')

mimi_host =  os.getenv('mimi_HOST', '')
mimi_user =  os.getenv('mimi_USER', '')
mimi_port = int(os.getenv('mimi_PORT', 22))
mimi_password = os.getenv('mimi_PASS', '')

def get_inventory():
    """
    Return dynamic inventory data
    """
    inventory = {
        # Define groups and their hosts
        'vps': {
            'hosts': ['mimi'],
            'vars': {}
        },
        # Meta information
        '_meta': {
            'hostvars': {
                'mimi': {
                    'ansible_host':  mimi_host,
                    'ansible_user': mimi_user,
                    'ansible_port': mimi_port,
                    'ansible_ssh_pass': mimi_password
                }
            }
        }
    }
    return inventory

def get_host_vars(host):
    """
    Return variables for a specific host
    """
    inventory = get_inventory()
    return inventory['_meta']['hostvars'].get(host, {})

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        # Return all inventory data
        print(json.dumps(get_inventory(), indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        # Return host-specific variables
        print(json.dumps(get_host_vars(sys.argv[2]), indent=2))
    else:
        print("Usage: {} --list | --host <hostname>".format(sys.argv[0]))
        sys.exit(1)