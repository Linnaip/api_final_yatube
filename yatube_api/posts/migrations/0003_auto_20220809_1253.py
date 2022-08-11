# Generated by Django 2.2.16 on 2022-08-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220809_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follwing',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_following'),
        ),
    ]
