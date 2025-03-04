'''Main module for the FastAPI application'''

from fastapi import FastAPI, HTTPException

from routes import user_router, assignment_router, student_assignment_router,\
submission_router

# mvc (view/api)

app = FastAPI(title="ProjecTrack-backend")
app.title = "Seguimiento de tareas académicas"
app.version = "0.0.5"

# Basic hello world test
@app.get("/greeting/", tags=["Greeting"])
async def hello_root():
    """Just a hello world message. :)"""
    return {"message": "Hello World!", "signs": "The ProjectTrack dev team"}

# Include routers
app.include_router(user_router.router)
app.include_router(assignment_router.router)
app.include_router(student_assignment_router.router)
app.include_router(submission_router.router)
