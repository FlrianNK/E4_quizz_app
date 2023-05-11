import json

class Question(object):

	def __init__(self, text = "", title = "", image="", position=0, possibleAnswers=[]):
		self.text = text
		self.title = title
		self.image = image
		self.position = position
		self.possibleAnswers = possibleAnswers
        
	def toJson(self):
		return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4)
	def fromJson(self, json_data):
		newQuestion = Question(**(json.loads(json_data)))
		self.__dict__.update(newQuestion.__dict__)
	
	class Answer(object):
		def __init__(self):
			self.text = ""
			self.isCorrect = False
		def toJson(self):
			return json.dumps(self.__dict__)
		def fromJson(self, json_data):
			newAnswer = Question(**(json.loads(json_data)))
			self.__dict__.update(newAnswer.__dict__)

def sendQuestionToDB():
	return

def getQuestionFromDB():
	return
			
# q = Question()
# print(q.toJson())
# data = str({
#     "text": "vqev",
#     "title": "vzev",
#     "image": "",
#     "position": 0,
#     "possibleAnswers": []
# }).replace("\'", "\"")
# print(data)
# q.fromJson(data)
# print(q.text)