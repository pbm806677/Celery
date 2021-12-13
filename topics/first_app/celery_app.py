from celery import Celery

# create celery app
# mention broker and celery instance backend
# use kwargs of Celery(broker,backend)
# broker = any message broker e.g (RabbitMQ, Redis, etc)
# backend = any database (Redis recommended) 

app = Celery(broker="localhost",backend="rpc://")

# start the celery app
if __name__ == "__main__":
    app.start()
