import pytest

from курсовая_3.bp_posts.dao.post import Post
from курсовая_3.bp_posts.dao.post_dao import PostDAO

def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    for field in fields:
        assert hasattr(post, field), f'Нет поля {field}'


class TestPostsDAO:
    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO('post_mock.json')
        return post_dao_instance

    ###Функция получения всех

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, 'incorrect type for result'
        post = post_dao.get_all()[0]
        assert type(post) == Post, 'Incorrect type for result single item'

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_all()
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_all()
        correct_pks = {1, 2, 3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, 'Не совпадают полученные id'

        ###Функция получения одного по pk

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, 'Incorrect type for result single item'

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_by_pk(999)
        assert post is None, 'Should be None for non existent pk'

    @pytest.mark.parametrize('pk', [1,2,3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_by_pk(pk)
        assert post.pk == pk, f'Incorrect post.pk for requesten post with pk'

        ###Функция получения постов по имени автора






