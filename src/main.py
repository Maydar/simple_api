import asyncio
import os
import yaml
from aiohttp import web
from mongoengine import connect

from src.handlers.user_handler import UserHandler

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

loop = asyncio.get_event_loop()

config = yaml.safe_load(open(os.path.join(CURRENT_DIR + '/config.yaml')))

app = web.Application(loop=loop)
app['config'] = config

# users
app.router.add_get('/users', UserHandler.get_all_users)
app.router.add_get('/users/{first_name}', UserHandler.get_user_by_first_name)
app.router.add_post('/users', UserHandler.add_user)
app.router.add_post('/users/{user_id}', UserHandler.delete_user)


connect('test_database', host=app['config'].get('host'), port=app['config'].get('port'))
web.run_app(app)