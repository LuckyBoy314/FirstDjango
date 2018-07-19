from django.shortcuts import render
from .models import Comment
from article.models import Article
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)


@login_required
def create_comment(request):
    article_id = int(request.POST["article_id"])
    content = request.POST["content"].strip()
    to_comment_id = int(request.POST.get("to_comment_id", 0))

    if not content:
        return json_response({"status": "error",
                              "msg": "评论内容不能为空."})
    article = Article.objects.get(id=article_id)

    if to_comment_id!= 0:
        to_comment = Comment.objects.get(id=to_comment_id)
    else:
        to_comment = None

    comment = Comment(to_comment=to_comment, article=article, owner=request.user, content=content)
    comment.save()
    return json_response({"status": "ok", "msg": ""})