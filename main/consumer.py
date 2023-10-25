import pika, json
from main import Product, db, app

app_ctx = app.app_context()
app_ctx.push()


params = pika.URLParameters('amqps://ckcuzimk:jGl1ba7PptdKhkufNn4K7_R2c_2cTCCE@crow.rmq.cloudamqp.com/ckcuzimk')

connection = pika.BlockingConnection(params)

chanel = connection.channel()

chanel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Recive in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product creted')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product deleted')


chanel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Starting consumiong')

chanel.start_consuming()

chanel.close()
