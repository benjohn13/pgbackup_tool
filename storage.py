# Storage module for pgbackup tool
#
# (pgbackup-E7nj_BsO) [pgbackup $]
# (pgbackup-E7nj_BsO) [pgbackup $] vim src/pgbackup/storage.py

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()
    
    
def s3(client, infile, bucket, file_name):
	client.upload_fileobj(infile, bucket, file_name)
