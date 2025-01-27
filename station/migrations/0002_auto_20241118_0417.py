# Generated by Django 2.2.28 on 2024-11-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos_personnages/'),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='etat',
            field=models.CharField(choices=[('actif', 'Actif'), ('reposé', 'Reposé'), ('fatigué', 'Fatigué'), ('affamé', 'Affamé')], default='actif', max_length=50),
        ),
        migrations.AlterField(
            model_name='habitant',
            name='nom',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
