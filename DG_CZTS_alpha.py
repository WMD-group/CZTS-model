def main():
    from materials import CZTS, Cu, Zn, Sn, alpha_S
    import numpy as np

    from DG_CZTS_S8 import plot_potential

    T = np.linspace(100,1000,100)    # K
    P = np.array( np.logspace(1,7,100),ndmin=2).transpose() # Pa
    
    D_mu = CZTS.mu_kJ(T,P) - (2*Cu.mu_kJ(T,P) +
                                    Zn.mu_kJ(T,P) +
                                    Sn.mu_kJ(T,P) +
                                    4*alpha_S.mu_kJ(T,P)
        )
    
    D_mu_label = '$\Delta G_f$ / kJ mol$^{-1}$'
    scale_range = [-370,-330]
    
    plot_potential(T,P,D_mu,D_mu_label,scale_range)

if __name__ == "__main__":
    main()
