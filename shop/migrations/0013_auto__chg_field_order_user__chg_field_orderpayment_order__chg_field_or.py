# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Order.user'
        db.alter_column(u'shop_order', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['login_with_email.User'], null=True))

        # Changing field 'OrderPayment.order'
        db.alter_column(u'shop_orderpayment', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ex_shop.Order']))

        # Changing field 'OrderExtraInfo.order'
        db.alter_column(u'shop_orderextrainfo', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ex_shop.Order']))

        # Changing field 'ExtraOrderPriceField.order'
        db.alter_column(u'shop_extraorderpricefield', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ex_shop.Order']))

        # Changing field 'OrderItem.order'
        db.alter_column(u'shop_orderitem', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ex_shop.Order']))

        # Changing field 'Product.slug'
        db.alter_column(u'shop_product', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

        # Changing field 'Cart.user'
        db.alter_column(u'shop_cart', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['login_with_email.User'], unique=True, null=True))

    def backwards(self, orm):

        # Changing field 'Order.user'
        db.alter_column(u'shop_order', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'OrderPayment.order'
        db.alter_column(u'shop_orderpayment', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Order']))

        # Changing field 'OrderExtraInfo.order'
        db.alter_column(u'shop_orderextrainfo', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Order']))

        # Changing field 'ExtraOrderPriceField.order'
        db.alter_column(u'shop_extraorderpricefield', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Order']))

        # Changing field 'OrderItem.order'
        db.alter_column(u'shop_orderitem', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Order']))

        # Changing field 'Product.slug'
        db.alter_column(u'shop_product', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True))

        # Changing field 'Cart.user'
        db.alter_column(u'shop_cart', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True))

    models = {
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ex_shop.order': {
            'Meta': {'object_name': 'Order', '_ormbases': ['shop.Order']},
            'billing_method': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'order_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Order']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'login_with_email.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'shop.cart': {
            'Meta': {'object_name': 'Cart'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['login_with_email.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'shop.cartitem': {
            'Meta': {'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['shop.Cart']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'shop.extraorderitempricefield': {
            'Meta': {'object_name': 'ExtraOrderItemPriceField'},
            'data': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.OrderItem']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        },
        'shop.extraorderpricefield': {
            'Meta': {'object_name': 'ExtraOrderPriceField'},
            'data': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_shipping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ex_shop.Order']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        },
        'shop.order': {
            'Meta': {'object_name': 'Order'},
            'billing_address_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cart_pk': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order_subtotal': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'order_total': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'shipping_address_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['login_with_email.User']", 'null': 'True', 'blank': 'True'})
        },
        'shop.orderextrainfo': {
            'Meta': {'object_name': 'OrderExtraInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'extra_info'", 'to': "orm['ex_shop.Order']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'shop.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_subtotal': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'line_total': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['ex_shop.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_reference': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        },
        'shop.orderpayment': {
            'Meta': {'object_name': 'OrderPayment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ex_shop.Order']"}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['shop']