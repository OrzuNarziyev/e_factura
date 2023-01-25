from django import forms
from .models import Factura, Department, FacturaSpecification, FacturaType, FacturaSpecificationValue, Image, File
from django.forms.models import inlineformset_factory
from django.forms import formset_factory


class FormFacturaType(forms.Form):
    xujjat_turi = forms.ModelChoiceField(label='Xujjat turi', queryset=FacturaType.objects.all(),
                                         empty_label='Хат турини танлаш')


class FacturaForm(forms.ModelForm):
    no_doc = forms.CharField(label='№ документ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_doc = forms.DateTimeField(
        label="Дата Документ",
        widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}))
    description = forms.CharField(label='Киска Мазмун',
                                  widget=forms.Textarea(
                                      attrs={'placeholder': 'Киска Мазмун', 'class': 'form-control', 'rows': '2', }))

    class Meta:
        model = Factura
        fields = ['no_doc', 'date_doc', 'description']


class BuyruqForm(forms.Form):
    hujjat_no = forms.CharField()
    doc_date = forms.DateTimeField(widget=forms.DateTimeInput)
    description = forms.CharField(widget=forms.Textarea)


class DalolatnomaForm(forms.Form):
    name = forms.CharField(label='ФИО', help_text="Имзо чекувчи исм шариши",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Имзо чекувчи исм шариши'}))


class FileModelFormset(forms.ModelForm):
    file = forms.FileField(label='Файл',
                           widget=forms.FileInput(attrs=
                                                  {'class': 'form-control'}))

    class Meta:
        model = File
        fields = ['file']


class ImageModelFormset(forms.ModelForm):
    image = forms.ImageField(
        label='Расм ',
        widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Image
        fields = ['image']


Dalolatnona_formset = formset_factory(DalolatnomaForm, extra=1)

FileFormset = inlineformset_factory(Factura, File, FileModelFormset, extra=1, fields=['file'])
ImageFormset = inlineformset_factory(Factura, Image, ImageModelFormset, extra=1, fields=['image'])

# department formset
# DepartmentFormset = inlineformset_factory(Department, Factura, extra=1, fields=['user'])
