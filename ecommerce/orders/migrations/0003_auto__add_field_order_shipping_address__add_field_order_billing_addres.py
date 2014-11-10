# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.shipping_address'
        db.add_column(u'orders_order', 'shipping_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='shipping_address', to=orm['accounts.UserAddress']),
                      keep_default=False)

        # Adding field 'Order.billing_address'
        db.add_column(u'orders_order', 'billing_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='billing_address', to=orm['accounts.UserAddress']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.shipping_address'
        db.delete_column(u'orders_order', 'shipping_address_id')

        # Deleting field 'Order.billing_address'
        db.delete_column(u'orders_order', 'billing_address_id')


    models = {
        u'accounts.useraddress': {
            'Meta': {'ordering': "['-updated', '-timestamp']", 'object_name': 'UserAddress'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'billing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'shipping': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'carts.cart': {
            'Meta': {'object_name': 'Cart'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '100', 'decimal_places': '2'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'orders.order': {
            'Meta': {'object_name': 'Order'},
            'billing_address': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'billing_address'", 'to': u"orm['accounts.UserAddress']"}),
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carts.Cart']"}),
            'final_total': ('django.db.models.fields.DecimalField', [], {'default': '10.99', 'max_digits': '1000', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'shipping_address': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'shipping_address'", 'to': u"orm['accounts.UserAddress']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Started'", 'max_length': '120'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '10.99', 'max_digits': '1000', 'decimal_places': '2'}),
            'tax_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '1000', 'decimal_places': '2'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']