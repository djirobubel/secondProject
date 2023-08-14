from flask import Blueprint
from models import *

tag_bp = Blueprint('tag', __name__)


@tag_bp.route('/tags')
def get_tags():
    return list(Tag.select().dicts())
