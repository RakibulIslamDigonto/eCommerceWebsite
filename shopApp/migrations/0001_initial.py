# Generated by Django 4.0.4 on 2022-04-24 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True, null=True)),
                ('modified_at', models.DateField(auto_now=True, null=True)),
                ('enable', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True, null=True)),
                ('modified_at', models.DateField(auto_now=True, null=True)),
                ('enable', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images/products/')),
                ('is_featured', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopApp.category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]