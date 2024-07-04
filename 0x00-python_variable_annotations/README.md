# Python Variable Annotation

Brief showing python variable annotation.

No Annotations
```py
def createStudents(students):
    """Create a list of students with their name and age.

    Args:
        students (list): A list of students.

    Returns:
        list: A list of students with their name and age.
    """
    return students
```

With Annotations
```py
def createStudents(students: list) -> list:
    """Create a list of students with their name and age."""
    return students
```
