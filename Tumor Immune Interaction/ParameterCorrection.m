function imumutherapy3ParameterCorrection = ctla4(t,x,p);
%LORENZ: Computes the derivatives involved in solving the
%Lorenz equations.
sig=p(1);
kesi=p(2);
gama=p(3); 
alpha1=p(4);
alpha2=p(5);
beta=p(6);
x1prime=x(1)/(1+(x(1)^(1/3))/6);


%imumutherapy3=[-sig*x(1)*(x(2)+x(3));-alpha*x(1)*x(2)-kesi*(x(1)+0.57)*x(2);-beta*x(3)*x(1)+alpha*x(1)*x(2)-kesi*(x(1)+0.57)*x(3);];
% imumutherapy3=[-sig*x(1)*(x(2)+x(3)+x(4));
%                 -alpha1*x(2)-kesi*(x(1)+0.57)*x(2);
%                 alpha1*x(2)-kesi*(x(1)+0.57)*x(3)-alpha2*x(3);
%                 -beta*x(4)*x(1)+alpha2*x(3)-kesi*(x(1)+0.57)*x(4)];
            imumutherapy3ParameterCorrection=[-sig*x1prime*(x(2)+x(3)+x(4));
                -alpha1*x(2)-kesi*x(1)*x(2);
                alpha1*x(2)-kesi*x(1)*x(3)-alpha2*x(3);
                -beta*x(4)*x1prime+alpha2*x(3)-kesi*x(1)*x(4)];

  

            
            
            