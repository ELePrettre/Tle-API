#!usr/bin/env python3
# coding : utf-8

import meteo
from flask import Flask, render_template, request
import urllib


app = Flask(__name__, template_folder='rep')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def resultat0():
    ville    = request.form['text1']
    return render_template("index.html",
        text1=ville, result0=meteo.meteo_actuelle(ville)[0],
                           result1=meteo.meteo_actuelle(ville)[1],
                           result2=meteo.meteo_actuelle(ville)[2],
                           result3=meteo.meteo_actuelle(ville)[3],
                           result4=meteo.meteo_actuelle(ville)[4],
                           result5=meteo.meteo_actuelle(ville)[5],
                           resultat00=meteo.prevision(ville)[0][0]
,resultat01=meteo.prevision(ville)[0][1]
,resultat02=meteo.prevision(ville)[0][2]
#,resultat10=meteo.prevision(ville)[1][0]
#,resultat11=meteo.prevision(ville)[1][1]
#,resultat12=meteo.prevision(ville)[1][2]
,resultat20=meteo.prevision(ville)[2][0]
,resultat21=meteo.prevision(ville)[2][1]
,resultat22=meteo.prevision(ville)[2][2]
#,resultat30=meteo.prevision(ville)[3][0]
#,resultat31=meteo.prevision(ville)[3][1]
#,resultat32=meteo.prevision(ville)[3][2]
,resultat40=meteo.prevision(ville)[4][0]
,resultat41=meteo.prevision(ville)[4][1]
,resultat42=meteo.prevision(ville)[4][2]
#,resultat50=meteo.prevision(ville)[5][0]
#,resultat51=meteo.prevision(ville)[5][1]
#,resultat52=meteo.prevision(ville)[5][2]
,resultat60=meteo.prevision(ville)[6][0]
,resultat61=meteo.prevision(ville)[6][1]
,resultat62=meteo.prevision(ville)[6][2]
#,resultat70=meteo.prevision(ville)[7][0]
#,resultat71=meteo.prevision(ville)[7][1]
#,resultat72=meteo.prevision(ville)[7][2]
,resultat80=meteo.prevision(ville)[8][0]
,resultat81=meteo.prevision(ville)[8][1]
,resultat82=meteo.prevision(ville)[8][2]
#,resultat90=meteo.prevision(ville)[9][0]
#,resultat91=meteo.prevision(ville)[9][1]
#,resultat92=meteo.prevision(ville)[9][2]
,resultat100=meteo.prevision(ville)[10][0]
,resultat101=meteo.prevision(ville)[10][1]
,resultat102=meteo.prevision(ville)[10][2]
#,resultat110=meteo.prevision(ville)[11][0]
#,resultat111=meteo.prevision(ville)[11][1]
#,resultat112=meteo.prevision(ville)[11][2]
,resultat120=meteo.prevision(ville)[12][0]
,resultat121=meteo.prevision(ville)[12][1]
,resultat122=meteo.prevision(ville)[12][2]
#,resultat130=meteo.prevision(ville)[13][0]
#,resultat131=meteo.prevision(ville)[13][1]
#,resultat132=meteo.prevision(ville)[13][2]
,resultat140=meteo.prevision(ville)[14][0]
,resultat141=meteo.prevision(ville)[14][1]
,resultat142=meteo.prevision(ville)[14][2]
#,resultat150=meteo.prevision(ville)[15][0]
#,resultat151=meteo.prevision(ville)[15][1]
#,resultat152=meteo.prevision(ville)[15][2]
,resultat160=meteo.prevision(ville)[16][0]
,resultat161=meteo.prevision(ville)[16][1]
,resultat162=meteo.prevision(ville)[16][2]
#,resultat170=meteo.prevision(ville)[17][0]
#,resultat171=meteo.prevision(ville)[17][1]
#,resultat172=meteo.prevision(ville)[17][2]
,resultat180=meteo.prevision(ville)[18][0]
,resultat181=meteo.prevision(ville)[18][1]
,resultat182=meteo.prevision(ville)[18][2]
#,resultat190=meteo.prevision(ville)[19][0]
#,resultat191=meteo.prevision(ville)[19][1]
#,resultat192=meteo.prevision(ville)[19][2]
,resultat200=meteo.prevision(ville)[20][0]
,resultat201=meteo.prevision(ville)[20][1]
,resultat202=meteo.prevision(ville)[20][2]
#,resultat210=meteo.prevision(ville)[21][0]
#,resultat211=meteo.prevision(ville)[21][1]
#,resultat212=meteo.prevision(ville)[21][2]
,resultat220=meteo.prevision(ville)[22][0]
,resultat221=meteo.prevision(ville)[22][1]
,resultat222=meteo.prevision(ville)[22][2]
#,resultat230=meteo.prevision(ville)[23][0]
#,resultat231=meteo.prevision(ville)[23][1]
#,resultat232=meteo.prevision(ville)[23][2]
,resultat240=meteo.prevision(ville)[24][0]
,resultat241=meteo.prevision(ville)[24][1]
,resultat242=meteo.prevision(ville)[24][2]
                           )

app.run(debug=True)

