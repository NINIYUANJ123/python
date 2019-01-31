student = []
N = 5
for i in range(5):
    student.append(['','',[]])

def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(1):
            stu[i][2].append(int(input('score:\n')))

def output_stu(stu):
    for i in range(N):
        print ('%-6s%-10s' % ( stu[i][0],stu[i][1] ))

if __name__ == '__main__':
    input_stu(student)
    print (student)
    output_stu(student)
