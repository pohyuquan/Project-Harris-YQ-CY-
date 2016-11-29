from django import forms
from .models import Input, STATES, schools, SCHOOL_DISTRICTS

class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    state = forms.ChoiceField(choices=STATES, required=True,
                              widget = forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['state']

class SchoolsForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    district = forms.ChoiceField(choices=SCHOOL_DISTRICTS, required=True,
                              widget = forms.Select(attrs = attrs))

    class Meta:

        model = schools
        fields = ['district']
