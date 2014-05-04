# -*- coding: utf8 -*-
#
# Copyright (C) 2005 Matthew Good <trac@matt-good.net>
#
# "THE BEER-WARE LICENSE" (Revision 42):
# <trac@matt-good.net> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Matthew Good
#
# Author: Matthew Good <trac@matt-good.net>

from urllib2 import build_opener, HTTPBasicAuthHandler, \
                    HTTPDigestAuthHandler, HTTPPasswordMgrWithDefaultRealm

from trac.core import Component, implements
from trac.config import Option

from acct_mgr.api import IPasswordStore, _, N_


class HttpAuthStore(Component):
    implements(IPasswordStore)

    auth_url = Option('account-manager', 'authentication_url', '',
        doc = N_("URL of the HTTP authentication service"))

    def check_password(self, user, password):
        acctmgr = HTTPPasswordMgrWithDefaultRealm()
        acctmgr.add_password(None, self.auth_url, user, password)
        try:
            build_opener(HTTPBasicAuthHandler(acctmgr),
                         HTTPDigestAuthHandler(acctmgr)).open(self.auth_url)
        except IOError:
            return None
        except ValueError:
            return None
        else:
            return True

    def get_users(self):
        return []

    def has_user(self, user):
        return False

