import tensorflow as tf


sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

x.initializer.run()

sub = tf.subtract(x, a)
print(sub.eval())

# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))
#
# a = tf.constant(10)
# b = tf.constant(32)
# print(sess.run(a+b))

# # 构造三个节点
# matrix1 = tf.constant([[3., 3.]])
# matrix2 = tf.constant([[2.], [2.]])
# product = tf.matmul(matrix1, matrix2)
#
# with tf.Session() as sess:
#     result = sess.run([product])
#     print(result)


# # 启动默认图
# sess = tf.Session()
#
# # 触发节点执行
# result = sess.run(product)
# print(result)
#
# # 关闭会话
# sess.close()
