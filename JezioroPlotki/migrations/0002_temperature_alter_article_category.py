# Generated by Django 4.2.1 on 2023-05-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JezioroPlotki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Strona-Glowna', 'Strona Główna'), ('Informacje', 'Informacje'), ('Hydrobiologia', 'Hydrobiologia'), ('Obszar-Natura-2000', 'Obszar Natura 2000'), ('Hydrologia-Jeziora', 'Hydrologia Jeziora')], default='Index', max_length=256),
        ),
    ]