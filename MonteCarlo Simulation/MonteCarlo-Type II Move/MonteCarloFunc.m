function [Ms, Es, CLs] = MonteCarloFunc(T) 
%samples spins sum
Ms = [];

%samples energy
Es = [];
%samples correlation length
CLs=[];
% Generate a random initial configuration
SystemState=zeros(20,20);
for i=1:20
     for j=1:20     
 spinstate=[1 -1]; 
 SystemState(i,j)=spinstate(randi(numel(spinstate)));
     end
end
righthandenergy=sum(sum(SystemState.*circshift(SystemState,1,2)));
leftthandenergy=sum(sum(SystemState.*circshift(SystemState,19,2)));
upwardenergy=sum(sum(SystemState.*circshift(SystemState,1,1)));
downwardenergy=sum(sum(SystemState.*circshift(SystemState,19,1)));

 %total energy
 E=-1/2*(righthandenergy+leftthandenergy+upwardenergy+downwardenergy);
 
for i=1:500000 
%ij=randi(20,2,3);
ij=randi(20,2,2);
Stest=SystemState;

Stest(ij(1,1),ij(2,1))=-Stest(ij(1,1),ij(2,1));
Stest(ij(1,2),ij(2,2))=-Stest(ij(1,2),ij(2,2));
%Stest(ij(1,3),ij(2,3))=-Stest(ij(1,3),ij(2,3));

%total testenergy

Etest1=Stest(ij(1,1),ij(2,1)).*(Stest(mod(ij(1,1),20)+1,ij(2,1))+Stest(mod(ij(1,1)-2,20)+1,ij(2,1))+Stest(ij(1,1),mod(ij(2,1),20)+1)+Stest(ij(1,1),mod(ij(2,1)-2,20)+1));
Etest2=Stest(ij(1,2),ij(2,2)).*(Stest(mod(ij(1,2),20)+1,ij(2,2))+Stest(mod(ij(1,2)-2,20)+1,ij(2,2))+Stest(ij(1,2),mod(ij(2,2),20)+1)+Stest(ij(1,2),mod(ij(2,2)-2,20)+1));
%Etest3=Stest(ij(1,3),ij(2,3))*(Stest(mod(ij(1,3),20)+1,ij(2,3))+Stest(mod(ij(1,3)-2,20)+1,ij(2,3))+Stest(ij(1,3),mod(ij(2,3),20)+1)+Stest(ij(1,3),mod(ij(2,3)-2,20)+1));

Etest=Etest1+Etest2;
deltaE=2*Etest;

 p=min(1,exp(-deltaE/T));
  r=rand;
   if p>=r
     
       SystemState=Stest;
       E=E+deltaE;
   end

if i>=10000&& mod(i,1000)==0
    
    %calculation of samples magnetizations
Ms=[Ms sum(sum(SystemState))];

%energy
%E=sum(sum(SystemState.*circshift(SystemState,1,2)),2)+sum(sum(SystemState.*circshift(SystemState,19,2)),2)+sum(sum(SystemState.*circshift(SystemState,1,1)),2)+sum(sum(SystemState.*circshift(SystemState,19,1)),2);
Es=[Es E];

%calculation of autocorrelation length
AutocorrMatrix=zeros(20,20);
MeanAutocorr=zeros(1,20);
counter=0;
     for z=1:20
     AutocorrMatrix(z,:)=autocorr((SystemState(z,:)),19);
     end
       for zz=1:20
        MeanAutocorr(zz)=mean(AutocorrMatrix(:,zz));
       end
       for zzz=1:20
       while MeanAutocorr(zzz)>=exp(-1);
       counter=counter+1;
       break
       end
       end

   CLs=[CLs counter];
end

 end
