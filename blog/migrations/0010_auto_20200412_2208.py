# Generated by Django 3.0.4 on 2020-04-12 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_roomcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomcategory',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='roomcategory',
            old_name='Sharing',
            new_name='sharing',
        ),
    ]
