#coding:utf-8
#!/usr/bin/env python2.7 
import priorityQueue
class GlobalVar: 
	InstQueue = {}
	InstNotDealt = {}
	#
	def insert_notDealt(self,inst):
		aa = GlobalVar().InstNotDealt
		
		if(aa.has_key(inst[4])):
			aa[inst[4]].append(inst)
		else:
			aa[inst[4]]=[]
			aa[inst[4]].append(inst)
			
	def insert(self,inst):
	#inst = (ID,time,type,StockID,securityID,accountID,quantity,price) 
	#	[0] [1]  [2]  [3]	[4]	 [5]	   [6]	    [7]
		aa = GlobalVar.InstQueue
		bb = GlobalVar.InstNotDealt
		if(aa.has_key(inst[3])):
			if(inst[2]==0):#type0==buy 队首是最高买价
				aa[inst[3]][0].put_h2l((inst,inst[7]))
				self.insert_notDealt(inst)
			elif(inst[2]==1):#type1==sell 队首是最低卖价
				aa[inst[3]][1].put_l2h((inst,inst[7]))
				self.insert_notDealt(inst)
			else:
				return False # not buy or sell
		else:
			return False # no such stock
	
	def delete(self,inst):
		aa = GlobalVar.InstQueue
		if(aa.has_key(inst[3])):
			if(inst[2]==0):#type0==buy 队首是最高买价
				aa[inst[3]][0].get()
				delete_notDealt(inst)
			elif(inst[2]==1):#type1==sell 队首是最低卖价
				aa[inst[3]][1].get()
				delete_notDealt(inst)
			elif(inst[2]==2):#type1==revoke
				return False # not buy or sell
		else:
			return False # no such stock