from django import forms


from .models import Event, Building


class EventForm(forms.ModelForm):

    event_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Event
        exclude = ['event_name']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['buildings'] = forms.ModelMultipleChoiceField(required=False, queryset=Building.objects.all(), widget=forms.CheckboxSelectMultiple())
