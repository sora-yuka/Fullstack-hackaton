# Generated by Django 4.1.5 on 2023-01-24 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('In proccess', 'In proccess'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=30, null=True)),
                ('is_confirm', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activation_code', models.UUIDField(default=uuid.uuid4)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='product.product')),
            ],
        ),
    ]
