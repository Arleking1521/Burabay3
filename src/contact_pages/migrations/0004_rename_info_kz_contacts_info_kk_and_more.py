# Generated by Django 5.0.2 on 2024-03-29 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_pages', '0003_rename_info_kk_contacts_info_kz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='info_kz',
            new_name='info_kk',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='title_kz',
            new_name='title_kk',
        ),
        migrations.RenameField(
            model_name='managers',
            old_name='name_kz',
            new_name='name_kk',
        ),
        migrations.RenameField(
            model_name='managers',
            old_name='post_kz',
            new_name='post_kk',
        ),
        migrations.RenameField(
            model_name='managers',
            old_name='reception_kz',
            new_name='reception_kk',
        ),
    ]
