function [V_t]= LJEnergyFunc(pos)
global nPeriods
cutoff=3;
UnitLenght=15;
xpos=mod(pos(:,1:25),UnitLenght);
ypos=mod(pos(:,26:50),UnitLenght);
V_t=zeros(1,nPeriods+1);

for Time=1:nPeriods+1
    V_point=zeros(25,25); 
for j=1:25
    for i=1:25
        if j~=i 
           if abs (xpos(Time,i)-xpos(Time,j))<cutoff && abs(ypos(Time,i)-ypos(Time,j))<cutoff
                   r = sqrt((xpos(Time,i)-xpos(Time,j))^2+(ypos(Time,i)-ypos(Time,j))^2);
                       V_point(j,i) = 4*((1/r)^12-(1/r)^6);
           else
             if abs ((xpos(Time,i)+UnitLenght)-xpos(Time,j))<cutoff && abs((ypos(Time,i)+UnitLenght)-ypos(Time,j))<cutoff
                 r = sqrt(((xpos(Time,i)+UnitLenght)-xpos(Time,j))^2+((ypos(Time,i)+UnitLenght)-ypos(Time,j))^2);
                     V_point(j,i) = 4*((1/r)^12-(1/r)^6);
             else
               if abs ((xpos(Time,i)-UnitLenght)-xpos(Time,j))<cutoff && abs((ypos(Time,i)-UnitLenght)-ypos(Time,j))<cutoff
                   r = sqrt(((xpos(Time,i)-UnitLenght)-xpos(Time,j))^2+((ypos(Time,i)-UnitLenght)-ypos(Time,j))^2);
                       V_point(j,i) = 4*((1/r)^12-(1/r)^6);
               else
                 if abs (xpos(Time,i)-xpos(Time,j))<cutoff && abs((ypos(Time,i)+UnitLenght)-ypos(Time,j))<cutoff
                     r = sqrt((xpos(Time,i)-xpos(Time,j))^2+((ypos(Time,i)+UnitLenght)-ypos(Time,j))^2);
                         V_point(j,i) = 4*((1/r)^12-(1/r)^6);

                 else
                   if abs ((xpos(Time,i)+UnitLenght)-xpos(Time,j))<cutoff && abs(ypos(Time,i)-ypos(Time,j))<cutoff
                       r = sqrt(((xpos(Time,i)+UnitLenght)-xpos(Time,j))^2+(ypos(Time,i)-ypos(Time,j))^2);
                           V_point(j,i) = 4*((1/r)^12-(1/r)^6);
                   else
                    if abs ((xpos(Time,i)-UnitLenght)-xpos(Time,j))<cutoff && abs(ypos(Time,i)-ypos(Time,j))<cutoff
                       r = sqrt(((xpos(Time,i)-UnitLenght)-xpos(Time,j))^2+(ypos(Time,i)-ypos(Time,j))^2);
                           V_point(j,i) = 4*((1/r)^12-(1/r)^6);

                    else
                      if abs (xpos(Time,i)-xpos(Time,j))<cutoff && abs((ypos(Time,i)-UnitLenght)-ypos(Time,j))<cutoff
                          r = sqrt((xpos(Time,i)-xpos(Time,j))^2+((ypos(Time,i)-UnitLenght)-ypos(Time,j))^2);
                              V_point(j,i) = 4*((1/r)^12-(1/r)^6);
                      else
                        if abs ((xpos(Time,i)+UnitLenght)-xpos(Time,j))<cutoff && abs((ypos(Time,i)-UnitLenght)-ypos(Time,j))<cutoff
                             r = sqrt(((xpos(Time,i)+UnitLenght)-xpos(Time,j))^2+((ypos(Time,i)-UnitLenght)-ypos(Time,j))^2);
                                 V_point(j,i) = 4*((1/r)^12-(1/r)^6);
                        else
                         if abs ((xpos(Time,i)-UnitLenght)-xpos(Time,j))<cutoff && abs((ypos(Time,i)+UnitLenght)-ypos(Time,j))<cutoff
                              r = sqrt(((xpos(Time,i)-UnitLenght)-xpos(Time,j))^2+((ypos(Time,i)+UnitLenght)-ypos(Time,j))^2);
                                  V_point(j,i) = 4*((1/r)^12-(1/r)^6);
                         end
                        end
                      end
                    end
                   end
                 end
               end
             end
           end
            

        end
    end

end
 V_t(Time)=1/2*sum(sum(V_point),2);
end
 %ThermCapacity=(var(V_t))/temp^2;
 end