import sys
import boto

class GetAllInstances(object):

    def __init__(self):
	self.aws_access_key = 'XXXXXXXXXXXXXXXXXX'
	self.aws_secret_access_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	print 'Connection successful!'
	if self.aws_access_key == '' or self.aws_secret_access_key == '':
	   print 'Enter AWS access and secret access keys'

    def get_all_running_instances(self, region):
        try:
	    conn = boto.ec2.connect_to_region(region, aws_access_key_id=self.aws_access_key, aws_secret_access_key_id=self.aws_secret_access_key)

	    reservations = conn.get_all_reservations()
	    for reservation in reservations:
		for instance in reservation.instances:
		    print region + ':', instance.id

	    for volume in conn.get_all_volumes():
		print region + ':', volume.id

	except:
	    print str(sys.exc_info()[0])
