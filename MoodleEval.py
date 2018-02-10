#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:32:09 2017

@author: sven
"""
import pandas as pd
import numpy as np


def compute_points_non_mc(df_types, df_points):
    """
    Computes the points for each student from the non-MC questions.
    
    Parameters:
    --------------
    df_types: df,
             a dataframe which contains at least two columsn "Typ", "Aufgabe".
             Aufgabe is the EXACT same number of the question as in ISIS!
             Typ is a description of the question type ("MC", "Lueckentext",
             "Drag and Drop", etc.)
             
    df_points: df,
             a dataframe that can be exported from ISIS and contains all the
             points for the exam
    """
    #first do the easy part and the points for all "special assignments" (e.g. drag and Drop)
    df_types_other = df_types[df_types["Typ"] != "MC"]
    
    used_regex = "|".join(["F {} .*".format(nassignment) for nassignment in df_types_other["Aufgabe"]])
    
    
    points_other = df_points.filter(regex=used_regex)
    #number of cols = number of questions
    n_other_types = points_other.shape[1]
    points_other.columns = ["Punkte " + str(i).split("/")[0].split()[1].zfill(2) +" "+ \
                            "({} Pkt) (OT)".format(str(i).split("/")[1].replace(",",".")) 
                            for i in points_other.columns]
    points_other["Summe_Other"] = points_other.sum(axis=1)
    
    return(points_other, n_other_types)


def compute_points_mc(df_types, df_details):
    """
    Computes the points for each student from the MC questions.
    The following grading scheme is applied for 4 questions:
        
    4 correct: 1 Point
    3 correct: 2/3 Point
    2 correct: 1/3 Point
    1 correct: 0 Point
    0 correct: 0 Point
    
    Parameters:
    --------------
    df_types: df,
             a dataframe which contains at least two columsn "Typ", "Aufgabe".
             Aufgabe is the EXACT same number of the question as in ISIS!
             Typ is a description of the question type ("MC", "Lueckentext",
             "Drag and Drop", etc.)
             
    df_details: df,
             a dataframe that can be exported from ISIS and contains all the
             detailed questions and answers from ISIS.
    """
    df_types_mc = df_types[df_types["Typ"] == "MC"]
    n_questions_cm = df_types_mc.shape[0]
    numbers =  df_types_mc["Aufgabe"] #.iloc[[0]]
    
    cols0 = ["0idx", u'Nachname', u'Vorname', u'Institution', u'Abteilung',
           u'E-Mail-Adresse', u'Status', u'Begonnen am', u'Beendet',
           u'Verbrauchte Zeit']
    cols1 = ["Frage {}".format(i) for i in numbers]
    cols2 = ["Antwort {}".format(i) for i in numbers]
    cols3 = ["Richtige Antwort {}".format(i) for i in numbers]
    all_cols = cols0 + cols1 + cols2  + cols3
    df_mc = df_details[all_cols]
    
    points_dic = {"Punkte {} (1.00 Pkt) (MC)".format(str(i).zfill(2)):[] for i in numbers}
    #iterate over students
    for studenti, rowi in df_mc.groupby("0idx"):
        #iteate over questions
        for questioni in numbers:
#            if questioni == 15:
#                break
            #extract the dataframe entries into variables
            question = rowi["Frage {}".format(questioni)].values[0]
            
            answer = rowi["Antwort {}".format(questioni)].values[0]
            answer = set([i.strip() for i in answer.split(";")])
            
            correct_answer = rowi["Richtige Antwort {}".format(questioni)].values[0]
            correct_answer = set([i.strip() for i in correct_answer.split(";")])
            
            #how many are correct
            overlap = answer & correct_answer
            ncorrect = len(overlap)
            
            #how many are wrong
            wrong = answer - correct_answer
            nwrong = len(wrong)
            
            #how many correct are missing
            missing = correct_answer - answer
            nmissing = len(missing)
            
            nmistakes = nwrong + nmissing
            #get the points
            if nmistakes == 0:
                points = 1
                
            elif nmistakes == 1:
                points = 2/3.
                
            elif nmistakes == 2:
                points = 1/3.
            else:
                points = 0

            points_dic["Punkte {} (1.00 Pkt) (MC)".format(str(questioni).zfill(2))].append(points)

    df_points = pd.DataFrame(points_dic)
    df_points["Summe_MC"] = df_points.sum(axis=1)
    pd.concat([df_mc[cols0], df_points], axis=1)
    return(df_points, n_questions_cm)
    
# =============================================================================
# CHANGE the file names here!
# =============================================================================
#set the filenames here
#this file is manually created and contains the question types (MC, Lueckentext, etc)
#example:
#Aufgabe	Typ	Gebiet
#1	Lueckentext	Chromatographie
exam_question_types = "FragenTypen.csv"

#this file contains the points as determined by ISIS
#(needs to be exported from moodle)
exam_details = "[intern] Bioanalytik 2-Bioanalytik II Zwischentest - WiSe 1718-Antworten.csv"

#this file contains the detailed answers or each question
#(needs to be exported from moodle)
exam_points = "[intern] Bioanalytik 2-Bioanalytik II Zwischentest - WiSe 1718-Bewertungen.csv"


# =============================================================================
# Do not edit anything here unless you know what you are doing
# =============================================================================
#read the stuff into dataframes
df_points = pd.read_csv(exam_points, decimal=",")
df_points = df_points[df_points["Nachname"] != "Gesamtdurchschnitt"]

df_types = pd.read_csv(exam_question_types, sep="\t", decimal=",")
df_types = df_types[df_types["Gebiet"] != "Kommentar"]

df_details = pd.read_csv(exam_details, decimal=",")

print ("#####################################################################")
print ("Fragen Typen haben die folgende Form:")
print (df_types.shape)

print ("Anzahl an Ergebnisse (Punkte) runtergeladen:")
print (df_points.shape)

print ("Anzahl an Detailantworten (Text) runtergeladen:")
print (df_details.shape)

idx = np.arange(0, df_points.shape[0])
df_points["0idx"] = idx
df_details["0idx"] = idx

points_other, nquestions_other = compute_points_non_mc(df_types, df_points)
points_mc, nquestions_mc = compute_points_mc(df_types, df_details)

details = df_points[["0idx", u'Nachname', u'Vorname', u'Institution', 
                     u'Abteilung', u'E-Mail-Adresse', u'Status', 
                     u'Begonnen am', u'Beendet', u'Verbrauchte Zeit']]
details.columns = ["0_"+str(i) for i in details.columns]

all_points = pd.concat([details, points_other, points_mc], axis=1)
all_points = all_points[sorted(all_points.columns)]
all_points["Summe_Total"] = all_points["Summe_MC"] + all_points["Summe_Other"]
print ("The Exam contained:")
print ("{} multiple choice questions".format(nquestions_mc))
print ("{} 'other type' questions".format(nquestions_other))
print ("#####################################################################")
#final task store the results
all_points.to_excel("Ergebnisse_ISISTest.xlsx")
       