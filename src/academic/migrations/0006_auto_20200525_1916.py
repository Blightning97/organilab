# Generated by Django 2.2.12 on 2020-05-26 01:16

from django.db import migrations
import django.db.models.deletion
import laboratory.catalog

def change_procedurerequiredobject(apps, schema_editor):
    ShelfObject = apps.get_model('academic', 'ProcedureRequiredObject')
    mydata = ShelfObject.objects.all()
    Catalog = apps.get_model('laboratory', 'Catalog')

    units = dict((   #  ShelfObject   measurement_unit
                ('0', Catalog.objects.filter(description='Metros').first().pk),
                ('1', Catalog.objects.filter(description='Milímetros').first().pk),
                ('2', Catalog.objects.filter(description='Centímetros').first().pk),
                ('3', Catalog.objects.filter(description='Litros').first().pk),
                ('4', Catalog.objects.filter(description='Mililitros').first().pk),
                ("5", Catalog.objects.filter(description='Unidades').first().pk),
                ('6', Catalog.objects.filter(description='Gramos').first().pk),
                ('7', Catalog.objects.filter(description='Kilogramos').first().pk),
                ('8', Catalog.objects.filter(description='Miligramos').first().pk),
                ('9', Catalog.objects.filter(description='Metro cúbico').first().pk) )
                )

    for element in mydata:
        if element.measurement_unit:
            element.measurement_unit = str(units[str(element.measurement_unit)])
            element.save()



class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_auto_20200302_2337'),
        ('laboratory', '0003_pre_catalog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='procedure',
            options={'ordering': ('pk',), 'verbose_name': 'Procedure', 'verbose_name_plural': 'Procedures'},
        ),
        migrations.AlterModelOptions(
            name='procedureobservations',
            options={'ordering': ('pk',), 'verbose_name': 'Procedure Observation', 'verbose_name_plural': 'Procedure Observations'},
        ),
        migrations.AlterModelOptions(
            name='procedurerequiredobject',
            options={'ordering': ('pk',), 'verbose_name': 'Procedure Required Object', 'verbose_name_plural': 'Procedure Required Objects'},
        ),
        migrations.AlterModelOptions(
            name='procedurestep',
            options={'ordering': ('pk',), 'verbose_name': 'Procedure step', 'verbose_name_plural': 'Procedure steps'},
        ),

        migrations.RunPython(change_procedurerequiredobject),
        migrations.AlterField(
            model_name='procedurerequiredobject',
            name='measurement_unit',
            field=laboratory.catalog.GTForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='laboratory.Catalog', verbose_name='Measurement unit'),
        ),
    ]
