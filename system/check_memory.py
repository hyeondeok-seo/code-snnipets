import subprocess
import time

import fire


def check_memory(pids, sleep_time=1, max_count=3600):
    pids = pids if isinstance(pids, list) else [pids]
    cmd = ['ps', 'u', '-p', ','.join(map(str, pids))]
    out = subprocess.Popen(cmd, stdout=subprocess.PIPE) \
                    .communicate()[0].split(b'\n')
    rss_index = out[0].split().index(b'RSS')
    vsz_index = out[0].split().index(b'VSZ')
    print('count,pid,rss(MB),vsz(MB),time(s)')
    count = 0
    while True:
        time.sleep(sleep_time)
        count += 1
        if count >= max_count:
            break
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE) \
                        .communicate()[0].split(b'\n')
        for pid_index, pid in enumerate(pids):
            mem_rss = float(out[pid_index+1].split()[rss_index]) / 1024
            mem_vsz = float(out[pid_index+1].split()[vsz_index]) / 1024
            print(f'{count},{pid},{mem_rss:.2f},{mem_vsz:.2f},{time.time():.2f}')


if __name__ == '__main__':
    fire.Fire(check_memory)
