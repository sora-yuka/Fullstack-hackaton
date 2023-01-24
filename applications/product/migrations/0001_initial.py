# Generated by Django 4.1.5 on 2023-01-24 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=200)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Thrieler', 'Thrieler'), ('Mystery', 'Mystery'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'), ('Anti utopia', 'Anti utopia'), ('Utopia', 'Utopia')], max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('image', models.ImageField(upload_to='image/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
