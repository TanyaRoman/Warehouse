from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Manager
from .forms import ManagerModelFormForChange, ManagerModelForm
from django.views.generic import edit
from django.views.generic.edit import UpdateView


class ManagerUpdate(UpdateView):
    model = Manager
    template_name = 'manager_html/change.html'
    fields = '__all__'


def manager_list_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Начальная страница</h1>")
    manager_list = Manager.objects.all()
    # goods_list = GoodsModelForm
    return render(request, "manager_html/list.html", {'manager_list': manager_list})
    # return render(request, )


def manager_detail_view(request, pk):
    try:
        manager_detail = Manager.objects.get(pk=pk)
    except Manager.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Goods id {goods_detail}")
    return render(request, "manager_html/detail.html", {'manager': manager_detail})


def manager_create_view(request, *args, **kwargs):
    form = ManagerModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = ManagerModelForm()
    return render(request, "manager_html/create.html", {"form": form})


# def manager_change_view(request, *args, **kwargs):
#     form = ManagerModelFormForChange(request.POST or None)
#     if form.is_valid():
#         obj = form.clean()
#         obj.save()
#         form = ManagerModelFormForChange()
#     return render(request, "manager_html/create.html", {"form": form})


def manager_delete_view(request, pk):
    # new_to_delete = get_object_or_404(Goods)
    manager_delete = Manager.objects.get(pk=pk)
    manager_delete.delete()
    return render(request, "manager_html/delete.html")


def back(request):
    return redirect('/manager')


def home(request):
    return redirect('/')


# class GoodsChangeView(edit.UpdateView):
#     goods = GoodsModelForm
#     # form = GoodsModelFormForChange(request.POST or None)
