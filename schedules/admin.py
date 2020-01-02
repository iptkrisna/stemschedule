# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .import models

import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
# from utils import EventCalendar

class RoomSlotAdmin(admin.ModelAdmin):
    list_display = ['hari', 'ruang','waktu_mulai','waktu_selesai', 'jumlah_sks']
class TimeSlotAdmin(admin.ModelAdmin):
    ordering = ('time_at',)
class LecturerAdmin(admin.ModelAdmin):
    ordering = ('nama',)
class RoomAdmin(admin.ModelAdmin):
    ordering = ('kode_ruang',)
class MataKuliahAdmin(admin.ModelAdmin):
    ordering = ('subject_code',)
class StudentAdmin(admin.ModelAdmin):
    ordering = ('kode_prodi',)
class JadwalHarianAdmin(admin.ModelAdmin):
    list_filter = ('dosen',)
class KuliahAdmin(admin.ModelAdmin):
    list_filter = ('start_time',)

class NewKuliahAdmin(admin.ModelAdmin):
    list_filter = ('start_time',)

# Register your models here.
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.TimeSlot, TimeSlotAdmin)
admin.site.register(models.Lecturer, LecturerAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.RoomSlot, RoomSlotAdmin)
admin.site.register(models.MataKuliah, MataKuliahAdmin)
admin.site.register(models.JadwalHarian, JadwalHarianAdmin)
admin.site.register(models.Kuliah, KuliahAdmin)

admin.site.register(models.NewKuliah, NewKuliahAdmin)

admin.site.site_header = 'STEM Class Admin'
