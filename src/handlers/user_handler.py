import json

from aiohttp import web

from src.base.constants import OK_STATUS
from src.models.user import User


class UserHandler:
    @staticmethod
    async def get_all_users(request):
        users = User.objects()

        return web.json_response(data={
            'status': OK_STATUS,
            'users': users.to_json()
        })


    @staticmethod
    async def get_user_by_first_name(request):
        first_name = request.match_info['first_name']

        users = User.objects(first_name=first_name)

        return web.json_response(data={
            'status': OK_STATUS,
            'users': users.to_json()
        })


    @staticmethod
    async def add_user(request):
        data = await request.post()
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        user = User(first_name=first_name,
                    last_name=last_name,
                    email=email)

        user.save()

        return web.json_response({
            'status': OK_STATUS
        })

    @staticmethod
    async def delete_user(request):
        user_id = request.match_info['user_id']
        user = User.objects(pk=user_id)
        user.delete()

        return web.json_response({
            'status': OK_STATUS
        })