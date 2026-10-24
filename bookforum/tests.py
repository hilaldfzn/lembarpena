from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from bookforum.models import ForumComment, ForumHead


class UniqueCommentsJsonTest(TestCase):
    def test_missing_forum_returns_404(self):
        response = self.client.get(reverse("bookforum:show_uniquecomments_json", args=[999]))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["status"], "error")

    def test_existing_forum_returns_comments(self):
        user = User.objects.create_user("reader")
        forum = ForumHead.objects.create(user=user, title="Judul", question="Pertanyaan")
        ForumComment.objects.create(user=user, comment_to=forum, answer="Jawaban")

        response = self.client.get(reverse("bookforum:show_uniquecomments_json", args=[forum.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual([c["fields"]["answer"] for c in response.json()], ["Jawaban"])
