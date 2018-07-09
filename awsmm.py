import boto3
import click

session = boto3.Session()
ec2 = session.resource('ec2')

@click.command()
@click.option('--project', default=None)

def list_instances(project):
  "list-instances : To list all instances in the AWS account"
  instances= [] #Initialise empty list to process projectName parameter
  if project:
      filters= [{'Name':'tag:Project','Values':[project]}]
      instances = ec2.instances.filter(Filters=filters)
  else :
      instances = ec2.instances.all()

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

if __name__ == '__main__':
  list_instances()
