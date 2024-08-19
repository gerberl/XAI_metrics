"""


* created on: 19-Aug-24
* last updated on: 19-Aug-24

"""



def monotonicity(u, v):
    """
    a function for monotonicity (Huw's proposal)
    see https://thescipub.com/pdf/jmssp.2012.221.228.pdf
    this is the absolute value of their 'rm' (sample version of the measure)
    we ignore the sign since we don't care about the sense of the correlation

    

    """
    # rescale to 0,1
    u = (u - np.min(u))/(np.max(u)-np.min(u))
    v = (v - np.min(v))/(np.max(v)-np.min(v))
    # sort
    up = np.sort(u)
    vp = np.sort(v)
    cov = np.sum((u-np.mean(u))*(v-np.mean(v)))/(u.shape[0]-1)
    if cov == 0.0:
        return 0.0
    elif cov < 0.0:
        vp = np.flip(vp)
    covp = np.sum((up-np.mean(up))*(vp-np.mean(vp)))/(up.shape[0]-1)
    return cov/covp