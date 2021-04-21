#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 15:26:46 2014
@author: Erin
"""

from pydream.core import run_dream
from pysb.integrate import Solver
import numpy as np
from pydream.parameters import SampledParam
from pydream.parameter import parameter
from pydream.convergence import Gelman_Rubin
from scipy.stats import norm
import inspect
import os.path
import cobra


# from massaction import model as KineticModel

pydream_path = os.path.dirname(inspect.getfile(run_dream))

#Initialize PySB solver object for running simulations.  Simulation timespan should match experimental data.
# tspan = np.linspace(0,10, num=100)
# solver = Solver(cox2_model, tspan)
# solver.run()
model = cobra.io.read_sbml_model('/home/fateme/Desktop/Toy/Toy_Model')
model.metabolites[:3]
model.optimize()



setattr(model, parameter)


#Load experimental data to which Toy model will be fit here
location= pydream_path+'/Toy/exp_data/'
exp_data_PG = np.loadtxt(location+'exp_data_pg.txt')
#exp_data_PGG = np.loadtxt(location+'exp_data_pgg.txt')

exp_data_sd_PG = np.loadtxt(location+'exp_data_sd_pg.txt')
#exp_data_sd_PGG = np.loadtxt(location+'exp_data_sd_pgg.txt')



# #generic kf in units of inverse microM*s (matches model units).  All kf reactions are assumed to be diffusion limited.
# generic_kf = np.log10(1.5e4)

#Create scipy normal probability distributions for data likelihoods
like_Obj = norm(loc=exp_data_PG, scale=exp_data_sd_PG)
#like_thermobox = norm(loc=1, scale=1e-2)
kcat1=1000
kcat2=830
kcat3=1.3
kcat4=1.0e-3
kcat5=3.3e-6
kcat6=2.3
kcat7=1.0e-3
kcat8=8.3e-6
kcat9=1.3
kcat10=1000
kcat11=760
kcat12=1.2
kcat13=1.0e-3
kcat14=4.8e-4
kcat15=1.0e-3
kcat16=1.9e-6
kcat17=0.21
kcat18=0.21




#Create lists of sampled pysb parameter names to use for subbing in parameter values in likelihood function and for setting all kfs to diffusion limited value.
pysb_sampled_parameter_names = ['kcat1', 'kcat2', 'kcat3','kcat4','kcat5','kcat6','kcat7','kcat8','kcat9','kcat10','kcat11','kcat12','kcat13','kcat14','kcat15','kcat16','kcat17','kcat18']
#kf_idxs = [i for i, param in enumerate(model.parameters) if param.name in kfs_to_change]

param_dict= {'kcat1': 2, 'kcat2' : 18, 'kcat3': 10,'kcat4': 16,'kcat5':18 ,'kcat6': 18,'kcat7':19,'kcat8':12,'kcat9':13,'kcat10':13,'kcat11':13,'kcat12':12,'kcat13':11,'kcat14':12,'kcat15':12,'kcat16':11,'kcat17':12,'kcat18':12}

for param in param_dict.values() :     #shoud be assigned to reactions   dict besaz
     constraint = model.problem.Constraint(0, lb=0, ub=param*50 )
     model.add_cons_vars(constraint)
# pysb_sampled_parameter_names.__setattr__(name, value) 
# Add PySB rate parameters to be sampled as unobserved random variables to DREAM with normal priors.


# Kcat1 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat1'].value), scale=.66)
# Kcat2 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat2'].value), scale=.66)
# Kcat3 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat3'].value), scale=.66)
# Kcat4 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat4'].value), scale=.66)
# Kcat5 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat5'].value), scale=.66)
# Kcat6 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat6'].value), scale=.66)
# Kcat7 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat7'].value), scale=.66)
# Kcat8 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat8'].value), scale=.66)
# Kcat9 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat9'].value), scale=.66)
# Kcat10 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat10'].value), scale=.66)
# Kcat11 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat11'].value), scale=.66)
# Kcat12 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat12'].value), scale=.66)
# Kcat13 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat13'].value), scale=.66)
# Kcat14 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat14'].value), scale=.66)
# Kcat15 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat15'].value), scale=.66)
# Kcat16 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat16'].value), scale=.66)
# Kcat17 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat17'].value), scale=.66)
# Kcat18 = SampledParam(norm, loc=np.log10(KineticModel.parameters['kcat18'].value), scale=.66)

Kcat1 = SampledParam(norm, loc=np.log10(model.parameter['kcat1'].value), scale=.66)
Kcat2 = SampledParam(norm, loc=np.log10( model.parameter['kcat2'].value ), scale=.66)
Kcat3 = SampledParam(norm, loc=np.log10(model.parameter[' kcat3 '].value ), scale=.66)
Kcat4 = SampledParam(norm, loc=np.log10( model.parameter['kcat4 '].value ), scale=.66)
Kcat5 = SampledParam(norm, loc=np.log10( model.parameter['kcat5 '].value ), scale=.66)
Kcat6 = SampledParam(norm, loc=np.log10( model.parameter['kcat6 '].value ), scale=.66)
Kcat7 = SampledParam(norm, loc=np.log10( model.parameter['kcat7 '].value ), scale=.66)
Kcat8 = SampledParam(norm, loc=np.log10( model.parameter['kcat8 '].value ), scale=.66)
Kcat9 = SampledParam(norm, loc=np.log10( model.parameter['kcat9 '].value ), scale=.66)
Kcat10 = SampledParam(norm, loc=np.log10( model.parameter['kcat10 '].value ), scale=.66)
Kcat11 = SampledParam(norm, loc=np.log10( model.parameter['kcat11 '].value ), scale=.66)
Kcat12 = SampledParam(norm, loc=np.log10( model.parameter['kcat12 '].value ), scale=.66)
Kcat13 = SampledParam(norm, loc=np.log10( model.parameter['kcat13 '].value ), scale=.66)
Kcat14 = SampledParam(norm, loc=np.log10( model.parameter['kcat14 '].value ), scale=.66)
Kcat15 = SampledParam(norm, loc=np.log10( model.parameter['kcat15 '].value ), scale=.66)
Kcat16 = SampledParam(norm, loc=np.log10( model.parameter['kcat16 '].value ), scale=.66)
Kcat17 = SampledParam(norm, loc=np.log10( model.parameter['kcat17 '].value ), scale=.66)
Kcat18 = SampledParam(norm, loc=np.log10( model.parameter['kcat18 '].value ), scale=.66)


sampled_parameter_names = [kcat1, kcat2, kcat3, kcat4, kcat5, kcat6, kcat7, kcat8, kcat9, kcat10, kcat11, kcat12, kcat13, kcat14, kcat15, kcat16, kcat17, kcat18]

# DREAM should be run with at least 3 chains.
# Set these options so script can be called with command line arguments (needed for tests)


nchains = 5

niterations = 10000

# Change model kf values to be assumed diffusion-limited value.
# for idx in kf_idxs:
    # model.parameters[idx].value = 10 ** generic_kf

# Define likelihood function to generate simulated data that corresponds to experimental time points.
# This function should take as input a parameter vector (parameter values are in the order dictated by first argument to run_dream function below).
# The function returns a log probability value for the parameter vector given the experimental data.
# C=zeros[18]
def likelihood(parameter_vector):

    param_dict = {pname: pvalue for pname, pvalue in zip(pysb_sampled_parameter_names, parameter_vector)}

    for pname, pvalue in list(param_dict.items()):

        # Change model parameter values to current location in parameter space

        # if 'kr' in pname:
        #     model.parameters[pname].value = 10 ** (pvalue + generic_kf)

        # elif 'kcat' in pname:
            #KineticModel.parameters[pname].value = 10 ** pvalue
           # for i in range 17: 
           #     if i= 
           #  C[i] =10**pvalue
           #  i=i+1
           itr=iter(param_dict.item())
           next(itr)
           pvalue= 10**pvalue

    # Simulate experimentally measured PG and PGG values at all experimental AA and 2-AG starting conditions.

    Obj_array = np.zeros((7, 7), dtype='float64')
    # PGG_array = np.zeros((7, 7), dtype='float64')

    arr_row = 0
    arr_col = 0

    # for AA_init in exp_cond_AA:
    #     for AG_init in exp_cond_AA:
    #         model.parameters['AA_0'].value = AA_init
    #         model.parameters['AG_0'].value = AG_init
            
            #solver.run()
           
    Obj_array[arr_row, arr_col] = model.optimize().objective_value 
            # PGG_array[arr_row, arr_col] = solver.yobs['obsPGG'][-1]
    if arr_col < 6:
                arr_col += 1
    else:
                arr_col = 0
    arr_row += 1

    # Calculate log probability contribution from simulated PG and PGG values.

    logp_Obj = np.sum(like_Obj.logpdf(Obj_array))
   # logp_PGG = np.sum(like_PGGs.logpdf(PGG_array))

    # Calculate conservation for thermodynamic boxes in enyzme-substrate interaction diagram.

    # box1 = (1 / (10 ** KD_AA_cat1)) * (1 / (10 ** param_dict['kr_AA_allo2'])) * (10 ** param_dict['kr_AA_cat3']) * (
    # 10 ** param_dict['kr_AA_allo1'])
    # box2 = (1 / (10 ** param_dict['kr_AA_allo1'])) * (1 / (10 ** param_dict['kr_AG_cat3'])) * (
    # 10 ** param_dict['kr_AA_allo3']) * (10 ** KD_AG_cat1)
    # box3 = (1 / (10 ** param_dict['kr_AG_allo1'])) * (1 / (10 ** param_dict['kr_AA_cat2'])) * (
    # 10 ** param_dict['kr_AG_allo2']) * (10 ** KD_AA_cat1)
    # box4 = (1 / (10 ** KD_AG_cat1)) * (1 / (10 ** KD_AG_allo3)) * (10 ** param_dict['kr_AG_cat2']) * (
    # 10 ** param_dict['kr_AG_allo1'])

    # Calculate log probability contribution from thermodynamic box energy conservation.

    # logp_box1 = like_thermobox.logpdf(box1)
    # logp_box2 = like_thermobox.logpdf(box2)
    # logp_box3 = like_thermobox.logpdf(box3)
    # logp_box4 = like_thermobox.logpdf(box4)

    total_logp = logp_Obj
    # + logp_box1 + logp_box2 + logp_box3 + logp_box4

    # If model simulation failed due to integrator errors, return a log probability of -inf.
    if np.isnan(total_logp):
        total_logp = -np.inf

    return total_logp


if __name__ == '__main__':

    # Run DREAM sampling.  Documentation of DREAM options is in Dream.py.
    converged = False
    total_iterations = niterations
    sampled_params, log_ps = run_dream(parameters=sampled_parameter_names, likelihood=likelihood, niterations=niterations, nchains=nchains, multitry=False, gamma_levels=4, adapt_gamma=True, history_thin=1, model_name='Toy_dreamzs_5chain', verbose=True)

    # Save sampling output (sampled parameter values and their corresponding logps).
    for chain in range(len(sampled_params)):
        np.save('Toy_dreamzs_5chain_sampled_params_chain_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
        np.save('Toy_dreamzs_5chain_logps_chain_' + str(chain)+'_'+str(total_iterations), log_ps[chain])

    #Check convergence and continue sampling if not converged

    GR = Gelman_Rubin(sampled_params)
    print('At iteration: ',total_iterations,' GR = ',GR)
    np.savetxt('Toy_dreamzs_5chain_GelmanRubin_iteration_'+str(total_iterations)+'.txt', GR)

    old_samples = sampled_params
    if np.any(GR>1.2):
        starts = [sampled_params[chain][-1, :] for chain in range(nchains)]
        while not converged:
            total_iterations += niterations
            sampled_params, log_ps = run_dream(parameters=sampled_parameter_names, likelihood=likelihood,
                                               niterations=niterations, nchains=nchains, start=starts, multitry=False, gamma_levels=4,
                                               adapt_gamma=True, history_thin=1, model_name='Toy_dreamzs_5chain',
                                               verbose=True, restart=True)


            # Save sampling output (sampled parameter values and their corresponding logps).
            for chain in range(len(sampled_params)):
                np.save('Toy_dreamzs_5chain_sampled_params_chain_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
                np.save('Toy_dreamzs_5chain_logps_chain_' + str(chain)+'_'+str(total_iterations), log_ps[chain])

            old_samples = [np.concatenate((old_samples[chain], sampled_params[chain])) for chain in range(nchains)]
            GR = Gelman_Rubin(old_samples)
            print('At iteration: ',total_iterations,' GR = ',GR)
            np.savetxt('Toy_dreamzs_5chain_GelmanRubin_iteration_' + str(total_iterations)+'.txt', GR)

            if np.all(GR<1.2):
                converged = True

    try:
        #Plot output
        import seaborn as sns
        from matplotlib import pyplot as plt
        total_iterations = len(old_samples[0])
        burnin = total_iterations/2
        samples = np.concatenate((old_samples[0][burnin:, :], old_samples[1][burnin:, :], old_samples[2][burnin:, :], old_samples[3][burnin:, :], old_samples[4][burnin:, :]))

        ndims = len(sampled_parameter_names)
        colors = sns.color_palette(n_colors=ndims)
        for dim in range(ndims):
            fig = plt.figure()
            sns.distplot(samples[:, dim], color=colors[dim], norm_hist=True)
            fig.savefig('PyDREAM_example_Toy_dimension_'+str(dim))

    except ImportError:
        pass

else:

    run_kwargs = {'parameters':sampled_parameter_names, 'likelihood':likelihood, 'niterations':niterations, 'nchains':nchains, \
                  'multitry':False, 'gamma_levels':4, 'adapt_gamma':True, 'history_thin':1, 'model_name':'Toy_dreamzs_5chain', 'verbose':False}
