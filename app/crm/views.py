import uuid

from app.web.utils import json_response
from aiohttp.web_exceptions import HTTPNotFound
from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema

from app.crm.models import User
from app.crm.schemes import ListUsersResponseSchema, UserGetResponseSchema, \
    UserGetRequestSchema, UserAddSchema
from app.web.app import View
from app.web.schemes import OkResponseScheme


class AddUserView(View):
    @docs(tags=["crm"], summary="Add new user", discription="Add new user to database")
    @request_schema(UserAddSchema)
    @response_schema(OkResponseScheme, 200)
    async def post(self):
        data = self.request["data"]
        user = User(email=data["email"], id_=uuid.uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response()


class ListUsersView(View):
    @docs(tags=["crm"], summary="List users", discription="List users from database")
    @response_schema(ListUsersResponseSchema, 200)
    async def get(self):
        users = await self.request.app.crm_accessor.list_users()
        row_users = [{"email": user.email, "id": str(user.id_)} for user in users]
        return json_response(data={"users": row_users})


class GetUserView(View):
    @docs(tags=["crm"], summary="Get user", discription="Get user from database")
    @querystring_schema(UserGetRequestSchema)
    @response_schema(UserGetResponseSchema, 200)
    async def get(self):
        user_id = self.request.query.get('id')
        user = await self.request.app.crm_accessor.get_user(uuid.UUID(user_id))
        if user:
            return json_response(data={"user": {"email": user.email, "id": str(user.id_)}})
        raise HTTPNotFound
