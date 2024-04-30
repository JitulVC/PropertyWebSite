from flask import Flask, request, jsonify, render_template, redirect
from http import HTTPStatus
import pandas as p
from json import loads, dumps

class TestimonialModelView:     
    def loaddata(self):
        df = p.read_excel('PropBuildDB.xlsx',sheet_name='Testimonials')

        dj = df.to_json(orient="records")
        dj = loads(dj)
        return dj

