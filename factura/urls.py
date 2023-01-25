from django.urls import path
from . import views

app_name = 'factura'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<slug>/', views.detail_department, name='list_invoice'),
    path('detail/', views.detail_invoice, name='detail_invoice'),
    path('page/', views.PageDetailView.as_view(), name='page'),
    path('form/', views.FormView.as_view(), name='form'),
    path('formset/<type>', views.formset_view, name='formset')
]
