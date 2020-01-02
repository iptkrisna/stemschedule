# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class Kuliah(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    class_date = models.DateTimeField()
    day = models.CharField(max_length=20,null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    full_name = models.CharField(max_length=100,null=True, blank=True)
    initial = models.CharField(max_length=10,null=True, blank=True)
    subject_code = models.CharField(max_length=20,null=True, blank=True)
    subject_name = models.CharField(max_length=100,null=True, blank=True)
    cohort_name = models.CharField(max_length=100,null=True, blank=True)
    room_no = models.CharField(max_length=100,null=True, blank=True)
    def __unicode__(self):
        return '{}'.format(self.subject_code)

# Create your models here.
class Room(models.Model):
    """Room that available in Prasmul BSD Campus"""
    GEDUNG_LIST = (
        ('STEM Lab', 'STEM Lab'),
        ('Gedung Liem', 'Gedung Liem')
    )
    JENIS_LIST = (
        ('Kelas', 'Kelas'),
        ('Lab VLAB', 'Lab VLAB'),
        ('Lab Non-VLAB', 'Lab Non-VLAB'),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    nama_ruang = models.CharField(max_length=100,null=True, blank=True)
    jenis= models.CharField(max_length=30,choices=JENIS_LIST,null=False, blank=False)
    kode_ruang= models.CharField(max_length=30,null=False, blank=False,unique=True)
    gedung = models.CharField(max_length=50, choices=GEDUNG_LIST,null=False, blank=False)
    kapasitas = models.IntegerField(null=False, blank=False)

    def __unicode__(self):
        return '{} | {} | {}'.format(self.kode_ruang, self.gedung, self.nama_ruang)

class MataKuliah(models.Model):
    """Room that available in Prasmul BSD Campus"""
    created_on = models.DateTimeField(auto_now_add=True)
    subject_code = models.CharField(max_length=12,null=True, blank=True)
    subject_name= models.CharField(max_length=30,null=False, blank=False,unique=True)
    max_credit = models.IntegerField(null=False, blank=False)

    def __unicode__(self):
        return '{} | {} | ({}sks)'.format(self.subject_code, self.subject_name, self.max_credit)

class Lecturer(models.Model):
    """Lecturer in Prasetiya Mulya"""
    created_on = models.DateTimeField(auto_now_add=True)
    nama = models.CharField(max_length=40,null=False, blank=False)
    initial_nama = models.CharField(max_length=5,null=False, blank=False, unique=True)
    PRODI_LIST = (
        ('Business Mathematic (BM)', 'Business Mathematic (BM)'),
        ('Renewable Energy Engineering (REE)', 'Renewable Energy Engineering (REE)'),
        ('Food Business Technology (FBT)', 'Food Business Technology (FBT)'),
        ('Product Design Engineering (PDE)','Product Design Engineering (PDE)'),
        ('Software Engineering (SE)', 'Software Engineering (SE)'),
        ('Computer Systems Engineering (CSE)', 'Computer Systems Engineering (CSE)')
    )
    STATUS = (
        ('Fulltime', 'Fulltime'),
        ('Partime', 'Partime')
    )

    prodi = models.CharField(max_length=50, choices=PRODI_LIST,null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS,null=False, blank=False)

    def __unicode__(self):
        return '{} ({}) | {}'.format(self.nama, self.initial_nama, self.status)

class TimeSlot(models.Model):
    """Lecturer in Prasetiya Mulya"""
    created_on = models.DateTimeField(auto_now_add=True)
    time_at = models.TimeField(max_length=40,null=False, blank=False)

    def __unicode__(self):
        return '{}'.format(self.time_at)

class Student (models.Model):
    CLASS_LIST = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('E','E'),
    )
    PRODI_LIST = (
        ('Business Mathematic (BM)', 'Business Mathematic (BM)'),
        ('Renewable Energy Engineering (REE)', 'Renewable Energy Engineering (REE)'),
        ('Food Business Technology (FBT)', 'Food Business Technology (FBT)'),
        ('Product Design Engineering (PDE)','Product Design Engineering (PDE)'),
        ('Software Engineering (SE)', 'Software Engineering (SE)'),
        ('Computer Systems Engineering (CSE)', 'Computer Systems Engineering (CSE)')
    )
    PRODI_KODE = (
        ('BM', 'BM'),
        ('REE', 'REE'),
        ('FBT', 'FBT'),
        ('PDE','PDE'),
        ('SE', 'SE'),
        ('CSE', 'CSE')
    )

    FACULTY_LIST = (
        ('STEM', 'STEM'),
        ('SBE', 'SBE')
    )

    ANGKATAN_LIST = (
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021')
    )

    angkatan = models.CharField(max_length=10, choices=ANGKATAN_LIST, null=False, blank=False)
    kelas = models.CharField(max_length=10, choices=CLASS_LIST, null=False, blank=False)
    prodi = models.CharField(max_length=50, choices=PRODI_LIST,null=False, blank=False)
    kode_prodi = models.CharField(max_length=3, choices=PRODI_KODE,null=False, blank=False)
    faculty = models.CharField(max_length= 40, choices=FACULTY_LIST, null=False, blank=False)
    jumlah = models.IntegerField(null=False, blank=False)

    def __unicode__(self):
        return '{}{}{}'.format(self.kode_prodi,self.angkatan, self.kelas)

class RoomSlot(models.Model):
    DAY_LIST = (
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
    )
    SKS_LIST = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    hari = models.CharField(max_length=10,choices=DAY_LIST, null=False, blank=False)
    waktu_mulai = models.ForeignKey('TimeSlot',on_delete=models.CASCADE,null=False, blank=False,  related_name='waktu_mulai')
    waktu_selesai = models.ForeignKey('TimeSlot',on_delete=models.CASCADE,null=False, blank=False,  related_name='waktu_selesai')
    ruang = models.ForeignKey('Room',on_delete=models.CASCADE,null=False, blank=False,  related_name='ruang')
    jumlah_sks = models.CharField(max_length=3,null=False,choices=SKS_LIST, blank=False)

    def __unicode__(self):
        return '{} | {} | {}-{} | {}sks'.format(self.hari, self.ruang, self.waktu_mulai, self.waktu_selesai, self.jumlah_sks)

class JadwalHarian(models.Model):
    """Jadwal in Prasetiya Mulya"""
    SKS_LIST = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    nama_mata_kuliah = models.ForeignKey('MataKuliah',on_delete=models.CASCADE,null=False, blank=False,  related_name='matakuliah')
    dosen = models.ForeignKey('Lecturer',on_delete=models.CASCADE,null=False, blank=False,  related_name='dosen')
    mahasiswa = models.ForeignKey('Student',on_delete=models.CASCADE,null=False, blank=False,  related_name='mahasiwa')
    jumlah_sks = models.CharField(max_length=3,null=False,choices=SKS_LIST, blank=False)
    room_slot = models.OneToOneField(
        RoomSlot,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name = 'roomslot'
    )

    def get_absolute_url(self):
        return reverse("jadwalcreate")

    def __unicode__(self):
        return '{}sks | {} | {} | {} '.format(self.nama_mata_kuliah,  self.mahasiswa, self.dosen, self.room_slot)

    def clean(self):
        jadwaldosens = JadwalHarian.objects.filter(dosen=self.dosen)
        if jadwaldosens.exists():
            for jdwal in jadwaldosens:
                if jdwal.room_slot.hari== self.room_slot.hari:
                    if jdwal.room_slot.waktu_mulai ==  self.room_slot.waktu_mulai:
                        raise ValidationError(str(jdwal.dosen)+' TIDAK AVAILABLE di: ' +  str(jdwal.room_slot.hari)+' ( '+ str(jdwal.room_slot.waktu_mulai)+'-'+str(jdwal.room_slot.waktu_selesai)+')')
        jdwalmahasiswa = JadwalHarian.objects.filter(mahasiswa=self.mahasiswa)
        if jdwalmahasiswa.exists():
            for jdwal in jdwalmahasiswa:
                if jdwal.room_slot.hari== self.room_slot.hari:
                    if jdwal.room_slot.waktu_mulai ==  self.room_slot.waktu_mulai:
                        raise ValidationError(str(jdwal.mahasiswa)+' TIDAK AVAILABLE di: ' +  str(jdwal.room_slot.hari)+' ( '+ str(jdwal.room_slot.waktu_mulai)+'-'+str(jdwal.room_slot.waktu_selesai)+')')
        if self.jumlah_sks != self.room_slot.jumlah_sks:
            raise ValidationError("Jumlah SKS tidak sesuai dengan slot ruangan yang ada. Pastikan Jumlah SKS yang di input BENAR!")




class NewKuliah(models.Model):
    created_on      = models.DateTimeField(auto_now_add=True)
    program_id      = models.CharField(max_length=20, null=True, blank=True)
    program_name    = models.CharField(max_length=100,null=True, blank=True)
    section_id      = models.CharField(max_length=20, null=True, blank=True)
    section_name    = models.CharField(max_length=100, null=True, blank=True)
    day             = models.CharField(max_length=20,null=True, blank=True)
    date            = models.CharField(max_length=20,null=True, blank=True)
    subject_name    = models.CharField(max_length=20,null=True, blank=True)
    event_obj       = models.CharField(max_length=20,null=True, blank=True)
    event_name      = models.CharField(max_length=100,null=True, blank=True)
    start_time      = models.TimeField()
    end_time        = models.TimeField()
    capacity        = models.IntegerField()
    location        = models.CharField(max_length=20,null=True, blank=True)
    nik             = models.CharField(max_length=5, null=True, blank=True)
    faculty_name    = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.subject_name)
