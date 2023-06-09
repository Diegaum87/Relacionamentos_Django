# Generated by Django 4.2.1 on 2023-06-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_recipes_recipe'),
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipes',
            field=models.ManyToManyField(related_name='ingredients', to='recipes.recipe'),
        ),
    ]