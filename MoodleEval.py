#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:32:09 2017

@author: sven
"""
import pandas as pd
import numpy as np
import datetime
import sys

def eval_answer(truth, guess, max_points=1):
    """
    Given the sets
    """
    nmistakes = get_wrong(truth, guess)
    return(get_points(nmistakes, max_points))
    
    
def verbose_test(exp_points, points):
    """
    """
    if exp_points == points:
        print ("passed")
    else:
        sys.exit("FAILED!")
        print ("failed")
        
def test_evalution():
    """
    Tests the point counting
    
    mimic:
    question = rowi["Frage {}".format(questioni)].values[0]
    
    answer = rowi["Antwort {}".format(questioni)].values[0]
    answer = set([i.strip() for i in answer.split(";")])
                
    correct_answer = rowi["Richtige Antwort {}".format(questioni)].values[0]
    correct_answer = set([i.strip() for i in correct_answer.split(";")])
    
    #get the points
    nmistakes = get_wrong(answer, correct_answer)
    points = get_points(nmistakes, max_points)
    """
    # =========================================================================
    #  Four correct
    # =========================================================================
    print ("Four correct")
    truth = set(["A", "B", "C", "D"])
    answers = set(["","A", "B", "C", "D"])
    expected = [0, 0, 1/3., 2/3., 1]
    for i in range(0, 5):
        ans_list = sorted(list(answers))
        if i > 0:
            ans_list = ans_list[1:]
        points = eval_answer(truth, set(ans_list[:i]))
        #print ("Expected: {}".format(expected[i]), "Got: {}".format(points))
        if  points == expected[i]:
            print ("passed")
            #print ("Passed 4|{} test".format(i))
        else:
            print ("failed")
            #print ("Failed 4|{} test".format(i))
            sys.exit("FAILED!")
        print ("################")

 
    # =========================================================================
    # Three correct
    # =========================================================================
    print ("#################################################################")
    print ("Three correct")
    truth = set(["A", "B", "C"])
    answers = set(["","A", "B", "C", "D"])
    
    #1 point
    print ("1 Point.")
    exp_points = 1.
    points = eval_answer(truth, set(["A", "B", "C"]))
    verbose_test(exp_points, points)
    
    #0.66 point -> 1 mistake
    print ("0.6 Point.")
    exp_points = 2/3.
    points = eval_answer(truth, set(["A", "B"]))
    verbose_test(exp_points, points)
      
    points = eval_answer(truth, set(["A", "B","C", "D"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["A", "B"]))
    verbose_test(exp_points, points)
        
    #0.333 point -> 2 mistake
    print ("0.3 Point.")
    exp_points = 1/3.
    points = eval_answer(truth, set(["A", "B","D"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["A", "C", "D"]))
    verbose_test(exp_points, points)
    
    
    #0.333 point -> 3 mistake
    print ("0 Point.")
    exp_points = 0
    points = eval_answer(truth, set(["A","D"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["C", "D"]))
    verbose_test(exp_points, points)
    
    
    #0.333 point -> 3 mistake
    exp_points = 0
    points = eval_answer(truth, set(["A","D"]))
    verbose_test(exp_points, points)
    
    # =========================================================================
    # Two correct
    # =========================================================================
    print ("#################################################################")
    print ("Three correct")
    truth = set(["A", "B"])
    
    #1 point
    print ("1 Point.")
    exp_points = 1.
    points = eval_answer(truth, set(["A", "B"]))
    verbose_test(exp_points, points)
    
    #0.66 point -> 1 mistake
    print ("0.6 Point.")
    exp_points = 2/3.
    points = eval_answer(truth, set(["A", "B","D"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["A", "B", "C"]))
    verbose_test(exp_points, points)
        
    points = eval_answer(truth, set(["A"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["B"]))
    verbose_test(exp_points, points)
    
    #0.333 point -> 2 mistake
    print ("0.3 Point.")
    exp_points = 1/3.
    
    points = eval_answer(truth, set(["A","B", "C", "D"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["A", "D"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["A", "C"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["B","C"]))
    verbose_test(exp_points, points)
    
    #0.333 point -> 3 mistake
    print ("0 Point.")
    exp_points = 0
    points = eval_answer(truth, set(["A","C", "D"]))
    verbose_test(exp_points, points)

    points = eval_answer(truth, set(["B","C", "D"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["A","C", "D"]))
    verbose_test(exp_points, points)
    # =========================================================================
    # One correct
    # =========================================================================
    print ("#################################################################")
    print ("One correct")
    truth = set(["A"])
    
    #1 point
    print ("1 Point.")
    exp_points = 1.
    points = eval_answer(truth, set(["A"]))
    verbose_test(exp_points, points)
    
    #0.66 point -> 1 mistake
    print ("0.6 Point.")
    exp_points = 2/3.
    points = eval_answer(truth, set(["A", "B"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["A", "C"]))
    verbose_test(exp_points, points)
        
    points = eval_answer(truth, set([]))
    verbose_test(exp_points, points)
    
    #0.333 point -> 2 mistake
    print ("0.3 Point.")
    exp_points = 1/3.
    
    points = eval_answer(truth, set(["A","B", "C"]))
    verbose_test(exp_points, points)
    
    points = eval_answer(truth, set(["D"]))
    verbose_test(exp_points, points)
        
    #0.333 point -> 3 mistake
    print ("0 Point.")
    exp_points = 0
    points = eval_answer(truth, set(["A","B", "C", "D"]))
    verbose_test(exp_points, points)


    
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


def get_points(nmistakes, max_points):
    """
    Based on ... get the number of points.
    """
    if nmistakes == 0:
        points = 1 * max_points
        
    elif nmistakes == 1:
        points = 2/3. * max_points
        
    elif nmistakes == 2:
        points = 1/3. * max_points
    else:
        points = 0
    return(points)
    
    
def get_wrong(answer, correct_answer):
    """
    """
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
    return(nmistakes)
    
def compute_points_mc(df_types, df_details, max_points=1, 
                      special_treatment=False):
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
    
    max_points: float,
                maximum number of points per MC question
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
    
    points_dic = {"Punkte {} ({} Pkt) (MC)".format(str(i).zfill(2), max_points):[] for i in numbers}
    #iterate over students
    for studenti, rowi in df_mc.groupby("0idx"):
        #iteate over questions
        for questioni in numbers:
            #print (studenti, questioni, rowi)
#            if questioni == 15:
#                break
            #extract the dataframe entries into variables
            question = rowi["Frage {}".format(questioni)].values[0]
            
            answer = rowi["Antwort {}".format(questioni)].values[0]
            answer = set([i.strip() for i in answer.split(";")])
                        
            correct_answer = rowi["Richtige Antwort {}".format(questioni)].values[0]
            correct_answer = set([i.strip() for i in correct_answer.split(";")])
            
            #get the points
            nmistakes = get_wrong(answer, correct_answer)
            points = get_points(nmistakes, max_points)

            # =================================================================
            # START - SPECIAL HARD CODED STUFF FOR EXAM QUESTIONS...
            # =================================================================
            #treatment of special questions
            if special_treatment:
                if questioni == 16:
                    points = 1
                
                if questioni == 47:
                    answer = rowi["Antwort {}".format(questioni)].values[0]
                    answer = set([i.strip() for i in answer.split(";")])
                    
                    fullpoints1 = set(["Kupfersulfat (Biuret Assay)"])
                    fullpoints2 = set(["Kupfersulfat (Biuret Assay)", "Coomassie"])
                    
                    if (answer == fullpoints1) or (answer == fullpoints2):
                        points = 1
                    else:
                        nmistakes1 = get_wrong(answer, fullpoints1)
                        points1 = get_points(nmistakes1, max_points)
    
                        nmistakes2 = get_wrong(answer, fullpoints2)
                        points2 = get_points(nmistakes2, max_points)
    
                        points = np.max([points1, points2])                    
            # =================================================================
            # END - SPECIAL HARD CODED STUFF FOR EXAM QUESTIONS...
            # =================================================================                        
#                    print (answer),
#                    print (points)
            points_dic["Punkte {} ({} Pkt) (MC)".format(str(questioni).zfill(2), 
                       max_points)].append(points)

    df_points = pd.DataFrame(points_dic)
    df_points["Summe_MC"] = df_points.sum(axis=1)
    pd.concat([df_mc[cols0], df_points], axis=1)
    return(df_points, n_questions_cm)
    


def evaluate_exam(exam_question_types, exam_details, exam_points, outname, 
                  max_points, special_treatment=False):
    """
    
    Evaluates an ISIS exam based on the exports given from the system.
    
    Parameters:
    ---------------------
    exam_question_types: str,
                        file location of the mapping of the question types 
                        (MC, Lueckentext,e tc)
    exam_details: str,
                 file location of the details in the answers (export ISIS)
    exam_points: str,
                 file location of the point table from ISIS
                 
    max_points: float,
                maximal points per MC question
    
    outname: str,
            name for the output files
            
    special_treatment: bool,
                        if True some hard coded rules are used for some questions...
                        uggly but currently necessary! Watch out!
            
    Example:
    -----------------------
       
    #set the filenames here
    #this file is manually created and contains the question types (MC, Lueckentext, etc)
    #example:
    #Aufgabe	Typ	Gebiet
    #1	Lueckentext	Chromatographie
    exam_question_types = "FragenTypen_Abschlusstest.csv"
    
    #this file contains the points as determined by ISIS
    #(needs to be exported from moodle)
    #"-Antworten" file
    exam_details = "[WiSe1718] BAII-Abschlusstest - WiSe 1718-Antworten.csv"
    #this file contains the detailed answers or each question
    #(needs to be exported from moodle)
    #"-Bewertungen" file
    exam_points = "[WiSe1718] BAII-Abschlusstest - WiSe 1718-Bewertungen.csv"
    
    #what is the max number of points per MC-question?
    #Abschlusstest = 0.79
    #Zulassungstest = 0.38
    #Zwischentest = 1
    max_points = 0.79
    """
    if special_treatment:
        print ("!!!!Special Treatment is NOT active!!!!!")
    else:
        print ("!!!!Special Treatment IS active!!!!!")
        
    #name of the output file
    outname += "_" + datetime.date.today().strftime("%m%d%y")

    #%% run the evaluation
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
    points_mc, nquestions_mc = compute_points_mc(df_types, df_details, 
                                                 max_points=max_points,
                                                 special_treatment=special_treatment)
    
    details_cols = ["0idx", u'Nachname', u'Vorname', u'Institution', 
                         u'Abteilung', u'E-Mail-Adresse', u'Status', 
                         u'Begonnen am', u'Beendet', u'Verbrauchte Zeit']
    
    details = df_points[details_cols]
    details.columns = ["0_"+str(i) for i in details.columns]
    
    if "Matrikelnummer" in df_details["Frage 1"].iloc[0]:
        print ("Found Matrikelnummer! Will be added to final dataframe!")
        matrikel_df = df_details[["0idx", "Antwort 1"]]
        matrikel_df.columns = ["0idx", "Matrikelnummer"]
        all_points = pd.concat([details, points_other, 
                                points_mc, matrikel_df], axis=1)
        #details_cols.append("Antwort 1")
    else:
        print ("""Attention! There was no Matrikelnummer in Question 1! Data will
                   be returned with this information!""")
        all_points = pd.concat([details, points_other, points_mc], axis=1)
    
    
    
    all_points = all_points[sorted(all_points.columns)]
    all_points["Summe_Total"] = all_points["Summe_MC"] + all_points["Summe_Other"]#
    all_points["Summe_Total_Round"] = np.round(all_points["Summe_Total"], 1)
    print ("The Exam contained:")
    print ("{} multiple choice questions".format(nquestions_mc))
    print ("{} 'other type' questions".format(nquestions_other))
    
    print ("Max. Punkte: {}".format(all_points["Summe_Total_Round"].max()))
    print ("Min. Punkte: {}".format(all_points["Summe_Total_Round"].min()))
    print ("#####################################################################")
    #final task store the results
    all_points.to_excel("Ergebnisse_"+outname+".xlsx")
# =============================================================================
# CHANGE the file names here!
# =============================================================================
#%% set filenames and settings
    
    
def run():
    #Zwischentest
    special_treatment = False
    exam_question_types = "FragenTypen_Zwischentest.csv"
    exam_details = "[WiSe1718] BAII-Zwischentest - WiSe 1718-Antworten.csv"
    exam_points = "[WiSe1718] BAII-Zwischentest - WiSe 1718-Bewertungen.csv"
    evaluate_exam(exam_question_types, exam_details, exam_points, "Zwischentest",
                  1, special_treatment)
    
    
    #Zulassungstest
    special_treatment = False
    exam_question_types = "FragenTypen_Zulassungstest.csv"
    exam_details = "[WiSe1718] BAII-Zulassungstest - WiSe 1718-Antworten.csv"
    exam_points = "[WiSe1718] BAII-Zulassungstest - WiSe 1718-Bewertungen.csv"
    evaluate_exam(exam_question_types, exam_details, exam_points, "Zulassungstest",
                  0.38, special_treatment)
    
    #Abschlusstest
    special_treatment = True
    exam_question_types = "FragenTypen_Abschlusstest.csv"
    exam_details = "[WiSe1718] BAII-Abschlusstest - WiSe 1718-Antworten.csv"
    exam_points = "[WiSe1718] BAII-Abschlusstest - WiSe 1718-Bewertungen.csv"
    evaluate_exam(exam_question_types, exam_details, exam_points, "Abschlusstest",
                  0.79, special_treatment)









       
