import pytest

from chapter3.test_multiple_implementations import JSONSerializer, \
    XMLSerializer, YAMLSerializer, Quantity, Pipe


class Test:

    @pytest.fixture(params=[JSONSerializer, XMLSerializer, YAMLSerializer])
    def test_serializer(self, request):
        return request.param()

    def test_quantity(self, serializer):
        quantity = Quantity(10, 'm')
        data = serializer.serialize_quantity(quantity)
        new_quantity = serializer.deserialize_quantity(data)
        assert new_quantity == quantity

    def test_pipe(self, serializer):
        pipe = Pipe(length=Quantity(1000, 'm'), diameter=Quantity(35, 'cm'))
        data = serializer.serialize_pipe(pipe)
        new_pipe = serializer.deserialize_quantity(data)
        assert new_pipe == pipe
