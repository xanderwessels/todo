from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title','text','image', 'color')

    def clean(self):

        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        image = self.cleaned_data['image']

        if title is "" and text is "" and image is "":
            print("Fill in at least one of the three fields")
            raise forms.ValidationError("Fill in at least one of the three fields")