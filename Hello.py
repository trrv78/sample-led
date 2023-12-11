# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import streamlit as st
import paho.mqtt.publish as publish

# Set the MQTT broker information
mqtt_broker = "192.168.4.1"  # IP address of the ESP8266 in AP mode
mqtt_port = 1883
mqtt_topic = "led_control"

# Streamlit App
st.title("ESP8266 LED Control")

# Function to send MQTT message to ESP8266
def send_mqtt_message(message):
    publish.single(mqtt_topic, message, hostname=mqtt_broker, port=mqtt_port)

# UI for LED control
led_status = st.checkbox("Turn On/Off LED")

if led_status:
    send_mqtt_message("ON")
else:
    send_mqtt_message("OFF")

