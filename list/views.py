from django.shortcuts import render
from django.utils import timezone
from list.models import Item
from list.forms import ItemForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'list/item.html', {'items': items})


def new(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('index'))

    context = {
        "formset": form
    }
    return render(request, "list/new.html", context)


def archive(request, id):
    item = get_object_or_404(Item, pk=id)
    item.archive()
    return HttpResponseRedirect(reverse('index'))


def edit(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    context = {
        "formset": form
    }
    return render(request, "list/edit.html", context)
