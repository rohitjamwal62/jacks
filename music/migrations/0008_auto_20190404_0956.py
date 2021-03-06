# Generated by Django 2.1.7 on 2019-04-04 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_delete_myobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('qrcode', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='anonymous user', max_length=50, null=True)),
                ('rating', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('review', models.ForeignKey(default='NA', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='music.feedback')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.product'),
        ),
    ]
