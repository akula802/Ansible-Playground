## Resources for initial setup on managed nodes

These resources I use in my lab to configure new nodes as they come online.


### Requirements

* The 'ansible_managed' parameter must be set in ansible.cfg in order for the templates to include the desired comment or information.
* The 'create-remote-mgmt-user' playbook requires the ansible.posix collection.
