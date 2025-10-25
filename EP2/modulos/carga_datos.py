import pandas as pd
from .modelos import Estudiante

def cargar_estudiantes(ruta_csv: str):
    df = pd.read_csv(ruta_csv)

    estudiantes = []
    for _, row in df.iterrows():
        estudiante = Estudiante(
            row["anxiety_level"],
            row["self_esteem"],
            row["mental_health_history"],
            row["depression"],
            row["headache"],
            row["blood_pressure"],
            row["sleep_quality"],
            row["breathing_problem"],
            row["noise_level"],
            row["living_conditions"],
            row["safety"],
            row["basic_needs"],
            row["academic_performance"],
            row["study_load"],
            row["teacher_student_relationship"],
            row["future_career_concerns"],
            row["social_support"],
            row["peer_pressure"],
            row["extracurricular_activities"],
            row["bullying"],
            row["stress_level"]
        )
        estudiantes.append(estudiante)

    return estudiantes
