# Generated by Django 4.2 on 2023-04-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('Web Dev', 'Web Dev'), ('AI/ML', 'AI/ML'), ('Basic Coding', 'Basic Coding')], max_length=100),
        ),
    ]
