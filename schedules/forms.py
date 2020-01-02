from django import forms
from .models import JadwalHarian, RoomSlot
from django.db.models import Q

class JadwalForm(forms.ModelForm):
    class Meta:
        model = JadwalHarian
        fields = '__all__'

        widgets = {
            'nama_mata_kuliah': forms.Select(attrs={'class':'form-control'}),
            'dosen': forms.Select(attrs={'class':'form-control'}),
            'mahasiswa': forms.Select(attrs={'class':'form-control'}),
            'jumlah_sks': forms.Select(attrs={'class':'form-control'}),
            'room_slot': forms.Select(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(JadwalForm, self).__init__(*args, **kwargs)

        #only provide users that are not already linked to an actor, plus the user that was already chosen for this Actor
        self.fields['room_slot'].queryset = RoomSlot.objects.filter(Q(roomslot__isnull=True)|Q(roomslot=self.instance))
