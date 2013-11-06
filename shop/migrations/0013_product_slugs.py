# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'Product.slug'
        db.alter_column(u'shop_product', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

    def backwards(self, orm):
        # Changing field 'Product.slug'
        db.alter_column(u'shop_product', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True))

    complete_apps = ['shop']
