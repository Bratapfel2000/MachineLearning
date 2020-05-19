% The ; denotes we are going back to a new row.
A = [1, 2, 3; 4, 5, 6; 7, 8, 9; 10, 11, 44]

% Initialize a vector 
v = [1;2;3] 

% Get the dimension of the matrix A where m = rows and n = columns
[m,n] = size(A)

% You could also store it this way
dim_A = size(A)

% Get the dimension of the vector v 
dim_v = size(v)

% Now let's index into the 2nd row 3rd column of matrix A
A_23 = A(2,3)

% Initialize matrix C and D 
C = [1, 2, 4; 5, 3, 2]
D = [1, 3, 4; 1, 1, 1]

% Initialize constant s 
s = 2

% See how element-wise addition works
add_CD = C + D 

% See how element-wise subtraction works
sub_CD = C - D

% See how scalar multiplication works
mult_Cs = C * s

% Divide C by s
div_Cs = C / s

% What happens if we have a Matrix + scalar?
add_Cs = C + s

% Initialize matrix E 
E = [1, 2, 3; 4, 5, 6;7, 8, 9] 

% Initialize vector w 
w = [1; 1; 1] 

% Multiply E * w
Ew = E * w

% Initialize a 3 by 2 matrix 
F = [1, 2; 3, 4;5, 6]

% Initialize a 2 by 1 matrix 
G = [1; 2] 

% We expect a resulting matrix of (3 by 2)*(2 by 1) = (3 by 1) 
mult_FG = F*G

% Initialize random matrices A and B 
J = [1,2;4,5]
K = [1,1;0,2]

% Initialize a 2 by 2 identity matrix
I = eye(2)

% The above notation is the same as I = [1,0;0,1]

% What happens when we multiply I*J ? 
IJ = I*J 

% How about J*I ? 
JI = J*I 

% Compute J*K 
JK = J*K 

% Is it equal to K*J? 
KJ = K*J 

% Note that IJ = JI but JK != KJ

% Initialize matrix L 
L = [1,2,0;0,5,6;7,0,9]

% Transpose L 
L_trans = L' 

% Take the inverse of L 
L_inv = inv(L)

% What is L^(-1)*L? 
L_invL = inv(L)*L

