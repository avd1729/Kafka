import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka-1c908455-kafka-1729.g.aivencloud.com:12891",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)

producer.send(
    "test-topic",
    key={"key": 1},
    value={"message": "hello world!"}
)

producer.flush()
