from array import array

class MyCollection:

	def __new__(cls, type, value):
		return object.__new__(cls)


	def __init__(self, type, value):
		if type == int:
			self.data = array('i', value)
			self.code = 'i'
			#i
		elif type == float:
			self.data = array('d', value)
			self.code = 'd'
			#d
		elif type == str:
			self.data = array('u', value)
			self.code = 'u'
			#u
		else:
			raise Exception("BadType")
		self.type = type

	def __str__(self):
		new_list = []
		for x in self.data:
			new_list.append(x)
		return str(new_list)

	def __getitem__(self, index):
		return self.data[index]

	def __setitem__(self, index, value):
		if type(value) != self.type:
			raise Exception("BadType")
		self.data[index] = value

	def __iter__(self):
		#return iter(self.data)
		for it in range(self.data.buffer_info()[1]):
			yield self.data[it]

	def __len__(self):
		len = 0
		for i in self.data:
			len += 1
		return len

	def __delitem__(self, index):
		del self.data[index]

	def insert(self, index, value):
		if type(value) != self.type:
			raise Exception("BadType")
		new_collection = MyCollection(self.type, [])
		for it in range(len(self.data) + 1):
			if it == index:
				new_collection.append(value)
				break
			else:
				new_collection.append(self.data[it])
		for x in self.data[it::]:
			new_collection.append(x)
		self.data = new_collection.data


	def __contains__(self, value):
		if type(value) != self.type:
			raise Exception("BadType")
		return value in self.data

	def __reversed__(self):
		new_list = []
		for x in self.data:
			new_list.append(x)
		return new_list[::-1]

	def index(self, value):
		if type(value) != self.type:
			raise Exception("BadType")
		if value in self.data:
			it = -1
			for x in self.data:
				it += 1
				if x == value:
					return it
		else:
			raise Exception("ValueError")

	def count(self, value):
		if type(value) != self.type:
			raise Exception("BadType")
		it = 0
		for x in self.data:
			if x == value:
				it += 1
		return it

	def append(self, value):
		if type(value) != self.type:
			raise Exception("BadType")
		new_arr = array(self.code, [value])
		self.data += new_arr

	def pop(self, index = "default"):
		if index == "default":
			index = len(self) - 1
		value = self.data[index]
		del self.data[index]
		return value

	def extend(self, value):
		for x in value:
			if type(x) != self.type:
				raise Exception("BadType")
			self.append(x)
		

	def remove(self, value):
		if type(value) != self.type:
			raise Exception("BadType")
		if value in self.data:
			index = self.index(value)
			del self.data[index]
		else:
			raise Exception("ValueError")

	def __iadd__(self, value):
		for x in value:
			if type(x) != self.type:
				raise Exception("BadType")
		new_arr = self.data + value.data
		self.data = new_arr
		return self

collection = MyCollection(int, [6, 3, 7, 2, 8])

for x in collection:
	print(x)

