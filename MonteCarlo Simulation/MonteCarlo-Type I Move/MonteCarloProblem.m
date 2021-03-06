EnergyVector=[];
MeanMagnetization = [];
Thermalcapacity = [];
MeanAutocorr=[];
Tempreture=[1:0.1:4];
% Montecarlo sampling
for T=1:0.1:4
   Magnetization = [];
   EnergySamples = [];
   CorrelationLength=[];
   %random state generation
   c=zeros(20,20);
for i=1:20
     for j=1:20     
 spinstate=[1 -1]; 
 systemstate(i,j)=spinstate(randi(numel(spinstate)));
     end
end
for i=1:500000,
% neighbors matrixes
neighbors=circshift(systemstate,1,2)+circshift(systemstate,19,2)+circshift(systemstate,1,1)+circshift(systemstate,19,1);
%energy matrix of spin transitions
SystemEnergy= systemstate.* neighbors;
%generating a target system with energy equals to -(SystemEnergy)
 deltaE = 2 *SystemEnergy;
 
 %matrix of transition probobility
  p = exp(-deltaE/(T));
  
%refining the transition probability
  a=(rand(20) < 0.1);
   %spin selection for transition based on p
  b=(rand(20)< p );
   TransitionMatrix = b.*a * -2 + 1;
   
   %the final state
    systemstate = systemstate .* TransitionMatrix;
    
    % energy of transitions (in a fixed T) for plotting energy equlibrium
    if T==2
        EnergyVector=[EnergyVector -sum(sum(SystemEnergy))/2];
    end
    
    %sampling the objected variables
    
if i>=10000&& mod(i,1000)==0
Magnetization=[Magnetization sum(sum(systemstate))];
EnergySamples=[EnergySamples -sum(sum(SystemEnergy))/2];


AutocorrMatrix=zeros(20,20);
SpatialAutocorr=zeros(1,20);
counter=0;
     for z=1:20
     AutocorrMatrix(z,:)=autocorr((systemstate(z,:)),19);
     end
       for zz=1:20
        SpatialAutocorr(zz)=mean(AutocorrMatrix(:,zz));
       end
       for zzz=1:20
       while SpatialAutocorr(zzz)>=exp(-1);
       counter=counter+1;
       break
       end
       end
       
CorrelationLength=[CorrelationLength counter];
end
%load('MonteCarloProblem.mat')
%save('MonteCarloProblem.mat')

end


MeanMagnetization = [MeanMagnetization mean(Magnetization)/(20^2)];
Thermalcapacity = [Thermalcapacity var(EnergySamples)/T^2];
MeanAutocorr=[MeanAutocorr var(CorrelationLength)/T^2];

end
%ploting the results
plot(EnergyVector);
ylabel('Energy');
figure
plot(1./Tempreture,MeanMagnetization,'o','MarkerFaceColor',[0.1,0.1,0.5]);
ylabel('Magnetization');
xlabel('Temperature');
figure
plot(Tempreture,Thermalcapacity)
ylabel('Thermal Capacity');
xlabel('Temperature');
figure
plot(Tempreture,MeanAutocorr)
ylabel('Autocorrelation Length');
xlabel('Temperature');


