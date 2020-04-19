# SPark-Streaming-With-Kafka-Crime

In this project, a real-world dataset, extracted from Kaggle, on San Francisco crime incidents will be used to simulate a real-time streaming dataset. Statistical analyses of the data using Apache Spark Structured Streaming will be implemented. A Kafka server wuill be used to produce data, and ingest data through Spark Structured Streaming.

## Running the Project
Open a new command line window to execute the following codes in order.

1) To start the ZooKeeper Server
Use the following command to start the ZooKeeper Server
```
/usr/bin/zookeeper-server-start config/zookeeper.properties
```
2) To start the Kafka Server
Use the following command to start the Kakfa Server. 
```
/usr/bin/kafka-server-start config/server.properties
```

3) Kafka Producer
Use the following command to start ingesting data into Kafka Server. The data is read from `police-department-calls-for-service.json` and pushed to Kafka Server periodically. 
```
python kafka_server.py
```

4) To run the Consumer Kafka Server
To check whether data had been successfully produced by the Kafka producer, adn correctly implemented the Kafka Producer, run the following command to see the what are the data produced by Kafka producer.

```
kafka-console-consumer --topic "<topic name>" --from-beginning --bootstrap-server localhost:9092
```
In this case, the topic name I have choosen is "com.udacity.dep.police.service", hence, for example, I will run the following command:
```
kafka-console-consumer --topic "com.udacity.dep.police.service" --from-beginning --bootstrap-server localhost:9092
```



