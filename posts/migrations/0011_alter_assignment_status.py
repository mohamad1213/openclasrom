# Generated by Django 5.0.6 on 2024-06-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_assignment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(blank=True, choices=[('onprogress', 'On Progress'), ('completed', 'Completed')], default='onprogress', max_length=10, null=True),
        ),
    ]
