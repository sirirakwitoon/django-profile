from django.http import response
from django.test import TestCase
from myprofile.models import Profile, Subscriberlist


class TestProfile(TestCase):
    def test_profile_should_have_defined_fields(self):
        profile = Profile.objects.create(
            name="Sirirak"
        )

        assert profile.name == "Sirirak"


class TestIndexView(TestCase):
    def test_index_view_should_my_name(self):
        Profile.objects.create(name="Sirirk")

        response = self.client.get("/")

        response = self.client.get("/")
        assert response.status_code == 200

    def test_index_view_should_save_subscriber_email_when_input_form(self):

        Profile.objects.create(name="Sirirak")

        data = {
            "email" "nutsrk@odds.team"

        }
        response = self.client.post("/", data=data)

        # Then
        a = Subscriberlist.objects.last()
        assert a.email == "nutsrk@odds.team"
