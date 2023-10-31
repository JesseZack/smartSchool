from django.contrib.gis.db import models

# Create your models here.
from academics.models import Subject
from users.models import Student


class Exam(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField(default=30)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}'


class Question (models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class MultipleChoiceQuestion(Question):
    options = models.JSONField(default=list)
    correct_option = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.text}'


class EssayQuestion(Question):
    max_score = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.text}'


class ExamSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)
    submitted_at = models.DateTimeField()

    def __str__(self):
        return f'{self.exam} ({self.submitted_at})'


class StudentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.student} - {self.exam} ({self.score}/{self.exam.question_set.count()})'


class StudentAnswer(models.Model):
    submission = models.ForeignKey(ExamSubmission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.PositiveIntegerField(null=True, blank=True)
    essay_answer = models.TextField(blank=True)

    def __str__(self):
        return f'{self.submission} - {self.question}'



class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)