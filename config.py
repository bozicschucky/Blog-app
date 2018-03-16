import os


class Configuartion(object):
    """docstring for Configuartion"""
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    # format for postgresql
    # postgresql://postgres:secretpassword@localhost:5432/blog_db
    # dialect+driver://username:password@host:port/database format for databases.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
