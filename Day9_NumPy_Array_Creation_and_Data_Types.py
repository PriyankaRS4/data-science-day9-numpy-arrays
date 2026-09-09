import numpy as np
import pandas as pd

df = pd.read_csv("student_marks.csv")

# 1D and 2D arrays
marks_1d = np.array([78, 85, 92, 67, 88])
marks_2d = np.array([[78,82,75],[90,88,92],[65,70,68]])

print("1D:", marks_1d)
print("2D:\n", marks_2d)
print("2D shape:", marks_2d.shape)
print("2D ndim:", marks_2d.ndim)
print("2D size:", marks_2d.size)
print("2D dtype:", marks_2d.dtype)

# Numerical operations
marks = np.array([60,70,80,90,100])
print("Add 5:", marks+5)
print("Multiply by 2:", marks*2)
print("Mean:", marks.mean())
print("Max:", marks.max())
print("Min:", marks.min())
print("Sum:", marks.sum())

# Student dataset
subjects = ['Maths','Physics','Chemistry','English','Biology','Economics','History','Civics']
student_marks = df[subjects].to_numpy(dtype=float)
print("Student marks shape:", student_marks.shape)
print("Average per subject:", student_marks.mean(axis=0))
print("Average per student:", student_marks.mean(axis=1))

# List comparison
python_list = [10,20,30,40]
numpy_array = np.array([10,20,30,40])
print("Python list * 2:", python_list*2)
print("NumPy array * 2:", numpy_array*2)
