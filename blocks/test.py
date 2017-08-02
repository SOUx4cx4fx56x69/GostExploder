import blocksreader as bh

def parse(path):
	blockchain = open(path, 'rb')
	print 'print Parsing Block Chain'
	continueParsing = True
	counter = 0
	blockchain.seek(0, 2)
	fSize = blockchain.tell() - 80 #Minus last Block header size for partial file
	blockchain.seek(0, 0)
	block = None
	while counter < 1000:	
		block = bh.BlockReader(blockchain)		
		continueParsing = not block.endOfFile
		if continueParsing:
			tmp = block.ReturnAllToList()
			print "+"*30
			print "Magic %8x " % tmp["Magic"]
			print "BlockSize %d " % tmp["BlockSize"]
			print "version %d " % tmp["BlockHeader"]['version']
			print "previousHash %s " % tmp["BlockHeader"]['previousHash']
			print "Merkle root %s" % tmp['BlockHeader']['merkleRoot']
			print "Difficulty %8x " % tmp["BlockHeader"]['nbits']
			print "nonce %s " % tmp["BlockHeader"]['nonce']
			print "ntime %s " % str(tmp["BlockHeader"]['ntime'])
			print "~"*15+"TX"+"~"*15
			for txs in tmp["Txs"]:
			 tmptxs = txs.GetAllAsList()
			 print "TxVersion %d" % tmptxs["TxVersion"]
			 print "#"*15+"INPUTS"+"#"*15
			 print "Count inputs %s " % tmptxs["TxInputs"]
			 for i in tmptxs['TxInput']:
				print i.GetAllAsList()			 
			 print "@"*15+"OUTPUTS"+"@"*15
			 print "Count OutPuts %s " % tmptxs["TxOutPuts"]
			 for i in tmptxs['TxOutputs']:
				 print i.GetAllAsList()
			 print "Lock Time %s " % tmptxs["TxLockTime"]
			print "~"*15+"~~"+"~"*15
			print "+"*30
		counter+=1

	print 'Parsed 1000 blocks'
	print "Last seek %s" % block.lastSeek

parse("/home/lock/.gostcoin/blocks/blk00000.dat")
