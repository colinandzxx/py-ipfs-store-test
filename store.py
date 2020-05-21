# import ipfsapi


class Store:

    def __init__(self):
        self.api = None

    def init(self, api):
        if api == None:
            return False

        self.api = api
        return True

    def store_1(self, file, recursive=False):
        res = self.api.add(file=file, recursive=recursive)
        return res
