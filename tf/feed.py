import tensorflow as tf
import input_data

input1 = tf.placeholder(tf.dtypes.float32)
input2 = tf.placeholder(tf.dtypes.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1: [7.0], input2: [3.0]}))

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

