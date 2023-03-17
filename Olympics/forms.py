from django import forms
from Olympics.models import Athlete,Leaderboard

class AthleteForms(forms.ModelForm):
    class Meta:
        model=Athlete
        fields="__all__"

class LeaderboardForms(forms.ModelForm):
    class Meta:
        model=Leaderboard
        fields="__all__"
