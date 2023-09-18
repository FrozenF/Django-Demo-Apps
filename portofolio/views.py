from django.shortcuts import render, redirect, get_object_or_404
from .models import PortofolioItem
from .forms import PortofolioItemForm

def portofolio(request):
    items = PortofolioItem.objects.all()
    return render(request, 'portofolio/portofolio.html', {'items': items})

def create_portofolio_item(request):
    if request.method == 'POST':
        form = PortofolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portofolio')
    else:
        form = PortofolioItemForm()
    return render(request, 'portofolio/create.html', {'form': form})

def edit_portofolio_item(request, pk):
    item = get_object_or_404(PortofolioItem, pk=pk)
    if request.method == 'POST':
        form = PortofolioItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('portofolio')
    else:
        form = PortofolioItemForm(instance=item)
    return render(request, 'portofolio/update.html', {'form': form, 'item': item})

def delete_portofolio_item(request, pk):
    item = get_object_or_404(PortofolioItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('portofolio')
    return render(request, 'portofolio/delete.html', {'item': item})