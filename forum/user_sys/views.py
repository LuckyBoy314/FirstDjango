from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from  .forms import UserForm
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return render(request, 'register_success.html')
        else:
            return render(request, self.template_name, {'form': form})

