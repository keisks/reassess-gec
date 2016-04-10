#!/usr/bin/env python
#encoding: utf-8

import sys
import os
import csv
import ast
import itertools
import skll
import random

turker_file = open(sys.argv[1], 'r')

expertResultBySentence = {}
turkerResultBySentence = {}
reader = csv.DictReader(turker_file)

for row in reader:
    if row["Input.type"] == "control": # control or refs
        systems = []
        ranks = []
        systems.append(row["Input.system1"])
        systems.append(row["Input.system2"])
        systems.append(row["Input.system3"])
        systems.append(row["Input.system4"])
        systems.append(row["Input.system5"])
        ranks.append(row["Answer.rank_1"])
        ranks.append(row["Answer.rank_2"])
        ranks.append(row["Answer.rank_3"])
        ranks.append(row["Answer.rank_4"])
        ranks.append(row["Answer.rank_5"])

        if "###" in systems:
            idx = systems.index("###")
            systems.pop(idx)
            ranks.pop(idx)

        sentID = int(row["Input.sentID"])
        systems_pairs = itertools.combinations(systems, 2)
        ranks_pairs = itertools.combinations(ranks, 2)

        for sys_pair, rank_pair in zip(systems_pairs, ranks_pairs):
            system_index = "-".join(list(set(sys_pair)))
            key = str(sentID)+'_'+system_index

            if key in turkerResultBySentence:
                turkerResultBySentence[key].append(rank_pair)
            else:
                turkerResultBySentence[key] = []
                turkerResultBySentence[key].append(rank_pair)

conf = open("./highAgreedAMU.txt", 'r')

for c in conf.readlines():
    sid = int(c.rstrip().split('\t')[0]) -1 #sid = startswith 0
    system_rank_dict = ast.literal_eval(c.rstrip().split('\t')[2])
    system_names = system_rank_dict.keys()[0]
    for full_rank in system_rank_dict.values()[0]:
        systems_pairs = itertools.combinations(system_names.split("||"), 2)
        rank_pairs = itertools.combinations(full_rank, 2)
        for s, r in zip(systems_pairs, rank_pairs):
            system_index = "-".join(list(set(s)))
            key = str(sid)+"_"+system_index

            if key in expertResultBySentence:
                expertResultBySentence[key].append(r)
            else:
                expertResultBySentence[key] = []
                expertResultBySentence[key].append(r)

n = 0
turk_tri = []
turk_exp_tri = []
exp_tri = []

def sign(pair):
    if int(pair[0])> int(pair[1]):
        return -1
    elif int(pair[0])== int(pair[1]):
        return 0
    elif int(pair[0])< int(pair[1]):
        return 1
    else:
        raise

def add_trinary(pairs, flag):
    for p in itertools.combinations(pairs, 2):
        if "" in (p[0][0], p[0][1], p[1][0], p[1][1]):
            pass
        else:
            if flag == 't':
                turk_tri.append((sign(p[0]), sign(p[1])))
            elif flag == 'e':
                exp_tri.append((sign(p[0]), sign(p[1])))
            elif flag == 'te':
                turk_exp_tri.append((sign(p[0]), sign(p[1])))

n = 0
num_agree = 0
for k, turker in turkerResultBySentence.items():
    if k in expertResultBySentence:
        n+= 1
        experts = expertResultBySentence[k]
        if len(turker) >=2 and len(experts) >= 2:
            add_trinary(turker, 't')
            add_trinary(experts, 'e')
            add_trinary(turker+experts, 'te')

def compute_kappa(data):
    print "kappa: ",
    print skll.kappa(data[0], data[1])
    #print skll.kappa(data[0], data[1], weights='linear')
    print "quadratic weighted kappa: ",
    print skll.kappa(data[0], data[1], weights='quadratic')

print "Turker-control kappa: "
compute_kappa(zip(*turk_tri))
print "Experts(AMU)-control kappa: ",
compute_kappa(zip(*exp_tri))
print "Turker-Experts-control kappa: ",
compute_kappa(zip(*turk_exp_tri))

