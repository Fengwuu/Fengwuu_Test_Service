from django import forms


class TestUserAnswer(forms.Form):
    choice = forms.CheckboxInput()

    class Meta:
        fields = ['choice']
        widgets = {

        }
