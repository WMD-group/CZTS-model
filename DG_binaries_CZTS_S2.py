def main():
    from materials import CZTS, Cu2S_low, ZnS_zincblende, SnS2
    import numpy as np

    from DG_CZTS_S8 import plot_potential

    T = np.linspace(100,1000,100)    # K
    P = np.array( np.logspace(1,7,100),ndmin=2).transpose() # Pa
    
    D_mu = CZTS.mu_kJ(T,P) - (Cu2S_low.mu_kJ(T,P) +
                              ZnS_zincblende.mu_kJ(T,P) +
                              SnS2.mu_kJ(T,P)
                                      )
    
    D_mu_label = '$\Delta G_f$ / kJ mol$^{-1}$'
    scale_range = [-50,-40]
    
    plot_potential(T,P,D_mu,D_mu_label,scale_range)

if __name__ == "__main__":
    main()
