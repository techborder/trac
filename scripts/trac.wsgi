import os

os.environ['TRAC_ENV_PARENT_DIR'] = '/opt/bitnami/apps/trac/trac_projects'

import trac.web.main
application = trac.web.main.dispatch_request

