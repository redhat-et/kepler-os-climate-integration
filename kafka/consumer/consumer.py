                                                                                                                                                          
from ensurepip import bootstrap
from confluent_kafka import Consumer
import os



def consume(topic_name,bootstrap_server):
    c = Consumer({
    'bootstrap.servers': bootstrap_server,
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'})

    c.subscribe([topic_name])

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()



if __name__ == "__main__":
    topic_name = os.getenv('TOPIC', 'new-topic')
    bootstrap_server = os.getenv('BOOTSTRAP_SERVER','localhost:9092')
    consume(topic_name,bootstrap_server)