import sys
import time
import os
import subprocess
import shlex

my_splitter = '-'.join(['*' for _ in range(20)])

def write_split(stat_file_path):
    with open(stat_file_path, 'a+') as ifs:
        ifs.write(my_splitter + my_splitter + '\n')
        ifs.write(my_splitter + my_splitter + '\n')

def run_exp():
    algo_lst = [
        'sha256d',
        'cryptonight',
        'ethash',
        'cuckoo'
    ]
    exec_path_lst = [
        # '../cpuminer-multi/cpuminer',
        '../ccminer/ccminer',
        # '../cpuminer-multi/cpuminer',
        '../ccminer/ccminer',
        # '../ethash/build/bin/ethash-fakeminer',
        '../ethminer/build/ethminer/ethminer',
        # '../cuckoo/src/cuckoo/mean29x8',
        '../cuckoo/src/cuckoo/cuda29',
    ]
    params_lst = [
        # '--benchmark -a sha256d -q',
        '--benchmark -a sha256d -d 0',
        # '--benchmark -a cryptonight -q',
        '--benchmark -a cryptonight -d 0',
        # '-b 10000 -i 50',
        '--benchmark 10000 -U --cu-devices 0',
        # '-r 10',
        '-r 10',
    ]
    tag = 'exp_results'
    folder_name = 'gpu'

    for i, algo_path in enumerate(exec_path_lst):
        for repeat_cnt in range(3):
            algo_name = algo_lst[i]
            stat_dir = os.sep.join(map(str, ['.', tag, folder_name]))
            os.system('mkdir -p ' + stat_dir)
            stat_file_path = stat_dir + os.sep + algo_name + '.txt'

            os.system(' '.join(['echo', my_splitter + time.ctime() + my_splitter, '>>', stat_file_path]))
            params = map(str, [algo_path, params_lst[i]])
            cmd = ' '.join(params)
            print(cmd)
            with open(stat_file_path, 'a+') as stat_file:
                try:
                    subprocess.call(shlex.split(cmd), stdout=stat_file, stderr=stat_file, timeout=120)
                except subprocess.TimeoutExpired:
                    print('benchmark finished: ' + cmd)

if __name__ == '__main__':
    run_exp()
