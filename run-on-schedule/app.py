from chalice import Chalice
import boto3

app = Chalice(app_name='run-on-schedule')

instance_id = "......"

@app.schedule('cron(0 8 * * *)')
def daily_task():
   #Your code to execute everyday at midnight
   print ("Turning off EC2 instance")
   ec2 = boto3.client('ec2')
   response = ec2.stop.instances(instance_id)
