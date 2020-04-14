from django import forms

from cmsplus.fields import PlusModelMultipleChoiceField, PlusModelChoiceField
from cmsplus.forms import PlusPluginFormBase
from cmsplus.tests.models import Test


class TestForm(PlusPluginFormBase):
    test = forms.EmailField()
    test_model = PlusModelChoiceField(queryset=Test.objects.all())
    test_multi = PlusModelMultipleChoiceField(queryset=Test.objects.all())
