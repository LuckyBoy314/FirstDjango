from django.shortcuts import render, redirect
from message.models import Message
from django.contrib.auth.decorators import login_required

@login_required
def message_list(request):
    unread_messages = Message.objects.filter(owner=request.user, status=0).order_by('-id')
    return render(request, 'messages.html', {'unread_messages': unread_messages})


@login_required
def read_message(request, msg_id):
    msg_id = int(msg_id)
    read_message = Message.objects.get(id=msg_id)
    link = read_message.link
    read_message.status = -1
    read_message.save()
    return redirect(link)