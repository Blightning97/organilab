# Generated by Django 2.2.13 on 2020-10-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0015_ue_storage_nfpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='sustancecharacteristics',
            name='seveso_list',
            field=models.BooleanField(default=False, verbose_name='Listado Seveso III'),
        ),
    ]
