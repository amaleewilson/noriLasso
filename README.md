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