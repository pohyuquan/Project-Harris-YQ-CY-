from django import forms
from .models import Input, STATES, schools, SCHOOL_DISTRICTS, grade, GRADES, sub, SUBGROUP, subjects, SUBJECT

class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    state = forms.ChoiceField(choices=STATES, required=True,
                              widget = forms.Select(attrs = attrs))

    class Meta:

        model = Input
        fields = ['state']

class InputForm1(forms.ModelForm):

    state = forms.ChoiceField(choices=STATES, required=True,
                              widget = forms.Select())

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

class SchoolsForm1(forms.ModelForm):

    district = forms.ChoiceField(choices=SCHOOL_DISTRICTS, required=True,
                              widget = forms.Select())

    class Meta:

        model = schools
        fields = ['district']


class GradesForm(forms.ModelForm):

    gradelevel = forms.ChoiceField(choices=GRADES, required=True,
                              widget = forms.Select())

    class Meta:

        model = grade
        fields = ['gradelevel']

class SubgroupForm(forms.ModelForm):

    subgroups = forms.ChoiceField(choices=SUBGROUP, required=True,
                              widget = forms.Select())

    class Meta:

        model = sub
        fields = ['subgroups']

class SubjectForm(forms.ModelForm):

    topic = forms.ChoiceField(choices=SUBJECT, required=True,
                              widget = forms.Select())

    class Meta:

        model = subjects
        fields = ['topic']
