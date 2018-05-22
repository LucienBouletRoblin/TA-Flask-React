import os

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_jwt_extended import JWTManager, jwt_required
from flask_restful import Api

from database import db_session, init_db

app = Flask(__name__)

app.config["DEBUG"] = os.environ.get("DEBUG", True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'prout'

CORS(app)
api = Api(app)

init_db()

app.config['JWT_SECRET_KEY'] = 'jwt-secret-prout'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)

from models.user import RevokedTokenModel


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


import resources

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

from general_schema import schema


def protected_graphql_view():
    view = GraphQLView.as_view('protected_graphql', schema=schema, context={'session': db_session},
                               graphiql=True)
    return jwt_required(view)


app.add_url_rule(
    '/protected/graphql',
    view_func=protected_graphql_view()
)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql_user',
        schema=schema,
        graphiql=True
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
