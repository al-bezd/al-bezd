# Generated by Django 3.1.5 on 2021-01-12 11:19

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210112_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='content',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='portfoliopage',
            name='section_des',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
