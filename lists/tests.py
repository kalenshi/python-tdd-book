from django.test import TestCase
from rest_framework import status

from lists.models import Item


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        request_data = {"item_text": "A new list item"}
        self.client.post("/", data=request_data)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(request_data["item_text"], new_item.text)

    def test_redirect_after_a_post(self) -> None:
        request_data = {"item_text": "A new list item"}
        response = self.client.post("/", data=request_data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response["location"], "/lists/the-only-list-in-the-world/")

    def test_only_saves_items_when_necessary(self) -> None:
        self.client.get("/")
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):

    def test_save_and_retrieving_items(self) -> None:
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(2, saved_items.count())

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")


class ListViewTest(TestCase):
    def test_displays_all_items(self) -> None:
        Item.objects.create(text="itemy 1")
        Item.objects.create(text="itemy 2")

        response = self.client.get("/lists/the-only-list-in-the-world/")

        self.assertContains(response, "itemy 1")
        self.assertContains(response, "itemy 2")
        self.assertTemplateUsed(response, "list.html")
