# Generated by Django 3.1 on 2020-08-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_sectionimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
            ],
        ),
    ]