from numpy.random import rand
from numpy import arange, ones, zeros, sqrt
from PyGran import Analyzer
import collections

data = collections.OrderedDict()
natoms = 10
radius = 25.0

data['natoms'] = natoms * natoms * natoms
data['id'] = arange(data['natoms'])

data['x'], data['y'], data['z'] = zeros(data['natoms']), zeros(data['natoms']), zeros(data['natoms'])

data['id'] = arange(data['natoms'])
count = 0
for i in range(natoms):
	for j in range(natoms):
		for k in range(natoms):
			data['x'][count] = (2.0 * i + ((j + k) % 2)) * radius
			data['y'][count] = (sqrt(3.) * (j + 1.0/3.0 * (k % 2))) * radius
			data['z'][count] = (2.0 * sqrt(6.0) / 3.0 * k) * radius
			count += 1

data['radius'] = ones(data['natoms']) * radius
data['timestep'] = 0
data['box'] = ([-0.001, 0.001], [-0.001, 0.001], [0.0, 0.004])

system = Analyzer.System()
system.data = data
system.write('traj.dump')