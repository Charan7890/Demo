if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    per = 0.00
    x = student_marks[query_name]
    # print(x)
    for val in x:
        per+=val
    
    percentage = per/len(x)
    print('{:0.2f}'.format(percentage))
