import tensorflow as tf

import json
import sys

from train_model import build_column
from card_name_to_vector import card_name_to_vector

card_vector_size = 234

card_1 = tf.placeholder('float32', [None, card_vector_size])
card_2 = tf.placeholder('float32', [None, card_vector_size])
card_3 = tf.placeholder('float32', [None, card_vector_size])

output_1 = build_column(card_1)
output_2 = build_column(card_2)
output_3 = build_column(card_3)

output = output_1 + output_2 + output_3

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, sys.argv[1])

    while True:
        try:
            while True:
                try:
                    card_1_name = input('Card 1: ')
                    card_1_vector = card_name_to_vector(card_1_name)
                    break

                except StopIteration:
                    print('Card Not Found')

            while True:
                try:
                    card_2_name = input('Card 2: ')
                    card_2_vector = card_name_to_vector(card_2_name)
                    break

                except StopIteration:
                    print('Card Not Found')

            while True:
                try:
                    card_3_name = input('Card 3: ')
                    card_3_vector = card_name_to_vector(card_3_name)
                    break

                except StopIteration:
                    print('Card Not Found')

            output_ = list(sess.run(output, feed_dict={
                card_1: [card_1_vector],
                card_2: [card_2_vector],
                card_3: [card_3_vector],
            })[0])

            choices = ['Skip', card_1_name, card_2_name, card_3_name]
            print('The Neural Network chooses: {choice}'.format(
                choice=choices[output_.index(max(output_))].title()
            ))

        except KeyboardInterrupt:
            break
