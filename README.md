# noriLasso

Requires cvc5 to be built with Python API, e.g. `./configure.sh --python-bindings --auto-download`


```
python3.11 run_cvc5.py -if NoriSharma-2013FSE-Fig8_true-termination.c_Iteration1_Lasso_4-pieceTemplate.smt2                                                            
Solve Time: 64.47738122940063
Resources : 6512094
Conflicts : 7444
Decisions : 1366571
Result    : unsat
```

```
python3.11 run_partitions.py -if NoriSharma-2013FSE-Fig8_true-termination.c_Iteration1_Lasso_4-pieceTemplate.smt2 -p  ~/repos/main_cvc5/cvc5/build/bin/cvc5                                              
Generated partitions 8 in 3.1308488845825195 seconds
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
P0 Solve Time: 121.83121371269226
P0 Resources : 7178770
P0 Conflicts : 8812
P0 Decisions : 1312799
P0 Result    : unsat

P1 Solve Time: 1.9480493068695068
P1 Resources : 1671274
P1 Conflicts : 0
P1 Decisions : 0
P1 Result    : unsat

P2 Solve Time: 1.93983793258667
P2 Resources : 1671274
P2 Conflicts : 0
P2 Decisions : 0
P2 Result    : unsat

P3 Solve Time: 1.9049060344696045
P3 Resources : 1671279
P3 Conflicts : 0
P3 Decisions : 0
P3 Result    : unsat

P4 Solve Time: 1.9331810474395752
P4 Resources : 1671274
P4 Conflicts : 0
P4 Decisions : 0
P4 Result    : unsat

P5 Solve Time: 2.010748863220215
P5 Resources : 1671279
P5 Conflicts : 0
P5 Decisions : 0
P5 Result    : unsat

P6 Solve Time: 2.0047812461853027
P6 Resources : 1671279
P6 Conflicts : 0
P6 Decisions : 0
P6 Result    : unsat

P7 Solve Time: 1.953009843826294
P7 Resources : 1671284
P7 Conflicts : 0
P7 Decisions : 0
P7 Result    : unsat
```

Interestingly, behavior is different when producing unsat cores. 

```
python3.11 run_cvc5.py -if NoriSharma-2013FSE-Fig8_true-termination.c_Iteration1_Lasso_4-pieceTemplate.smt2 --dump-unsat-cores --dump-file original_unsat_core_dump.out
Solve Time: 278.27903413772583
Resources : 12024667
Conflicts : 15923
Decisions : 2125452
Result    : unsat
```

```
python3.11 run_partitions.py -if NoriSharma-2013FSE-Fig8_true-termination.c_Iteration1_Lasso_4-pieceTemplate.smt2 -p  ~/repos/main_cvc5/cvc5/build/bin/cvc5 --dump-unsat-cores --dump-file partitions_unsat_core_dump.out
Generated partitions 8 in 3.402176856994629 seconds
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
P0 Solve Time: 121.46920323371887
P0 Resources : 6379674
P0 Conflicts : 7636
P0 Decisions : 926348
P0 Result    : unsat

P1 Solve Time: 2.896038055419922
P1 Resources : 2141745
P1 Conflicts : 0
P1 Decisions : 0
P1 Result    : unsat

P2 Solve Time: 2.9803969860076904
P2 Resources : 2141745
P2 Conflicts : 0
P2 Decisions : 0
P2 Result    : unsat

P3 Solve Time: 2.9520010948181152
P3 Resources : 2141746
P3 Conflicts : 0
P3 Decisions : 0
P3 Result    : unsat

P4 Solve Time: 2.8266079425811768
P4 Resources : 2141745
P4 Conflicts : 0
P4 Decisions : 0
P4 Result    : unsat

P5 Solve Time: 2.855386257171631
P5 Resources : 2141746
P5 Conflicts : 0
P5 Decisions : 0
P5 Result    : unsat

P6 Solve Time: 2.887199878692627
P6 Resources : 2141746
P6 Conflicts : 0
P6 Decisions : 0
P6 Result    : unsat

P7 Solve Time: 2.9592182636260986
P7 Resources : 2141747
P7 Conflicts : 0
P7 Decisions : 0
P7 Result    : unsat
```


Now trying th simplfied version (I removed the simulated partitions): 

```
python3.11 run_cvc5.py -if ~/repos/SMTExamples/NoriSimp.smt2 
Solve Time: 229.24306273460388
Resources : 8393776
Conflicts : 12806
Decisions : 1201971
Result    : unsat
```

```
python3.11 run_partitions.py -if ~/repos/SMTExamples/NoriSimp.smt2  -p  ~/repos/main_cvc5/cvc5/build/bin/cvc5                                               
Generated partitions 8 in 4.295189142227173 seconds
(and (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0) (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0) (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0))
(and (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0) (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0) (not (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0)))
(and (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0) (not (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0)) (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0))
(and (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0) (not (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0)) (not (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0)))
(and (not (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0)) (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0) (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0))
(and (not (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0)) (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0) (not (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0)))
(and (not (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0)) (not (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0)) (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0))
(and (not (>= (+ motzkin_13511_0 (* (- 1) motzkin_13511_1) motzkin_13511_3 (* (- 1) motzkin_13511_4)) 0)) (not (>= (+ (* (- 1) motzkin_13511_0) motzkin_13511_1 motzkin_13511_5) 0)) (not (>= (+ (* (- 1) motzkin_13511_3) motzkin_13511_4) 0)))
P0 Solve Time: 205.1964201927185
P0 Resources : 6851639
P0 Conflicts : 11548
P0 Decisions : 1028079
P0 Result    : unsat

P1 Solve Time: 1.8981389999389648
P1 Resources : 1565608
P1 Conflicts : 0
P1 Decisions : 0
P1 Result    : unsat

P2 Solve Time: 1.839169979095459
P2 Resources : 1565608
P2 Conflicts : 0
P2 Decisions : 0
P2 Result    : unsat

P3 Solve Time: 1.904181957244873
P3 Resources : 1565613
P3 Conflicts : 0
P3 Decisions : 0
P3 Result    : unsat

P4 Solve Time: 1.8569653034210205
P4 Resources : 1565608
P4 Conflicts : 0
P4 Decisions : 0
P4 Result    : unsat

P5 Solve Time: 1.9116439819335938
P5 Resources : 1565613
P5 Conflicts : 0
P5 Decisions : 0
P5 Result    : unsat

P6 Solve Time: 1.8653020858764648
P6 Resources : 1565613
P6 Conflicts : 0
P6 Decisions : 0
P6 Result    : unsat

P7 Solve Time: 1.8581230640411377
P7 Resources : 1565618
P7 Conflicts : 0
P7 Decisions : 0
P7 Result    : unsat
```

Trying to partition on first 3 decisions (original problem): 
```
python3.11 run_partitions.py -if NoriSharma-2013FSE-Fig8_true-termination.c_Iteration1_Lasso_4-pieceTemplate.smt2 -p  ~/repos/main_cvc5/cvc5/build/bin/cvc5 -cbp 1
Generated partitions 8 in 2.513467311859131 seconds
(and (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0)) (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0) (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0))
(and (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0)) (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0) (not (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0)))
(and (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0)) (not (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0)) (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0))
(and (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0)) (not (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0)) (not (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0)))
(and (not (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0))) (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0) (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0))
(and (not (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0))) (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0) (not (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0)))
(and (not (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0))) (not (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0)) (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0))
(and (not (not (>= (+ (* (- 1) si12583c) (* 2 motzkin_12582_1) motzkin_12582_2 (* (- 1) motzkin_12582_3) (* (- 1) motzkin_12582_4) motzkin_12582_5) 0))) (not (>= (+ (* (- 1) motzkin_13709_4) motzkin_13709_5 motzkin_13715_5 (* (- 1) motzkin_13715_6)) 0)) (not (>= (+ (* (- 1) si12833c) motzkin_13715_3 (* (- 1) motzkin_13715_4) (* (- 1) motzkin_13715_5) motzkin_13715_6) 0)))
P0 Solve Time: 251.07379508018494
P0 Resources : 10416036
P0 Conflicts : 13359
P0 Decisions : 1993343
P0 Result    : unsat

P1 Solve Time: 183.69241499900818
P1 Resources : 8303337
P1 Conflicts : 10170
P1 Decisions : 1600645
P1 Result    : unsat

P2 Solve Time: 2.0732028484344482
P2 Resources : 1671483
P2 Conflicts : 7
P2 Decisions : 13
P2 Result    : unsat

P3 Solve Time: 2.025279998779297
P3 Resources : 1671491
P3 Conflicts : 7
P3 Decisions : 12
P3 Result    : unsat

P4 Solve Time: 249.23270797729492
P4 Resources : 9214155
P4 Conflicts : 12201
P4 Decisions : 1817390
P4 Result    : unsat

P5 Solve Time: 117.62706708908081
P5 Resources : 7784935
P5 Conflicts : 9410
P5 Decisions : 1475603
P5 Result    : unsat

P6 Solve Time: 2.120968818664551
P6 Resources : 1671466
P6 Conflicts : 7
P6 Decisions : 13
P6 Result    : unsat

P7 Solve Time: 2.0804998874664307
P7 Resources : 1671474
P7 Conflicts : 7
P7 Decisions : 12
P7 Result    : unsat
```


Partitioning on first 3 decisions (simplified problem):
```
python3.11 run_partitions.py -if ~/repos/SMTExamples/NoriSimp.smt2 -p  ~/repos/main_cvc5/cvc5/build/bin/cvc5 -cbp 1 
Generated partitions 8 in 2.42874813079834 seconds
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0)) (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0)) (>= (+ motzkin_13715_5 _let_1) 0)))
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0)) (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0)) (not (>= (+ motzkin_13715_5 _let_1) 0))))
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0)) (not (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0))) (>= (+ motzkin_13715_5 _let_1) 0)))
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0)) (not (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0))) (not (>= (+ motzkin_13715_5 _let_1) 0))))
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0))) (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0)) (>= (+ motzkin_13715_5 _let_1) 0)))
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0))) (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0)) (not (>= (+ motzkin_13715_5 _let_1) 0))))
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0))) (not (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0))) (>= (+ motzkin_13715_5 _let_1) 0)))
(let ((_let_1 (* (- 1) motzkin_13715_6))) (and (not (not (>= (+ (* (- 1) si12585c) (* 2 motzkin_12584_1) motzkin_12584_2 (* (- 1) motzkin_12584_3) (* (- 1) motzkin_12584_4) motzkin_12584_5) 0))) (not (not (>= (+ (* (- 1) motzkin_13715_3) motzkin_13715_4 motzkin_13715_5 _let_1) 0))) (not (>= (+ motzkin_13715_5 _let_1) 0))))
P0 Solve Time: 156.8487629890442
P0 Resources : 6515855
P0 Conflicts : 11110
P0 Decisions : 1058360
P0 Result    : unsat

P1 Solve Time: 144.87387919425964
P1 Resources : 7204251
P1 Conflicts : 10248
P1 Decisions : 1240529
P1 Result    : unsat

P2 Solve Time: 421.9641230106354
P2 Resources : 12480049
P2 Conflicts : 18580
P2 Decisions : 2196620
P2 Result    : unsat

P3 Solve Time: 241.69115114212036
P3 Resources : 8776293
P3 Conflicts : 13043
P3 Decisions : 1555306
P3 Result    : unsat

P4 Solve Time: 301.14756083488464
P4 Resources : 10334048
P4 Conflicts : 12870
P4 Decisions : 1822013
P4 Result    : unsat

P5 Solve Time: 353.62824034690857
P5 Resources : 9620390
P5 Conflicts : 15059
P5 Decisions : 1560440
P5 Result    : unsat

P6 Solve Time: 215.91140484809875
P6 Resources : 8234732
P6 Conflicts : 11912
P6 Decisions : 1445212
P6 Result    : unsat

P7 Solve Time: 178.16045308113098
P7 Resources : 7130754
P7 Conflicts : 9830
P7 Decisions : 1114130
P7 Result    : unsat
```



When using the same partitions for original and simplified problem, behavior is preserved: 

```
python3.11 run_cvc5.py -if NoriSharma-2013FSE-Fig8_true-termination.c_Iteration1_Lasso_4-pieceTemplate.smt2
Solve Time: 59.936448097229004
Resources : 6512094
Conflicts : 7444
Decisions : 1366571
Result    : unsat
```

```
python3.11 run_set_partitions.py -if NoriSharma-2013FSE-Fig8_true-termination.c_Iteration1_Lasso_4-pieceTemplate.smt2 -p  ~/repos/main_cvc5/cvc5/build/bin/cvc5
Generated partitions 8 in 0.0 seconds
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
P0 Solve Time: 111.75183367729187
P0 Resources : 7178770
P0 Conflicts : 8812
P0 Decisions : 1312799
P0 Result    : unsat

P1 Solve Time: 1.9607698917388916
P1 Resources : 1671274
P1 Conflicts : 0
P1 Decisions : 0
P1 Result    : unsat

P2 Solve Time: 1.9564340114593506
P2 Resources : 1671274
P2 Conflicts : 0
P2 Decisions : 0
P2 Result    : unsat

P3 Solve Time: 1.9480340480804443
P3 Resources : 1671279
P3 Conflicts : 0
P3 Decisions : 0
P3 Result    : unsat

P4 Solve Time: 2.1038482189178467
P4 Resources : 1671274
P4 Conflicts : 0
P4 Decisions : 0
P4 Result    : unsat

P5 Solve Time: 2.011591911315918
P5 Resources : 1671279
P5 Conflicts : 0
P5 Decisions : 0
P5 Result    : unsat

P6 Solve Time: 1.9415302276611328
P6 Resources : 1671279
P6 Conflicts : 0
P6 Decisions : 0
P6 Result    : unsat

P7 Solve Time: 1.912503957748413
P7 Resources : 1671284
P7 Conflicts : 0
P7 Decisions : 0
P7 Result    : unsat
```

```
python3.11 run_cvc5.py -if ~/repos/SMTExamples/NoriSimp.smt2                                                                     
Solve Time: 237.34437561035156
Resources : 8393776
Conflicts : 12806
Decisions : 1201971
Result    : unsat
```


```
python3.11 run_set_partitions.py -if ~/repos/SMTExamples/NoriSimp.smt2 -p  ~/repos/main_cvc5/cvc5/build/bin/cvc5                 
Generated partitions 8 in 3.814697265625e-06 seconds
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0))
(and (not (>= (+ motzkin_13490_0 (* (- 1) motzkin_13490_1) motzkin_13490_3 (* (- 1) motzkin_13490_4)) 0)) (not (>= (+ (* (- 1) motzkin_13490_0) motzkin_13490_1 motzkin_13490_5) 0)) (not (>= (+ (* (- 1) motzkin_13490_3) motzkin_13490_4) 0)))
P0 Solve Time: 372.96286487579346
P0 Resources : 11373584
P0 Conflicts : 16814
P0 Decisions : 2051978
P0 Result    : unsat

P1 Solve Time: 1.9026298522949219
P1 Resources : 1565608
P1 Conflicts : 0
P1 Decisions : 0
P1 Result    : unsat

P2 Solve Time: 1.9681987762451172
P2 Resources : 1565608
P2 Conflicts : 0
P2 Decisions : 0
P2 Result    : unsat

P3 Solve Time: 1.8368699550628662
P3 Resources : 1565613
P3 Conflicts : 0
P3 Decisions : 0
P3 Result    : unsat

P4 Solve Time: 1.8750169277191162
P4 Resources : 1565608
P4 Conflicts : 0
P4 Decisions : 0
P4 Result    : unsat

P5 Solve Time: 1.984494924545288
P5 Resources : 1565613
P5 Conflicts : 0
P5 Decisions : 0
P5 Result    : unsat

P6 Solve Time: 2.0130341053009033
P6 Resources : 1565613
P6 Conflicts : 0
P6 Decisions : 0
P6 Result    : unsat

P7 Solve Time: 2.064584970474243
P7 Resources : 1565618
P7 Conflicts : 0
P7 Decisions : 0
P7 Result    : unsat
```