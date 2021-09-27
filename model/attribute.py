AttributeMetas = {}


class AttributeMeta(object):
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type

    def validate_data_type(self, data_type):
        if self.data_type != data_type:
            raise Exception(f"Data type mismatch: expected {self.data_type}, got {data_type}")

    @staticmethod
    def get_or_create_attribute_meta(name, data_type):
        if name in AttributeMetas:
            attribute_meta = AttributeMetas[name]
            attribute_meta.validate_data_type(data_type)
            return attribute_meta
        attribute_meta = AttributeMeta(name, data_type)
        AttributeMetas[name] = attribute_meta
        return attribute_meta


class Attribute(object):
    def __init__(self, name, value):
        self.value = value
        self.meta = AttributeMeta.get_or_create_attribute_meta(name, type(value))

    def to_dict(self):
        return {
            'name': self.meta.name,
            'value': self.value
        }
