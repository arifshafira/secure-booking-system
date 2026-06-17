from django import forms
from .models import Booking, RoomType
import re

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room_type', 'title', 'check_in_date', 'check_out_date', 'guests', 'special_requests', 'status']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room_type'].queryset = RoomType.objects.filter(is_available=True)
        self.fields['room_type'].empty_label = "Select a Room"

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not re.match(r'^[\w\s\-.,!?()]+$', title):
            raise forms.ValidationError('Title contains invalid characters.')
        return title

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in_date')
        check_out = cleaned_data.get('check_out_date')
        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError('Check-out date must be after check-in date.')
        return cleaned_data