b=xlsread('NORMALIZED ACTIVITY CTL-4.PD-1.xlsx');
bb=b(15:143,14);
bbb=b(15:143,16);
% p=[0.0000003 0.005];
% p=[0.0000008 0.0000013];
%0.00000025
p=[0.0000003 0.00000035];

%[t,x]=ode45(@combo,[0 142],[9000 0.35],[],p);
% x0=[0.35 114556.14270614];
x0=[21825 114556.14270614];
tspan=[0,128];
[t,x]=ode45(@combo,tspan,x0,[],p); %p vector reversed
figure(1)
plot(t(:,1),x(:,2))
hold on
errorbar(bb(:,1),bbb(:,1))
dim = [0.6 0.5 0.2 0.4];
str = {'Combination Therapy'};
annotation('textbox',dim,'String',str,'FitBoxToText','on')
xlabel('Frames')
ylabel('Lymphocyte Activity')
figure(2)
plot(t(:,1),x(:,1))
str = {'Combination Therapy'};
annotation('textbox',dim,'String',str,'FitBoxToText','on')
xlabel('Frames')
ylabel('Tumor Cells')



