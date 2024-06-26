# Generated by Django 5.0.6 on 2024-06-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('onprogress', 'On Progress'), ('completed', 'Completed')], default='onprogress', max_length=10),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='marks',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
    ]
