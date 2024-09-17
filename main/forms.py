from django.forms import ModelForm
from main.models import VBucksEntry

class VBucksEntryForm(ModelForm):
    class Meta:
        model = VBucksEntry
        fields = ["name", "price", "description", "bonus"]