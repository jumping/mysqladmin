# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class DbHost(models.Model):
    id = models.AutoField(primary_key=True)
    dbname = models.CharField(max_length=45L)
    db_instance = models.ForeignKey('DbInstance', null=True, blank=True)
    db_rds = models.ForeignKey('DbRds', null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        db_table = 't_db_host'
    def __unicode__(self):
        return u'%s  %s   %s' %(self.dbname, self.db_instance, self.db_rds)

class DbInstance(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    instance_id = models.CharField(max_length=45L, unique=True)
    master_user = models.CharField(max_length=45L)
    master_password = models.CharField(max_length=45L)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        db_table = 't_db_instance'

class DbRds(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    endpoint = models.CharField(max_length=100L, unique=True)
    master_user = models.CharField(max_length=45L)
    master_password = models.CharField(max_length=45L)
    instance_class = models.CharField(max_length=45L)
    storage = models.IntegerField()
    minor_update = models.BooleanField()
    multi_az = models.BooleanField()
    zone = models.CharField(max_length=45L)
    backup_window = models.CharField(max_length=255L)
    maintenance_window = models.CharField(max_length=255L)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        db_table = 't_db_rds'

class InstanceHistory(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=45L)
    instance_info = models.ForeignKey('InstanceInfo')
    update_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        db_table = 't_instance_history'

class InstanceInfo(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    instance_id = models.CharField(max_length=45L, unique=True)
    instance_type = models.CharField(max_length=45L)
    ip_address = models.CharField(max_length=45L, null=True,blank=True)
    private_ip_address = models.CharField(max_length=45L, null=True, blank=True)
    public_dns_name = models.CharField(max_length=255L,null=True, blank=True)
    private_dns_name = models.CharField(max_length=255L,null=True, blank=True)
    region = models.CharField(max_length=45L)
    zone = models.CharField(max_length=45L)
    key_name = models.CharField(max_length=45L)
    dns_name = models.CharField(max_length=255L, blank=True)
    tags = models.CharField(max_length=255L, blank=True)
    groups = models.CharField(max_length=255L, blank=True)
    state = models.CharField(max_length=45L, blank=True)
    launch_time = models.DateTimeField()
    monitored = models.BooleanField()
    image_id = models.CharField(max_length=45L)
    architecture = models.CharField(max_length=45L)
    persistent = models.BooleanField()
    ramdisk = models.CharField(max_length=45L, null=True)
    kernel = models.CharField(max_length=45L, null=True)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        db_table = 't_instance_info'
    def __unicode__(self):
        return u'%s  %s   %s   %s' %(self.instance_id, self.instance_type, self.state, self.tags)

class UserDb(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserInfo')
    db = models.ForeignKey(DbHost)
    source_ip = models.CharField(max_length=45L)
    permission = models.CharField(max_length=45L)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        db_table = 't_user_db'

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45L)
    password = models.CharField(max_length=45L, blank=True)
    email = models.CharField(max_length=45L, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        db_table = 't_user_info'

