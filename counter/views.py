from flask import Blueprint

from counter.models import Counter

counter_app = Blueprint("counter_app", __name__)


@counter_app.route("/")
def init():
    counter = Counter.objects.all().first()
    if counter:
        counter.count += 1
        counter.save()
    else:
        counter = Counter()
        counter.count = 1
        counter.save()
    return "<h1>Counter: " + str(counter.count) + "</h1>"
