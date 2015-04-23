import sys, os
from resource_management import *

class Client(Script):
  def install(self, env):
    import params
    self.configure(env)

  def configure(self, env):
    import params
    env.set_params(params)

  def stop(self, env):
    import params
    Execute(params.script_path + ' stop rest --infoport ' + str(params.rest_port))

  def start(self, env):
    import params
    Execute(params.script_path + ' start rest --infoport ' + str(params.rest_port))

  def restart(self, env):
    import params
    Execute(params.script_path + ' restart rest --infoport ' + str(params.rest_port))

  def status(self, env):
    import params
    check_process_status(params.pid_dir + '/hbase-" + params.hbase_user + '-rest.pid')

if __name__ == "__main__":
  Client().execute()
