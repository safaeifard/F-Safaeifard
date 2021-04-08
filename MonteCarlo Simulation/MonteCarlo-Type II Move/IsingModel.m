
MeanMagnetization = [];
Thermalcapacity = [];
spatialcorrelationlength=[];
temperature=[2:0.05:3];

% MonteCarlo loop
for T=2:0.05:3
[Ms, Es, CLs] = MonteCarloFunc(T);
% Record the results
MeanMagnetization = [MeanMagnetization mean(Ms)/(20^2)];
Thermalcapacity = [Thermalcapacity var(Es)/T^2];
spatialcorrelationlength=[spatialcorrelationlength mean(CLs)];

end

plot(temperature,MeanMagnetization)
ylabel('Magnetization');
xlabel('temperature^-1');

figure
plot(temperature,Thermalcapacity)
ylabel('Thermalcapacity');
xlabel('temperature');

figure
plot(temperature,spatialcorrelationlength)
ylabel('correlation length');
xlabel('temperature');

