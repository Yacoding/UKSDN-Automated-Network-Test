#written By David Pennington October 2013

####Description
# This program is the base class for the testing of the connections between hosts
# it uses an ssh python plugin to talk to the hosts and then runs a combination
# of ping and iperf to test the connection
####

####USAGE
# if importing for another program, just run the test_connection function
# if using from the command line, type test_connection.py <host_1> <host_2>
####


####Import Statements
import #
#
#
####

# build a list of hosts and their ip's
list_of_hosts = [	'h1','h2','h3',
					'h4','h5','h6']
host_system_ip = '10.0.0.'
list_of_host_ips = ['1','2','3','4','5','6']

def test_connection(host_1,host_2):
	#open ssh connections to both systems
	#ping from 1 to 2
	#ping from 2 to 1

	#start iperf server 1
	#start iperf client 2

	#start iperf server 2
	#start iperf client 1

@staticmethod
def main():
	import sys

	#get the hosts to run the test on
	test_h_name_1 = 'h1'
	test_h_name_2 = 'h2'

	if len(sys.argv) == 3:
		#grab the requested values to test
		if sys.argv[1] in list_of_hosts:
			test_h_name_1  = sys.argv[1]
		else:
			#if we couldnt find the requested host
			#just tell them we couldnt, list the hosts and and exit
			print "Could not find Host 1 (" + sys.argv[1] + ") in the list of hosts"
			print  list_of_hosts
			print "Choose one of these hosts or change the config"
			sys.exit()

		if sys.argv[2] in list_of_hosts:
			test_h_name_2  = sys.argv[2]
		else:
			#if we couldnt find the requested host
			#just tell them we couldnt, list the hosts and and exit
			print "Could not find Host 2 (" + sys.argv[2] + ") in the list of hosts"
			print  list_of_hosts
			print "Choose one of these hosts or change the config"
			sys.exit()

	test_connection(test_h_name_1,test_h_name_2)

if __name__ == "__main__":
	__main():