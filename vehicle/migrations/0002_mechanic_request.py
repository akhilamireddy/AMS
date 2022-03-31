

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/MechanicProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('two wheeler', 'two wheeler'), ('three wheeler', 'three wheeler')], max_length=50)),
                ('vehicle_no', models.PositiveIntegerField()),
                ('vehicle_name', models.CharField(max_length=40)),
                ('vehicle_model', models.CharField(max_length=40)),
                ('vehicle_brand', models.CharField(max_length=40)),
                ('problem_description', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.Customer')),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.Mechanic')),
            ],
        ),
    ]
