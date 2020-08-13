# Generated by Django 2.2.6 on 2020-02-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_id', models.CharField(max_length=20)),
                ('rfid', models.CharField(max_length=20)),
                ('train_id', models.PositiveIntegerField()),
                ('sender_name', models.CharField(max_length=50)),
                ('sender_adhar', models.CharField(max_length=20)),
                ('reciever_name', models.CharField(max_length=50)),
                ('reciever_adhar', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('parcel_from', models.CharField(max_length=20)),
                ('parcel_to', models.CharField(max_length=20)),
                ('parcel_info', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Ordered', 'Ordered'), ('ShippingSoon', 'ShippingSoon'), ('Shipped', 'Shipped'), ('OutForDelivery', 'OutForDelivery'), ('Delivered', 'Delivered')], max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Parcel',
            },
        ),
    ]
