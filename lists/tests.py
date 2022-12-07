from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_post_request(self):
        request_data = {"item_text": "A new list item"}
        response = self.client.post("/", data=request_data)

        self.assertIn(
            request_data["item_text"], response.content.decode("utf8")
        )
        self.assertTemplateUsed(response, "home.html")


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
