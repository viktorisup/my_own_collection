#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: creates a file in your fs

version_added: "1.0.0"

description: This module creates a file in your file system.

options:
    path:
        description: Path to new file.
        required: true
        type: str
    content:
        description: New file content.
        required: true
        type: str

author:
    - Viktor Isupov (@viktorisup)
'''

EXAMPLES = r'''
# Create file
- name: Create file with content
  create_file:
    path: "/tmp/my_file_name.txt"
    content: "My file content"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
    description: The output message that the module generates.
    type: str
    returned: always
    sample: 'File /tmp/my_file_name.txt was created successfully!'
'''

from ansible.module_utils.basic import AnsibleModule

import os

def run_module():
    module_args = {
        "path": {"type": "str", "required": True},
        "content": {"type": "str", "required": True},
    }
    result = {}

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )    

    if module.check_mode:
        module.exit_json(**result)

    my_path = module.params["path"]
    my_content = module.params["content"]

    if os.path.isfile(my_path):
        with open(my_path, "r") as read_file:
            existing_content = read_file.read()
            if my_content == existing_content:
                result["msg"] = "A file with this content already exists. Creation is not required."
                module.exit_json(**result)

    try:
        with open(my_path, "w") as write_file:
            write_file.write(my_content)
            result["msg"] = "File content updated."
    except IOError as e:
        result["msg"] = f"Error writing to file: {e}"
        module.fail_json(**result)
    
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()