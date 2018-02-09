# Storage module for pgbackup tool
#
# (pgbackup-E7nj_BsO) [pgbackup $]
# (pgbackup-E7nj_BsO) [pgbackup $] vim src/pgbackup/storage.py

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()