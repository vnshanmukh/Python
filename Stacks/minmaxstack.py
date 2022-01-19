class MinMaxStack:
	def __init__(self):
		self.minmaxstack =[]
		self.stack =[]

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        self.minmaxstack.pop()
		return self.stack.pop()

    def push(self, number):
		newminmax ={"min":number, "max":number}
		if len(self.minmaxstack):
			lastminmax = self.minmaxstack[len(self.minmaxstack)-1]
			newminmax["min"] = min(lastminmax["min"],number)
			newminmax["max"] = max(lastminmax["max"],number)
		self.minmaxstack.append(newminmax)
		self.stack.append(number)
		
    def getMin(self):
		return self.minmaxstack[len(self.minmaxstack)-1]["min"]

    def getMax(self):
		return self.minmaxstack[len(self.minmaxstack)-1]["max"]