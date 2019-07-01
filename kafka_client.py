#!/usr/bin/env python
# coding: utf-8

from kafka import KafkaConsumer
from kafka import TopicPartition
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')


def kafka_consumer_test():
    topic_name = 'topic_test'
    bootstrap_servers = ['localhost:9092']

    # consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, group_id='test_group', auto_offset_reset='earliest')
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id='test_group', auto_offset_reset='earliest')
        # enable_auto_commit=True（默认）才能断点续消，此时服务端会保存该group_id的offset
        # auto_offset_reset='earliest'，默认值是latest，只在offset发生异常是起作用，
    
    partition_set = consumer.partitions_for_topic(topic_name)
    partitions = [ TopicPartition(topic_name, partition_idx) for partition_idx in partition_set ]
    consumer.assign(partitions)
    topic_partition_set = consumer.assignment()

    #consumer.seek_to_beginning()    # 设置offset到集群中保存的第一个值，不一定是0, 没有参数则，对consumer的每一个partition设置
    #consumer.seek_to_end()    # 设置offset到当前没有消费的第一个值, 没有参数则，对consumer的每一个partition设置
    for topic_partition in topic_partition_set:
        offset = consumer.position(topic_partition)
        print "partition: %d, offset: %d" % (topic_partition.partition, offset)
        #consumer.seek(topicTopicPartition, offset)     # 尽量不要手动设置这个值


    for msg in consumer:
        print ("topic:%s, partition:%d, offset:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value.decode("utf-8")))

if __name__ == '__main__':
    kafka_consumer_test()

