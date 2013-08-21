#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
import os
import sys
sys.path.append(os.path.join(os.getcwd(),'../'))

from django.core.management import setup_environ
import bpo.settings
setup_environ(bpo.settings);

import mysqladmin.models
