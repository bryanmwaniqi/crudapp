from flask import _app_ctx_stack
import psycopg2

def init_app(app):
    app.teardown_appcontext(close_db)

def get_db():
    '''Function for creating a database connection object'''
    ctx = _app_ctx_stack.top
    con = getattr(ctx, 'myapp_db', None)
    if con is None:
        con = psycopg2.connect(ctx.app.config['DATABASE'])
        ctx.myapp_db = con
    return con

def close_db(error=None):
    '''Function for closing a database connection'''
    con = getattr(_app_ctx_stack.top, 'myapp_db', None)
    if con is not None:
        con.close()
