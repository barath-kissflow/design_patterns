import json
import xml.etree.ElementTree as et
from abc import ABC, abstractmethod


# interface
class BaseSerializer(ABC):
    @abstractmethod
    def to_str(self):
        pass

    @abstractmethod
    def start_object(self, object_name, object_id):
        pass

    @abstractmethod
    def add_property(self, name, value):
        pass


# concrete
class JsonSerializer(BaseSerializer):
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer(BaseSerializer):
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


# Factory - creator
class SerializerFactory:

    def get_serializer(self, format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)


factory = SerializerFactory()


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)


# client code
class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


if __name__ == '__main__':
    song = Song('1', 'Water of Love', 'Dire Straits')
    serializer = ObjectSerializer()

    serializer.serialize(song, 'JSON')
    '{"id": "1", "title": "Water of Love", "artist": "Dire Straits"}'

    serializer.serialize(song, 'XML')
    '<song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>'

    serializer.serialize(song, 'YAML')
    # error: unsupported format: 'YAML'
