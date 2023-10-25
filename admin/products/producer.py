import pika, json


params = pika.URLParameters('amqps://ckcuzimk:jGl1ba7PptdKhkufNn4K7_R2c_2cTCCE@crow.rmq.cloudamqp.com/ckcuzimk')

connection = pika.BlockingConnection(params)

chanel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    chanel.basic_publish(exchange='', routing_key='main',
                         body=json.dumps(body), properties=properties
                         )
