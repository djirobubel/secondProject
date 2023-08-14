from flask import Blueprint, request, Response
from models import *

comment_bp = Blueprint('comment', __name__)


@comment_bp.route('/comments', methods=['POST'])
def add_comment():
    comment = Comment.create(content=request.json['content'], article_id=request.json['articleId'])
    return {'id': comment.id}


@comment_bp.route('/comments/<id>', methods=['PUT'])
def update_comment(id):
    try:
        comment = Comment.get(Comment.id == id)
        comment.content = request.json['content']
        comment.save()
        return Response(status=204)

    except Comment.DoesNotExist:
        return {'error': 'not found'}, 404


@comment_bp.route('/comments/<id>', methods=['DELETE'])
def delete_comment(id):
    try:
        comment = Comment.get(Comment.id == id)
        comment.delete_instance()
        return Response(status=204)

    except Comment.DoesNotExist:
        return {'error': 'not found'}, 404