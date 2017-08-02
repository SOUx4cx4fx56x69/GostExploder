import MYSQL as SQL
import sys
sys.path.append( "../blocks/" )
import blocksreader as bh
from datetime import datetime


def InstallTables(self):
	tmpBase = SQL()
	INSTALLING='''
create table Blocks(id bigint(255) unsigned PRIMARY KEY AUTO_INCREMENT, 
		    size int(255) unsigned,
		    version int(255) unsigned,
	            magic varchar(8),
			prevhash varchar(63),
			MerkleRoot varchar(63),
			Difficulty double unsigned,
			nonce int(255) unsigned,
			date varchar(24)
);
create table Blocks_Transactions(id bigint(255) unsigned PRIMARY KEY AUTO_INCREMENT,
TxVersion int unsigned,
Count_inputs bigint(255) unsigned,
Count_outputs bigint(255) unsigned
);
create table Blocks_Transactions_Input(from_id bigint(255) unsigned,
txOutId int(255) unsigned,
seqNo int(255) unsigned,
prevhash varchar(63),
scriptSig varchar(255),
scriptlen int(255) unsigned 
);
create table Blocks_Transactions_Output(from_id bigint(255) unsigned,
pubkey varchar(255),
value double unsigned,
scriptlen int(255) unsigned 
);
'''
	cursor = tmpBase.query(INSTALLING)
	cursor.close()
	tmpBase.commit()
	tmpBase.destruct()
	tmpBase = None	

def AddBlock(dat):
	block = bh.BlockReader(blockchain)
	if block == False:
	 return False
	BlocksAdd = '''
	insert into Blocks(size,version,magic,prevhash,MerkleRoot,Difficulty,nonce,date) values
	(
	%s,%s,%s,%s,%s,%s,%s,%s
	);
	'''	
	
	BlocksTransactionsAdd = '''insert into Blocks_Transactions values(%s,%s,%s,%s);'''
	BlocksTransactionsInputAdd = '''insert into Blocks_Transactions_Input values(%s,%s,%s,%s,%s,%s);'''
	BlocksTransactionsInputOutput = '''insert into Blocks_Transactions_Output values(%s,%s,%s,%s);'''

	LastBlockCount = '''SELECT COUNT(*) as last from Blocks;'''
	tmp = block.ReturnAllToList()
	cursor = tmpBase.query(BlocksAdd,(tmp['BlockSize'],tmp["BlockHeader"]['version'],tmp["Magic"],tmp["BlockHeader"]['previousHash'],tmp['BlockHeader']['merkleRoot'],bh.GetDiff(tmp["BlockHeader"]['nbits']),tmp["BlockHeader"]['nonce'],datetime.datetime.utcfromtimestamp(tmp["BlockHeader"]['ntime']).strftime('%Y.%m.%d %H:%M:%S GMT0'),))
	cursor.close()
    	cursor = tmpBase.query(LastBlockCount)
	LastBlock = 0
	for (last) in cursor:
	 LastBlock = last
	cursor.close()
	for txs in tmp["Txs"]:
	 tmptxs = txs.GetAllAsList()
	 # Add bluh-bluh
	 for i in tmptxs['TxInput']:
		pass
	 for i in tmptxs['TxOutputs']:
		pass
	 # Add bluh-bluh
	tmpBase.commit()
	tmpBase.close()
	tmpBase = None
	block = None

