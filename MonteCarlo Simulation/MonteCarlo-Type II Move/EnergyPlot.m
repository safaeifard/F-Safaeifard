%generating random matrix

systemstate=zeros(20,20);
for i=1:20
     for j=1:20     
 spinstate=[1 -1]; 
 systemstate(i,j)=spinstate(randi(numel(spinstate)));
     end
end
%energy of righthand interactions
righthandcoss=systemstate.*circshift(systemstate,1,2);
rightcolumnsum =sum(righthandcoss);
righthandenergy=sum(rightcolumnsum,2);

leftthandcross=systemstate.*circshift(systemstate,19,2);
lefttcolumnsum =sum(righthandcoss);
leftthandenergy=sum(lefttcolumnsum,2);

upwardcross=systemstate.*circshift(systemstate,1,1);
upcolumnsum =sum(upwardcross);
upwardenergy=sum(upcolumnsum,2);

downwardcross=systemstate.*circshift(systemstate,19,1);
downcolumnsum =sum(downwardcross);
downwardenergy=sum(downcolumnsum,2);
 %total energy
 E=-1/2*(righthandenergy+leftthandenergy+upwardenergy+downwardenergy);
 s0=systemstate;
 msize = numel(systemstate);
 energyvector=zeros(1,500);

s0=systemstate;
%finalenergyvector=zeros(1,(500000-500*counter)/(50*counter));
finalenergyvector=[];
%megnetizationvector=zeros(1,(500000-500*counter)/(50*counter));
for i=1:500000
idx = randperm(msize);
Stest=s0;

Stest(idx(1))=-Stest(idx(1));
Stest(idx(2))=-Stest(idx(2));


rhctest=Stest.*circshift(Stest,1,2);
rcolsumtest =sum(rhctest);
rhetest=sum(rcolsumtest,2);

lhctest=Stest.*circshift(Stest,19,2);
lcolsumtest =sum(lhctest);
lhetest=sum(lcolsumtest,2);

uhctest=Stest.*circshift(Stest,1,1);
upcolsumtest =sum(uhctest);
uhetest=sum(upcolsumtest,2);

dhctest=Stest.*circshift(Stest,19,1);
downcolsumtest =sum(dhctest);
dhetest=sum(downcolsumtest,2);

%total testenergy
 Etest=-1/2*(rhetest+lhetest+uhetest+dhetest);
 deltaE=Etest-E;
 
 P=min(1,exp(-deltaE/T));
 r=rand;
   if P>=r
     s0=Stest;
     E=Etest;
  end
   
      finalenergyvector=[finalenergyvector E];
     
     
    end



    
