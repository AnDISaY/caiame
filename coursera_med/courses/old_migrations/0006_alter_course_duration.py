# Generated by Django 4.2.13 on 2024-07-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_duration_alter_course_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.SmallIntegerField(choices=[(36, '36ч'), (72, '72ч')]),
        ),
    ]
