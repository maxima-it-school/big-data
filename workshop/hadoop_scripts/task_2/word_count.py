from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=conf)

text_file = sc.textFile("hdfs://namenode:9000/data/task_2/data.txt")
word_counts = text_file.flatMap(lambda line: line.split(" ")) \
                       .map(lambda word: (word, 1)) \
                       .reduceByKey(lambda a, b: a + b)

word_counts.saveAsTextFile("hdfs://namenode:9000/data/task_3")