from controllers.RedisController import RedisController
from extensions import api, app, config
import logging

logging.basicConfig(level=logging.INFO)


@app.route('/')
def hello_world():
    return 'Hello Pandemic World!'


# Redis
api.add_resource(RedisController, "/redis")


if __name__ == '__main__':

    app.run(debug=True)
