from django.shortcuts import render
from app.models import Brand, Outlet, Items, Menu
from django.contrib.auth.decorators import login_required


@login_required
def brand_list(request):
    
    brands = Brand.objects.filter(owner=request.user)
    outlets = Outlet.objects.all()
    context = {'brands': brands, 'outlets': outlets}

    return render(request, 'brand_page.html', context)
