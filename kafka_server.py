import producer_server

## Some Configuration Parameters
## ==============================
TOPIC_NAME = 'com.udacity.dep.police.service'
SERVER_URL = 'localhost:9092'
CLIENT_ID = 'com.udacity.dep.police.broker'


def run_kafka_server():
	# TODO get the json file path
    input_file = "police-department-calls-for-service.json" 

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file, # Read from the input json file
        topic=TOPIC_NAME,
        bootstrap_servers=SERVER_URL,
        client_id=CLIENT_ID
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
