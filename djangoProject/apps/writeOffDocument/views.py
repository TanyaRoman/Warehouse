from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from .models import WriteOffDocument
from .forms import WriteOffDocumentModelForm
from django.views.generic import edit
from django.views.generic.edit import UpdateView


class WriteOffUpdate(UpdateView):
    model = WriteOffDocument
    template_name = 'write_off_html/change.html'
    fields = '__all__'


def write_off_list_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Начальная страница</h1>")
    write_off_list = WriteOffDocument.objects.all()
    # goods_list = GoodsModelForm
    return render(request, "write_off_html/list.html", {'write_off_list': write_off_list})
    # return render(request, )


def write_off_detail_view(request, pk):
    try:
        write_off_detail = WriteOffDocument.objects.get(pk=pk)
    except WriteOffDocument.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Goods id {goods_detail}")
    return render(request, "write_off_html/detail.html", {'write_off': write_off_detail})


def write_off_create_view(request, *args, **kwargs):
    form = WriteOffDocumentModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = WriteOffDocumentModelForm()

    return render(request, "write_off_html/create.html", {"form": form})


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


def write_off_delete_view(request, pk):
    # new_to_delete = get_object_or_404(Goods)
    write_off_delete = WriteOffDocument.objects.get(pk=pk)
    write_off_delete.delete()
    return render(request, "write_off_html/delete.html")


def back(request):
    return redirect('/write_off')


def home(request):
    return redirect('/')
