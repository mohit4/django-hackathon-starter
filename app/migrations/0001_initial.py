# Generated by Django 2.2 on 2019-08-17 14:32

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
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('points', models.PositiveIntegerField(default=10)),
                ('cost', models.DecimalField(decimal_places=2, default=99.99, max_digits=12)),
                ('category', models.CharField(choices=[('AUT', 'Automobile'), ('INF', 'Infrastructure'), ('RND', 'Research and Development')], max_length=3)),
                ('active', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=100)),
                ('profile_image', models.ImageField(default='default_profile.jpg', upload_to='entity/')),
                ('cover_image', models.ImageField(default='default_cover.jpg', upload_to='entity/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Entity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
