import sys, os
PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, PATH)

from tracer import create_app
application = create_app()
