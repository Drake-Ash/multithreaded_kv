class BaseStore(object):
    def __init__(self):
        self.kv_store = None

    def key_exists(self, key):
        raise NotImplementedError

    def store(self, key, attributes):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def update(self, key, attributes):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def get_secondary_index(self, predicate_key, predicate_value):
        raise NotImplementedError
