# Running background tasks

The `background_tasks` app controls background execution. If it is in `INSTALLED_APPS`, stuff can be run in background. If it is not, stuff will block the request handler.

As a general rule, everything that is supposed to be run in a background task should check for `'background_tasks' in settings.INSTALLED_APPS` and run synchronously if it's not (unless it would be insane). See an example

Production deployments are expected to use `background_tasks`.

To use `background_tasks`, you need an AMQP 0.91 broker such as RabbitMQ. Not tested with anything else, such as ActiveMQ.

## Getting started

To install and configure RabbitMQ and the associated Python modules, do

    sudo apt-get install rabbitmq-server
    sudo -Hu rabbitmq rabbitmqctl add_vhost turskadev
    sudo -Hu rabbitmq rabbitmqctl add_user turskadev turskadev
    sudo -Hu rabbitmq rabbitmqctl set_permissions -p turskadev '.*' '.*' '.*'

    pip install -r requirements-background_tasks.txt

Edit `settings.py`, uncomment the line with `background_tasks` in `INSTALLED_APPS`. Also have a look at the configuration section further below that starts with

    if 'background_tasks' in INSTALLED_APPS:

Now you should be able to

    python manage.py celery worker