import json
from json import JSONDecodeError

from курсовая_3.bp_posts.dao.comment import Comment
from курсовая_3.exceptions.data_exceptions import DataSourceError


class CommentDAO:
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

    def _load_comments(self):
        '''Возвращает список экземпляров Comment'''
        comments_data = self._load_data()
        list_of_post = [Comment(**comment_data) for comment_data in comments_data]
        comments = [Comment(**comment_data) for comment_data in comments_data]
        return list_of_post

    def get_comments_by_post_pk(self, post_pk:int) -> list[Comment]:
        '''Получает все комментарии к определённому посту по его рк'''
        comments: list[Comment] = self._load_comments()
        comments_match: list[Comment] = [c for c in comments if c.post_pk == post_pk]
        return comments_match
# cd = CommentDAO('../../data/comments.json')
# print(cd.get_comments_by_post_pk(2))