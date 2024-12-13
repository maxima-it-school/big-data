docker-compose up --build

http://localhost:9870/ - hadoop namenode 
http://localhost:8080/ - spark master
http://localhost:8081/ - spark worker

hdfs dfs -mkdir /data/task_2
hdfs dfs -put data/task_2/data.txt /data/task_2
hadoop fs -cat /data/task_3/part-00000

spark-submit --master spark://spark-master:7077 --deploy-mode client /scripts/word_count.py

docker-compose down