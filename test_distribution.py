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
import paramiko # ssh library
####

# build a list of hosts and their ip's
list_of_hosts = [	'h1','h2','h3',
					'h4','h5','h6',
					'h7','h8']
host_system_ip = '10.0.0.'
list_of_host_ips = ['2','3','4',
					'5','6','7',
					'8','9']

usernames = [	'host1',
				'host2',
				'host3',
				'host4',
				'ubuntu',
				'ubuntu',
				'ubuntu',
				'ubuntu']

passwords = [	'cc-nie',
				'cc-nie',
				'cc-nie',
				'cc-nie',
				'cc-nie',
				'pastH0pe',
				'pastH0pe',
				'pastH0pe',
				'pastH0pe']

def test_connection(host_1,host_2):
	#open ssh connections to both systems
	host_1 = host_1.lower()
	host_2 = host_2.lower()
	if host_1 in list_of_hosts:
		host_1_index = list_of_hosts.index(host_1)
		host_1_ip = host_system_ip + list_of_host_ips[host_1_index]
	else:
		print "Wrong Host_1 name, If this list is wrong, change it"
		print list_of_hosts
		print "exiting"
		return False
	if host_2 in list_of_hosts:
		host_2_index = list_of_hosts.index(host_2)
		host_2_ip = host_system_ip + list_of_host_ips[host_2_index]
	else:
		print "Wrong Host_2 name, If this list is wrong, change it"
		print list_of_hosts
		print "exiting"
		return False


	#build the ssh objects hopefully using forks
	ssh_1 = paramiko.SSHClient()
	ssh_1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_1.connect(host_1_ip, username=usernames[host_1_index],password=passwords[host_2_index])

	ssh_2 = paramiko.SSHClient()
	ssh_2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_2.connect(host_2_ip, username=usernames[host_2_index],password=passwords[host_2_index])


	#prepare both machines for running
	def prepare_hosts(ssh):
		#check if the test connection file is there
		stdin, stdout, stderr = ssh_1.exec_command("ls | grep UKSDN-Automated-Network-Test")
		if 'UKSDN-Automated-Network-Test' not in ' '.join(stdout):
			#get the test connection file
			stdin, stdout, stderr = ssh.exec_command(
			"git clone https://github.com/dpenning/UKSDN-Automated-Network-Test.git")
		#change into the test directory
		stdin, stdout, stderr = ssh_1.exec_command("cd UKSDN-Automated-Network-Test")

	def test_connection(s1,s2):
		#check if IPERf is runnning on s2.
		# if it isnt, start it.
		stdin2, stdout2, stderr2 = s2.exec_command('ps aux | grep iperf')
		if 'iperf -s' not in stdin2:
			stdin2, stdout2, stderr2 = s2.exec_command("nohup iperf -s > /dev/null 2>&1 &")
		stdin1, stdout1, stderr1 = s1.exec_command("./test_connection.sh")
		stdin2.write(chr(3))#send control-c
		stdin2.flush()
		return stdout

	prepare_hosts(ssh_1)
	prepare_hosts(ssh_2)

	#test from 1 to 2
	print test_connection(ssh_1,ssh_2)
	#test from 2 to 1
	print test_connection(ssh_1,ssh_2)

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
	main()