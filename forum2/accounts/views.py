from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
#from  .forms import UserForm
import uuid
from django.core.mail import send_mail
from .models import ActivateValidation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        # form = UserForm(request.POST)
        # if form.is_valid():
            # user = form.save(commit=False)
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        email = request.POST['email'].strip()
        user = User.objects.create_user(username, email, password)
        user.is_active = False  # 要将激活状态改为False
        user.save()

        # 获取激活码
        activate_key = str(uuid.uuid4()).replace('-', '')
        activate_link = 'http://%s/accounts/activate/%s' % (request.get_host(), activate_key)
        validate_user = ActivateValidation(user=user, activate_key=activate_key)
        validate_user.save()

        send_mail(subject='message',
                  message='It is a message %s' % activate_link,
                  # html_message='''点击<a href="%s">这里</a>激活''' % activate_link,
                  from_email='xxmeteobservatory@163.com',
                  recipient_list=[user.email],
                  fail_silently=False
                  )
        return render(request, 'registration/register_success.html')
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

@login_required
def upload_avatar(request):
    if request.method == 'GET':
        return render(request, 'upload_avatar.html')
    else:
        # 从POST请求中获取上传的文件，上传文件类似于字典，通过键名获取，键名即input属性中的name属性值
        # 获取的文件被Django封装成类似Python文件的对象
        avatar_file = request.FILES.get('avatar', None)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        upload_file_name = str(request.user.id) + '_' + avatar_file.name
        file_path = os.path.join(BASE_DIR, 'static', 'avatar', upload_file_name)

        with open(file_path, 'wb+') as destination:
            for chunk in avatar_file.chunks(): # 分段写入
                destination.write(chunk)

        url = 'http://' +  os.path.join('127.0.0.1', 'avatar', upload_file_name)
        print(url)
        profile = request.user.userprofile
        profile.avatar = url
        profile.save()

        return redirect('/')
