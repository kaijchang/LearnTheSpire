import tensorflow as tf

import json
import sys

from learnthespirelogger import logger

n_nodes_hl1 = 10
n_nodes_hl2 = 10

card_vector_size = 234

batch_size = 10

n_choices = 4

card_1 = tf.placeholder('float32', [None, card_vector_size])
card_2 = tf.placeholder('float32', [None, card_vector_size])
card_3 = tf.placeholder('float32', [None, card_vector_size])

player_choice = tf.placeholder('float32', [None, n_choices])


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

    return tf.add_n([output_1, output_2, output_3])


def train_neural_network(dataset, labels):
    prediction = neural_network_model()
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction, labels=player_choice))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    hm_epochs = 100

    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0

            for batch in range(int(len(dataset) / batch_size)):
                epoch_x, epoch_y = (dataset[batch * batch_size: (batch + 1) * batch_size],
                                    labels[batch * batch_size: (batch + 1) * batch_size])

                _, c = sess.run([optimizer, cost], feed_dict={
                    card_1: [data[0] for data in epoch_x],
                    card_2: [data[1] for data in epoch_x],
                    card_3: [data[2] for data in epoch_x],
                    player_choice: epoch_y
                })
                epoch_loss += c

            logger.info('Epoch {epoch} completed out of {hm_epochs} loss: {epoch_loss}'.format(
                epoch=epoch + 1,
                hm_epochs=hm_epochs,
                epoch_loss=epoch_loss)
            )

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(labels, 1))

        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        logger.info('Accuracy: {accuracy}%'.format(accuracy=accuracy.eval({
            card_1: [data[0] for data in dataset],
            card_2: [data[1] for data in dataset],
            card_3: [data[2] for data in dataset],
            player_choice: labels
        }) * 100))

        save_path = saver.save(sess, './models/{character}.model'.format(
                character=sys.argv[1].split('_')[0]))

        logger.info('Model saved to {save_path}'.format(save_path=save_path))


if __name__ == '__main__':
    with open(sys.argv[1]) as training_data_file:
        dataset = json.load(training_data_file)
        train_neural_network([data[0] for data in dataset], [data[1] for data in dataset])
