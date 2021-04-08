
UnitLenght=15;
Temp=0.01;
% InitPos=15*rand(50,1);
h1=[1.5 ;4.5 ;7.5; 10.5 ;13.5 ];
h2=cat(1,h1(2:5),h1(1));
h3=cat(1,h1(3:5),h1(1:2));
h4=cat(1,h1(4:5),h1(1:3));
h5=cat(1,h1(5),h1(1:4));
hh=[1.5; 4.5; 7.5; 10.5 ;13.5 ];
InitPos=cat(1,h1,h1,h1,h1,h1,h1,h2,h3,h4,h5);

   F=@BrwDynFunction;
   G = @(t,xycoord)((sqrt(2*Temp)* eye (50)));
   nPeriods =5000;                   % 50000 for higher  temp riding of Nan
   dt       =   1;                     % 0.1 for higher  temp riding of Nan
    nsteps=1000;
    
 mySDE = sde(F, G, 'startstate',InitPos);

[pos,T] = simulate(mySDE, nPeriods, 'DeltaTime', dt,'nTrials', 1, 'nsteps',nsteps); 
% 100 for higher  temp riding of Nan

 M= mod (pos,UnitLenght);
  xcoord_M=M(:,1:25);
  ycoord_M=M(:,26:50);

 for j = 1:nPeriods+1
scatter (xcoord_M(j,:),ycoord_M(j,:),'filled')
%scatter (xcoord_M(j,1),ycoord_M(j,1),[], xcoord_M(1,1),'filled')
 xlim ([0 15])
 ylim ([0 15])
    drawnow
    getframe;
end

   
% Tempreture=(1:11);
% %scatter(M(:,1:25), M(:,26:50))
 %plot(M(:,1:25), M(:,26:50),'o')
% plot(M(61,:), M(61,:),'o')
% figure
%plot(T,M(:,1))n
% plot(Tempreture,Final_V)
