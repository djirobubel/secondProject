from peewee import *

db = SqliteDatabase('secondproject.db')


class Base(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Article(Base):
    title = CharField()
    content = TextField(unique=True)

    class Meta:
        db_table = 'articles'


class Comment(Base):
    content = TextField(unique=True)
    article_id = ForeignKeyField(Article)

    class Meta:
        db_table = 'comments'


class Tag(Base):
    title = CharField(unique=True)

    class Meta:
        db_table = 'tags'


class ArticleTag(Model):
    article_id = ForeignKeyField(Article)
    tag_id = ForeignKeyField(Tag)

    class Meta:
        database = db
        db_table = 'article_tags'
