# Generated by Django 4.0.6 on 2022-07-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_rename_zip_code_branch_postcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='is_running',
            field=models.BooleanField(default=True, verbose_name='운영 여부'),
        ),
    ]
