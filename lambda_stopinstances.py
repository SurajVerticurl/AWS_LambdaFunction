import boto3

def lambda_handler(event, context):
    try:
        # Replace 'your-instance-id' with the actual ID of your EC2 instance
        instance_id = 'i-0b42fa3210f3f4583'
        
        # Create an EC2 client
        ec2 = boto3.client('ec2')
        
        # Stop the specified instance
        response = ec2.stop_instances(InstanceIds=[instance_id])
        
        # Print the response
        print("Stop response:", response)
        
        # You can also check the state of the instance after stopping
        # Describe the instance
        instance_state = ec2.describe_instances(InstanceIds=[instance_id])
        print("Current State:", instance_state['Reservations'][0]['Instances'][0]['State']['Name'])
        
        return {
            'statusCode': 200,
            'body': 'Instance stopping...'
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': 'Error stopping instance'
        }
