class Communicate:
    data = []

    def __init__(self, data):
        self.data = data

    def next(self):
        if len(self.data) == 0:
            return ""
        if isinstance(self.data[0], str):
            return self.data.pop(0)
        elif isinstance(self.data[0], dict):
            text = "".join(self.data[0].keys)
            self.data.pop(0)
            return text
        return ""
