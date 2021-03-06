"""
This example shows how to read and write variable-length string datatypes to a
dataset.  The program first writes strings to a dataset with a dataspace of
DIM0, then closes the file.  Next, it reopens the file, reads back the data,
and outputs it to the screen.
"""
import numpy as np
import h5py

FILE = "h5ex_t_vlstring.h5"
DATASET = "DS1"

DIM0 = 4

def run():

    # Must use the special variable-length string dtype.
    dtype = h5py.special_dtype(vlen=str)
    wdata = ['Parting', 'is such', 'sweet', 'sorrow']

    with h5py.File(FILE, 'w') as f:
        dset = f.create_dataset(DATASET, (DIM0,), dtype=dtype)
        dset[...] = wdata


    with h5py.File(FILE) as f:
        dset = f[DATASET]
        rdata = dset[...]

    print("%s:" % DATASET)
    print(rdata)


if __name__ == "__main__":
    run()        
   

