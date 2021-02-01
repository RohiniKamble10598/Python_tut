# marks = [84,89,78,91]
# percentage1 = (sum(marks)/400)*100
# print(percentage1)

# marks2 = [82,79,85,71]
# percentage2 = (sum(marks2)/400)*100
# print(percentage2)
            # OR
def percentage(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

marks1 = [84,89,78,91]
percentage1 = percentage(marks1)
print(percentage1)

marks2 = [82,79,85,71]
percentage2 = percentage(marks2)
print(percentage2)