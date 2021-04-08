function imumutherapy1 = pd1(t,x,p);

sig=p(1);
kesi=p(2);
gama=p(3); 
x1prime=x(1)/(1+(x(1)^(1/3))/6);


% imumutherapy1=[-sig*x(1)*x(2);-gama*x(1)*x(2)-(kesi*(x(1)+0.57)*x(2))];
imumutherapy1=[-sig*x1prime*x(2);
    -gama*x1prime*x(2)-kesi*x(1)*x(2)];