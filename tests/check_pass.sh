#!/bin/bash

for i in pass/*.yaml; do
	aq-morftest -Ci $i;
done;
