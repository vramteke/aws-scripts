import boto3
import click

session = boto3.Session()
ec2 = session.resource('ec2')

def filter_instances(project):
  instances= [] #Initialise empty list to process projectName parameter
  if project:
     filters= [{'Name':'tag:Project','Values':[project]}]
     instances = ec2.instances.filter(Filters=filters)
  else :
     instances = ec2.instances.all()
  return instances


@click.group()
def instances ():
    "Commands for instances"

@instances.command('list')
@click.option('--project', default=None)
def list_instances(project):
  "List EC2 instances in the AWS account "
  instances = filter_instances(project)

  for i in instances:
    tag_names={t['Key']:t['Value'] for t in i.tags or []}
    # The above command will create a dict from i.tags that is a list of dicts
    print('| '.join((
      i.id,
      i.instance_type,
      i.placement['AvailabilityZone'],
      i.state['Name'],
      i.public_dns_name,
      tag_names.get('Project','<no project>') # Use get to handle cases where tags are not defined
    )))
  return


@instances.command('start')
@click.option('--project', default=None)
def start_instances(project):
  "Start EC2 instances in the AWS account"
  instances = filter_instances(project)

  for i in instances:
      print('Starting instance {0} ...'.format(i.id))
      i.start()

  return


@instances.command('stop')
@click.option('--project', default=None)
def stop_instances(project):
  "Stop EC2 instances in the AWS account"
  instances = filter_instances(project)

  for i in instances:
      print('Stopping instance {0} ...'.format(i.id))
      i.stop()

  return

if __name__ == '__main__':
  instances()
