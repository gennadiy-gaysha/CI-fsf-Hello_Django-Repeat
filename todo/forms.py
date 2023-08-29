from django import forms
from .models import Item


# In Django it's possible to create forms directly from the model itself.
# And allow Django to handle all the form validation.

# Here we create a form that is directly associated with a Django model

# The purpose of this form is to allow users to interact with the Item model's
# data using a web form.

class ItemForm(forms.ModelForm):
    # To tell the form which model it's going to be associated with we need to provide an
    # inner class called meta.
    # This inner class just gives our form some information about itself.
    class Meta:
        model = Item
        fields = ['name', 'status', 'priority']


