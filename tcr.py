
# -*- coding: utf-8 -*-

import Aan
from Aan.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = Aan.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
