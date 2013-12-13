from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend

def plot (name, t, n, avocado):

    avocado_speedup = []

    for a in avocado:
        
        avocado_speedup.append (avocado [0] / a)

    exp_n = [n [0], n [-1]]
      
    loglog (n, avocado_speedup, 'bx-', basex=2, basey=2)
    loglog (exp_n, exp_n, 'b--', basex=2, basey=2)
    ylabel ("Speedup")
    xlabel ("Number of Machines")
    title (t)
    grid (True)
    savefig (name)

n = [1, 2, 4, 8]

#avocado = [276.0 / , 180, 31, 17]
avocado = [276.0, 180.0, 31.0, 17.0]

plot ("speedup_na12878_chr11.pdf",
      "Speedup on NA12878, Chromosome 11",
      n, avocado)
