a=xlsread('NORMALIZED ACTIVITY PD-1.xlsx');
aa=a(15:138,17);
aaa=a(15:138,18);
% p=[0.0000003 0.005 0.038];
%p=[0.00000021 0.00000025 0.000002];
%0.000005
p=[0.0000003 0.00000035 0.000002];
tspan=[0,123];
%x0=[0.35 22851.1180876601]; 
x0=[21825 22851.1180876601];
[t,x]=ode45(@pd1,tspan,x0,[],p);
figure(1)
plot(t(:,1),x(:,1))
% dim = [0.65 0.5 0.2 0.4];
% str = {'PD-1 Blockade'};
% annotation('textbox',dim,'String',str,'FitBoxToText','on')
xlabel('Time(frame)')
ylabel('Tumor Cells')
figure(2)
%plot(0:123,aa(:,1))
errorbar(aa,aaa)
hold on
plot(t(:,1),x(:,2))
% dim = [0.65 0.5 0.2 0.4];
% str = {'PD-1 Blockade'};
% annotation('textbox',dim,'String',str,'FitBoxToText','on')
xlabel('frame')
ylabel('Lymphocyte Activity (\mum)')

