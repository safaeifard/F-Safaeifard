global nPeriods
UnitLenght=15;
h1=[1.5 ;4.5 ;7.5; 10.5 ;13.5 ];
h2=cat(1,h1(2:5),h1(1));
h3=cat(1,h1(3:5),h1(1:2));
h4=cat(1,h1(4:5),h1(1:3));
h5=cat(1,h1(5),h1(1:4));
hh=[1.5; 4.5; 7.5; 10.5 ;13.5 ];
InitPos=cat(1,h1,h1,h1,h1,h1,h1,h2,h3,h4,h5);

for Temp=0:0.1:3;
   F=@BrwDynFunction;
   G = @(t,xycoord)((sqrt(2*Temp)* eye (50)));
   nPeriods =10000;  
   dt       =   1;
   nsteps=1000;
    
 mySDE = sde(F, G, 'startstate',InitPos);

[pos,T] = simulate(mySDE, nPeriods, 'DeltaTime', dt,'nTrials', 1, 'nsteps',nsteps);
  
  [V_t]=LJEnergyFunc(pos);
  
    figure
   plot(V_t)
   xlabel('Time')
   ylabel('Lenard-Jones Potential')
   
   
end

