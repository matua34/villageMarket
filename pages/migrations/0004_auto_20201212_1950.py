# Generated by Django 3.1.4 on 2020-12-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='natural',
            name='isPublished',
            field=models.BooleanField(default=True, verbose_name='YAYIN DURUMU'),
        ),
        migrations.AlterField(
            model_name='carpet',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='EKLENME TARİHİ'),
        ),
        migrations.AlterField(
            model_name='carpet',
            name='description',
            field=models.TextField(verbose_name='HALI AÇIKLAMASI'),
        ),
        migrations.AlterField(
            model_name='carpet',
            name='image',
            field=models.CharField(max_length=50, verbose_name='HALI FOTOĞRAFI'),
        ),
        migrations.AlterField(
            model_name='carpet',
            name='name',
            field=models.CharField(max_length=150, verbose_name='HALI ADI'),
        ),
        migrations.AlterField(
            model_name='natural',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='EKLENME TARİHİ'),
        ),
        migrations.AlterField(
            model_name='natural',
            name='description',
            field=models.TextField(verbose_name='ÜRÜN AÇIKLAMASI'),
        ),
        migrations.AlterField(
            model_name='natural',
            name='image',
            field=models.CharField(max_length=50, verbose_name='ÜRÜN FOTOĞRAFI'),
        ),
        migrations.AlterField(
            model_name='natural',
            name='name',
            field=models.CharField(max_length=150, verbose_name='ÜRÜN ADI'),
        ),
    ]
