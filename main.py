from flask import Flask
from blueprints.article.article import article_bp
from blueprints.comment.comment import comment_bp
from blueprints.tag.tag import tag_bp

app = Flask(__name__)
app.register_blueprint(article_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(tag_bp)

if __name__ == "__main__":
    app.run()


