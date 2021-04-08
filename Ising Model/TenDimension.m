% 10*10 matrix
energyrange=linspace(-200,200,13);
energyspan=zeros(1,12);
%generating random matrix
for ii=1:10^7
systemstate=zeros(10,10);
 for i=1:10
     for j=1:10      
 spinstate=[1 -1]; 
  systemstate(i,j)=spinstate(randi(numel(spinstate)));
  
     end
 end
 %energy of righthand interactions
 aa1=systemstate;
 bb1=systemstate(:,1);
 systemstate(:,1)=[];
 D1=cat(2,systemstate,bb1);
 f1=D1.*aa1;
 rightsum1=sum(f1);
 rightsum2=sum(rightsum1,2);
 
 %energy of lefthand interactions
 aa2=aa1;
 bb2=aa1(:,10);
 aa1(:,10)=[];
 D2=cat(2,bb2,aa1);
 f2=D2.*aa2;
 leftsum1=sum(f2);
 leftsum2=sum(leftsum1,2);
 
 %energy of upward interactions 
 aa3=aa2;
 bb3=aa2(10,:);
 aa2(10,:)=[];
 D3=cat(1,bb3,aa2);
 f3=D3.*aa3;
 upsum1=sum(f3);
 upsum2=sum(upsum1,2);
 
 %energy of underneath interactions
 aa4=aa3;
 bb4=aa3(1,:);
 aa3(1,:)=[];
 D4=cat(1,aa3,bb4);
 f4=D4.*aa4;
 downsum1=sum(f4);
 downsum2=sum(downsum1,2);
 
 %total energy
 E=-1/2*(rightsum2+leftsum2+upsum2+downsum2);
 
for i=1:12
    if E>energyrange(i)&& E<energyrange(i+1)
        energyspan(i)=energyspan(i)+1;
    end
end 
end
%calculation of system entropy 
boltzman.cons= physconst('Boltzmann');
entropy1=boltzman.cons*log(energyspan);

%set lower and upper bound to zero
entropy2=cat(2,0,entropy1);
entropy=cat(2,entropy2,0);

% calculation of energy span middels
normalizedenergyrange=energyrange+(energyrange(1,10)-energyrange(1,9))/2;

%set lower and upper bound to -200 and 200
normalizedenergyrange(13)=200;
energy=cat(2,-200,normalizedenergyrange);

plot(energy,entropy)
xlabel('Energy')
ylabel('Entropy')

%calculation of derivative(temperature)
T=zeros(1,13);

for i=1:13
   derivative=(entropy(i+1)-entropy(i))/(energy(i+1)-energy(i));
   T(i)=-1/derivative;
end

% calculation of entropy span middels
normalizedentropy=zeros(1,13);
for i=1:13
normalizedentropy1=entropy(i)+(entropy(i+1)-entropy(i))/2;
normalizedentropy(i)=normalizedentropy1;
end

figure
plot(T,normalizedentropy)
ylabel('Entropy')
xlabel('Temperature')

figure
plot (T)
ylabel('Temperature')

% calculation of thermal capacity

cv=zeros(1,12);
for i=1:12

thermalcapacity=(energy(i+1)-energy(i))/(T(i+1)-T(i)); 
cv(i)=thermalcapacity;
end
T(:,13)=[];
figure
plot(T,cv)
xlabel('Temperature')
ylabel('Thermal Capacity')

figure
plot(cv)
ylabel('Thermal Capacity')
