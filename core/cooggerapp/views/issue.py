# django
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

# model
from core.cooggerapp.models import (UTopic, Issue, Commit)

# form
from core.cooggerapp.forms import NewIssueForm, ReplyIssueForm

# utils 
from core.cooggerapp.utils import paginator

# python
import json


class IssueView(TemplateView):
    template_name = "issue/index.html"

    def get_context_data(self, username, topic, **kwargs):
        user = authenticate(username=username)
        utopic = UTopic.objects.filter(user=user, name=topic)[0]
        issues = Issue(user=user, utopic=utopic)
        context = super().get_context_data(**kwargs)
        context["content_user"] = user
        context["queryset"] = issues.get_open_issues
        context["utopic"] = utopic
        return context


class NewIssue(LoginRequiredMixin, View):
    template_name = "issue/new.html"
    form_class = NewIssueForm
    
    def get(self, request, username, topic):
        user = authenticate(username=username)
        context = dict(
            issue_form=self.form_class,
            content_user=user,
            utopic=UTopic.objects.filter(user=user, name=topic)[0]
        )
        return render(request, self.template_name, context)

    def post(self, request, username, topic):
        if request.user.username == username:
            user = authenticate(username=username)
            utopic = UTopic.objects.filter(user=user, name=topic)[0]
            issue_form = self.form_class(request.POST)
            if issue_form.is_valid():
                issue_form = issue_form.save(commit=False)
                issue_form.user = user
                issue_form.utopic = utopic
                issue_form.save()
                return redirect(
                    reverse(
                        "detail-issue", 
                        kwargs=dict(
                            username=request.user.username,
                            topic=topic,
                            permlink=issue_form.permlink)
                        )
                    )


class DetailIssue(View):
    template_name = "issue/detail.html"
    form_class = ReplyIssueForm

    def get(self, request, username, topic, permlink):
        user = authenticate(username=username)
        utopic = UTopic.objects.get(user=user, name=topic)
        issue = Issue.objects.get(user=user, utopic=utopic, permlink=permlink)
        context = dict(
            content_user=issue.user,
            queryset=issue,
            utopic=utopic,
            md_editor=True,
        )
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, username, topic, permlink):
        if request.user.username == username and request.is_ajax:
            user = authenticate(username=username)
            utopic = UTopic.objects.filter(user=user, name=topic)[0]
            issue = Issue.objects.get(user=user, utopic=utopic, permlink=permlink)
            issue_form = self.form_class(request.POST)
            if issue_form.is_valid():
                issue_form = issue_form.save(commit=False)
                issue_form.user = user
                issue_form.utopic = utopic
                issue_form.reply = issue
                issue_form.save()
                new_reply = Issue.objects.get(
                    user=user, 
                    utopic=utopic, 
                    permlink=issue_form.permlink)
                return HttpResponse(
                    json.dumps(
                        dict(
                            username=new_reply.username,
                            topic_name=new_reply.topic_name,
                            parent_permlink=new_reply.parent_permlink,
                            parent_username=new_reply.parent_username,
                            get_absolute_url=new_reply.get_absolute_url,
                            created=str(new_reply.created),
                            reply_count=new_reply.reply_count,
                            status=new_reply.status,
                            reply=new_reply.reply_id,
                            body=new_reply.body,
                            title=new_reply.title,
                            permlink=new_reply.permlink,
                            )
                        )
                    )