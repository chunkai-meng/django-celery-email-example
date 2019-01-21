# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


@shared_task
def add(x, y):
    time.sleep(3)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# add.apply_async((7,30), link=on_success.s())
@shared_task
def on_success(res):
    return res
