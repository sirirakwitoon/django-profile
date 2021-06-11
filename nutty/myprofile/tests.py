# from django.http import response
from django.test import TestCase
from myprofile.models import Profile, Subscriberlist


class TestProfile(TestCase):
    def test_profile_should_have_defined_fields(self):
        profile = Profile.objects.create(
            name="Sirirak"
        )

        assert profile.name == "Sirirak"

    def test_profile_should_have_fields_email(self):
        profile = Profile.objects.create(
            email="nutsrk@odds.team"
        )
        assert profile.email == "nutsrk@odds.team"


class TesSubscriberlist(TestCase):
    def test_scriberlist_should_have_email(self):
        subscriberlist = Subscriberlist.objects.create(
            email="nutsrk@odds.team"
        )
        assert subscriberlist.email == "nutsrk@odds.team"


class TestIndexView(TestCase):
    def test_index_view_should_my_name(self):
        # Given
        Profile.objects.create(name="Sirirk")

        # When
        response = self.client.get("/")
        response = self.client.get("/")

        # Then
        assert response.status_code == 200

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        # Given

        Profile.objects.create(name="Sirirak")

        # When
        data = {
            "email": "nutsrk@odds.team"
        }
        response = self.client.post("/", data=data)
        assert response.email == "nutsrk@odds.team"
        # Then
        subscriber = Subscriberlist.objects.last()
        assert subscriber.email == "nutsrk@odds.team"

    def test_index_view_should_not_save_subscriber_email_when_email_is_invalid(self):
        # Given
        Profile.objects.create(name="Sirirak")

        # When
        data = {
            "email": "nutty.com"
        }
        self.client.post("/", data={"email": "nutsrk@odds.team"})
        self.client.post("/", data=data)

        # Then
        subscriber = Subscriberlist.objects.last()
        assert subscriber.email != "nutty.com"
