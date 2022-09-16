# Note: this code can run on https://www.online-python.com/

def hcfnaive(a, b):
    # source: https://www.geeksforgeeks.org/gcd-in-python/
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)

def cornerHit(dimensions, initialCoordinates, screenSize):
    # Returns the number of collisions to get to a corner ;
    # Returns False if the logo never hits a corner ;
    # Note: these are 2 differents types! be careful when using this function
    
    # 0 -------> x axis (width)
    # |
    # |
    # |
    # v   y axis (height)
    
    # Initial trajectory : when the logo move +1 x, it moves +1 y
    
    # I tried to solve it by myslef. It was fun, but my math were soooo wrong!
    # My code is based on this thing :
    #   https://prgreen.github.io/blog/2013/09/30/the-bouncing-dvd-logo-explained/
    
    # top left of the logo
    x = initialCoordinates[0]
    y = initialCoordinates[1]

    # a logo of size w by h moving in a W by H screen is equivalent to
    # a point moving in a W-w by H-h screen
    w = screenSize[0] - dimensions[0]
    h = screenSize[1] - dimensions[1]
    
    if (abs(x-y) % hcfnaive(w, h) == 0): #tricky math that I don't really grasp
        # The logo hits a corner! 
        # How many hits? Just "draw" the lines until it hits a corner
        # I cheat : the logo always moves in the same direction, but in a
        # infinite number of screens. The screens repeats itslef periodically,
        # and symetrically. Since I only care "when" it bounces, not "where",
        # I can exploit this.
        #  ____________ ____________ ____________ ____________
        # | OG screen  |    first   |   second   |     etc    |
        # |         L \|    right   |    right   |            |
        # |__________\/|____copy____|____copy____|____________|
        # |           \|            |            |            |
        # |            |\           |            |            |
        # |____________|_\/_________|____________|____________|

        isCornerHit = False
        count = 0
        while not isCornerHit:
            count +=1
            # go the the nearest wall
            dist_wall_Right = w - x
            dist_wall_Bottom = h - y
            if dist_wall_Right < dist_wall_Bottom:
                x = 0
                y = (y + dist_wall_Right) % h
            elif dist_wall_Right > dist_wall_Bottom:
                y = 0
                x = (x + dist_wall_Bottom) % w
            else: # dist_wall_Right == dist_wall_Bottom
                isCornerHit = True
        return count
    else:
        return False

# Unit Test
def test(dimensions, initialCoordinates, screenSize, expected):
    print("Test")
    print("|   dimensions, initialCoordinates, screenSize = ", dimensions, initialCoordinates, screenSize)
    print("|   expected output = ", expected)
    result = cornerHit(dimensions, initialCoordinates, screenSize)
    if result == expected:
        print("|   Test OK ✅ (result matches expected)") 
    else:
        print("|   ❌ Test FAILED ; result = ", result)
        raise Exception("Unit Test failed")

test([5,5], [0,0], [100,100], 1)
test([5,5], [45,70], [400,200], 102)
test([5,5], [46,70], [400,200], False)
