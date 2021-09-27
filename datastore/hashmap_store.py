import threading

from datastore.base_store import BaseStore
from model.attribute import Attribute


class HashMapStore(BaseStore):
    def __init__(self):
        super().__init__()
        self.kv_store = {}
        self.lock = threading.Lock()

    def key_exists(self, key):
        if key not in self.kv_store:
            raise Exception('Key does not exist')

    def store(self, key, attributes):
        with self.lock:
            if key in self.kv_store:
                raise Exception('Key already used, use update to change values')
            attributes_set = set()
            for attribute in attributes:
                if attribute.meta.name in attributes_set:
                    raise Exception("cannot store same key again")
                attributes_set.add(attribute.meta.name)
            self.kv_store[key] = attributes

    def get(self, key):
        self.key_exists(key)
        values = self.kv_store[key]
        return [value.to_dict() for value in values]

    def update(self, key, attributes):
        with self.lock:
            self.key_exists(key)
            value = self.kv_store[key]
            value_map = dict((attribute.meta.name, attribute) for attribute in value)
            for attribute in attributes:
                if attribute.meta.name in value_map:
                    val = value_map[attribute.meta.name]
                    val.value = attribute.value
                else:
                    value.append(attribute)

    def delete(self, key):
        with self.lock:
            self.key_exists(key)
            del self.kv_store[key]

    def get_secondary_index(self, predicate_key, predicate_value):
        search_attribute = Attribute(predicate_key, predicate_value)
        result = []
        for key, values in self.kv_store.items():
            for value in values:
                if value.meta.name == search_attribute.meta.name and value.value == search_attribute.value:
                    result.append(key)
        return result
