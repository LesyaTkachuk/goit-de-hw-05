# goit-de-hw-05
Data Engineering. Implemented Apache Kafka for message interchange in the Internet of Things (IoT) domain. Developed a system for collecting sensor data and sending alerts, utilizing Python for efficient implementation.

> **_NOTE:_**   For normal operation of kafka package it is recommended to use a virtual environment with python3.11 version. Kafka package has an open issue with python3.12 and python3.13 versions for the moment of writing.

To create and activate virtual environment and install necessary packages perform the next commands:

```commandline
python3.11 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

To imitate the operation of a building sensors and produce sensor data run the script sensor_data_producer.py. It will generate and send objects that contain sensor id, temperature, humidity, time of data collection.
To imitate several sensors run the script in several separate terminals.

```commandline
python sensor_data_producer.py
```
To receive sensor data run the script sensor_data_consumer.py. Consumer will receive data from the topic and process it. If temperature and humidity are out of normal range, alerts will be sent to the topic_temperature_alerts and topic_humidity_alerts.

```commandline
python sensor_data_consumer.py
```
To receive temperature and humidity alerts run the script alerts_consumer.py. Consumer will receive data from the topic and print these alerts.

```commandline
python alerts_consumer.py
```