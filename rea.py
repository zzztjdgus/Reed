# 유명한 직사각형, 정사각형 사례
# 일반적으로 정사각형은 직사각형입니다. 즉 정사각형 is 직사각형의 관계이며, 이는 상속이 가능합니다. 
class Rectangle:
    def get_width(self):
        return self.width;

    def get_height(self):
        return self.height;

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.width = height
        self.height = height

if __name__ == "__main__":
	square = Square()
	square.set_width(20)
	square.set_height(30)
	check = square.get_width() == 20 & square.get_height() == 30 #부모의 명세와 다름
	print(check)
	print(square.get_width())
	print(square.get_height())