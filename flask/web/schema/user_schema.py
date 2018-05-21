import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.user import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(lambda: User, id=graphene.Int())

    def resolve_user(self, context, id):
        query = User.get_query(context)
        return query.filter(UserModel.id == id).first()

    def resolve_users(self, info):
        query = User.get_query(info)  # SQLAlchemy query
        return query.all()
