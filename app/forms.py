from dataclasses import field
from django import forms
from django.forms import ModelForm
from app.models import Brand, Items, Outlet, Menu


class BrandForm(ModelForm):

    class Meta:
        model = Brand
        fields = ['name', 'manager']