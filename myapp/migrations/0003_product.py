# Generated by Django 4.2.13 on 2024-07-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer_email_customer_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='product_img/')),
            ],
        ),
    ]
