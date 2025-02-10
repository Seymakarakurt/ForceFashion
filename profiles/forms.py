from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Platzhalter und Klassen hinzufügen, automatisch generierte entfernen
        Etiketten und stellen Sie den Autofokus auf das erste Feld ein
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'profile_picture': 'Profilbild',
            'default_phone_number': 'Telefonnummer',
            'default_street_address1': 'Adresse',
            'default_street_address2': 'Zusatzadresse',
            'default_postcode': 'Postleitzahl',
            'default_town_or_city': 'Stadt',
            'default_county': 'Land',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
