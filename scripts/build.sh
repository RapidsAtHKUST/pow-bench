#!/bin/bash
# cpuminer-multi
cd ../cpuminer-multi
./build.sh

# ccminer
cd ../ccminer
./build.sh

# ethash
cd ../ethash
mkdir build
cd build
cmake ..
cmake --build .

# ethminer
cd ../../ethminer
mkdir build
cd build
cmake .. -DETHASHCL=OFF
cmake --build .

# cuckoo
cd ../../cuckoo/src/cuckoo
make mean29x8
make cuda29
