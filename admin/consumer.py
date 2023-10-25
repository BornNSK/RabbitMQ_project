import pika


params = pika.URLParameters('amqps://ckcuzimk:jGl1ba7PptdKhkufNn4K7_R2c_2cTCCE@crow.rmq.cloudamqp.com/ckcuzimk')

connection = pika.BlockingConnection(params)

chanel = connection.channel()

chanel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Recive in admin')
    print(body)


chanel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Starting consumiong')

chanel.start_consuming()

chanel.close()
