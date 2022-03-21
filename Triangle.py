class Triangle():
    def __init__(self, a, b, c):
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        x = self.side1
        y = self.side2
        z = self.side3
        return (((x+y+z)*(-1*x+y+z)*(x-y+z)*(x+y-z))**0.5)/4

    def scale(self, sc_fact):
        return Triangle(self.side1*sc_fact, self.side2*sc_fact, self.side3*sc_fact)

    def is_valid(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self.side3
        if (s1+s2)>s3:
            if(s2+s3)>s1:
                if(s1+s3)>s2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def is_right(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self.side3
        if s1>=s2 and s1>=s3:
            if s1**2==s2**2+s3**2:
                return True
            else:
                return False            
        elif s2>=s1 and s2>=s3:
            if s2**2==s1**2+s3**2:
                return True
            else:
                return False
        elif s3>=s1 and s3>=s2:
            if s3**2==s1**2+s2**2:
                return True
            else:
                return False
        else:
            False

t = Triangle(4,13,15)

print(t.perimeter())
print(t.area())

t_sc = t.scale(2)

print(t_sc.perimeter())

t_v = Triangle(1,2,1)

print(t_v.is_valid())

t_r = Triangle(1,1,1)

print(t_r.is_right())
