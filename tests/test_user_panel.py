from typing import Union

from django.contrib.auth import get_user
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse


class UserPanelTests(TestCase):
    def assertCurrentUser(self, expected_user: Union[User, AnonymousUser]) -> None:
        request = HttpRequest()
        request.session = self.client.session
        user = get_user(request)
        self.assertEqual(expected_user, user, "Wrong user on session")

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create(
            email='demo@example.com',
            username='demo-example',
        )
        User.objects.create(
            email='other@example.com',
            username='other-example',
        )

    def test_login_form_view(self) -> None:
        response = self.client.post(
            reverse('djdt:debug-userpanel-login-form'),
            data={'val': self.user.email},
        )
        self.assertRedirects(
            response,
            '/',
            fetch_redirect_response=False,
        )
        self.assertCurrentUser(self.user)

    def test_login_id_view(self) -> None:
        response = self.client.post(
            reverse('djdt:debug-userpanel-login', args=(self.user.pk,)),
        )
        self.assertRedirects(
            response,
            '/',
            fetch_redirect_response=False,
        )
        self.assertCurrentUser(self.user)

    def test_logout_view(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('djdt:debug-userpanel-logout'),
        )
        self.assertRedirects(
            response,
            '/',
            fetch_redirect_response=False,
        )
        self.assertCurrentUser(AnonymousUser())
