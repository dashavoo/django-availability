import datetime
from django import forms
from django.utils import formats
from django.utils.encoding import force_str
from django.utils.translation import ugettext_lazy as _, ungettext_lazy
from django.utils.translation import ungettext

DATE_FORMATS =  ['%d/%m/%y', '%d/%m/%Y', '%d.%m.%y']

class MultiDateField(forms.fields.BaseTemporalField):
    input_formats = formats.get_format_lazy('DATE_INPUT_FORMATS')
    default_error_messages = {
        'invalid': _('Enter a list of dates separated by a comma'),
    }

    def to_python(self, value):
        """
        Validates that the input can be converted to a list of dates. Returns a Python
        list of datetime.date objects.
        """
        return super(MultiDateField, self).to_python(value)

    def strptime(self, value, format):
        if len(value)>0:
            values = value.split(",")
            dates = [datetime.datetime.strptime(force_str(d), format).date() for d in values]
        else:
            dates = []

        return list(dates)

class AvailabilityForm(forms.Form):
    dates = MultiDateField(input_formats=DATE_FORMATS, required=False, widget=forms.widgets.HiddenInput)

