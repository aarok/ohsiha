from django.forms import ModelForm
from fishprofile.models import Fish

class AddFishForm(ModelForm):
    class Meta:
        model = Fish
        fields = ['species', 'catch_date', 'catch_time', 'form_of_fishing',
        'catch_latitude', 'catch_longitude']
