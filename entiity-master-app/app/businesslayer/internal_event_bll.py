rom domain.internal_event import InternalEvent
and other import statements

class InternalEventBll():
        INTERNAL_EVENT_TOPIC = "cemh.internal.event.v1"

        def publish_internal_event(self, event:InternalEvent):
               create_internal_event(event)

               producer = KafkaProducer(bootstrap_servers=AppConfig().
               get_kafka_config()["bootstrap_servers"], 
              value_serializer=lambda x: x.encode('utf-8'))

              producer.send(self.INTERNAL_EVENT_TOPIC, value=event.to_json_string())


