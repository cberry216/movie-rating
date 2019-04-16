# Generated by Django 2.2 on 2019-04-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20190416_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('rated', models.CharField(blank=True, choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], default='PG-13', max_length=5, null=True)),
                ('released', models.DateField()),
                ('runtime_minutes', models.IntegerField()),
                ('genre', models.CharField(blank=True, max_length=20, null=True)),
                ('director', models.CharField(blank=True, max_length=80, null=True)),
                ('plot', models.TextField(blank=True, null=True)),
                ('poster_link', models.CharField(blank=True, max_length=250, null=True)),
                ('imdb_rating', models.FloatField(blank=True, null=True)),
                ('rt_rating', models.IntegerField(blank=True, null=True)),
                ('added_to_db', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]