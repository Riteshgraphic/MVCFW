SESSION={}

class request:
    def __init__(self, method="GET", data=None):
        self.method=method.upper()
        self.data = data or {}
        self.POST = self.data if self.method == "POST" else {}
        self.GET = self.data if self.method == "GET" else {}
        self.session = SESSION
