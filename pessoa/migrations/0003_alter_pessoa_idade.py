# Generated by Django 5.1.7 on 2025-04-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_alter_pessoa_endereco_alter_pessoa_idade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
    ]
