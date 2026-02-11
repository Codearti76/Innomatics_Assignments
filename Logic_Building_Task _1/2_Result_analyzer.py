marks = [45, 78, 90, 33, 60]

pass_count=0
fail_count=0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Total Students:",len(marks))
print("Total no. of Passed students:",pass_count)
print("Total no. of Failed students:",fail_count)
