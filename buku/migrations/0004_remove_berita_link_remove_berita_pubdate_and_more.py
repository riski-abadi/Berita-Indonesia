# Generated by Django 4.1.2 on 2022-12-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0003_berita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='berita',
            name='link',
        ),
        migrations.RemoveField(
            model_name='berita',
            name='pubDate',
        ),
        migrations.RemoveField(
            model_name='berita',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='berita',
            name='author',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='berita',
            name='content',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='berita',
            name='publishedAt',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='berita',
            name='url',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='berita',
            name='urlToImage',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='berita',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='berita',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
