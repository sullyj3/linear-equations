#for now, this presumes that all endpoints are inclusive, rather than exclusive

def solve(**kwargs):
    #y=mx+c
    y,m,x,c='y','m','x','c'
    for key in kwargs:
        kwargs[key]=float(kwargs[key])
        
    if not len(kwargs)==3:
        raise TypeError("Need exactly 3 Arguments")

    if not 'y' in kwargs:
        try:
            m,x,c=kwargs[m],kwargs[x],kwargs[c]
        except KeyError("wrong arguments"):
            pass
        return m*x+c

    elif not 'm' in kwargs:
        try:
            y,x,c=kwargs[y],kwargs[x],kwargs[c]
        except KeyError("wrong arguments"):
            pass
        return (y-c)/x

    elif not 'x' in kwargs:
        try:
            y,m,c=kwargs[y],kwargs[m],kwargs[c]
        except KeyError("wrong arguments"):
            pass
        return (y-c)/m
            
    elif not 'c' in kwargs:
        try:
            y,m,x=kwargs[y],kwargs[m],kwargs[x]
        except KeyError("wrong arguments"):
            pass
        return y-(m*x)

class real_interval(object): #unfinished
    def __init__(self,
        #a vaid mathematical interval notation string, like (1,2).
        #use [] on either or both sides for inclusive, () for exclusive
        #leave one of the numbers blank for negative or positive infinity

        parse_str='', 
        left=None, #real number
        right=None, #real number
        left_is_inclusive=True, #bool
        right_is_inclusive=True #bool
        ):

        if not parse_str=='':
            assert (left==None and
                    right==None and
                    left_is_inclusive==True and
                    right_is_inclusive==True)
            
            assert len(parse_str) in range(3,6)

            if parse_str[0] == '(':
                self.left_is_inclusive == False
            elif parse_str[0] == '[':
                self.left_is_inclusive == True
            else:
                raise ValueError("Error parsing real interval generation string {0} at position 0: Invalid Syntax".format(parse_str))

class line(object): #unfinished
    def __init__(self,
            vertical=False,
            m=None,
            known_point_x=None,
            known_point_y=None,
            c=None,
            endpoint_left=None, # x value
            endpoint_right=None # x value
            ):

        #prevent integer division problems
        for arg in (m,c,endpoint_left,endpoint_right):
            if not arg is None:
                arg=float(arg)

        self.vertical=vertical
        self.m=m
        self.c=c
        self.endpoint_left=endpoint_left
        self.endpoint_right=endpoint_right
        
        if not vertical:
            if m and known_point_x>None and known_point_y>None:
                self.c=solve(m=m,x=known_point_x,y=known_point_y)
            if c and known_point_x>None and known_point_y>None:
                self.m=solve(c=c,x=known_point_x,y=known_point_y)
            if not endpoint_left is None:
                self.y_endpoint_left = self.m * self.endpoint_left + self.c
            if not endpoint_right is None:
                self.y_endpoint_right = self.m * self.endpoint_right + self.c

def furthest_left(line1,line2): 
    if line1.endpoint_left == line2.endpoint_left: 
        #covers 'endpoints are equal' and 'endpoints are both None'
        return None
    elif line1.endpoint_left is None and not line2.endpoint_left is None:
        return line1
    elif line2.endpoint_left is None and not line1.endpoint_left is None:
        return line2
    else: #both must have left endpoints, which are not equal
        if line1.endpoint_left < line2.endpoint_left:
            return line1
        elif line2.endpoint_left < line1.endpoint_left: 
            return line2

def furthest_down(line1,line2): #unfinished
    if line1.endpoint_left == line2.endpoint_left: 
        #covers 'endpoints are equal' and 'endpoints are both None'
        return None
    elif line1.endpoint_left is None and not line2.endpoint_left is None:
        return line1
    elif line2.endpoint_left is None and not line1.endpoint_left is None:
        return line2
    else: #both must have left endpoints, which are not equal
        if line1.endpoint_left < line2.endpoint_left:
            return line1
        elif line2.endpoint_left < line1.endpoint_left: 
            return line2

def test_domain_overlap(leftmost, rightmost):
    #sort input lines by furthest left
    if furthest_left(leftmost,rightmost) is rightmost:
        leftmost,rightmost=rightmost,leftmost
    elif furthest_left(leftmost,rightmost) is None:
        return True

    if leftmost.endpoint_right > rightmost.endpoint_left:
        return True
    else:
        return False

def test_range_overlap(bottom, top): #unfinished
    #sort input lines by furthest left
    if furthest_left(leftmost,rightmost) is rightmost:
        leftmost,rightmost=rightmost,leftmost
    elif furthest_left(leftmost,rightmost) is None:
        return True

    if leftmost.endpoint_right > rightmost.endpoint_left:
        return True
    else:
        return False

def test_intersect(line1, line2): #unfinished

    #check if they both have domains
    #if they both do, see if they intersect.
    if not ((line1.endpoint_left is None and line1.endpoint_right is None) or
            (line2.endpoint_left is None and line2.endpoint_right is None)): #checks that neither line has no endpoints


        #determine which line extends furthest left
        if type(line1.endpoint_left) is None:
            if type(line2.endpoint_left) is None:
                if not line1.m==line2.m:
                    return True
            leftmost=line1
        elif line2.endpoint_left < line1.endpoint_left: 
            leftmost=line2


        #figure out conditions where the domains intersect
        #right endpoint of line furthest left is RIGHT of left endpoint of other line
        if ((line1.endpoint_right >= line2.endpoint_left) or
        (line2.endpoint_right >= line1.endpoint_left)):
            pass



    if not (type(line1.m) is None or type(line2.m) is None):
        if line1.m == line2.m:
            return False

        elif line1.m != line2.m:
            #solve for line1=line2
            #m1x+c1=m2x+c2
            #c2-c1 = m1x-m2x = x(m1-m2)
            #x=(c2-c1)/(m1-m2)
            x_solution = (line2.c - line1.c)/(line1.m - line2.m)
            y_solution = (line1.m * x_solution) + line1.c

            #ensure solution is within intersection of domains
