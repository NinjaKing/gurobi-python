\ Model matching
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  17.8 var_0_0 + 16.96 var_0_1 + 13.56 var_0_2 + 12.22 var_0_3
   + 15.88 var_0_4 + 17.59 var_0_5 + 13.11 var_1_0 + 7.14 var_1_1
   + 8.57 var_1_2 + 8.67 var_1_3 + 7.23 var_1_4 + 14.49 var_1_5
   + 12.62 var_2_0 + 9.1 var_2_1 + 8.97 var_2_2 + 7.75 var_2_3
   + 16.71 var_2_4 + 16.59 var_2_5 + 12.87 var_3_0 + 7.14 var_3_1
   + 9.75 var_3_2 + 13.87 var_3_3 + 13.59 var_3_4 + 12.37 var_3_5
   + 17.92 var_4_0 + 14.5 var_4_1 + 14.91 var_4_2 + 10 var_4_3
   + 13.67 var_4_4 + 12.56 var_4_5 + 9.9 var_5_0 + 15.7 var_5_1
   + 15.32 var_5_2 + 16.8 var_5_3 + 17.34 var_5_4 + 18.21 var_5_5
Subject To
 R0: var_0_0 + var_0_1 + var_0_2 + var_0_3 + var_0_4 + var_0_5 = 1
 R1: var_1_0 + var_1_1 + var_1_2 + var_1_3 + var_1_4 + var_1_5 = 1
 R2: var_2_0 + var_2_1 + var_2_2 + var_2_3 + var_2_4 + var_2_5 = 1
 R3: var_3_0 + var_3_1 + var_3_2 + var_3_3 + var_3_4 + var_3_5 = 1
 R4: var_4_0 + var_4_1 + var_4_2 + var_4_3 + var_4_4 + var_4_5 = 1
 R5: var_5_0 + var_5_1 + var_5_2 + var_5_3 + var_5_4 + var_5_5 = 1
 R6: var_0_0 + var_1_0 + var_2_0 + var_3_0 + var_4_0 + var_5_0 <= 2
 R7: var_0_1 + var_1_1 + var_2_1 + var_3_1 + var_4_1 + var_5_1 <= 2
 R8: var_0_2 + var_1_2 + var_2_2 + var_3_2 + var_4_2 + var_5_2 <= 2
 R9: var_0_3 + var_1_3 + var_2_3 + var_3_3 + var_4_3 + var_5_3 <= 2
 R10: var_0_4 + var_1_4 + var_2_4 + var_3_4 + var_4_4 + var_5_4 <= 2
 R11: var_0_5 + var_1_5 + var_2_5 + var_3_5 + var_4_5 + var_5_5 <= 2
Bounds
Binaries
 var_0_0 var_0_1 var_0_2 var_0_3 var_0_4 var_0_5 var_1_0 var_1_1 var_1_2
 var_1_3 var_1_4 var_1_5 var_2_0 var_2_1 var_2_2 var_2_3 var_2_4 var_2_5
 var_3_0 var_3_1 var_3_2 var_3_3 var_3_4 var_3_5 var_4_0 var_4_1 var_4_2
 var_4_3 var_4_4 var_4_5 var_5_0 var_5_1 var_5_2 var_5_3 var_5_4 var_5_5
End
