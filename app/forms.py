from django import forms
c=[['django','DJANGO'],['Python','PYTHON']]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100,label='First',label_suffix='Name',help_text='only alphabets')
    age=forms.IntegerField(min_value=18)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #course=forms.ChoiceField(choices=c)
    #course=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
