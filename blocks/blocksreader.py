from util import *

def calculate_target(nBits):
    # cf. CBigNum::SetCompact in bignum.h
    shift = 8 * (((nBits >> 24) & 0xff) - 3)
    bits = nBits & 0x7fffff
    sign = -1 if (nBits & 0x800000) else 1
    return sign * (bits << shift if shift >= 0 else bits >> -shift)

def target_to_difficulty(target):
    return ((1 << 224) - 1) * 1000 / (target + 1) / 1000.0

def GetDiff(nbits):
  return target_to_difficulty(calculate_target(nBits))

class Tx:
	def __init__(self, blockchain):
		self.version = uint4(blockchain)
		self.inCount = varint(blockchain)
		self.inputs = []
		for i in range(0, self.inCount):
			input = txInput(blockchain)
			self.inputs.append(input)
		self.outCount = varint(blockchain)
		self.outputs = []
		if self.outCount > 0:
			for i in range(0, self.outCount):
				output = txOutput(blockchain)
				self.outputs.append(output)	
		self.lockTime = uint4(blockchain)
	def GetAllAsList(self):
		return {
		"TxInput":self.inputs,
		"TxOutputs":self.outputs,
		"TxVersion":self.version,
		"TxInputs":self.inCount,
		"TxOutPuts":self.outCount,
		"TxLockTime":self.lockTime
		}

class txInput:
	def __init__(self, blockchain):
		self.prevhash = hash32(blockchain)
		self.txOutId = uint4(blockchain)
		self.scriptLen = varint(blockchain)
		self.scriptSig = blockchain.read(self.scriptLen)
		self.seqNo = uint4(blockchain)
	def GetAllAsList(self):
	 return {
		"PrevHash":self.prevhash,
		"txOutId":self.txOutId,
		"scriptLen":self.scriptLen,
		"scriptSig":self.scriptSig,
		"seqNo":self.seqNo
		}		
class txOutput:
	def __init__(self, blockchain):	
		self.value = uint8(blockchain)
		self.scriptLen = varint(blockchain)
		self.pubkey = blockchain.read(self.scriptLen)
	def GetAllAsList(self):
	 return {
		"value":self.value,
		"scriptLen":self.scriptLen,
		"pubkey":self.pubkey
		}

class BlockHeader:
	def __init__(self, blockchain):
		self.version = uint4(blockchain)
		self.previousHash = hash32(blockchain)
		self.merkleHash = hash32(blockchain)
		self.time = uint4(blockchain)
		self.bits = uint4(blockchain)
		self.nonce = uint4(blockchain)
	def GetAllAsList(self):
		return {
		"version": self.version,
		"previousHash": hashStr(self.previousHash),
		"merkleRoot": hashStr(self.merkleHash),
		"ntime": self.time,
		"nbits": self.bits,
		"nonce": self.nonce	
		}

class BlockReader:
	def __init__(self,blockchain,seek=0):
	 self.endOfFile=True
	 self.lastSeek = seek
	 self.magicNum = 0
	 self.blocksize = 0
	 self.blockheader = {}
	 self.txCount = 0
	 self.Txs = []
	 if seek != 0:
		blockhasin.seek(seek)
	 if self.hasLength(blockchain, 8):	#If has 8 byte length(8 chars)
		self.magicNum = uint4(blockchain)
		self.blocksize = uint4(blockchain)
		self.endOfFile=False
	 else:			# if end of file
		self.endOfFile = True
		return False
		
	 if self.hasLength(blockchain, self.blocksize):
		self.setHeader(blockchain)
		self.txCount = varint(blockchain)
		self.Txs = []

		for i in range(0, self.txCount):
		 tx = Tx(blockchain)
		 self.Txs.append(tx)
	 else:
		 self.lastSeek = blockhain.tell()
		 self.endOfFile = True
	
	def getBlocksize(self):
		return self.blocksize

	def hasLength(self, blockchain, size):
		curPos = blockchain.tell()
		blockchain.seek(0, 2)
		
		fileSize = blockchain.tell()
		blockchain.seek(curPos)

		tempBlockSize = fileSize - curPos
		self.lastSeek = blockchain.tell()
		if tempBlockSize < size:
			return False
		return True

	def setHeader(self, blockchain):
		tmpheaderObject = BlockHeader(blockchain)
		self.blockHeader = tmpheaderObject.GetAllAsList()
		tmpheaderObject=None

	def ReturnAllToList(self):
		return {
			"Magic":self.magicNum,
			"BlockSize":self.blocksize,
			"BlockHeader":self.blockHeader,
			"Txs":self.Txs
		       }
