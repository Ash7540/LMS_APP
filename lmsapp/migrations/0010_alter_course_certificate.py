# Generated by Django 4.2.5 on 2023-09-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0009_course_certificate_course_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
