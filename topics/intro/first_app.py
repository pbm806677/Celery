from celery import Celery

app = Celery(broker="localhost",backend="rpc://")


if __name__ == '__main__':
    app.start()