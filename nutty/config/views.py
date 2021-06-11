# from django import forms
import re
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import serializers
from myprofile.models import Profile, Subscriberlist
from myprofile.forms import SubscriberForm
from myprofile.serializers import SubscriberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


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


class SubscriberAPIView(APIView):
    def get(self, request):
        # data = {
        #     "text": "Hello Nutty"
        # }
        # return JsonResponse(
        #     data
        # )


        subscriber = Subscriberlist.objects.all()
        serializers = SubscriberSerializer(subscriber, many=True)

        return Response(serializers.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():

            print(serializer.data)
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

