# coding=utf-8
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1'
import tensorflow as tf
with tf.Session() as sess:
	x = tf.range(3, 1, -0.5)
	print sess.run(x)


