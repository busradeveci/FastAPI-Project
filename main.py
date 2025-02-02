from fastapi import Body, FastAPI

app = FastAPI()

#db databases'mizdir. bu databases'imiz düz bir liste şu an .
# 15.000 tane kişi kurs da olabilir.bunları grup şeklinde path veya query filtreleme ile ayarlayabiliriz.

courses_db = [
    {"id": 1, "instructor": "busra", "title": "Python", "category": "development"},
    {"id": 2, "instructor": "asya", "title": "Java", "category": "development"},
    {"id": 3, "instructor": "ali", "title": "Jenkins", "category": "devops"},
    {"id": 4, "instructor": "veli", "title": "Kubernetes", "category": "devops"},
    {"id": 5, "instructor": "zeynep", "title": "Machine learning", "category": "AI"},
    {"id": 6, "instructor": "mehmet", "title": "Deep learning", "category": "AI"}
]

@app.get("/")
async def hello_word():
    return {"message": "hello world"}


@app.get("/courses")
async def get_all_courses():
    return courses_db

#Path parametresi
#course.title ile path ile filtreleme yapma işlemi

@app.get("/courses/{course_title}")
async def get_course(course_title: str):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold():
            return course

#bu fonksiyon çalıştırılmıyor.
@app.get("/courses/{course_id}")
async def get_course_by_id(course_id: str):
    for course in courses_db:
        if course.get('id').casefold() == course_id.casefold():
            return course


@app.get("/courses/by_id/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course

#query ile filtreleme
@app.get("/courses/")
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
            return course

#hem path hemde query ile kod çalışması.
@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    courses_to_return = [] #boş bir dizi oluşturuyoruz.
    for course in courses_db:  #for loop döngüsünü çalıştırıyoruz.
        if course.get('instructor').casefold() == course_instructor.casefold() and course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return

#Post işlemi, Body parametresiyle yapılıyor.
@app.post("/courses/create_course")
async def create_course(new_course: dict = Body(...)):
    courses_db.append(new_course)

#update işlemi, aynı id yerine başka bir id ekleme işlemi
@app.put("/courses/update_course")
async def update_course(updated_course: dict = Body(...)):
    for i in range(len(courses_db)):  #id'si tutuyor mu diye bakıyoruz.
        if courses_db[i].get('id') == updated_course.get('id'):
            courses_db[i] = updated_course

#delete işlemi, id silme işlemi
@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):
    for i in range(len(courses_db)):
        if courses_db[i].get("id") == course_id:
            courses_db.pop(i)
            break
