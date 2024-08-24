from django.shortcuts import render, get_list_or_404, get_object_or_404
from .forms import ChaiVareityform
from .models import ChaiVariety, Store

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        # form with values filled submission state
        form = ChaiVareityform(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety'] #from the Chai Variety Form
            stores = Store.objects.filter(chai_varieties = chai_variety)
    else:
        '''form default state without any value association, not handling this case will result in UnboundLocalError: cannot access local variable 'form' where it is not associated with a value'''
        form = ChaiVareityform()
    return render(request, 'chai/chai_store.html', {'stores': stores, 'form': form})