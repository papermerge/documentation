# Ansible

Ansible playbook is available at [papermerge/ansible](https://github.com/papermerge/ansible).

Playbook will install web app, one worker, database, Redis and Solr search
engine on target host. All services will be started via docker containers.

Inventory file is not provided in the repository, you will need
to create one. Here is an example of inventory file:

```
192.168.56.99 secret_key=abc superuser_password=1234 superuser_username=eugen database_url="postgresql://scott:tiger@db/mydatabase"  db_pass=tiger
```

Playbook was tested in vagrant environment, with Ubuntu 22.04 as target host.
Ansible config file is not in repository, you need to create one.
Here is an example of Ansible config file:

```
[defaults]
inventory = inventory
host_key_checking = False
deprication_warnings = False
remote_user = vagrant
private_key_file = .vagrant/machines/default/virtualbox/private_key
```

All other variables, with their defaults are in ``group_vars/all`` file.


## Install

To install {{ extra.project }}, simply run ``install.yml`` playbook:

```
ansible-playbook -i inventory install.yml
```

After installation is complete, the application will be available at:

```
http://<target-host>:<web_app_port>
```

``web_app_port`` variable is in ``group_vars/all`` file.
The ``web_app_port`` default value is 9400.


## Backup

On the target host, folder ``/backup`` is mounted to web_app's container folder ``/backup``.

In order to create a backup, run following playbook:

```
ansible-playbook -i inventory backup.yml
```

Above command will create backup file in  ``/backup/`` in web app's folder, but
because that folder is mounted by default to target VM host, you will see
backup archive available in ``/backup/`` folder of host VM as well.


## Restore

To restore a backup, run following playbook:

```
ansible-playbook restore.yml --extra-vars "backup_file=/backup/backup_20_11_2023-07_33_03.tar.gz"
```

File path is one from web app's docker container.


## Contribute

As mentioned above, currently playbook assumes only Ubuntu 22.04 host.
We are happy to accept your pull requests for other hosts.

Ansible playbook repository is available at [papermerge/ansible](https://github.com/papermerge/ansible).
