# Generated by Django 3.2.3 on 2021-05-25 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_alter_state_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='district',
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.state'),
        ),
    ]
