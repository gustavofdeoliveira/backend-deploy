# Basic imports
from textwrap import dedent

from analyze.routes import analyze
from point.routes import point
from robot.routes import robot
from route.routes import route
from sanic import Sanic
# Routes imports
from user.routes import user


def create_server() -> Sanic:
    app = Sanic(__name__)
    app.config.CORS_ORIGINS = "*"
    return app


app = create_server()

app.ext.openapi.describe(
    "Turtle Controller API",
    version="2.0",
    description=dedent(
        """
        ## Description
        This is a simple API created with Sanic and Sanic-Ext that allows you to control a Turtlebot3 robot.
        All the endpoints are described below.
        """
    ),
)

app.blueprint(analyze, url_prefix='/analyze')
app.blueprint(point, url_prefix='/point')
app.blueprint(robot, url_prefix='/robot')
app.blueprint(route, url_prefix='/route')
app.blueprint(user, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3001)
