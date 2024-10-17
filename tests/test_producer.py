import unittest
from kafka_producer_consumer import produce

class TestKafkaProducer(unittest.TestCase):
    def test_produce(self):
        config = {"bootstrap.servers": "localhost:9092"}
        topic = "test_topic"
        produce(topic, config)
        # Assert something about the message being produced...
