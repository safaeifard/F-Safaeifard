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
from pydream.convergence import Gelman_Rubin
from scipy.stats import norm
import inspect
import os.path
import cobra

#from corm import model as cox2_model

pydream_path = os.path.dirname(inspect.getfile(run_dream))


model = cobra.io.read_sbml_model('/home/fateme/Desktop/Proposal/Toy_Model')
model.metabolites[:3]
model.optimize()


#Create scipy normal probability distributions for data likelihoods
like_Obj = norm(loc=, scale=)


#Create lists of sampled pysb parameter names to use for subbing in parameter values in likelihood function and for setting all kfs to diffusion limited value.
pysb_sampled_parameter_names = ['kcat1', 'kcat2', 'kcat3','kcat4','kcat5','kcat6','kcat7','kcat8','kcat9','kcat10','kcat11','kcat12','kcat13','kcat14','kcat15','kcat16','kcat17','kcat18']


# Add PySB rate parameters to be sampled as unobserved random variables to DREAM with normal priors.


Kcat_dist=numpy.zero(18)

    for i in range (17):    #constraints definition
        Kcat_dist[i] = SampledParam(norm, loc=np.log10([Kcat[i]]), scale=.66)
        


#sampled_parameter_names = [kcat1, kcat2, kcat3,kcat4,kcat5,kcat6,kcat7,kcat8,kcat9,kcat10,kcat11,kcat12,kcat13,kcat14,kcat15,kcat16,kcat17,kcat18]

# DREAM should be run with at least 3 chains.
# Set these options so script can be called with command line arguments (needed for tests)
nchains = 5

niterations = 10000



# Define likelihood function to generate simulated data that corresponds to experimental time points.
# This function should take as input a parameter vector (parameter values are in the order dictated by first argument to run_dream function below).
# The function returns a log probability value for the parameter vector given the experimental data.

def likelihood(parameter_vector):

    param_dict = {pname: pvalue for pname, pvalue in zip(pysb_sampled_parameter_names, parameter_vector)}

    for pname, pvalue in list(param_dict.items()):

        # Change model parameter values to current location in parameter space

        if 'kr' in pname:
            model.parameters[pname].value = 10 ** (pvalue + generic_kf)

        elif 'kcat' in pname:
            model.parameters[pname].value = 10 ** pvalue

    # Simulate experimentally measured PG and PGG values at all experimental AA and 2-AG starting conditions.

    Obj_array = np.zeros((7, 7), dtype='float64')


    arr_row = 0
    arr_col = 0

    for AA_init in exp_cond_AA:
        for AG_init in exp_cond_AA:
            model.parameters['AA_0'].value = AA_init
            model.parameters['AG_0'].value = AG_init
            
            #solver.run()
            model.optimize()
            Obj_array[arr_row, arr_col] = solver.yobs['obsobj'][-1]
           
            if arr_col < 6:
                arr_col += 1
            else:
                arr_col = 0
        arr_row += 1

    # Calculate log probability contribution from simulated PG and PGG values.

    logp_Obj = np.sum(like_Obj.logpdf(Obj_array))
    

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

    logp_box1 = like_thermobox.logpdf(box1)
    logp_box2 = like_thermobox.logpdf(box2)
    logp_box3 = like_thermobox.logpdf(box3)
    logp_box4 = like_thermobox.logpdf(box4)

    total_logp = logp_Obj + logp_box1 + logp_box2 + logp_box3 + logp_box4

    # If model simulation failed due to integrator errors, return a log probability of -inf.
    if np.isnan(total_logp):
        total_logp = -np.inf

    return total_logp


if __name__ == '__main__':

    # Run DREAM sampling.  Documentation of DREAM options is in Dream.py.
    converged = False
    total_iterations = niterations
    sampled_params, log_ps = run_dream(parameters=sampled_parameter_names, likelihood=likelihood, niterations=niterations, nchains=nchains, multitry=False, gamma_levels=4, adapt_gamma=True, history_thin=1, model_name='CBM_dreamzs_5chain', verbose=True)

    # Save sampling output (sampled parameter values and their corresponding logps).
    for chain in range(len(sampled_params)):
        np.save('CBM_dreamzs_5chain_sampled_params_chain_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
        np.save('CBM_dreamzs_5chain_logps_chain_' + str(chain)+'_'+str(total_iterations), log_ps[chain])

    #Check convergence and continue sampling if not converged

    GR = Gelman_Rubin(sampled_params)
    print('At iteration: ',total_iterations,' GR = ',GR)
    np.savetxt('CBM_dreamzs_5chain_GelmanRubin_iteration_'+str(total_iterations)+'.txt', GR)

    old_samples = sampled_params
    if np.any(GR>1.2):
        starts = [sampled_params[chain][-1, :] for chain in range(nchains)]
        while not converged:
            total_iterations += niterations
            sampled_params, log_ps = run_dream(parameters=sampled_parameter_names, likelihood=likelihood,
                                               niterations=niterations, nchains=nchains, start=starts, multitry=False, gamma_levels=4,
                                               adapt_gamma=True, history_thin=1, model_name='CBM_dreamzs_5chain',
                                               verbose=True, restart=True)


            # Save sampling output (sampled parameter values and their corresponding logps).
            for chain in range(len(sampled_params)):
                np.save('CBM_dreamzs_5chain_sampled_params_chain_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
                np.save('CBM_dreamzs_5chain_logps_chain_' + str(chain)+'_'+str(total_iterations), log_ps[chain])

            old_samples = [np.concatenate((old_samples[chain], sampled_params[chain])) for chain in range(nchains)]
            GR = Gelman_Rubin(old_samples)
            print('At iteration: ',total_iterations,' GR = ',GR)
            np.savetxt('CBM_dreamzs_5chain_GelmanRubin_iteration_' + str(total_iterations)+'.txt', GR)

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
            fig.savefig('PyDREAM_example_CBM_dimension_'+str(dim))

    except ImportError:
        pass

else:

    run_kwargs = {'parameters':sampled_parameter_names, 'likelihood':likelihood, 'niterations':niterations, 'nchains':nchains, \
                  'multitry':False, 'gamma_levels':4, 'adapt_gamma':True, 'history_thin':1, 'model_name'CBM_dreamzs_5chain', 'verbose':False}