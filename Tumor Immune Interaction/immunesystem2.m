function wholesystem = immunesystem(t,x);

% sig=0.0000003;
% kesi=0.005;
% gama=0.038; 
% alpha=0.035;
% beta=2;
sig=0.00000025;
kesi=0.0000003;
gama=0.000002; 
alpha=0.02;
beta=0.00005;
x1prime=x(1)/(1+(x(1)^(1/3))/6);

% wholesystem=[-sig*x(1)*(x(2)+x(3)+x(4));
%              -gama*x(1)*x(2)-alpha*x(2)-kesi*(x(1)+0.57)*x(2);
%              -gama*x(1)*x(3)-alpha*x(3)+alpha*x(2)-kesi*(x(1)+0.57)*x(3);
%              -gama*x(1)*x(4)-beta*x(1)*x(4)+alpha*x(3)-kesi*(x(1)+0.57)*x(4);
%              +gama*x(1)*x(2);
%              +gama*x(1)*x(3);
%              +gama*x(1)*x(4);
%              +beta*x(1)*x(4)]; 
wholesystem=[-sig*x1prime*(x(2)+x(3)+x(4));
             -gama*x1prime*x(2)-alpha*x(2)-kesi*x(1)*x(2);
             -gama*x1prime*x(3)-alpha*x(3)+alpha*x(2)-kesi*x(1)*x(3);
             -gama*x1prime*x(4)-beta*x1prime*x(4)+alpha*x(3)-kesi*x(1)*x(4);
             +gama*x1prime*x(2);
             +gama*x1prime*x(3);
             +gama*x1prime*x(4);
             +beta*x1prime*x(4)]; 

         