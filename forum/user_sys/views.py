from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from  .forms import UserForm
import uuid
from django.core.mail import send_mail
from .models import ActivateValidation


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

            activate_key = str(uuid.uuid4()).replace('-', '')
            activate_link = 'http://%s/user/activate/%s' % (request.get_host(), activate_key)
            validate_user = ActivateValidation(user=user, activate_key=activate_key)
            validate_user.save()

            send_mail(subject='message',
                      message='It is a message %s' % activate_link,
                      #html_message='''点击<a href="%s">这里</a>激活''' % activate_link,
                      from_email='xxmeteobservatory@163.com',
                      recipient_list=[user.email],
                      fail_silently=False
                      )
            return render(request, 'register_success.html')
        else:
            return render(request, self.template_name, {'form': form})

def activate(request, activate_key):
    if ActivateValidation.objects.filter(activate_key=activate_key).exists():
        return HttpResponse('激活成功!')
    else:
        return HttpResponse('激活失败!')
