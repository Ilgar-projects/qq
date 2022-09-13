import logging

from flask import Blueprint, jsonify

from курсовая_3.bp_posts.dao.comment import Comment
from курсовая_3.bp_posts.dao.post import Post
from курсовая_3.bp_posts.dao.post_dao import PostDAO
from курсовая_3.bp_posts.dao.comment_dao import CommentDAO

from курсовая_3.config import DATA_PATH_POSTS, DATA_PATH_COMMENTS
# Создаём блюпринт
bp_api = Blueprint('bp_api', __name__)

# Создаём обьекты доступа к данным
post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentDAO(DATA_PATH_COMMENTS)
api_logger = logging.getLogger('api_logger')

@bp_api.route('/posts/')
def api_posts_all():
    '''Эндпоинт для всех постов'''
    all_posts: list[Post] = post_dao.get_all()
   # all_posts_as_dicts: list[dict] = [post.as_dict() for post in all_posts]
   # api_logger.debug('Запрошенны все посты')
   # return jsonify(all_posts_as_dicts), 200
    return jsonify(all_posts), 200

@bp_api.route('/posts/<int:pk>/')
def api_posts_single(pk:int):
    '''Эндпоинт для одного поста'''
    post: Post | None = post_dao.get_by_pk(pk)
    return jsonify(post)

###

@bp_api.route('/')
def api_posts_hello():
    return 'Это апи. Доступные эндпоинты /api/posts и /api/posts/<pk>.' \
           'Смотри документацию у меня на гитхабе!'



