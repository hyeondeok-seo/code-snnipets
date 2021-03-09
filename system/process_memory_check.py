import subprocess
import time


max_count = 3600
count = 0

pids = ['5180', '5187']
pids = ['57306']
out = subprocess.Popen(['ps', 'u', '-p', ','.join(pids)],
                       stdout=subprocess.PIPE).communicate()[0].split(b'\n')
rss_index = out[0].split().index(b'RSS')
vsz_index = out[0].split().index(b'VSZ')
print('count,pid,rss(MB),vsz(MB),time(s)')
while True:
    time.sleep(1)
    count+=1
    if count >= max_count:
        break
    out = subprocess.Popen(['ps', 'u', '-p', ','.join(pids)],
                           stdout=subprocess.PIPE).communicate()[0].split(b'\n')

    for pid_index, pid in enumerate(pids):
        mem_rss = float(out[pid_index+1].split()[rss_index]) / 1024
        mem_vsz = float(out[pid_index+1].split()[vsz_index]) / 1024
        print(f'{count},{pid},{mem_rss:.2f},{mem_vsz:.2f},{time.time():.2f}')
