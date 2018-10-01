import click
from girder_worker.app import app
from girder_worker_utils import types
from girder_worker_utils.decorators import parameter



@parameter('a', cli_opts={'type': click.FLOAT})
@parameter('b', cli_opts={'type': click.FLOAT})
@app.task(bind=True)
def foo(self, a, b):
    return {'a': a, 'b': b}


@parameter('a', cli_opts={'type': click.FLOAT})
@parameter('b', cli_opts={'type': click.FLOAT})
@app.task(bind=True)
def add(self, a, b):
    return a + b


@parameter('a', cli_opts={'type': click.INT})
@parameter('b', cli_opts={'type': click.INT})
@app.task()
def subtract(a, b):
    return a - b


@parameter('a', cli_opts={'type': click.INT})
@parameter('b', cli_opts={'type': click.INT})
@app.task(bind=True)
def multiply(self, a, b):
    return a * b


# Worst API ever!
@parameter('a', cli_opts={'type': click.INT})
@parameter('b', cli_opts={'type': click.INT})
@parameter('zero',
           cli_args=('-z', '--zero'),
           cli_opts={'type': click.BOOL,
                     'help': 'return "undefined" if dividing by zero'})
@app.task(bind=True)
def divide(self, a, b, zero=False):
    if zero and b == 0:
        return 'undefined'

    return a / b
