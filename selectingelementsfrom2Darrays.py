import numpy as np

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])
tanya_test_3 = student_scores[2,0]
cody_test_scores = student_scores[:,-1]
#selecting the first column a[:,0]
#selecting the second row a[1,:]
#selects the first three elements ofthe first row
#a[0,0:3]
