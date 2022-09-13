import json
from json import JSONDecodeError
from pprint import pprint as pp

#from post import Post
from курсовая_3.bp_posts.dao.post import Post
from курсовая_3.exceptions.data_exceptions import DataSourceError


class PostDAO:
    '''Менеджер постов - загружает, ищет, вытаскивает по рк и пользователя '''
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        '''Загружает данные из JSON и возвращает список словарей'''
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удаётся получить данные из файла {self.path}')
        return posts_data

    def _load_posts(self):
        '''Возвращает список экземпляров Post'''
        posts_data = self._load_data()
        list_of_post = [Post(**post_data) for post_data in posts_data]
        return list_of_post

    def get_all(self):
        '''Получает все посты, возвращает список экземпляров класса Post'''
        posts = self._load_posts()
        return posts

    def get_by_pk(self, pk):
        '''Получает пост по его PK'''
        if type(pk) != int:
            raise TypeError('pk must be an int')

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):
        '''Ищет посты, где в контенте встречается substring'''
        substring = str(substring).lower()
        posts = self._load_posts()
        matching_post = [post for post in posts if substring in post.content.lower()]
        return matching_post

    def get_by_poster(self, user_name):
        '''Ищет посты с определённым автором'''
        user_name = str(user_name).lower()
        posts = self._load_posts()
        matching_post = [post for post in posts if post.poster_name.lower() == user_name]
        return matching_post

#pd = PostDAO('../../data/posts.json')
#pp(pd.get_by_poster('leo'))
