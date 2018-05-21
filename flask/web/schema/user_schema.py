import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import db_session
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


class CreateUser(graphene.Mutation):
    class Arguments:
        last_name = graphene.String()
        first_name = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)

    def mutate(self, info, last_name, first_name, email):
        user = UserModel(last_name=last_name, first_name=first_name, email=email)
        db_session.add(user)
        db_session.commit()
        ok = True
        return CreateUser(user=user, ok=ok)


class UserMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
