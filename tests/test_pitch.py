import unittest
from app.models import User, Post


class PostModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='James', password='potato', email='james@ms.com')
        self.new_post = Post(id=1, post_title='Test', post_content='This is a test post', category="interview",
                               user=self.user_James, likes=0, dislikes=0)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.post_title, 'Test')
        self.assertEquals(self.new_post.post_content, 'This is a test post')
        self.assertEquals(self.new_post.category, "interview")
        self.assertEquals(self.new_post.user, self.user_James)

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_post = Post.get_post(1)
        self.assertTrue(got_post is not None)
