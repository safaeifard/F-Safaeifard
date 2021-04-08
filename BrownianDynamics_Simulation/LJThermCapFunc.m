function [ThermCapacity]= LJThermCapFunc(equilibrium_pos,Temp)
global nPeriods
cutoff=3;
UnitLenght=15;
xpos=equilibrium_pos(:,1:25);
ypos=equilibrium_pos(:,26:50);
V_t=[];
for Time=1:(nPeriods+1-49000)

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
 V_t=[V_t 1/2*sum(sum(V_point),2)];
end
 ThermCapacity=(var(V_t))/Temp^2;
 end