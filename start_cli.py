from argh import dispatch_commands
from argh.decorators import named, arg
import imp
import subprocess
import json
from geobricks_rest_engine.config.common_settings import settings as common_settings
from geobricks_rest_engine.config.rest_settings import settings as rest_settings
from geobricks_rest_engine.core.utils import dict_merge


@named('corr')
@arg('--common_settings', help='Common Settings file')
@arg('--rest_settings',help='Rest Settings file')
@arg('--processes', help='Processes')
def start_engine(**kwargs):
    settings_app = imp.load_source('geobricks_common_settings', kwargs['common_settings'])
    settings_rest_modules = imp.load_source('geobricks_rest_settings', kwargs['rest_settings'])

    # write files
    with open('/geobricks/config/common_settings.py', 'w') as f:
        f.write(json.dumps(common_settings))

    with open('/geobricks/config/rest_settings.py', 'w') as f:
        f.write(json.dumps(rest_settings))

    # run script

    subprocess.call(["sh", "/geobricks/script.sh"])

    # run engine
    #rest_engine.run_engine(False)

    # run uwsgi
    #from geobricks_rest_engine.rest.engine import app
    #subprocess.call(["env/bin/uwsgi", "--socket", "127.0.0.1:21000", "-w", app])
    # env/bin/uwsgi --socket 127.0.0.1:21000 -w WSGI:app -p 2




def main():
    dispatch_commands([start_engine])

if __name__ == '__main__':
    main()