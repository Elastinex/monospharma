# Generated by Django 3.0.8 on 2020-07-30 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_application_hr'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'List Item ',
                'verbose_name_plural': 'List Items',
            },
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list1',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list10',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list11',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list12',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list13',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list14',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list15',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list2',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list3',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list4',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list5',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list6',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list7',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list8',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_list9',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_title1',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_title2',
        ),
        migrations.RemoveField(
            model_name='hr',
            name='list_title3',
        ),
        migrations.CreateModel(
            name='ListTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='Text')),
                ('list_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ListItem', verbose_name='List item')),
            ],
            options={
                'verbose_name': 'List title ',
                'verbose_name_plural': 'List titles',
            },
        ),
        migrations.AddField(
            model_name='hr',
            name='list_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ListTitle', verbose_name='List title'),
        ),
    ]
