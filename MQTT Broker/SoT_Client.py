import requests, time, csv, json, simpy, random
import paho.mqtt.client as paho

NOTIFICATION_INTERVAL = 10 # Message interval
NUM_INSTANCES = 1           # Number of instances
SIM_TIME = float("inf")


# Simulation time in Secs

def main():
    #MQTT Setup
    broker="localhost"
    port=1883
    def on_publish(client,userdata,result):             #create function for callback
        print("HEART_data published :",result)
        pass
    mqttClient= paho.Client()                         #create client object
    mqttClient.on_publish = on_publish                          #assign function to callback
    mqttClient.username_pw_set("user", password="password")
    mqttClient.connect(broker,port)
    
    # Create an environment and start the setup process
    env = simpy.rt.RealtimeEnvironment(0,1,False)
    Dev= [SoT(env, i, mqttClient)
                    for i in range(NUM_INSTANCES)]
    env.run(until=SIM_TIME)
    print("Simulation Complete")


class SoT(object):
    def __init__(self, env, id, mqttClient):
        self.env = env
        self.id = id
        self.mqttClient = mqttClient
        # Create a new boject
        self.process = env.process(self.create())

    def create(self):
        while True:
            try:
                start = self.env.now
                self.getData(start)
                self.sendData(start)
                #yield self.env.timeout(NOTIFICATION_INTERVAL)
                    
            except simpy.Interrupt:
                print('time',self.now)
                
    def getData(self,data):
        
        data = {}
        with open ('SoT_Data.csv','r') as csvFile:
            reader = csv.reader(csvFile)
            for rows in reader:
                #if rows['Time'] == '':
                #    break
                Sample = rows[0]
                data[Sample] = rows
                print(data[Sample])
                dataJson = json.dumps(data[Sample])
                self.mqttClient.publish("Periodic",dataJson)
                time.sleep(NOTIFICATION_INTERVAL)

    def sendData(self,data):
        print(self.id,'time:',data);
    
if __name__ == '__main__':
    main()
