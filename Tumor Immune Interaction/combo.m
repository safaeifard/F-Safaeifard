function imumutherapy2 = combo(t,x,p);
%LORENZ: Computes the derivatives involved in solving the
%Lorenz equations.
%gama=p(2); 
sig=p(1); 
kesi=p(2);
x1prime=x(1)/(1+(x(1)^(1/3))/6);


% imumutherapy2=[-sig*x(1)*x(2);-kesi*(x(1)+0.57)*x(2)];
 imumutherapy2=[-sig*x1prime*x(2);
     -kesi*x(1)*x(2)];