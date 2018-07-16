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

    if not content:
        return json_response({"status": "error",
                              "msg": "评论内容不能为空."})
    article = Article.objects.get(id=article_id)

    comment = Comment(article=article, owner=request.user,
                      content=content)
    comment.save()
    return json_response({"status": "ok", "msg": ""})