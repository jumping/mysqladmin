#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
#import logging

import boto
import boto.ec2

from base import *

import logging

log = logging.getLogger(__name__)

def scan(region):
    '''
    '''
    running_instances = {}
    try:
        region_name = region.name
    except:
        region_name = region
    conn = boto.ec2.connect_to_region(region_name)
    reservations = conn.get_all_instances()
    for reservation in reservations:
        for instance in reservation.instances:
            instance_id = instance.id
            if not instance.key_name:
                log.warning("%s key_name is empty. " % instance_id)
                key_name = 'MissingKey'
            else:
                key_name = instance.key_name
            running_instances[instance_id] = ( instance.instance_type, instance.ip_address,
                    instance.private_ip_address, instance.public_dns_name,
                    instance.private_dns_name, instance.region.name,
                    instance.placement, key_name,
                    instance.dns_name, instance.tags,
                    ';'.join([x.name for x in instance.groups]),
                    instance.state, instance.launch_time,
                    instance.monitored, instance.image_id,
                    instance.architecture, instance.persistent,
                    instance.ramdisk, instance.kernel
                    )

    return running_instances

def main():
    '''
    '''
    regions = boto.ec2.regions()
    for region in regions:
        running_instances = scan(region)
        if not running_instances:
            continue
        for instance in running_instances:
            value = running_instances[instance]
            obj,created = mysqladmin.models.InstanceInfo.objects.get_or_create(instance_id=instance,
                defaults = {'instance_type':value[0],
                'ip_address':value[1], 'private_ip_address':value[2],
                'public_dns_name':value[3],'private_dns_name':value[4],
                'region':value[5],'zone':value[6],'key_name':value[7],
                'dns_name':value[8],'tags':value[9],'groups':value[10],
                'state':value[11],'launch_time':value[12],
                'monitored':value[13],'image_id':value[14],
                'architecture':value[15],'persistent':value[16],
                'ramdisk':value[17],'kernel':value[18]})
            if created:
                log.info("Created new {0} :\n {1}".format(instance, value))

            #save history
            history = mysqladmin.models.InstanceHistory()
            history.status = value[11]
            instance_info_id = mysqladmin.models.InstanceInfo.objects.get(id=obj.id)
            history.instance_info_id = instance_info_id
            history.save()


if __name__ == '__main__':
    log.info('Starting')
    main()
    log.info('End')


