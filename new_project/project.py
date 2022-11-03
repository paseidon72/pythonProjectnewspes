import psutil
import datetime

### *** CPU FUNCTIONS ***

# Number of logical CPUs in the system
print ("psutil.cpu_count() = {0}".format(psutil.cpu_count()))
print('-' * 100)

### *** DISK FUNCTIONS ***

# List of named tuples containing all mounted disk partitions
dparts = psutil.disk_partitions()
print("psutil.disk_partitions() = {0}".format(dparts))
print('-' * 100)
# Disk usage statistics
du = psutil.disk_usage('/')
print("psutil.disk_usage('/') = {0}".format(du))


### *** MEMORY FUNCTIONS ***

# System memory usage statistics
mem = psutil.virtual_memory()
print("psutil.virtual_memory() = {0}".format(mem))
print('-' * 100)

THRESHOLD = 100 * 1024 * 1024  # 100MB
if mem.available <= THRESHOLD:
    print("warning, available memory below threshold")
    print('-' * 100)


### *** PROCESS FUNCTIONS ***

# List of current running process IDs.
pids = psutil.pids()
print("psutil.pids() = {0}".format(pids))
print('-' * 100)


# Check whether the given PID exists in the current process list.
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        print(pinfo)
        print('-' * 100)


### *** SYSTEM INFORMATION FUNCTIONS ***

# System boot time expressed in seconds since the epoch
boot_time = psutil.boot_time()
print("psutil.boot_time() = {0}".format(boot_time))
print('-' * 100)

# System boot time converted to human readable format
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
print('-' * 100)

# Users currently connected on the system
users = psutil.users()
print("psutil.users() = {0}".format(users))
print('-' * 100)

