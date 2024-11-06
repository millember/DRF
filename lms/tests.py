from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User


class LmsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(title='course_test', owner=self.user)
        self.lesson = Lesson.objects.create(title='lesson_test', description='test description', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тест на просмотр урока"""
        url = reverse("lms:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        """Тест на создание урока"""
        url = reverse("lms:lesson_create")
        data = {
            "title": "Test",
            "description": "Test description",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)



    def test_lesson_update(self):
        """Тест на апдейт данных урока"""
        url = reverse("lms:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Test update",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test update")

    def test_lesson_delete(self):
        url = reverse("lms:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('lms:lesson_list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriptionTestCase(APITestCase):
    """Тест функционала работы подписки на обновления курса"""

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(title="Test Course", description="Test Course description")
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse("lms:course_subscribe")
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Подписка отключена"})