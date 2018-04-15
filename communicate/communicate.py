class Communicate:
    data = []

    def __init__(self, data):
        self.data = data

    def next(self):
        if isinstance(type(self.data[0]), str):
            return self.data.remove(0)
        elif isinstance(type(self.data[0]), dict):
            text = "".join(self.data[0].keys)
            self.data.remove(0)
            return text
        return ""