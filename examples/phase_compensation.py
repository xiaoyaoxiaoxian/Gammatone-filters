import matplotlib.pyplot as plt
import numpy as np
import sys
import os
sys.path.append('..\\')
from gtf import gtf

fig_dir = '../images/phase_compensation/'
if not os.path.exists(fig_dir):
    os.makedirs(fig_dir)

def savefig(fig,fig_name):
    fig_fpath = os.path.join(fig_dir,fig_name)
    fig.savefig(fig_fpath)


def phase_compensation_plot(irs,fs):
    t = np.arange(irs.shape[1])/fs*1e3
    fig = plt.figure()
    ha = fig.subplots(1,1)
    ha.plot(t,np.flipud(irs).T,linewidth=3) # plot high-cf filter ir first
    ha.set_xlabel('time(ms)')
    return fig


def phase_compensation_test():
    """"""
    fs = 16e3
    gtf_filter = gtf(fs=fs,freq_low=80,freq_high=1e3,n_band=4)

    ir_len = np.int16(50e-3*fs)

    irs = gtf_filter.get_ir()
    fig = phase_compensation_plot(irs[:,:ir_len],fs)
    savefig(fig,'irs.png')

    irs_env_aligned = gtf_filter.get_ir(is_env_aligned=True)
    fig = phase_compensation_plot(irs_env_aligned[:,:ir_len],fs)
    savefig(fig,'irs_env_aligned.png')

    irs_all_aligned = gtf_filter.get_ir(is_env_aligned=True,
                                        is_fine_aligned=True)
    fig = phase_compensation_plot(irs_all_aligned[:,:ir_len],fs)
    savefig(fig,'irs_all_aligned.png')


if __name__ == "__main__":
    phase_compensation_test()