# Generated by Django 3.0.1 on 2022-04-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegelistdiploma',
            name='NUMBER_OF_TEACHER_FEMALE',
            field=models.IntegerField(db_column='NUMBER_OF_TEACHER_FEMALE', default=''),
        ),
        migrations.AlterField(
            model_name='collegelistdiploma',
            name='NUMBER_OF_TEACHER_MALE',
            field=models.IntegerField(db_column='NUMBER_OF_TEACHER_MALE', default=''),
        ),
        migrations.AlterField(
            model_name='collegelistdiploma',
            name='NUMBER_OF_TEACHER_TOTAL',
            field=models.IntegerField(db_column='NUMBER_OF_TEACHER_TOTAL', default=''),
        ),
        migrations.AlterField(
            model_name='collegelistdiploma',
            name='SL_NO',
            field=models.IntegerField(db_column='SL_NO', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collegelistdiploma',
            name='STUDENT_ENROLMENT_FEMALE',
            field=models.IntegerField(db_column='STUDENT_ENROLMENT_FEMALE', default=''),
        ),
        migrations.AlterField(
            model_name='collegelistdiploma',
            name='STUDENT_ENROLMENT_MALE',
            field=models.IntegerField(db_column='STUDENT_ENROLMENT_MALE', default=''),
        ),
        migrations.AlterField(
            model_name='collegelistdiploma',
            name='STUDENT_ENROLMENT_TOTAL',
            field=models.IntegerField(db_column='STUDENT_ENROLMENT_TOTAL', default=''),
        ),
    ]
