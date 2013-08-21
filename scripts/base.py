#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
import os
import sys
import logging

sys.path.append(os.path.join(os.getcwd(),'../'))

from django.core.management import setup_environ
import bpo.settings
setup_environ(bpo.settings);

import mysqladmin.models

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log = logging.basicConfig(format=formatter,level='INFO')
