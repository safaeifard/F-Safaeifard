%in ra sakhtam ta bad az behbud dadan parameter alpha tozie jamiate avahie
 %ra emtehan konim va dobare parameter ra ba maghadire avahie dorosttar
 %tashih konim
% c=xlsread('AVERAGE ACTIVITY. CTL-4.xlsx');
% cc=c(15:144,32);
% x0=[0.35 102945 0 0 0 0 0 0];
%x0=[0.35 402945 0 0 0 0 0 0];
x0=[21825 74599.9889326763 42446.4750009074 6929.05273781641 0 0 0 0];
% tspan=[0,129];
tspan=[0,300];
[t,x]=ode45(@immunesystem,tspan,x0);
Z=x(:,2)+x(:,3)+x(:,4);
figure(1)
 plot(t(:,1),Z);
% hold on
 %plot(0:129,cc(:,1))
 ctla4Inactivated=x(end,5)+x(end,6)+x(end,7);
 ctla4Inactivatedvec=x(:,5)+x(:,6)+x(:,7);
 figure(2)
 plot(t(:,1),ctla4Inactivatedvec)
figure(3)
plot(t(:,1),x(:,1))