# Generated by Django 3.1.5 on 2021-01-19 05:51

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210119_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact_desc',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_text',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
