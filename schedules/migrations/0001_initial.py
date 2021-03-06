# Generated by Django 2.2.7 on 2020-01-03 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('class_date', models.DateTimeField()),
                ('day', models.CharField(blank=True, max_length=20, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('initial', models.CharField(blank=True, max_length=10, null=True)),
                ('subject_code', models.CharField(blank=True, max_length=20, null=True)),
                ('subject_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cohort_name', models.CharField(blank=True, max_length=100, null=True)),
                ('room_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nama', models.CharField(max_length=40)),
                ('initial_nama', models.CharField(max_length=5, unique=True)),
                ('prodi', models.CharField(choices=[('Business Mathematic (BM)', 'Business Mathematic (BM)'), ('Renewable Energy Engineering (REE)', 'Renewable Energy Engineering (REE)'), ('Food Business Technology (FBT)', 'Food Business Technology (FBT)'), ('Product Design Engineering (PDE)', 'Product Design Engineering (PDE)'), ('Software Engineering (SE)', 'Software Engineering (SE)'), ('Computer Systems Engineering (CSE)', 'Computer Systems Engineering (CSE)')], max_length=50)),
                ('status', models.CharField(choices=[('Fulltime', 'Fulltime'), ('Partime', 'Partime')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('subject_code', models.CharField(blank=True, max_length=12, null=True)),
                ('subject_name', models.CharField(max_length=30, unique=True)),
                ('max_credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NewKuliahRevise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('program_id', models.CharField(blank=True, max_length=20, null=True)),
                ('program_name', models.CharField(blank=True, max_length=100, null=True)),
                ('section_id', models.CharField(blank=True, max_length=20, null=True)),
                ('section_name', models.CharField(blank=True, max_length=100, null=True)),
                ('day', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField()),
                ('subject_name', models.CharField(blank=True, max_length=20, null=True)),
                ('event_obj', models.CharField(blank=True, max_length=20, null=True)),
                ('event_name', models.CharField(blank=True, max_length=100, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('capacity', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('nik', models.CharField(blank=True, max_length=5, null=True)),
                ('faculty_name', models.CharField(blank=True, max_length=100, null=True)),
                ('room', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nama_ruang', models.CharField(blank=True, max_length=100, null=True)),
                ('jenis', models.CharField(choices=[('Kelas', 'Kelas'), ('Lab VLAB', 'Lab VLAB'), ('Lab Non-VLAB', 'Lab Non-VLAB')], max_length=30)),
                ('kode_ruang', models.CharField(max_length=30, unique=True)),
                ('gedung', models.CharField(choices=[('STEM Lab', 'STEM Lab'), ('Gedung Liem', 'Gedung Liem')], max_length=50)),
                ('kapasitas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angkatan', models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], max_length=10)),
                ('kelas', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=10)),
                ('prodi', models.CharField(choices=[('Business Mathematic (BM)', 'Business Mathematic (BM)'), ('Renewable Energy Engineering (REE)', 'Renewable Energy Engineering (REE)'), ('Food Business Technology (FBT)', 'Food Business Technology (FBT)'), ('Product Design Engineering (PDE)', 'Product Design Engineering (PDE)'), ('Software Engineering (SE)', 'Software Engineering (SE)'), ('Computer Systems Engineering (CSE)', 'Computer Systems Engineering (CSE)')], max_length=50)),
                ('kode_prodi', models.CharField(choices=[('BM', 'BM'), ('REE', 'REE'), ('FBT', 'FBT'), ('PDE', 'PDE'), ('SE', 'SE'), ('CSE', 'CSE')], max_length=3)),
                ('faculty', models.CharField(choices=[('STEM', 'STEM'), ('SBE', 'SBE')], max_length=40)),
                ('jumlah', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('time_at', models.TimeField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='RoomSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat')], max_length=10)),
                ('jumlah_sks', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3)),
                ('ruang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ruang', to='schedules.Room')),
                ('waktu_mulai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waktu_mulai', to='schedules.TimeSlot')),
                ('waktu_selesai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waktu_selesai', to='schedules.TimeSlot')),
            ],
        ),
        migrations.CreateModel(
            name='JadwalHarian',
            fields=[
                ('jumlah_sks', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3)),
                ('room_slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='roomslot', serialize=False, to='schedules.RoomSlot')),
                ('dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dosen', to='schedules.Lecturer')),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mahasiwa', to='schedules.Student')),
                ('nama_mata_kuliah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matakuliah', to='schedules.MataKuliah')),
            ],
        ),
    ]
