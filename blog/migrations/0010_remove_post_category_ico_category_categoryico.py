# Generated by Django 4.0.3 on 2022-04-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_tag_post_category_ico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_ico',
        ),
        migrations.AddField(
            model_name='category',
            name='categoryico',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]