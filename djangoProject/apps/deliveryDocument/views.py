from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from .models import DeliveryDocument
from .forms import DeliveryDocumentModelForm
from django.views.generic import edit
from django.views.generic.edit import UpdateView


class DeliveryUpdate(UpdateView):
    model = DeliveryDocument
    template_name = 'delivery_html/change.html'
    fields = '__all__'


def delivery_list_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Начальная страница</h1>")
    delivery_list = DeliveryDocument.objects.all()
    # goods_list = GoodsModelForm
    return render(request, "delivery_html/list.html", {'delivery_list': delivery_list})
    # return render(request, )


def delivery_detail_view(request, pk):
    try:
        delivery_detail = DeliveryDocument.objects.get(pk=pk)
    except DeliveryDocument.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Goods id {goods_detail}")
    return render(request, "delivery_html/detail.html", {'delivery': delivery_detail})


def delivery_create_view(request, *args, **kwargs):
    form = DeliveryDocumentModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = DeliveryDocumentModelForm()

    return render(request, "delivery_html/create.html", {"form": form})


# def goods_change_view(request, pk):
#     try:
#         goods = Goods.objects.get(pk=pk)
#         if request.method == "POST":
#             goods.name = request.POST.get("name")
#             goods.category = request.POST.get("category")
#             goods.count = request.POST.get("count")
#             goods.prise = request.POST.get("prise")
#             goods.save()
#             return render(request, "goods_html/change.html", {"goods": goods})
#     except Goods.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")
#     # goods_change = Goods.objects.get(pk=pk)
#     # # goods_change.update()
#     # form = GoodsModelFormForChange(request.POST, instance=goods_change)
#     # if form.is_valid():
#     #     obj = form.clean()
#     #     obj.update()
#     #     form = GoodsModelFormForChange()


def delivery_delete_view(request, pk):
    # new_to_delete = get_object_or_404(Goods)
    delivery_delete = DeliveryDocument.objects.get(pk=pk)
    delivery_delete.delete()
    return render(request, "delivery_html/delete.html")


def back(request):
    return redirect('/delivery')


def home(request):
    return redirect('/')
