from python_actr import *

class myEnv(Model):
  pass
class myAg(ACTR):
  goal=Buffer()

  def init():
    goal.set("start coffee")
  
  def start1(goal="start coffee"):
    print ("coffee started")
    goal.set("stop")
  def stop1(goal="stop"):
    print ("coffee done")
    self.stop()
 
tim=myAg()
subway=myEnv()
subway.agent=tim
log_everything(subway)
subway.run()
