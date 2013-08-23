#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#

import boto
import boto.rds

from base import *

log = logging.getLogger(__name__)

def scan(region='us-east-1'):
    running_dbs = {}
    conn = boto.rds.connect_to_region(region)
    dbinstances = conn.get_all_dbinstances()
    for db in dbinstances:
        running_dbs[db.id] = ( db.endpoint[0], db.master_username,
            'test', db.instance_class,
            db.allocated_storage, db.AutoMinorVersionUpgrade,
            db.multi_az, db.availability_zone,
            db.preferred_backup_window,db.preferred_maintenance_window)
    return running_dbs

def main():
    '''
    '''
    running_dbs = scan()
    for db in running_dbs:
        value = running_dbs[db]
        obj, created = mysqladmin.models.DbRds.objects.get_or_create(endpoint=value[0],
            defaults = { 'master_user': value[1],
                    'master_password': value[2], 'instance_class': value[3],
                    'storage': value[4], 'minor_update': value[5],
                    'multi_az': value[6], 'zone': value[7],
                    'backup_window': value[8], 'maintenance_window': value[9]})
        if created:
            log.info("Created new {0} :\n {1}".format(db, value))



if __name__ == '__main__':
    main()


