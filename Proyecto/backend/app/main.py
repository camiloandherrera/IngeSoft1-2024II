'''Main module for the FastAPI application'''

from fastapi import FastAPI, HTTPException

from routes import class_router, assignment_router, student_assignment_router,\
submission_router, role_router, professor_router, student_router, user_router

# mvc (view/api)

app = FastAPI(title="ProjecTrack-backend")
app.title = "Seguimiento de tareas académicas"
app.version = "0.0.5"

# Basic hello world test
@app.get("/greeting/", tags=["Greeting"])
async def hello_root():
    """Just a hello world message. :)"""
    return {"message": "Hello World!", "signs": "The ProjectTrack dev team"}

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint for the API"""
    return {"message": "Welcome to the ProjectTrack API!"}

# Include routers
app.include_router(class_router.router)
app.include_router(assignment_router.router)
app.include_router(student_assignment_router.router)
app.include_router(submission_router.router)

app.include_router(role_router.router)
app.include_router(professor_router.router)
app.include_router(student_router.router)
app.include_router(user_router.router)
