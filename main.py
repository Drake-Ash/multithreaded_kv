from datastore.hashmap_store import HashMapStore
from model.attribute import Attribute
from service.kv_service import KVService


def happy_flow():
    kv_store = HashMapStore()
    kv_service = KVService(kv_store)
    kv_service.store("delhi", [Attribute('pollution_level', 'very high'), Attribute('population', '10 Million')])
    kv_service.store("jakarta", [Attribute('lat', -6.0), Attribute('lon', 106.0), Attribute('pollution_level', 'high')])
    kv_service.store("blr", [Attribute('lat', 12.94), Attribute('lon', 77.64), Attribute('pollution_level', 'moderate'),
                             Attribute('free_food', True)])
    kv_service.store("india", [Attribute('capital', 'delhi'), Attribute('population', '1.2 Billion')])
    kv_service.store("crocin", [Attribute('manufacturer', 'GSK')])
    print(kv_service.get('delhi'))
    # print(kv_service.get('asdf'))
    print(kv_service.get_secondary_index('pollution_level', 'high'))
    print(kv_service.get_secondary_index('manufacturer', 'GSK1'))


if __name__ == '__main__':
    kv_store = HashMapStore()
    kv_service = KVService(kv_store)
    kv_service.store("key1", [Attribute('temp1', True), Attribute('temp2', 'test'), Attribute('temp3', 1.123)])
    value = kv_service.get("key1")
    print(value)
    kv_service.store("key2", [Attribute('temp1', True), Attribute('temp2', 'test1'), Attribute('temp4', 1)])
    kv_service.update("key2", [Attribute('temp1', False), Attribute('temp5', False)])
    print(kv_service.get("key2"))
    print(kv_service.get_secondary_index('temp2', 'test'))
    kv_service.delete('key2')

    happy_flow()
