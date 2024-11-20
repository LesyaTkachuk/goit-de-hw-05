from kafka_admin import create_consumer, kafka_topics
from color_constants import BLUE, RED, END

# create Kafka Consumer
alerts_consumer = create_consumer("alerts_consumers_group")

# define topic names
topic_temperature_alerts = kafka_topics["topic_temperature_alerts"]
topic_humidity_alerts = kafka_topics["topic_humidity_alerts"]


def main():
    # subscribe to topic_temperature_alerts and topic_humidity_alerts
    alerts_consumer.subscribe([topic_temperature_alerts, topic_humidity_alerts])

    try:
        for message in alerts_consumer:
            print(
                f"{BLUE}Received alert: {message.value['alert']} Time: {message.value['obtained_at']}{END}"
            )
    except KeyboardInterrupt:
        print(f"{RED}Keyboard interrupt received. Exiting...{END}")
    except Exception as e:
        print(f"{RED}Error receiving alert: {e}{END}")
    finally:
        alerts_consumer.close()


if __name__ == "__main__":
    main()
