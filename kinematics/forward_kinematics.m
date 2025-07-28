 clc;
close all;
clear all;

syms th1 th2 th3 th4 d1 a1 a1 a2 a3
syms T0_1 T1_2 T2_3 T3_4 T4_5 T0_5

th1 = deg2rad(0);
th2 = deg2rad(90);
th3 = deg2rad(90);
th4 = deg2rad(0);

d1 = 105; a1 = 105; a2 = 75; a3 = 30;

T0_1 = [cos(th1) -sin(th1) 0 0; 
        sin(th1) cos(th1) 0 0; 
        0 0 1 d1; 
        0 0 0 1;
        ];

T1_2 = [cos(th2) -sin(th2) 0 0; 
        0 0 -1 0; 
        sin(th2) cos(th2) 0 0; 
        0 0 0 1;
        ];

T2_3 = [cos(th3) -sin(th3) 0 a1; 
        -sin(th3) -cos(th3) 0 0; 
        0 0 -1 0; 
        0 0 0 1;
        ];

T3_4 = [cos(th4) -sin(th4) 0 a2; 
        -sin(th4) -cos(th4) 0 0; 
        0 0 -1 0; 
        0 0 0 1;
        ];

T4_5 = [1 0 0 a3; 
        0 1 0 0; 
        0 0 1 0; 
        0 0 0 1;
        ];

T0_5 = T0_1*T1_2*T2_3*T3_4*T4_5;
disp(T0_5)