# Generated by Django 2.2 on 2020-07-06 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200706_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('mobile_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='QuestionPost',
        ),
    ]