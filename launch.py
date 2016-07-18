"""Openstack with remote databases

Usage:
    launch.py reservation [--site <city>]
    launch.py reservation [--duration <time>]
    launch.py reservation [--nodes <nb>]
    launch.py reservation [--cluster]
    launch.py reservation --only
    launch.py run --conf <file> [(--job_id <id> --job_site <city>)(--full | -i <impl>)]
    launch.py (-h | --help)
    launch.py --version

Options:
    -h --help          Show this screen
    --version          Show version
    --site <city>      Choose the site [default: rennes]
    --duration <time>  A duration, formatted hh:mm:ss, must be <= to [default: 03:00:00]
    --nodes <nb>       Number of nodes [default: 2]
    --full             Run tests for both implementation
    -i <impl>          Choose implementation (disco or mysql)
    --conf <file>      Configuration file
    --job_id <id>      Specify the job id of an already created job
    --job_site <city>  Specify the job site of an already created job

"""

import os, sys
import time
import traceback
import pandas as pd
from docopt import docopt
import execo as ex
import execo_g5k as ex5
from execo_g5k import oar
from execo_engine import logger
import json

class launch():
    
    def __init__(self):
        """Define options for the experiment"""
        self.argus = docopt(__doc__, version = 'Deployments 1.0')
        print(self.argus)
        if not self.argus['reservation']:
            try:
                with open(self.argus['--conf']) as config_file:
                    self.config = json.load(config_file)
                    print(self.config)

            except Exception as e:
                t, value, tb = sys.exc_info()
                print str(t) + " " + str(value)
                traceback.print_tb(tb)
                print("Config file not working")

                
    def run(self):

        #connect to g5k





if __name__ == "__main__":
    engine = launch()
    engine.run()
