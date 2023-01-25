from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
import uuid
from slugify import slugify


# Create your models here.

class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='department')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.full_name}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Factura(MPTTModel):
    waiting = _('waiting')
    refusal = _('refusal')
    accepted = _('accepted')

    status_choice = [
        ('waiting', waiting,),
        ('refusal', refusal,),
        ('accepted', accepted,),
    ]
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    owner = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='factura')

    no_doc = models.CharField(max_length=20)
    date_doc = models.DateField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=status_choice)
    view = models.DateTimeField(blank=True)


class FacturaType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FacturaSpecification(models.Model):
    factura_type = models.ForeignKey(FacturaType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class FacturaSpecificationValue(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='factura_specification_value')
    factura_specification = models.ForeignKey(FacturaSpecification, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, blank=True)
    value_date = models.DateField(blank=True)


class File(models.Model):
    file = models.FileField(upload_to='files')
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='file')


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='image')
