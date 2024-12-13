## Инструкция по разворачиванию окружения Hadoop + Spark

Развернуть проект из docker-compose
`docker-compose up --build`

После успешного завершения скрипта по разворачиванию, можно будет открыть интерфейсы:

http://localhost:9870/ - hadoop namenode 

http://localhost:8080/ - spark master

http://localhost:8081/ - spark worker

### Практическое задание 1:

Создать папку в hdfs.

`hdfs dfs -mkdir /data/task_2`

Добавить в созданную папку hdfs data/task_2 файл data.txt

`hdfs dfs -put data/task_2/data.txt /data/task_2`

Запустить python скрипт word_count.py для расчета количества слов в файле data.txt

`spark-submit --master spark://spark-master:7077 --deploy-mode client /scripts/word_count.py`

Просмотреть результаты выполнения скрипта word_count.py

`hadoop fs -cat /data/task_3/part-00000`

`hadoop fs -cat /data/task_3/part-00001`

Завершить работу контейнеров

`docker-compose down`