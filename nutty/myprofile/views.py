# from django import forms
from django.shortcuts import render
from django.views import View
from myprofile.models import Profile, Subscriberlist
from myprofile.forms import SubscriberForm


def index(request):
    return render(request, "index.html")


class IndexView(View):
    def get(self, request):
        name = Profile.objects.get(id=1).name

        form = SubscriberForm()

        facebook_url = "https://www.facebook.com/nut.ty.125"
        instagram_url = "https://www.instagram.com/nutsrk/"
        github_url = "https://github.com/sirirakwitoon/"
        return render(
            request,
            "index.html",
            {
                "name": name,
                "facebook_url": facebook_url,
                "instagram_url": instagram_url,
                "github_url": github_url,
                "form": form,
            },
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get("email"))

        name = Profile.objects.get(id=1).name

        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("email"))
            Subscriberlist.objects.create(email=form.cleaned_data.get("email"))
            # Ready to save into

        facebook_url = "https://www.facebook.com/nut.ty.125"
        instagram_url = "https://www.instagram.com/nutsrk/"
        github_url = "https://github.com/sirirakwitoon/"

        return render(
            request,
            "index.html",
            {
                "name": name,
                "facebook_url": facebook_url,
                "instagram_url": instagram_url,
                "github_url": github_url,
                "form": form,
            },
        )
