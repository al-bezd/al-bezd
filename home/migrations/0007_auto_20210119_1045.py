# Generated by Django 3.1.5 on 2021-01-19 05:45

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='keywords',
            field=models.TextField(blank=True, help_text='Ключевые слова для индексации поисковыми роботами', null=True, verbose_name='keywords'),
        ),
        migrations.CreateModel(
            name='HomePageSkillsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=50)),
                ('text', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='skillshistory', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
