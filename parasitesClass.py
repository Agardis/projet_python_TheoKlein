class parasites:
	parasites_list = []

	def __init__(self, parasites_file):
		with open(parasites_file, 'r') as file:
		  	for line in file:
		  		self.parasites_list.append(line.strip())

	def remove_parasites(self, word_count):
		for parasites in self.parasites_list:
			word_count.pop(parasites, None)
		return word_count