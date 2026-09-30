from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.ai.gemini import generate_fitness_plan

router = APIRouter()


class FitnessRequest(BaseModel):
    name: str
    user_id: str
    age: int
    weight: float
    fitness_goal: str
    workout_intensity: str


@router.get("/")
def home():
    return FileResponse("templates/index.html")


@router.post("/api/generate-plan")
def generate_plan(request: FitnessRequest):

    prompt = f"""
Create a safe, general fitness and wellness plan.

Name: {request.name}
User ID: {request.user_id}
Age: {request.age}
Weight: {request.weight} kg
Fitness Goal: {request.fitness_goal}
Workout Intensity: {request.workout_intensity}

Include:
1. A 7-day general fitness and wellness plan
2. Balanced nutrition guidance
3. Hydration
4. Rest and recovery
5. Safety tips

Focus on healthy habits and general wellness.
Do not recommend extreme dieting or excessive exercise.
"""

    plan = generate_fitness_plan(prompt)

    return {
        "success": True,
        "plan": plan
    }


@router.get("/feedback")
def feedback():
    return FileResponse("templates/feedback.html")