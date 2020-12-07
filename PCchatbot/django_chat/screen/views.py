from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from api.models import ChatInfo
from .forms import ChatInfoForm

# Create your views here.
def index(request):
    chatInfos = ChatInfo.objects.order_by('-pk')
    form = ChatInfoForm()
    context = {
        'chatInfos':chatInfos,
        'form':form,
    }
    return render(request, 'screen/index.html', context)

@require_POST
def create(request):
    if request.method == "POST":
        form = ChatInfoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('screen:index')

@require_POST
def delete(request, pk):
    chatInfo = get_object_or_404(ChatInfo, pk=pk)
    chatInfo.delete()
    return redirect('screen:index')