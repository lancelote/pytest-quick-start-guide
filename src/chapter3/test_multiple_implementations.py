import pytest


class Quantity:

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit


class Pipe:

    def __init__(self, length: Quantity, diameter: Quantity):
        self.length = length
        self.diameter = diameter


class Serializer:

    def serialize_quantity(self, quantity: Quantity) -> str:
        ...

    def deserialize_quantity(self, data: str) -> Quantity:
        ...

    def serialize_pipe(self, pipe: Pipe) -> str:
        ...

    def deserialize_pipe(self, data: str) -> Pipe:
        ...


class JSONSerializer(Serializer):
    pass


class Test:

    def test_quantity(self):
        serializer = JSONSerializer()
        quantity = Quantity(10, 'm')
        data = serializer.serialize_quantity(quantity)
        new_quantity = serializer.deserialize_quantity(data)
        assert new_quantity == quantity

    def test_pipe(self):
        serializer = JSONSerializer()
        pipe = Pipe(length=Quantity(1000, 'm'), diameter=Quantity(35, 'm'))
        data = serializer.serialize_pipe(pipe)
        new_pipe = serializer.deserialize_pipe(data)
        assert new_pipe == pipe


class XMLSerializer(Serializer):
    pass


class YAMLSerializer(Serializer):
    pass


@pytest.mark.parametrize(
    'serializer_class', [JSONSerializer, XMLSerializer, YAMLSerializer])
class TestMore:

    def test_quantity(self, serializer_class):
        serializer = serializer_class()
        quantity = Quantity(10, 'm')
        data = serializer.serialize_quantity(quantity)
        new_quantity = serializer.deserialize_quantity(data)
        assert new_quantity == quantity

    def test_pipe(self, serializer_class):
        serializer = serializer_class()
        pipe = Pipe(length=Quantity(1000, 'm'), diameter=Quantity(35, 'm'))
        data = serializer.serialize_pipe(pipe)
        new_pipe = serializer.deserialize_pipe(data)
        assert new_pipe == pipe
