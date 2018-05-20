from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from models import Department, Employee
from database import db_session, Base, engine

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/create-data')
def hello_world():
    Base.metadata.create_all(bind=engine)
    engineering = Department(name='Engineering')
    db_session.add(engineering)
    hr = Department(name='Human Resources')
    db_session.add(hr)

    peter = Employee(name='Peter', department=engineering)
    db_session.add(peter)
    roy = Employee(name='Roy', department=engineering)
    db_session.add(roy)
    tracy = Employee(name='Tracy', department=hr)
    db_session.add(tracy)
    db_session.commit()

    return 'Data created, hopefully'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
