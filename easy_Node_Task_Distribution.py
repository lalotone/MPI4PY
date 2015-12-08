import os
from mpi4py import MPI#Import mpi4py

comm=MPI.COMM_WORLD

rank = comm.rank

def proof():
    message = "Hi there, black"
    return message
if rank==2:#Node number two? Execute this part.
    command = os.system("hostname")
    key = proof()
    print key
    print ("Function counter running on device", command)
if rank==3:#Node number three? Execute this part.
    sum = 2 + 3
    print sum

