from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView, View, TemplateResponseMixin

from .forms import BuyruqForm, FormFacturaType, Dalolatnona_formset, FacturaForm, FileFormset, ImageFormset
from .models import FacturaType, Department
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from django.http import HttpResponse


class Dashboard(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'factura/dashboard.html'

    def get(self, request):
        departments = Department.objects.exclude(user=request.user)
        return self.render_to_response({
            'object_list': departments
        })


dashboard = Dashboard.as_view()


class DetailDepartment(DetailView):
    template_name = 'factura/second.html'
    model = Department
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def dispatch(self, request, *args, **kwargs):
        self.form = FacturaForm()
        self.formset = Dalolatnona_formset()

        return super().dispatch(request, *args, **kwargs)

    # def get(self, request):
    #     form = FormFacturaType()
    #     list_type = FacturaType.objects.all()
    #     form_class = Dalolatnona_formset()
    #
    #     return self.render_to_response({
    #         'form': form,
    #         'list_type': list_type,
    #         'formset': form_class
    #     })
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['formset_dalolatnoma'] = self.formset
        context['form'] = FormFacturaType()
        context['list_type'] = FacturaType.objects.all()
        context['formset'] = Dalolatnona_formset()
        # context['file_formset'] = self.file_formset
        # context['image_formset'] = self.image_formset
        return context

    # def post(self, request):
    #     form = FacturaForm()
    #     list_type = FacturaType.objects.all()
    #     form_class = Dalolatnona_formset()
    #
    #     return self.render_to_response({
    #         'form': form,
    #         'list_type': list_type,
    #         'formset': form_class
    #     })


# отделлар
detail_department = DetailDepartment.as_view()


class FormsetView(View):

    def post(self, request, type=None):
        form = FacturaForm(request.POST, request.FILES)
        file_formset = FileFormset(request.POST, request.FILES)
        image_formset = ImageFormset(request.POST, request.FILES)
        print(form.is_valid())
        print(image_formset.is_valid())
        print(file_formset.is_valid())
        return redirect('factura:list_invoice')


formset_view = FormsetView.as_view()


class FormView(JsonRequestResponseMixin, FormView):
    template_name = 'forms/formset.html'
    form_class = BuyruqForm

    def post(self, request):
        form = FacturaForm()
        file_formset = FileFormset()
        image_formset = ImageFormset()

        type_doc = self.request_json['type']

        if type_doc == 'Далолатнома':
            print(type_doc)
            self.form_class = Dalolatnona_formset()
        elif type_doc == 'Хат турини танлаш' or type_doc != 'Далолатнома':

            self.form_class = BuyruqForm
            return render(request, 'forms/blank.html')
        return self.render_to_response({
            'formset': self.form_class,
            'form': form,
            'file_formset': file_formset,
            'image_formset': image_formset,
        })


class DetailInvoice(TemplateView, View):
    template_name = 'factura/detail_factura.html'


detail_invoice = DetailInvoice.as_view()


class PageDetailView(TemplateResponseMixin, View):
    template_name = 'forms/page.html'

    def get(self, request, type):
        form = FormFacturaType()

        return self.render_to_response({
            'form': form,
            # 'formset':form_class
        })
