from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from .models import Goods
from .forms import GoodsModelFormForChange, GoodsModelForm
from django.views.generic import edit
from django.views.generic.edit import UpdateView


class GoodsUpdate(UpdateView):
    model = Goods
    template_name = 'goods_html/change.html'
    fields = '__all__'


def goods_list_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Начальная страница</h1>")
    goods_list = Goods.objects.all()
    # goods_list = GoodsModelForm
    return render(request, "goods_html/list.html", {'goods_list': goods_list})
    # return render(request, )


def goods_detail_view(request, pk):
    try:
        goods_detail = Goods.objects.get(pk=pk)
    except Goods.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Goods id {goods_detail}")
    return render(request, "goods_html/detail.html", {'goods': goods_detail})


def goods_create_view(request, *args, **kwargs):
    form = GoodsModelFormForChange(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = GoodsModelFormForChange()
    return render(request, "goods_html/create.html", {"form": form})


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


def goods_delete_view(request, pk):
    # new_to_delete = get_object_or_404(Goods)
    goods_delete = Goods.objects.get(pk=pk)
    goods_delete.delete()
    return render(request, "goods_html/delete.html")


def back(request):
    return redirect('/goods')


def home(request):
    return redirect('/')


# class GoodsUpdateCount(UpdateView):
#     model = Goods
#     # template_name = 'goods_html/change.html'
#     fields = ['count']


# def goods_change_count(request, pk, count):
#     # form = GoodsModelFormForChange(request.POST or None)
#     goods = Goods.objects.get(pk=pk)
#     goods.count = goods.count + count
#     # if form.is_valid():
#     #     obj = form.save(commit=False)
#     #     obj.save()
#         # form = GoodsModelFormForChange()
#     # return render(request, "goods_html/create.html", {"form": form})


# class GoodsChangeView(edit.UpdateView):
#     goods = GoodsModelForm
#     # form = GoodsModelFormForChange(request.POST or None)
