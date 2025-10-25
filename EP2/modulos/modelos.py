class Estudiante:
    def __init__(
        self, anxiety_level, self_esteem, mental_health_history,
        depression, headache, blood_pressure, sleep_quality,
        breathing_problem, noise_level, living_conditions, safety,
        basic_needs, academic_performance, study_load,
        teacher_student_relationship, future_career_concerns,
        social_support, peer_pressure, extracurricular_activities,
        bullying, stress_level
    ):
        self.anxiety_level = anxiety_level
        self.self_esteem = self_esteem
        self.mental_health_history = mental_health_history
        self.depression = depression
        self.headache = headache
        self.blood_pressure = blood_pressure
        self.sleep_quality = sleep_quality
        self.breathing_problem = breathing_problem
        self.noise_level = noise_level
        self.living_conditions = living_conditions
        self.safety = safety
        self.basic_needs = basic_needs
        self.academic_performance = academic_performance
        self.study_load = study_load
        self.teacher_student_relationship = teacher_student_relationship
        self.future_career_concerns = future_career_concerns
        self.social_support = social_support
        self.peer_pressure = peer_pressure
        self.extracurricular_activities = extracurricular_activities
        self.bullying = bullying
        self.stress_level = stress_level

    # métodos para evaluar riesgos y bienestar

    def riesgo_ansiedad(self):
        if self.anxiety_level >= 15:
            return "Alto"
        elif self.anxiety_level >= 8:
            return "Moderado"
        return "Bajo"

    def riesgo_depresion(self):
        if self.depression >= 15:
            return "Alto"
        elif self.depression >= 8:
            return "Moderado"
        return "Bajo"

    def riesgo_estres(self):
        if self.stress_level >= 15:
            return "Alto"
        elif self.stress_level >= 8:
            return "Moderado"
        return "Bajo"

    def bienestar_general(self):
        puntos_positivos = (
            self.self_esteem +
            self.sleep_quality +
            self.academic_performance +
            self.social_support
        )

        puntos_negativos = (
            self.anxiety_level +
            self.depression +
            self.stress_level
        )

        score = puntos_positivos - puntos_negativos

        if score <= -5:
            return "Muy preocupante"
        elif score <= 0:
            return "Preocupante"
        elif score <= 5:
            return "Estable / Moderado"
        else:
            return "Bueno"

    def resumen(self):
        return {
            "Ansiedad": self.riesgo_ansiedad(),
            "Depresión": self.riesgo_depresion(),
            "Estrés": self.riesgo_estres(),
            "Wellbeing Score": self.bienestar_general()
        }
