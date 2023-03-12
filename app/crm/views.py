import uuid
from aiohttp.web_response import json_response
from app.crm.models import User
from app.web.app import View


class AddUserView(View):
    async def post(self):
        data = await self.request.json()
        user = User(email=data['email'], _id=uuid.uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response(data={'status': 'ok'})
