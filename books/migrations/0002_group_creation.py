from django.contrib.auth.models import Group
from django.db import migrations


def create_groups(apps, schema_editor):
    Group.objects.create(name='Author')
    Group.objects.create(name='Collaborator')


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
