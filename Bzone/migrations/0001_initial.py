# Generated by Django 2.2.17 on 2023-03-31 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accomadetion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulding_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('land_mark', models.CharField(max_length=100)),
                ('room_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('E_mail', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='send_admitcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CANDIDATE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.candidates')),
                ('PROGRAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.program')),
            ],
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('time_from', models.CharField(max_length=100)),
                ('time_to', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('PROGRAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.program')),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('photo', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=10)),
                ('district', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.login')),
            ],
        ),
        migrations.CreateModel(
            name='judgment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=100)),
                ('CANDIDATE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.candidates')),
                ('PROGRAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.program')),
            ],
        ),
        migrations.CreateModel(
            name='judge_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JUDGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.judge')),
                ('PROGRAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.program')),
            ],
        ),
        migrations.AddField(
            model_name='judge',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.login'),
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('complaint', models.CharField(max_length=500)),
                ('reaplay', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=100)),
                ('COLLEGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.college')),
            ],
        ),
        migrations.CreateModel(
            name='committee_member_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MEMBER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.member')),
                ('PROGRAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.program')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.login'),
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=500)),
                ('from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_id', to='Bzone.login')),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_id', to='Bzone.login')),
            ],
        ),
        migrations.AddField(
            model_name='candidates',
            name='COLLEGE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.college'),
        ),
        migrations.AddField(
            model_name='candidates',
            name='PROGRAM',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.program'),
        ),
        migrations.CreateModel(
            name='appeals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('massage', models.CharField(max_length=500)),
                ('reaplay', models.CharField(max_length=500)),
                ('COLLEGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.college')),
                ('Participant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Bzone.candidates')),
            ],
        ),
        migrations.CreateModel(
            name='accomadation_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACCOMADATION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.accomadetion')),
                ('COLLEGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bzone.college')),
            ],
        ),
    ]
