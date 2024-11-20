from kafka_admin import create_consumer, create_producer, kafka_topics
from color_constants import GREEN, BLUE, RED, YELLOW, END
import time

# create sensor data Kafka Consumer
sensor_data_consumer = create_consumer("sensor_data_consumers_group")

# create Kafka Producer for temperature and humidity alerts sending
alerts_producer = create_producer()

# define topic names
topic_building_sensors = kafka_topics["topic_building_sensors"]
topic_temperature_alerts = kafka_topics["topic_temperature_alerts"]
topic_humidity_alerts = kafka_topics["topic_humidity_alerts"]


def main():
    # subscribe to topic_building_sensors topic
    sensor_data_consumer.subscribe([topic_building_sensors])

    try:
        for message in sensor_data_consumer:
            print(
                f"{BLUE}Received message: {message.value} from {YELLOW}{message.key}{END}"
            )
            process_data(message.value)
    except KeyboardInterrupt:
        print(f"{RED}Keyboard interrupt received. Exiting...{END}")
    except Exception as e:
        print(f"{RED}Error receiving data: {e}{END}")


def process_data(data):
    if data["temperature"] > 40:
        temperature_alert = f"Alert! Temperature is too high: {data['temperature']}C"
        data["alert"] = temperature_alert
        data["created_alert_at"] = (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        )
        print(
            f"{GREEN}Sending temperature alert to topic_temperature_alerts. Time:  {data['created_alert_at']}{END}"
        )
        try:
            alerts_producer.send(
                topic=topic_temperature_alerts,
                key=data["sensor_id"],
                value=data,
            )
            alerts_producer.flush()
        except Exception as e:
            print(f"{RED}Error sending temperature alert: {e}{END}")

    if data["humidity"] > 80 or data["humidity"] < 20:
        humidity_alert = f"Alert! Abnormal humidity detected: {data['humidity']}"
        data["alert"] = humidity_alert
        data["created_alert_at"] = (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        )
        print(
            f"{GREEN}Sending humidity alert to topic_humidity_alerts. Time: {data['created_alert_at']}{END}"
        )
        try:
            alerts_producer.send(
                topic=topic_humidity_alerts, key=data["sensor_id"], value=data
            )
            alerts_producer.flush()
        except Exception as e:
            print(f"{RED}Error sending humidity alert: {e}{END}")


if __name__ == "__main__":
    main()
