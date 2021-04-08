function Force=BrwDynFunction(t,xycoord)
cutoff=3;
UnitLenght=15;
    
 xcoord=mod(xycoord(1:25),UnitLenght);
 ycoord=mod(xycoord(26:50),UnitLenght); 
%  xcoord=xycoord(1:25);
%  ycoord=xycoord(26:50);
F_x=zeros(25,25);
F_y=zeros(25,25);
for j=1:25
    for i=1:25
        if j~=i
           if abs (xcoord(i)-xcoord(j))<cutoff && abs(ycoord(i)-ycoord(j))<cutoff
                   r = sqrt((xcoord(i)-xcoord(j))^2+(ycoord(i)-ycoord(j))^2);
             F_x(j,i) = (-12/r^13)*((xcoord(i)-xcoord(j))/r) - (-6/r^7)* ((xcoord(i)-xcoord(j))/r);
             F_y(j,i) = (-12/r^13)*((ycoord(i)-ycoord(j))/r) - (-6/r^7)* ((ycoord(i)-ycoord(j))/r);
           else
             if abs ((xcoord(i)+UnitLenght)-xcoord(j))<cutoff && abs((ycoord(i)+UnitLenght)-ycoord(j))<cutoff
                 r = sqrt(((xcoord(i)+UnitLenght)-xcoord(j))^2+((ycoord(i)+UnitLenght)-ycoord(j))^2);
               F_x(j,i) = (-12/r^13)*(((xcoord(i)+UnitLenght)-xcoord(j))/r) - (-6/r^7)* (((xcoord(i)+UnitLenght)-xcoord(j))/r);
               F_y(j,i) = (-12/r^13)*(((ycoord(i)+UnitLenght)-ycoord(j))/r) - (-6/r^7)* (((ycoord(i)+UnitLenght)-ycoord(j))/r);
             else
               if abs ((xcoord(i)-UnitLenght)-xcoord(j))<cutoff && abs((ycoord(i)-UnitLenght)-ycoord(j))<cutoff
                   r = sqrt(((xcoord(i)-UnitLenght)-xcoord(j))^2+((ycoord(i)-UnitLenght)-ycoord(j))^2);
                 F_x(j,i) = (-12/r^13)*(((xcoord(i)-UnitLenght)-xcoord(j))/r) - (-6/r^7)* (((xcoord(i)-UnitLenght)-xcoord(j))/r);
                 F_y(j,i) = (-12/r^13)*(((ycoord(i)-UnitLenght)-ycoord(j))/r) - (-6/r^7)* (((ycoord(i)-UnitLenght)-ycoord(j))/r);
               else
                 if abs (xcoord(i)-xcoord(j))<cutoff && abs((ycoord(i)+UnitLenght)-ycoord(j))<cutoff
                     r = sqrt((xcoord(i)-xcoord(j))^2+((ycoord(i)+UnitLenght)-ycoord(j))^2);
                   F_x(j,i) = (-12/r^13)*((xcoord(i)-xcoord(j))/r) - (-6/r^7)* ((xcoord(i)-xcoord(j))/r);
                   F_y(j,i) = (-12/r^13)*(((ycoord(i)+UnitLenght)-ycoord(j))/r) - (-6/r^7)* (((ycoord(i)+UnitLenght)-ycoord(j))/r);
                 else
                   if abs ((xcoord(i)+UnitLenght)-xcoord(j))<cutoff && abs(ycoord(i)-ycoord(j))<cutoff
                       r = sqrt(((xcoord(i)+UnitLenght)-xcoord(j))^2+(ycoord(i)-ycoord(j))^2);
                     F_x(j,i) = (-12/r^13)*(((xcoord(i)+UnitLenght)-xcoord(j))/r) - (-6/r^7)* (((xcoord(i)+UnitLenght)-xcoord(j))/r);
                     F_y(j,i) = (-12/r^13)*((ycoord(i)-ycoord(j))/r) - (-6/r^7)* ((ycoord(i)-ycoord(j))/r);
                   else
                    if abs ((xcoord(i)-UnitLenght)-xcoord(j))<cutoff && abs(ycoord(i)-ycoord(j))<cutoff
                       r = sqrt((xcoord(i)-UnitLenght)-xcoord(j))^2+((ycoord(i)-ycoord(j))^2);
                      F_x(j,i) = (-12/r^13)*(((xcoord(i)-UnitLenght)-xcoord(j))/r) - (-6/r^7)* (((xcoord(i)-UnitLenght)-xcoord(j))/r);
                      F_y(j,i) = (-12/r^13)*((ycoord(i)-ycoord(j))/r) - (-6/r^7)* ((ycoord(i)-ycoord(j))/r);
                    else
                      if abs (xcoord(i)-xcoord(j))<cutoff && abs((ycoord(i)-UnitLenght)-ycoord(j))<cutoff
                          r = sqrt((xcoord(i)-xcoord(j))^2+((ycoord(i)-UnitLenght)-ycoord(j))^2);
                         F_x(j,i) = (-12/r^13)*((xcoord(i)-xcoord(j))/r) - (-6/r^7)* ((xcoord(i)-xcoord(j))/r);
                         F_y(j,i) = (-12/r^13)*(((ycoord(i)-UnitLenght)-ycoord(j))/r) - (-6/r^7)* (((ycoord(i)-UnitLenght)-ycoord(j))/r);
                      else
                        if abs ((xcoord(i)+UnitLenght)-xcoord(j))<cutoff && abs((ycoord(i)-UnitLenght)-ycoord(j))<cutoff
                             r = sqrt(((xcoord(i)+UnitLenght)-xcoord(j))^2+((ycoord(i)-UnitLenght)-ycoord(j))^2);
                          F_x(j,i) = (-12/r^13)*(((xcoord(i)+UnitLenght)-xcoord(j))/r) - (-6/(r^7))* (((xcoord(i)+UnitLenght)-xcoord(j))/r);
                          F_y(j,i) = (-12/r^13)*(((ycoord(i)-UnitLenght)-ycoord(j))/r) - (-6/(r^7))* (((ycoord(i)-UnitLenght)-ycoord(j))/r);
                        else
                         if abs ((xcoord(i)-UnitLenght)-xcoord(j))<cutoff && abs((ycoord(i)+UnitLenght)-ycoord(j))<cutoff
                              r = sqrt(((xcoord(i)-UnitLenght)-xcoord(j))^2+((ycoord(i)+UnitLenght)-ycoord(j))^2);
                           F_x(j,i) = (-12/r^13)*(((xcoord(i)-UnitLenght)-xcoord(j))/r) - (-6/r^7)* (((xcoord(i)-UnitLenght)-xcoord(j))/r);
                           F_y(j,i) = (-12/r^13)*(((ycoord(i)+UnitLenght)-ycoord(j))/r) - (-6/r^7)* (((ycoord(i)+UnitLenght)-ycoord(j))/r);
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
    
  F_x_net=sum(F_x,2);
  F_y_net=sum(F_y,2);
  Force =[F_x_net; F_y_net];
end