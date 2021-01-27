from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from .models import PurchaseDocument
from .forms import PurchaseDocumentModelForm
from django.views.generic import edit
from django.views.generic.edit import UpdateView

from goods.models import Goods


class PurchaseUpdate(UpdateView):
    model = PurchaseDocument
    template_name = 'purchase_html/change.html'
    fields = '__all__'


def purchase_list_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Начальная страница</h1>")
    purchase_list = PurchaseDocument.objects.all()
    # goods_list = GoodsModelForm
    return render(request, "purchase_html/list.html", {'purchase_list': purchase_list})
    # return render(request, )


def purchase_detail_view(request, pk):
    try:
        purchase_detail = PurchaseDocument.objects.get(pk=pk)
    except PurchaseDocument.DoesNotExist:
        raise Http404
    return render(request, "purchase_html/detail.html", {'purchase': purchase_detail})


def purchase_create_view(request, *args, **kwargs):
    form = PurchaseDocumentModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        goods = Goods.objects.get(name=form.cleaned_data.get('goods_id'))
        goods.count = goods.count + form.cleaned_data.get('quantity')
        goods.save()
        obj.save()
        form = PurchaseDocumentModelForm()

    return render(request, "purchase_html/create.html", {"form": form})


def purchase_delete_view(request, pk):
    # new_to_delete = get_object_or_404(Goods)
    purchase_delete = PurchaseDocument.objects.get(pk=pk)
    goods = Goods.objects.get(name=purchase_delete.goods_id)
    goods.count = goods.count - purchase_delete.quantity
    goods.save()

    # goods_count(request, pk, purchase_delete.quantity)
    purchase_delete.delete()
    return render(request, "purchase_html/delete.html")


def back(request):
    return redirect('/purchase')


def home(request):
    return redirect('/')

#
# def goods_count(request, pk, count):
#     goods_change_count(request, pk, count)
