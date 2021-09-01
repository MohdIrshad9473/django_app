from django.shortcuts import render
from django.shortcuts import render
from .form import MyForm

# Create your views here.
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'myapp/task.html', {'form': form})

