# Generated by Django 3.0.1 on 2021-03-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelledapproval',
            name='cancelled_order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cancelledapproval',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cancelledorder',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]