class Ball:
    def bounce(self):
        if self.direction=="down":
            self.direction="up"
    def __str__(self):
        msg="GOOD!"
        return msg      
myball=Ball()
myball.direction='down'
myball.color='red'
myball.size='small'
print("哇哇哇哇哇")
myball.bounce()
print("yooho",myball.direction)
print(myball)