import MYSQL as SQL
import sys
sys.path.append( "./blocks/" )
import blocksreader as bh

from datetime import datetime


def InstallTables(self):
	tmpBase = SQL()
	INSTALLING='''
create table settings(conf_name varchar(255),conf_value varchar(255));
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
Count_outputs bigint(255) unsigned,
locktime int unsigned
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
insert into settings values('lseek', '0' );
'''
	cursor = tmpBase.query(INSTALLING)
	cursor.close()
	tmpBase.commit()
	tmpBase.destruct()
	tmpBase = None	

def AddBlock(dat,lseek=0):
	tmpBase = SQL()
	cursor = tmpBase.query("select * from settings where conf_name='lseek';")
	lseek = 0
	for (conf_value) in cursor:
	 lseek=int(conf_value)
	cursor.close()
	block = bh.BlockReader(dat,seek=lseek)
	if block == False:
	 tmpBase.destruct()
	 return False
	

	BlocksAdd = '''
	insert into Blocks(size,version,magic,prevhash,MerkleRoot,Difficulty,nonce,date) values
	(
	%s,%s,%s,%s,%s,%s,%s,%s
	);
	'''	
	
	BlocksTransactionsAdd = '''insert into Blocks_Transactions(TxVersion,Count_inputs,Count_outputs,locktime) values(%s,%s,%s,%s);'''
	BlocksTransactionsInputAdd = '''insert into Blocks_Transactions_Input values(%s,%s,%s,%s,%s,%s);'''
	BlocksTransactionsInputOutput = '''insert into Blocks_Transactions_Output values(%s,%s,%s,%s);'''
	addLastSeek = '''update settings set conf_value='%s' where conf_name='lseek';'''
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
	 cursor = tmpBase.query(BlocksTransactionsAdd,(tmptxs["TxVersion"],tmptxs["TxInputs"],tmptxs["TxOutPuts"],tmptxs["TxLockTime"],))
	 cursor.close()
	 for i in tmptxs['TxInput']:
	  t = i.GetAllAsList()
	  cursor = tmpBase.query(BlocksTransactionsInputAdd,(LastBlock,i['txOutId'],i['seqNo'],bh.hashstr(i['prevhash']),i['scriptSig'],i['scriptlen'],))
	  cursor.close()
	 for i in tmptxs['TxOutputs']:
	  t = i.GetAllAsList()
	  cursor = tmpBase.query(BlocksTransactionsInputAdd,(LastBlock,bh.hashstr(LastBlock,i['pubkey']),bh.FromSatToFull(i['value']),i['scriptlen'],))
	  cursor.close()
	cursor = tmpBase.query(addLastSeek,(block.lastSeek,))
	cursor.close()
	cursor=None
	tmpBase.commit()
	tmpBase.destruct()
	tmpBase = None
	block = None

