# Generated by Django 4.0.6 on 2022-07-18 02:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('srl', models.BigAutoField(primary_key=True, serialize=False, verbose_name='이용자 연번')),
                ('username', models.TextField(unique=True, verbose_name='이용자 아이디')),
                ('name', models.TextField(verbose_name='이름')),
                ('birthday', models.DateField(verbose_name='생년월일')),
                ('gender', models.TextField(choices=[('M', '남성'), ('F', '여성')], verbose_name='성별')),
                ('phone', models.TextField(verbose_name='전화번호')),
                ('license_type', models.TextField(choices=[('', ''), ('L1L', '1종 대형'), ('L1G', '1종 보통'), ('L1GA', '1종 보통 (자동)'), ('L2G', '2종 보통'), ('L2GA', '2종 보통 (자동)'), ('P', '장롱 면허')], null=True, verbose_name='면허 종류')),
                ('plan_type', models.TextField(choices=[('', ''), ('T', '시간제'), ('G', '합격보장제'), ('P', '장롱 면허')], null=True, verbose_name='요금제 유형')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('belong_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='branches.branch', verbose_name='소속 지점')),
            ],
            options={
                'verbose_name': '이용자',
            },
        ),
    ]
