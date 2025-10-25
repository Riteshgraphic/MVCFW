from pathlib import Path
from .protocols import request as RequestClass
import os
from prj import router

ROUTING_PIPE = ["Main", "index"]
BASE_DIR = Path(__file__).resolve().parent.parent

_refresh_callback = None

def ref(app, function):
    if app and function:
        return router.ROUTING[app][function]
    elif app:
        return router.ROUTING[app]
    else:
        print("Error: Reference cannot be null")

def set_refresh_callback(callback):
    global _refresh_callback
    _refresh_callback = callback

def goto(route, request=None):
    global ROUTING_PIPE
    ROUTING_PIPE = route
    app, func=ROUTING_PIPE
    if request:
        req=RequestClass(request.get("method", "GET"), request.get("data",{}))
    else:
        req=RequestClass("GET")
    controller_func = router.ROUTING[app][func]
    result=controller_func(req)
    if _refresh_callback:
        req.method="GET"
        _refresh_callback(req)
    return result
