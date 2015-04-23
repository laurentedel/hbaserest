#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

config = Script.get_config()

script_path = config['configurations']['hbaserest-config']['hbase.rest.path']
rest_port = config['configurations']['hbaserest-config']['hbase.rest.port']
#pid_dir = config['configurations']['hbase-env']['hbase_pid_dir']
pid_dir = config['configurations']['hbaserest-config']['hbase.pid.dir']
#hbase_user = config['configurations']['hbase-env']['hbase_user']
hbase_user = config['configurations']['hbaserest-config']['hbase.user']
