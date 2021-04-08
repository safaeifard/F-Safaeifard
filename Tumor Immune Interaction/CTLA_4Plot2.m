c=xlsread('NORMALIZED ACTIVITY CTL-4.xlsx');
cc=c(15:144,34);
ccc=c(15:144,35);
 %p=[0.0000003 0.005 0.038 0.035 0.035 2];
p=[0.0000003 0.00000035 0.000002 0.028 0.028 0.00005];
%p=[0.00000025 0.0000003 0.000005 0.03 0.03 0.00005];
%p=[0.00000025 0.0000003 0.00005 0.03 0.03 0.00005];
% delaye kame model fi khatere martabe aval budane (rabtesh be taghirate stoka???)
%bad khastim martabe ra taghir nadahim raftim sarvaghte interactiom
%mostaghim ya gheyre mostaghim)
%p=[0.00000459 0.0000090 0.0098890];

tspan=[0 129];
%  x0=[0.35 102944.401567572 0 0];
x0=[21825 124000.401567572 0 0];
figure(1)
%%%hold off
[t,x]=ode45(@ctla4,tspan,x0,[],p);
%%%plot(t(:,1),x(:,2))
% % % hold on
% % % plot(t(:,1),x(:,4))
%Z=zeros(length(x),1);
Z=x(:,2)+x(:,3)+x(:,4);
% for i=1:length(x)
%     Z(i)=x(i,2)+x(i,3)+x(i;
% end
%%%figure(2)
%%%hold off
plot(t(:,1),x(:,1))
%hold on
%plot(t(:,1),x(:,2))
% dim = [0.65 0.5 0.2 0.4];
% str = {'CTLA-4 Blockade'};
% annotation('textbox',dim,'String',str,'FitBoxToText','on')
xlabel('frame')
ylabel('Tumor Cells')
figure(3)
hold off
plot(t(:,1),Z);
hold on
% % % plot(t(:,1),x(:,2)+x(:,3));
% % % plot(t(:,1),x(:,3));

errorbar(cc,ccc)
% dim = [0.65 0.5 0.2 0.4];
% str = {'CTLA-4 Blockade'};
% annotation('textbox',dim,'String',str,'FitBoxToText','on')
xlabel('Time (frame)')
ylabel('Lymphocyte Activity')
%errorbar(0:129,cc(:,1),c(15:144,36))

