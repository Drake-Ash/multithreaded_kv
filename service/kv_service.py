from datastore.base_store import BaseStore


class KVService(object):
    def __init__(self, store):
        if not isinstance(store, BaseStore):
            raise Exception('invalid store')
        self.kv_store = store

    def store(self, key, attributes):
        self.kv_store.store(key, attributes)

    def get(self, key):
        return self.kv_store.get(key)

    def update(self, key, attributes):
        self.kv_store.update(key, attributes)

    def delete(self, key):
        self.kv_store.delete(key)

    def get_secondary_index(self, predicate_key, predicate_value):
        return self.kv_store.get_secondary_index(predicate_key, predicate_value)
