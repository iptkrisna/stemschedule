from rest_framework import serializers
from . import models


class RoomSerializer(serializers.ModelSerializer):
    """A serializer for Room"""
    class Meta:
        model = models.Room
        fields = '__all__'

class KuliahSerializer(serializers.ModelSerializer):
    """A serializer for Room"""
    class Meta:
        model = models.Kuliah
        fields = '__all__'

class LecturerSerializer(serializers.ModelSerializer):
    """A serializer for Lecturer"""
    class Meta:
        model = models.Lecturer
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    """A serializer for Student"""
    class Meta:
        model = models.Student
        fields = '__all__'

class MataKuliahSerializer(serializers.ModelSerializer):
    """A serializer for Student"""
    class Meta:
        model = models.MataKuliah
        fields = '__all__'

class TimeSlotSerializer(serializers.ModelSerializer):
    """A serializer for Student"""
    class Meta:
        model = models.TimeSlot
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    """A serializer for Schedule"""
    ruang = RoomSerializer(many=False, read_only=True)
    waktu_mulai = TimeSlotSerializer(many=False, read_only=True)
    waktu_selesai = TimeSlotSerializer(many=False, read_only=True)
    class Meta:
        model = models.RoomSlot
        fields = '__all__'

class JadwalSerializer(serializers.ModelSerializer):
    """A serializer for Schedule"""
    nama_mata_kuliah = MataKuliahSerializer(many=False, read_only=True)
    dosen = LecturerSerializer(many=False, read_only=True)
    mahasiswa = StudentSerializer(many=False, read_only=True)
    room_slot =  ScheduleSerializer(many=False, read_only=True)

    class Meta:
        model = models.JadwalHarian
        fields = '__all__'
