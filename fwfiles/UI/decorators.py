import importlib
from functools import wraps

def use_masterpage(master_path):
    """
        master_path: "app.views.masterpage_default.defaultmasterpage
    """
    def decorator(viewclass):
        @wraps(viewclass)
        def wrapper(root, *args, **kwargs):
            module_path, class_name=master_path.rsplit(".",1)
            module=importlib.import_module(module_path)
            masterclass=getattr(module, class_name)
            master=masterclass(root)
            body=master.body
            return viewclass(body, *args, **kwargs)
        return wrapper
    return decorator