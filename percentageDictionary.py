if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for student_name, grade in student_marks.items():
        if query_name == student_name:
            print(student_name, grade)
            print(sum(item['student_name'] for item in student_marks))
            #sum(d['cells'] for d in assets)
