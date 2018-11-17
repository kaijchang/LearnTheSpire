import tensorflow as tf

from card_name_to_vector import card_name_to_vector

n_nodes_hl1 = 10
n_nodes_hl2 = 10

batch_size = 10

card_vector_size = 234

n_choices = 4

card_1 = tf.placeholder('float32', [None, card_vector_size])
card_2 = tf.placeholder('float32', [None, card_vector_size])
card_3 = tf.placeholder('float32', [None, card_vector_size])


def build_column(data):
    hidden_1_layer = {
        'weights': tf.Variable(tf.random_normal([card_vector_size, n_nodes_hl1])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))
    }

    hidden_2_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))
    }

    output_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_choices])),
        'biases': tf.Variable(tf.random_normal([n_choices]))
    }

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    output = tf.add(tf.matmul(l2, output_layer['weights']), output_layer['biases'])

    return output


def neural_network_model():
    output_1 = build_column(card_1)
    output_2 = build_column(card_2)
    output_3 = build_column(card_3)

    return output_1 + output_2 + output_3


with tf.Session() as sess:
    prediction = neural_network_model()

    sess.run(tf.global_variables_initializer())

    print(
        sess.run(
            prediction, feed_dict={
                card_1: card_name_to_vector('bash'),
                card_2: card_name_to_vector('strike'),
                card_3: card_name_to_vector('defend')
            }
        )
    )
