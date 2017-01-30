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
    Execute(params.script_path + ' stop rest --port ' + str(params.rest_port) + ' --infoport ' + str(params.info_port))

  def start(self, env):
    import params
    Execute(params.script_path + ' start rest --port ' + str(params.rest_port) + ' --infoport ' + str(params.info_port))

  def restart(self, env):
    import params
    Execute(params.script_path + ' restart rest --port ' + str(params.rest_port) + ' --infoport ' + str(params.info_port))

  def status(self, env):
    import params
    check_process_status(params.pid_dir + '/hbase--rest.pid')

if __name__ == "__main__":
  Client().execute()
