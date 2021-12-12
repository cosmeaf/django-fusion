# Generated by Django 4.0 on 2021-12-12 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_staff_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Empregado', 'verbose_name_plural': 'Empregados'},
        ),
        migrations.AlterField(
            model_name='staff',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.officepost', verbose_name='Empregado'),
        ),
    ]