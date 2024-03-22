#Executes a command
exec { 'pkill killmenow':
	path => '/usr/bin:/urs/sbin:/bin'
}
