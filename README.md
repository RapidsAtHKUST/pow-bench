# pow-bench

This repository contains the source code of the paper "Evaluating Memory-Hard Proof-of-Work Algorithms on Three Processors", by [Zonghao Feng](http://www.cse.ust.hk/~zfengah/) and Prof. [Qiong Luo](http://www.cse.ust.hk/~luo/).

## Build

The build instructions for each algorithm are as follows. There is also a [build script](scripts/build.sh) available in the scripts folder.

### cpuminer-multi (Hashcash and Cryptonight, CPU and KNL)
```
./build.sh
```

### ccminer  (Hashcash and Cryptonight, GPU)
```
./build.sh
```

### ethash (Ethash, CPU)
```
mkdir build
cd build
cmake ..
cmake --build .
```

### ethminer (Ethash, GPU)
```
mkdir build
cd build
cmake .. -DETHASHCL=OFF
cmake --build .
```

### cuckoo (Cuckoo Cycle, CPU, KNL and GPU)
```
cd src/cuckoo
make mean29x8
make cuda29
```

## Run

Run performance tests for each algorithm with run.py in the scripts folder (requires Python 3.3+).

### cpuminer-multi
```
# -t [num_of_threads]
./cpuminer --benchmark -a sha256d -q -t 40
./cpuminer --benchmark -a cryptonight -q -t 40
```

### ccminer
```
# -d [device_id]
./ccminer --benchmark -a sha256d -d 0
./ccminer --benchmark -a cryptonight -d 0
```

### ethash
```
# -b [block_num] -i [iterations] -t [num_of_threads]
./ethash-fakeminer -b 10000 -i 50 -t 40
```

### ethminer
```
# [block_num] [device_id]
./ethminer --benchmark 10000 -U --cu-devices 0
```

### cuckoo
```
# -t [num_of_threads] -r [rounds]
./mean29x8 -t 64 -r 10 
./cuda29 -r 10
```

## Profiling

Requirement: perf (CPU, KNL), nvprof (GPU)

Power consumption monitoring: [s-tui](https://github.com/amanusk/s-tui) (CPU, KNL) and nvidia-smi (GPU)

### CPU

```
perf stat -e L1-dcache-load-misses,mem_uops_retired.all_loads,mem_uops_retired.l1_miss_loads,LLC-loads,l2_requests.miss,mem_uops_retired.l2_hit_loads,mem_uops_retired.l2_miss_loads,unc_e_rpq_inserts,unc_e_wpq_inserts,unc_m_cas_count.rd,unc_m_cas_count.wr
```

### KNL

```
perf stat -e mem_load_uops_retired.l1_hit,mem_load_uops_retired.l1_miss,mem_load_uops_retired.l2_hit,mem_load_uops_retired.l2_miss,mem_load_uops_retired.llc_hit,mem_load_uops_retired.llc_miss,uncore_imc/data_reads/,uncore_imc/data_writes/
```

### GPU

```
nvprof -m sm_efficiency, achieved_occupancy, dram_read_throughput, dram_write_throughput, shared_efficiency, shared_load_throughput, shared_store_throughput, l2_read_throughput, l2_write_throughput, sysmem_read_throughput, sysmem_write_throughput, stall_inst_fetch, stall_exec_dependency, stall_texture, stall_sync, stall_other
```

## Sample Results

|                      | i7-3770  | Xeon Gold 5115  | Xeon Phi 7210 | GTX 670 | Tesla K80 | GTX 1080 Ti | Tesla V100 |
|----------------------|----------|-----------------|---------------|---------|-----------|-------------|------------|
| Hashcash \(MH/s\)    | 25\.21   | 190\.26         | 191\.18       | 159\.31 | 577\.74   | 1832\.95    | 2724\.92   |
| CryptoNight \(H/s\)  | 128\.513 | 552\.95         | 1005\.2       | 91\.21  | 478\.57   | 780\.14     | 1541\.10   |
| Ethash \(MH/s\)      | 0\.75    | 2\.31           | 3\.09         | 16\.30  | 27\.97    | 32\.63      | 94\.21     |
| Cuckoo Cycle \(G/s\) | 0\.24    | 0\.67           | 0\.54         | \-      | 0\.85     | 3\.92       | 5\.39      |


## Acknowledgement

This project is based on the following open-source projects:

* [cpuminer-multi](https://github.com/tpruvot/cpuminer-multi)
* [ccminer](https://github.com/tpruvot/ccminer)
* [ethash](https://github.com/chfast/ethash)
* [ethminer](https://github.com/ethereum-mining/ethminer)
* [cuckoo](https://github.com/tromp/cuckoo)
