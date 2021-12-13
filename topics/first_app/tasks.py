from celery_app import app


@app.task("Dummy Task")
def dummy_task():
    return {"message" : "Hello World!!!!"}


