def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Science']
info = {'name':'John', 'age':23}  

student_info(*courses, **info)