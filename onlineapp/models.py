from django.db import models

# Create your models here.
class addp(models.Model):
    subject=models.CharField(max_length=122)
    
    q1=models.CharField(max_length=500)
    q1op1=models.CharField(max_length=122)
    q1op2=models.CharField(max_length=122)
    q1op3=models.CharField(max_length=122)
    q1op4=models.CharField(max_length=122)
    q1correctoption=models.IntegerField()
    
    q2=models.CharField(max_length=500)
    q2op1=models.CharField(max_length=122)
    q2op2=models.CharField(max_length=122)
    q2op3=models.CharField(max_length=122)
    q2op4=models.CharField(max_length=122)
    q2correctoption=models.IntegerField()
    
    q3=models.CharField(max_length=500)
    q3op1=models.CharField(max_length=122)
    q3op2=models.CharField(max_length=122)
    q3op3=models.CharField(max_length=122)
    q3op4=models.CharField(max_length=122)
    q3correctoption=models.IntegerField()
    
    q4=models.CharField(max_length=500)
    q4op1=models.CharField(max_length=122)
    q4op2=models.CharField(max_length=122)
    q4op3=models.CharField(max_length=122)
    q4op4=models.CharField(max_length=122)
    q4correctoption=models.IntegerField()
    
    q5=models.CharField(max_length=500)
    q5op1=models.CharField(max_length=122)
    q5op2=models.CharField(max_length=122)
    q5op3=models.CharField(max_length=122)
    q5op4=models.CharField(max_length=122)
    q5correctoption=models.IntegerField()
    
    q6=models.CharField(max_length=500)
    q6op1=models.CharField(max_length=122)
    q6op2=models.CharField(max_length=122)
    q6op3=models.CharField(max_length=122)
    q6op4=models.CharField(max_length=122)
    q6correctoption=models.IntegerField()
    
    q7=models.CharField(max_length=500)
    q7op1=models.CharField(max_length=122)
    q7op2=models.CharField(max_length=122)
    q7op3=models.CharField(max_length=122)
    q7op4=models.CharField(max_length=122)
    q7correctoption=models.IntegerField()
    
    q8=models.CharField(max_length=500)
    q8op1=models.CharField(max_length=122)
    q8op2=models.CharField(max_length=122)
    q8op3=models.CharField(max_length=122)
    q8op4=models.CharField(max_length=122)
    q8correctoption=models.IntegerField()

    
    q9=models.CharField(max_length=500)
    q9op1=models.CharField(max_length=122)
    q9op2=models.CharField(max_length=122)
    q9op3=models.CharField(max_length=122)
    q9op4=models.CharField(max_length=122)
    q9correctoption=models.IntegerField()

    q10=models.CharField(max_length=500)
    q0op1=models.CharField(max_length=122)
    q10op2=models.CharField(max_length=122)
    q10op3=models.CharField(max_length=122)
    q10op4=models.CharField(max_length=122)
    q10correctoption=models.IntegerField()

    def __str__(self):
        return self.subject