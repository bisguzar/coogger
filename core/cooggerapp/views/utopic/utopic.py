from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import TemplateView

from ...forms import UTopicForm
from ...models import Content, Topic, UTopic
from ..user.users import Common
from ..utils import create_redirect, paginator


class UserTopic(Common):
    template_name = "users/topic/index.html"

    def get_context_data(self, username, **kwargs):
        context = super().get_context_data(username, **kwargs)
        user = context["current_user"]
        context["queryset"] = paginator(self.request, UTopic.objects.filter(user=user))
        return context


class DetailUserTopic(TemplateView):
    "topic/@username"
    template_name = "users/topic/detail/contents.html"

    def get_context_data(self, username, permlink, **kwargs):
        user = get_object_or_404(User, username=username)
        utopic = UTopic.objects.get(user=user, permlink=permlink)
        queryset = Content.objects.filter(utopic=utopic).order_by("created")
        context = super().get_context_data(**kwargs)
        context["current_user"] = user
        context["queryset"] = queryset
        context["utopic"] = utopic
        return context


class CreateUTopic(LoginRequiredMixin, View):
    template_name = "forms/create.html"
    form_class = UTopicForm
    model = UTopic

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            dict(form=self.form_class(initial=dict(request.GET.items()))),
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            try:
                form.save()
            except IntegrityError:
                messages.warning(
                    request, f"{form.name.lower()} is already taken by yours"
                )
                return render(
                    request,
                    self.template_name,
                    dict(form=self.form_class(data=request.POST)),
                )
            return redirect(
                reverse(
                    "detail-utopic",
                    kwargs=dict(permlink=form.permlink, username=str(form.user)),
                )
            )
        return render(request, self.template_name, dict(form=form))


class UpdateUTopic(LoginRequiredMixin, View):
    template_name = "forms/create.html"
    form_class = UTopicForm
    update_fields = form_class._meta.fields

    def get(self, request, permlink, *args, **kwargs):
        instance_query = UTopic.objects.filter(user=request.user, permlink=permlink)
        if not instance_query.exists():
            messages.warning(request, f"you need to create the {permlink} topic first.")
            return redirect(reverse("create-utopic") + f"?name={permlink}")
        context = dict(
            form=self.form_class(instance=instance_query[0]), permlink=permlink
        )
        return render(request, self.template_name, context)

    def post(self, request, permlink, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form_ = form.save(commit=False)
            queryset = UTopic.objects.get(user=request.user, permlink=permlink)
            for field in self.update_fields:
                setattr(queryset, field, getattr(form_, field, None))
            if permlink != slugify(form_.name):
                self.update_fields.append("permlink")
                create_redirect(
                    old_path=reverse(
                        "detail-utopic",
                        kwargs=dict(username=str(request.user), permlink=permlink),
                    ),
                    new_path=reverse(
                        "detail-utopic",
                        kwargs=dict(
                            username=str(request.user), permlink=slugify(form_.name)
                        ),
                    ),
                )
                # new global topic save
                # TODO think about it.
                try:
                    topic = Topic.objects.get(permlink=permlink)
                except ObjectDoesNotExist:
                    Topic(name=form_.name.lower()).save()
                else:
                    if topic.how_many == 0:
                        topic.permlink = slugify(form_.name)
                        topic.save(update_fields=["permlink"])
                    else:
                        Topic(name=form_.name.lower()).save()
            try:
                queryset.save(update_fields=self.update_fields)
            except IntegrityError:
                messages.warning(
                    request, f"{form_.name.lower()} is already taken by yours"
                )
                return render(request, self.template_name, dict(form=form))
            else:
                return redirect(
                    reverse(
                        "detail-utopic",
                        kwargs=dict(
                            permlink=slugify(form_.name), username=str(request.user)
                        ),
                    )
                )
        return render(request, self.template_name, dict(form=form, permlink=permlink))
