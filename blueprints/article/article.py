from flask import Blueprint, request, Response
from models import *


article_bp = Blueprint('article', __name__)


@article_bp.route('/articles')
def get_articles():
    return list(Article.select().limit(10).order_by(Article.id.desc()).dicts())


@article_bp.route('/articles/<id>')
def get_article(id):
    try:
        article = Article.get(Article.id == id)

        comments = Comment.select().where(Comment.article_id == id)
        output1 = []
        for comment in comments:
            comment_data = {'content': comment.content}
            output1.append(comment_data)

        queries = ArticleTag.select().where(ArticleTag.article_id == id)
        output2 = []
        for query in queries:
            tags = Tag.select().where(Tag.id == query.tag_id)
            for tag in tags:
                tag_data = {'title': tag.title}
                output2.append(tag_data)

        return {'title': article.title, 'content': article.content, 'comments': output1, 'tags': output2}

    except Article.DoesNotExist:
        return {'error': 'not found'}, 404


@article_bp.route('/articles', methods=['POST'])
def add_article():
    article = Article.create(title=request.json['title'], content=request.json['content'])

    tags = request.json['tagId']
    for tag in tags:
        ArticleTag.create(article_id=article.id, tag_id=tag)

    return {'id': article.id}


@article_bp.route('/articles/<id>', methods=['PUT'])
def update_article(id):
    try:
        article = Article.get(Article.id == id)
        article.title = request.json['title']
        article.content = request.json['content']
        article.save()

        tag = ArticleTag.delete().where(ArticleTag.article_id == id)
        tag.execute()

        tags = request.json['tagId']
        for tag in tags:
            ArticleTag.create(article_id=article.id, tag_id=tag)

        return Response(status=204)

    except Article.DoesNotExist:
        return {'error': 'not found'}, 404


@article_bp.route('/articles/<id>', methods=['DELETE'])
def delete_article(id):
    try:
        article = Article.get(Article.id == id)
        article.delete_instance()

        comment = Comment.delete().where(Comment.article_id == id)
        comment.execute()

        tag = ArticleTag.delete().where(ArticleTag.article_id == id)
        tag.execute()

        return Response(status=204)

    except Article.DoesNotExist:
        return {'error': 'not found'}, 404


