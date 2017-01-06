from django.shortcuts import render
from django.utils import timezone
from list.models import Item
from list.serializers import ItemSerializer
from list.forms import ItemForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    items = Item.objects.filter(archived=False).order_by('created_date')
    return render(request, 'list/item.html', {'items': items})


def archived(request):
    items = Item.objects.filter(archived=True).order_by('created_date')
    return render(request, 'list/item.html', {'items': items})


def new(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "list/new.html", {"formset": form, 'all_okay': False})


def archive(request, id):
    item = get_object_or_404(Item, pk=id)

    if item.archived:
        item.dearchive()
    else:
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


def delete(request, id):
    item = get_object_or_404(Item, pk=id)

    if item.archived:
        item.delete()
        return HttpResponseRedirect(reverse('archived'))
    else:
        item.delete()
        return HttpResponseRedirect(reverse('index'))


@api_view(['GET'])
def item_collection(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def item_element(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
