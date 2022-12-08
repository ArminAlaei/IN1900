
#4.4 Compute the area of an arbitrary triangle


def triangle_area(vertices):
    v = vertices #renaming so the calculation below looks cleaner
    A = (v[1][0]*v[2][1]-v[2][0]*v[1][1]-v[0][0]*v[2][1]+v[2][0]*v[0][1]+v[0][0]*v[1][1]-v[1][0]*v[0][1])/2
    return(A)

#Test function given in the task
def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success,msg


test_triangle_area()
svar=triangle_area([[0,0],[1,0],[0,2]])
print(f"The area of the triangle is {svar}")


"""
Run code:
Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):

usr$ python3 triangle_area.py

The output in the terminal will be:

output:
The area of the triangle is 1.0


"""
