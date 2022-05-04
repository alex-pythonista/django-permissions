from django.shortcuts import redirect, render
from app.models import Brand, Outlet, Items, Menu
from django.contrib.auth.decorators import login_required
from app.forms import BrandForm
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def brand_list(request):
    
    brands = Brand.objects.filter(owner=request.user)
    outlets = Outlet.objects.all()
    context = {'brands': brands, 'outlets': outlets}

    return render(request, 'brand_page.html', context)

@login_required
def add_brand(request):

    form = BrandForm()
    if request.method == 'POST':
        form = BrandForm(request.POST)
        user = request.user
        if form.is_valid():
            brand = form.save(commit=False)
            brand.owner = user
            brand.save()
            print(brand)
            return redirect('brands')

    context = {'form': form, 'add': True}
    return render(request, 'add_brand.html', context)

@login_required
def edit_brand(request, pk):

    brand = Brand.objects.get(pk=pk)
    form = BrandForm(instance=brand)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand.save()
            print(brand)
            return redirect('brands')

    context = {'form': form, 'brand_name': brand.name}
    return render(request, 'add_brand.html', context)

@login_required()
def delete_brand(request, pk):
    brand = Brand.objects.get(id=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brands')
    context = {'item': brand}
    return render(request, 'delete.html', context)