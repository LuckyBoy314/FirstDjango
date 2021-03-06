from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from  .forms import UserForm
import uuid
from django.core.mail import send_mail
from .models import ActivateValidation
from django.contrib.auth.models import User

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):

        #form = UserForm(request.POST)
        #if form.is_valid():
            #user = form.save(commit=False)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.is_active = False
        user.save()

        activate_key = str(uuid.uuid4()).replace('-', '')
        activate_link = 'http://%s/accounts/activate/%s' % (request.get_host(), activate_key)
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
        #else:
        #    return render(request, self.template_name, {'form': form})

def activate(request, activate_key):
    if ActivateValidation.objects.filter(activate_key=activate_key).exists():
        user = ActivateValidation.objects.get(activate_key=activate_key).user
        user.is_active = True
        user.save() # 修改记录以后一定要保存！！！

        return HttpResponse('<h2>激活成功!</h2>')
    else:
        return HttpResponse('<h2>激活失败!</h2>')
