from django.test import TestCase


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
